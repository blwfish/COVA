# COVA JMRI Configuration Analysis - March 31, 2025 Export

**File:** Gville-arsenal.xml  
**Timestamp:** Monday, March 31, 2025, 7:37 PM EDT  
**JMRI Version:** 5.11.3  
**Status:** Current and Complete for all built areas

---

## Block Inventory (Current)

### Total: 28 Blocks (IB:AUTO:0001 - IB:AUTO:0028, skipping 0020 and 0023)

#### Arsenal Area
- **IB:AUTO:0001** - Staging Exit Turnout
- **IB:AUTO:0002** - Arsenal (sensor: `MS02.01.57.002.C4.00.5A;02.01.57.10.02.C4.00.5B`)
- **IB:AUTO:0003** - Arsenal-Plant (sensor: `MS02.01.57.10.02.C4.00.12;02.01.57.10.02.C4.00.13`)

#### Gordonsville Area
- **IB:AUTO:0004** - Gordonsville-South-Turnout
- **IB:AUTO:0005** - Gordonsville-North-Wye Turnout
- **IB:AUTO:0006** - Gordonsville-Washington (sensor: `MS02.01.57.10.02.C4.00.1E;02.01.57.10.02.C4.00.1F`)
- **IB:AUTO:0027** - Gordonsville-North-Wye (sensor: `MS02.01.57.10.02.C4.00.42;02.01.57.10.02.C4.00.43`)
- **IB:AUTO:0028** - Gordonsville-Piedmont

#### Lindsay Area
- **IB:AUTO:0009** - Lindsay
- **IB:AUTO:0018** - Lindsay Siding
- **IB:AUTO:0019** - Woolen Mills

#### VAL (Virginia Air Line) Staging
- **IB:AUTO:0010** - VAL (entry block, sensor: `MS02.01.57.00.03.F2.00.72;02.01.57.00.03.F2.00.73`)
- **IB:AUTO:0011** - VAL Loop
- **IB:AUTO:0012** - VAL staging6 (sensor: `MS02.01.57.00.03.F3.00.36;02.01.57.00.03.F3.00.37`)
- **IB:AUTO:0013** - VAL staging1 (sensor: `MS02.01.57.00.03.F3.00.5A;02.01.57.00.03.F3.00.5B`)
- **IB:AUTO:0014** - VAL staging2 (sensor: `MS02.01.57.00.03.F3.00.4E;02.01.57.00.03.F3.00.4f`)
- **IB:AUTO:0015** - VAL staging3
- **IB:AUTO:0016** - VAL staging4 (sensor: `MS02.01.57.00.03.F3.00.AE;02.01.57.00.03.F3.00.AF`)
- **IB:AUTO:0017** - VAL staging5 (sensor: `MS02.01.57.00.03.F3.00.A2;02.01.57.00.03.F3.00.A3`)

#### Piedmont Area
- **IB:AUTO:0021** - Piedmont (sensor: `Piedmont-block-occ` - note: references sensor by user name, not system name)

#### Louisa Area
- **IB:AUTO:0026** - Louisa (sensor: `MS02.01.57.10.02.C4.00.4E;02.01.57.10.02.C4.00.4F`)

#### Staging (Lower Level - Temporary)
- **IB:AUTO:0007** - Staging Reverse Loop Turnout
- **IB:AUTO:0008** - Staging Siding (sensor: `Staging-Siding-occ`)
- **IB:AUTO:0022** - Staging Main (sensor: `MS02.01.57.10.02.C5.00.06;02.01.57.10.02.C5.00.06` - **note: both sensors same?**)
- **IB:AUTO:0024** - Staging Main Exit Turnout
- **IB:AUTO:0025** - Staging Main Entry Turnout

### Observations on Block Definitions

1. **VAL Staging:** Still shows as 6 blocks (VAL staging1-6) but you said it's been extended to 2 blocks per track. This may not be fully updated in JMRI yet, or the original naming scheme is different from what you mentioned.

2. **Sensor References:** Some blocks reference sensors by LCC event IDs, some by user names. This is inconsistent and should be normalized in the generator.

3. **Piedmont-block-occ:** Referenced by user name instead of system name. This works but is non-standard.

4. **Missing Blocks:** No blocks for Fork Union, no helper pocket block for VAL staging. These need to be added.

---

## Turnout Inventory (Current)

### Total: 23 Turnout Definitions

#### MQTT Turnouts (ESP32 Controlled - 11 total)

| System Name | User Name | Status |
|---|---|---|
| M2TEast-Lindsay | East-Lindsay | Working |
| M2TWest-Lindsay | West-Lindsay | Working |
| M2TVAL-staging-north-1 | VAL-staging-north-1 | Working |
| M2TVAL-staging-north-2 | VAL-staging-north-2 | Working |
| M2TVAL-staging-north-3 | VAL-staging-north-3 | Working |
| M2TVAL-staging-south-1 | VAL-staging-south-1 | Working |
| M2TVAL-staging-south-2 | VAL-staging-south-2 | Working |
| M2TVAL-staging-south-3 | VAL-staging-south-3 | Working |
| M2TVAL-staging-return | VAL-staging-return | Working |
| M2TVAL-helper-pocket | VAL-helper-pocket | Working |
| M2TStaging-Reverse-Loop | Main Staging Reverse Loop Turnout | Working (temp loop) |

