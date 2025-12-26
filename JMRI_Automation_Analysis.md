# JMRI Automation Analysis: COVA Layout

## Current State of Configuration

### What's Already Working

Your `Gville-arsenal.xml` shows a well-structured, partially built layout with three operational subsystems:

1. **LCC-based occupancy detection** (RRcir-kits LCC Tower boards)
   - 17 occupancy sensors defined via OpenLCB/LCC protocol
   - System name format: `MS02.01.57...` (OpenLCB 64-bit event IDs)
   - User-friendly names: `Arsenal-block-occ`, `VAL-staging-1south-occ`, etc.
   - Two LCC "device groups" visible: `02.01.57.00.03.F2` and `02.01.57.00.03.F3` (different Tower boards)

2. **MQTT-based turnout control** (ESP32 servo system)
   - 10 turnouts defined via MQTT
   - System names like `M2TEast-Lindsay`, `M2TVAL-staging-north-1`
   - Direct MQTT topic mapping (system name = MQTT topic path)
   - These are your ESP32-controlled SG90 servos

3. **SPROG-based turnout control** (DCC via command station)
   - 16+ turnouts defined via SPROG protocol
   - System names: `ST200`, `ST201`, `ST202`, etc.
   - These are your Tortoises on the SwitchIt8s
   - Range appears to be ST200-ST215+ for Gordonsville area

4. **Layout Editor panel**
   - Visual representation of track layout
   - Turnout and sensor definitions referenced in the LayoutEditor

5. **MQTT-based pushbuttons** (5 defined)
   - Used for manual operation of critical functions
   - `Gordonsville-North-Button`, `Staging-Exit-Button`, etc.

### What's Missing (Not Yet Defined)

- **Blocks** - No block definitions found in the current XML. This is where the tedious manual work begins.
- **Routes** - No route definitions (train paths through the layout)
- **Signal logic** - No signaling system defined
- **The rest of the layout** - Pages 2-4 completely unmapped

## Key Insight: Manual Work Bottleneck

Looking at your 71 blocks + 61 turnouts, the manual process you're facing is:

1. **For each block:**
   - Create block definition in JMRI
   - Assign occupancy sensor(s) to that block
   - Define turnouts that feed into/out of that block
   
2. **For each turnout:**
   - Verify address assignments
   - Define which blocks it connects
   - Set feedback options

3. **Route creation:**
   - Define interlocking logic
   - Create signal logic
   - Build dispatcher routes

At 71 blocks and 61 turnouts, this is roughly 600-800 manual configuration entries.

## Data Structure in Current XML

### Turnout Definition (MQTT example)
```xml
<turnout feedback="DIRECT" inverted="false" automate="Off">
  <systemName>M2TEast-Lindsay</systemName>
  <userName>East-Lindsay</userName>
</turnout>
```

### Turnout Definition (SPROG example)
```xml
<turnout feedback="DIRECT" inverted="true" automate="Off">
  <systemName>ST202</systemName>
  <userName>Gordonsville-south</userName>
</turnout>
```

### Sensor Definition (LCC example)
```xml
<sensor inverted="false">
  <systemName>MS02.01.57.10.02.C4.00.5A;02.01.57.10.02.C4.00.5B</systemName>
  <userName>Arsenal-block-occ</userName>
</sensor>
```

---

## Automation Opportunity

### What We Can Generate

The JMRI XML config is completely parseable and generatable. We can build a Python tool that takes a **master data source** and generates all turnout, sensor, and block definitions.

### Master Data Source Structure

**Option 1: Hierarchical Python Dictionary** (recommended)
```python
layout_data = {
  "arsenal": {
    "turnouts": [
      {
        "id": "Arsenal-gate",
        "address": "ST200",
        "type": "SPROG",  # MQTT, SPROG, or LCC
        "inverted": False,
      },
      # ...
    ],
    "occupancy_sensors": [
      {
        "id": "Arsenal-block-occ",
        "lcc_address": "02.01.57.10.02.C4.00.5A;02.01.57.10.02.C4.00.5B",
      },
      # ...
    ],
    "blocks": [
      {
        "id": "Arsenal-block",
        "occupancy_sensor": "Arsenal-block-occ",
        "turnouts": ["Arsenal-gate", "Arsenal-lead"],
      },
      # ...
    ],
  },
  # Repeat for gordonsville, val_staging, pages 2-4, etc.
}
```

**Option 2: Structured CSV/JSON Files**
- `turnouts.csv` - All turnout definitions
- `sensors.csv` - All occupancy sensor definitions  
- `blocks.csv` - Block definitions + sensor assignments
- Easier to maintain, edit, and version control
- Can be edited in Excel/Numbers then exported

### What the Generator Would Do

1. **Parse master data**
2. **Generate valid JMRI XML sections:**
   - `<sensors>` blocks for LCC, MQTT, internal
   - `<turnouts>` blocks for MQTT, SPROG
   - `<blocks>` definitions (if JMRI supports them in XML—may need verification)
3. **Maintain existing layout editor XML** (just inject the new config sections)
4. **Version control the result** with git

### Benefits

- **Eliminates manual data entry** - Define once, generate many times
- **Consistency** - Same naming conventions everywhere
- **Tractability** - When you add 10 new turnouts to page 2, update the master data and regenerate
- **Reviewability** - See differences in git diffs before committing
- **Scalability** - Easy to add new areas as you build them
- **Professional practice** - Same methodology you use for FreeCAD generators

---

## Next Steps

### Phase 1: Data Extraction & Validation

1. Export all existing JMRI config sections from current XML
2. Create master data source capturing:
   - All 26 current sensors (LCC system names + user names)
   - All 26+ current turnouts (addresses + user names)
   - Which turnouts are where (Gordonsville, Arsenal, VAL staging, etc.)
3. Verify against Byron's track plan (which area does each turnout belong?)

### Phase 2: Build the Generator

Simple Python tool:
- Read master data (JSON or CSV)
- Generate valid JMRI XML sections
- Merge with existing config (or create fresh config)
- Validate schema
- Output clean, version-controlled XML

Estimated effort: **2-3 hours** to build a working generator

### Phase 3: Add New Areas

For each new area (rest of page 1, page 2, page 3):
1. Add turnouts/sensors to master data
2. Run generator
3. Import into JMRI
4. Test hardware connections
5. Commit to git

---

## Questions to Finalize Design

1. **JMRI Blocks support** - Do you want to use JMRI's block definitions (for route interlocking), or just track occupancy?
   
2. **Signal logic** - Will COVA have a signal system? If so, what type (3-aspect automatic, CTC, dispatcher only)?

3. **Master data format** - CSV (Excel-friendly) or Python dict (programmatic)?

4. **MQTT topic structure** - Your current turnouts use `M2T<name>`. What's the actual MQTT topic path your ESP32s listen to?
   - e.g., `layout/turnout/East-Lindsay` or `cova/turnout/East-Lindsay`?

5. **LCC Event IDs** - Are the occupancy sensor LCC addresses fixed/known, or do we extract them from the Tower board configuration?

6. **Future expansion** - Do you anticipate adding signal logic, cab bus, or other features beyond occupancy + turnout control?

---

## Rough Timeline

| Phase | Effort | Timeline |
|-------|--------|----------|
| Data extraction & validation | 1-2 hours | Next session |
| Build generator tool | 2-3 hours | 1-2 days after |
| Test & integrate with JMRI | 1-2 hours | Same day as generator |
| Add new areas as you build | 15-30 min per area | Ongoing |

**Total to automate away the manual drudgery: ~4-7 hours of focused work**