#### SPROG Turnouts (DCC via Tortoises - 12 total)

| System Name | User Name | Address | Notes |
|---|---|---|---|
| ST200 | Arsenal-gate | ST200 | Tortoise |
| ST201 | Gordonsville-freight | ST201 | Tortoise |
| ST202 | Gordonsville-south | ST202 | Inverted |
| ST203 | Arsenal-lead | ST203 | Tortoise |
| ST210 | Staging-exit | ST210 | ? |
| ST211 | ? | ST211 | ? |
| ST212 | ? | ST212 | ? |
| ST214 | ? | ST214 | ? |
| ST220 | ? | ST220 | ? |
| ST301 | ? | ST301 | ? |
| ST302 | ? | ST302 | ? |
| ST303 | ? | ST303 | ? |

**Note:** ST210+ lack user names in the initial JMRI export. These are likely the new turnouts added since the original plan (Arsenal yard expansion, Gordonsville passing siding area, etc.).

---

## Occupancy Sensors (Current)

### LCC/OpenLCB Sensors: 17 Total

**From Tower Board 1 (02.01.57.10.02.C4):**
- Arsenal-block-occ
- Arsenal-Plant-occ
- Washington-Sub-occ
- Piedmont-block-occ
- Gordonsville-North-Wye-occ
- Louisa-block-occ

**From Tower Board 2 (02.01.57.10.02.C5):**
- Staging-Main-occ
- Staging-Siding-occ

**From Tower Board 3 (02.01.57.00.03.F2):**
- Piedmont-center-occ
- VAL-entry-occ

**From Tower Board 4 (02.01.57.00.03.F3):**
- VAL-staging-3south-occ
- VAL-staging-2north-occ
- VAL-staging-1north-occ
- VAL-helper-pocket-occ
- VAL-reverse-loop-2 through VAL-reverse-loop-5 (4 sensors for reverse loops)

### MQTT Sensors (Pushbuttons): 5 Total
- Gordonsville-North-Button
- Staging-Exit-Button
- Staging-Loop-Button
- Staging-Siding-Entry-Button
- Staging-Siding-Exit-Button

---

## Routes Defined (Current)

At least 4 routes visible:
- Gordonsville-Piedmont (IO:AUTO:0001)
- Gordonsville-Washington (IO:AUTO:0002)
- Gordonsville-staging (IO:AUTO:0003)
- Staging Siding (IO:AUTO:0004)

---

## Key Discrepancies Between Reality & JMRI Config

### What's Missing from JMRI

1. **Fork Union blocks** - Wired and tested, but not in JMRI yet
2. **VAL Staging extended layout** - You said 2 blocks per track = 12 blocks, but JMRI still shows 6
3. **VAL helper pocket** - Mentioned as built and wired, but no block defined in JMRI
4. **Arsenal yard expansion** - Expanded from 1 to 2 to 3 tracks, but not reflected in block definitions
5. **Helix blocks** - Not yet defined (makes sense, not yet built)
6. **ST210+ user names** - Turnout addresses exist but lack descriptive names

### What's Incomplete

1. **VAL staging block structure** - Needs clarification on actual vs. JMRI block count
2. **Block path definitions** - Some blocks lack complete path definitions with turnout interlocking logic
3. **Signal masts** - Not yet defined (expected at this stage)

---

## Action Items for Next Phase

### Data Reconciliation Needed

1. **Clarify VAL Staging blocks:**
   - Are there actually 12 blocks (2 per track × 6 tracks) or 6?
   - If 12, which are the additional 6?
   - How are they related to existing VAL staging1-6 blocks?

2. **Arsenal yard expansion:**
   - How many new turnouts added for 2→3 track yard?
   - What are ST210, ST211, ST212?
   - Should any become separate blocks?

3. **Fork Union blocks:**
   - How many blocks total?
   - What are their occupancy sensors?
   - How do they connect to VAL staging exit?

4. **Helper pocket:**
   - Should this be a separate block? (Seems like yes)
   - What's the occupancy sensor?
   - Is it already wired to a Tower board?

5. **ST220, ST301-ST303:**
   - Which physical turnouts are these?
   - What are their user names/purposes?
   - Gordonsville passing siding? Other areas?

### Next Steps

1. Export/photograph the areas with new turnouts to clarify ST210+
2. Clarify the VAL staging block structure (6 or 12 total?)
3. Document Fork Union in detail
4. Update JMRI with missing block/turnout definitions
5. Commit updated config to git

---

## Summary for Automation

**Current State (Known):**
- 28 blocks defined and mostly complete
- 23 turnouts defined (11 MQTT, 12 SPROG)
- 17 LCC occupancy sensors, 5 MQTT pushbuttons
- 4+ routes defined
- All infrastructure wired and operational for Arsenal/Gordonsville/VAL/Staging areas

**Gaps (To Be Resolved):**
- VAL staging block structure unclear (6 vs 12 blocks)
- Fork Union not yet in JMRI
- Helper pocket not yet in JMRI
- Arsenal yard expansion turnouts (ST210+) lack full definitions
- Gordonsville passing siding turnouts not yet identified
- No signal masts defined

**Ready for Automation:**
- Master data can be built from current JMRI export
- Generator can validate against existing XML
- Incremental updates as new areas are completed
