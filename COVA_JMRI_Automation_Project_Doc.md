# COVA Layout JMRI Automation Project

**Document Version:** 1.0  
**Date Started:** 2025-01-20  
**Status:** Requirements & Discovery Phase  
**Last Updated:** 2025-01-20

---

## Project Overview

Automating JMRI configuration generation for the C&O in Virginia (COVA) HO-scale model railroad layout. Goal: eliminate ~600-800 manual configuration entries (turnouts, sensors, blocks, signals, routes) through data-driven generation.

**Scope:** Full layout automation from master data source, with phased implementation as new areas are built.

---

## Layout Physical State

### Currently Built & Operational (All Wired & Tested)

#### Arsenal Area (Page 1, Upper Left)
- **Track Layout:** Single main lead plus recently expanded 2-track yard (becoming 3-track soon)
- **Turnouts:** ~4-5 (Arsenal-gate, Arsenal-lead, plus yard leads)
- **Blocks:** Multiple (exact count TBD from JMRI export)
- **Occupancy Detection:** LCC Tower (wired and working)
- **Turnout Control:** 16 Tortoises on 2 SwitchIt8s (working)
- **Status:** In JMRI, operational

#### Gordonsville Yard Complex (Page 1, Center)
- **Track Layout:** Yard with wye, multiple ladder tracks
- **Turnouts:** ~15-20 estimated
- **Blocks:** Multiple (exact count TBD)
- **Occupancy Detection:** LCC Tower (wired and working)
- **Turnout Control:** Tortoises on SwitchIt8s
- **Status:** In JMRI, operational
- **Note:** Passing siding at Gordonsville is half-built, wired, but NOT yet added to JMRI

#### Lindsay to Woolen Mills Area (Page 1, East Side)
- **Status:** Track laid, DCC wired, occupancy detection wired and tested
- **Turnouts & Blocks:** In JMRI, operational
- **Turnout Control:** Tortoises on SwitchIt8s

#### VAL (Virginia Air Line) Staging (Page 2, Lower Deck)
- **Track Layout:** 
  - Original plan: 3 staging tracks (1 block each)
  - **EXTENDED:** Now 3 staging tracks, 2 blocks each = 6 blocks total
  - **ADDED:** 2-foot long helper pocket on outside of return loop = 1 block
  - **Total:** 7 blocks (6 staging + 1 helper pocket)
- **Turnouts:** Multiple access turnouts + return loop turnout(s)
- **Occupancy Detection:** LCC Tower (wired and working)
- **Turnout Control:** ESP32 + SG90 servos via MQTT (code ready, not yet deployed)
- **Status:** Physically complete, wired, occupancy working; servo code ready but not yet integrated into JMRI

#### VAL Exit Connector (Page 2 → Page 1 transition)
- **Track Layout:** Exit turnout from VAL staging that goes around under "SOU station" area
- **Destination:** Leads to helix (which continues downward)
- **Status:** Built and wired, NOT YET in JMRI
- **Note:** About 18" of track at end, stops just before helix begins

#### Fork Union Connector (Under Main Layout, Pages 2-4 transition)
- **Track Layout:** Fork Union section (hidden under layout), leads from VAL exit connector
- **Destination:** Runs ~18" toward where helix will exit
- **Turnouts & Blocks:** Wired and tested, NOT YET in JMRI
- **Status:** Built and wired, ready to be added to JMRI
- **Estimated Blocks:** ~3-5 (TBD from physical inspection)

#### Temporary Staging (Page 4, Temporary)
- **Track Layout:** 2-track reverse loop (temporary, will be removed)
- **Turnouts:** ~2
- **Status:** Operational except for 1 turnout with persistent derailing problem
- **Plan:** Will be removed when full main staging is built on lower level

### Planned/Not Yet Built

#### Helix (Vertical Transition, Page 1 → Lower Level)
- **Status:** NOT YET BUILT
- **Note:** Fork Union connector ends ~18" short of where helix will connect
- **Planned:** Will continue descending to lower level main staging area
- **Blocks/Turnouts:** TBD

#### Richmond Area (Page 1, Upper Left - replaces original main staging location)
- **Track Layout:** Includes Tobacco Row, Main Street Station, ALCO Richmond Locomotive Works (small section)
- **Status:** NOT YET BUILT
- **Plan:** Will eventually replace the space originally allocated for main staging
- **Estimated Complexity:** High (multiple industries, passenger station)

#### Main Staging (Lower Level, Page 4 Relocated)
- **Current Plan:** Being moved down one level to make room for Richmond
- **Status:** NOT YET FULLY DESIGNED
- **Challenge:** Layout team hasn't fully figured out topology yet
- **Will Include:** Multiple staging tracks (exact count TBD)

#### Pages 2 & 3 Unbuilt Sections
- **Status:** NOT YET BUILT
- **Estimated Blocks:** ~43+ (from 71 total - 28 current blocks)
- **Note:** Includes Charlottesville, Lyndhurst, main level C&O operations

---

## Current JMRI Configuration State

### What We Know (From Gville-arsenal.xml)

**Blocks Currently Defined:**
- 28 blocks total: IB:AUTO:0001 through IB:AUTO:0028
- 20 layout blocks: ILB1 through ILB20 with occupancy sensor assignments
- Layout blocks include paths with turnout interlocking logic

**Example Block Definition:**
```xml
<block systemName="IB:AUTO:0002" length="0.0" curve="0">
  <systemName>IB:AUTO:0002</systemName>
  <userName>Arsenal</userName>
  <occupancysensor>MS02.01.57.002.C4.00.5A;02.01.57.10.02.C4.00.5B</occupancysensor>
  <path todir="16" fromdir="32" block="IB:AUTO:0001" />
  <path todir="32" fromdir="16" block="IB:AUTO:0003">
    <beansetting setting="4">
      <turnout systemName="Arsenal-gate" />
    </beansetting>
  </path>
</block>
```

**Turnouts Currently Defined:**
- MQTT turnouts (ESP32 controlled): ~10 defined, via topics like `M2TVAL-staging-north-1`
- SPROG turnouts (DCC, Tortoises): ~16+ defined (ST200-ST215+)

**Occupancy Sensors:**
- LCC/OpenLCB sensors: ~17 defined
- MQTT sensors (pushbuttons): 5 defined
- System names: 64-bit OpenLCB event IDs like `MS02.01.57.10.02.C4.00.5A;02.01.57.10.02.C4.00.5B`

**Routes Currently Defined:**
- At least 3-4 routes visible (Gordonsville-Piedmont, Gordonsville-Washington, Gordonsville-staging, Staging Siding)

### What's Missing from This Export

**CRITICAL:** The XML file provided (`Gville-arsenal.xml`) may be outdated. It was last saved July 28, 2024.

**Missing from this file:**
- Fork Union blocks/turnouts (wired and tested but not yet in JMRI)
- Extended VAL staging blocks (if they've been refined since original plan)
- Gordonsville passing siding blocks (half-built, wired, not yet added)
- Latest route definitions
- Any signal mast definitions (not expected to exist yet, but need to verify)

**NEXT STEP:** Retrieve most recent JMRI profile file from git repository or directly from:
```
/Users/blw/Library/Preferences/JMRI/CO_in_Virginia.jmri/
```

---

## Control Hardware Infrastructure

### DCC Command Station
- **Current:** SPROG (exact model TBD)
- **Expandable:** Up to 3 additional boosters possible
- **WiThrottle Protocol:** WiFi throttles + DispatcherPro support

### Occupancy Detection (Fully Implemented)
- **Type:** RRcir-kits LCC Tower boards
- **Connection:** LCC bus → USB nexus
- **JMRI Integration:** Native OpenLCB/LCC protocol
- **LCC Device IDs Used:**
  - `02.01.57.10.02.C4` (Tower Board 1, Gordonsville area)
  - `02.01.57.10.02.C5` (Tower Board 2, Staging area)
  - `02.01.57.00.03.F2` (Tower Board 3, VAL staging)
  - `02.01.57.00.03.F3` (Tower Board 4, VAL staging additional)

### Turnout Control - Tortoises (Existing)
- **Quantity:** 16 reclaimed from prototype layout
- **Location:** Gordonsville area + Arsenal
- **Interface:** 2x SwitchIt8 servo controllers
- **JMRI Control:** DCC via SPROG (system names: ST200-ST215+)
- **Feedback:** Direct (no position feedback)

### Turnout Control - ESP32 + SG90 Servos (New, Partially Deployed)
- **Quantity:** All remaining turnouts (45+ estimated)
- **Control:** WiFi → MQTT → JMRI
- **Firmware:** Custom ESP32 code (already developed and tested)
- **JMRI Integration:** MQTT turnout manager
- **Status:** 
  - VAL staging servos: Code ready, hardware ready, JMRI integration pending
  - Other areas: Ready for deployment as new track is built

**MQTT Configuration Needed:**
- **Topic Structure:** Standard MQTT topics (exact format TBD from Brian's implementation)
  - Example anticipated: `layout/turnout/{turnout_id}` with CLOSED/THROWN payloads
  - Need to confirm actual topic paths from running system

### Future Expansion
- Potential for 3 additional boosters
- Scalable servo control via additional ESP32 boards

---

## Requirements for Automation

### 1. Block Definitions
- **Needed:** Complete block definitions for all 71 planned blocks
- **Currently:** 28 blocks in JMRI (need to verify actual count and structure)
- **Components:**
  - Block system name (IB:AUTO:XXXX format)
  - Block user name (human-readable)
  - Occupancy sensor assignment
  - Paths with turnout interlocking logic
  - Track curve/length metadata (optional, for visualization)

### 2. Signal Mast Definitions
- **Type:** Signal masts (3-aspect: Stop/Caution/Clear) - **ASSUMED, needs confirmation**
- **Placement:** TBD - need to define strategy:
  - Option A: Entry signal for every block boundary
  - Option B: Only at major decision points (yard leads, branch junctions)
  - Option C: Specific locations identified by Byron or Brian
- **Control Logic:**
  - Occupancy-based automatic: Show Clear if next block empty
  - Turnout interlocking: Can only show Clear if diverge turnout set correctly for that path
  - Permissive block logic if needed
- **Status:** Not yet designed; needs early definition

### 3. Routes / Transits for DispatcherPro
- **Needed:** Transit definitions for common train movements
- **Currently:** 3-4 basic routes exist
- **Approach:** TBD:
  - Option A: Generate transits from master data (requires detailed path definitions)
  - Option B: Build transits manually in JMRI UI (master data just provides blocks/signals)
  - Option C: Hybrid (generate skeleton transits, manual refinement in JMRI)

### 4. DispatcherPro Integration
- **Purpose:** Automated train dispatching, signal interlocking, route management
- **Requirements:**
  - Complete block network
  - Signal masts with clear operational logic
  - Routes/transits connecting blocks
  - Turnout interlocking rules
- **Timing:** Not critical until signal logic is defined

---

## Master Data Structure

### Format: JSON
Hierarchical structure with areas, sub-areas, turnouts, sensors, blocks, and rules.

### Key Sections:

```json
{
  "metadata": {
    "layout_name": "C&O in Virginia (COVA)",
    "scale": "HO",
    "version": "1.0.0",
    "date": "2025-01-20"
  },
  "areas": {
    "arsenal": { /* complete definition */ },
    "gordonsville": { /* complete definition */ },
    "val_staging": { /* complete definition */ },
    "fork_union": { /* complete definition */ },
    "helix": { /* TBD */ },
    "richmond": { /* TBD */ },
    "main_staging_lower": { /* TBD */ }
  },
  "signal_definitions": {
    "signal_types": [ /* 3-aspect mast definitions */ ],
    "signal_placement_rules": [ /* where signals go */ ],
    "signal_logic_rules": [ /* occupancy + interlocking */ ]
  }
}
```

---

## Generator Tool

### Current Status
- **Skeleton written:** Python script `jmri_config_gen.py`
- **Capabilities:** 
  - Reads master data JSON
  - Generates JMRI XML sections for turnouts (MQTT + SPROG)
  - Generates JMRI XML sections for LCC sensors
  - Merges with existing config
  - Version-controlled output

### Needed Expansions
- Block definition generation
- Signal mast definition generation
- Signal logic rule generation (occupancy + interlocking)
- Transit definition generation (if needed)
- Validation & schema checking

### Validation Strategy
- Generate XML that matches existing JMRI format exactly
- Test against working Gville-arsenal.xml
- Verify schema compliance
- Compare generated vs. manual definitions

---

## Outstanding Questions

### Immediate (Block Blocking Questions)

1. **Current JMRI State**
   - [ ] Is the most recent JMRI profile in git, or on disk only?
   - [ ] Are the VAL staging blocks updated to reflect 2-blocks-per-track layout?
   - [ ] Are Fork Union or extended VAL connector blocks already in JMRI?

2. **Blocks & Sensors Inventory**
   - [ ] Complete list of all 28 current blocks with occupancy sensor assignments
   - [ ] Turnout inventory for Fork Union (# of turnouts, addresses, types)
   - [ ] Block count estimate for Fork Union
   - [ ] Updated VAL staging block definitions (if changed from original)

3. **Signal Architecture**
   - [ ] Signal mast type: 3-aspect? Other?
   - [ ] Signal placement strategy: Every block? Major junctions only? Specific locations from Byron?
   - [ ] Control logic: Occupancy-based automatic + turnout interlocking?
   - [ ] Any existing signal definitions in current JMRI config?

4. **DispatcherPro Requirements**
   - [ ] Need full transit network immediately, or can be added incrementally?
   - [ ] Should transits be generated from master data or built manually in JMRI?
   - [ ] Example transits: "Arsenal to Gordonsville", "Staging to Lindsay", etc.?

### Medium-Term (Design Decisions)

5. **MQTT Topic Structure**
   - [ ] Exact MQTT topic paths your ESP32s are listening to
   - [ ] Payload format (CLOSED/THROWN? 0/1? Other?)

6. **Fork Union & Helix**
   - [ ] Fork Union: How many blocks, turnouts, sensor assignments?
   - [ ] Helix: Will it have intermediate stops/blocks, or continuous?
   - [ ] Connection logic between Fork Union → Helix → Main Staging Lower

7. **Richmond Area**
   - [ ] Estimated block/turnout count
   - [ ] Topology (Tobacco Row, Main Street, ALCO works - how are they wired together?)
   - [ ] Timeline for construction/JMRI integration?

8. **Pages 2-3 Unbuilt Sections**
   - [ ] Approximate block/turnout allocation by area
   - [ ] Build sequence (which areas first?)

### Lower Priority (Can Be Determined Later)

9. **Version Control**
   - [ ] Git repo for JMRI configs? (Strongly recommended)
   - [ ] Master data in same repo?

10. **Testing & Validation**
    - [ ] How to validate generated JMRI configs before importing?
    - [ ] Test layout available, or only live layout?

---

## Immediate Next Steps

### Phase 1: Information Gathering (In Progress)

1. **Retrieve most recent JMRI profile**
   - Source: `/Users/blw/Library/Preferences/JMRI/CO_in_Virginia.jmri/`
   - Or: Git repository (if committed)
   - Goal: Get authoritative current block/turnout/sensor inventory

2. **Photograph current construction**
   - Arsenal expanded yard area (2-track → 3-track)
   - Extended VAL staging with block boundaries marked
   - Fork Union connector section
   - Goal: Validate block/turnout counts, understand track flow

3. **Document Fork Union specifics**
   - Turnout count and addresses
   - Block count and sensor assignments
   - How it connects to helix approach

4. **Signal architecture decision**
   - Define signal mast type
   - Define placement strategy
   - Sketch signal locations on track plan or master data
   - Goal: Ready to generate signal definitions once blocks are complete

### Phase 2: Master Data Consolidation (Following Phase 1)

1. Create complete master data JSON with:
   - All 28 current blocks (verified from JMRI export)
   - Fork Union blocks (from photographs/documentation)
   - Extended VAL staging (from JMRI verification)
   - All turnouts with addresses and sensor mappings
   - Placeholder entries for unbuilt areas

2. Version control master data in git

3. Test generator against current state (should produce XML matching existing JMRI config)

### Phase 3: Signal Definitions (Following Phase 2)

1. Design signal mast logic
2. Expand generator to create signal mast definitions
3. Generate signal rules (occupancy + interlocking)
4. Test in JMRI

### Phase 4: Incremental Expansion (Ongoing)

1. As each new area is built:
   - Add blocks/turnouts to master data
   - Run generator
   - Import into JMRI
   - Test hardware
   - Commit to git

---

## Project Timeline (Estimated)

| Phase | Activity | Effort | Timeline |
|-------|----------|--------|----------|
| 1 | Information gathering | 2-3 hours | This week |
| 2 | Master data consolidation | 3-4 hours | Following week |
| 2 | Generator testing & refinement | 2-3 hours | Following week |
| 3 | Signal design & implementation | 3-4 hours | Week after |
| 3 | Signal generator expansion | 2-3 hours | Week after |
| 4+ | Incremental area expansion | 15-30 min/area | Ongoing as built |

**Total to full automation capability: ~15-20 hours of focused work**

---

## Success Criteria

1. **Master data accurately represents layout** (all blocks, turnouts, sensors documented)
2. **Generated JMRI config matches existing manually-created config** (bit-for-bit if possible, or at least functionally identical)
3. **New areas can be added to master data and generated into JMRI without manual configuration**
4. **DispatcherPro can create transits and dispatch trains using generated blocks/signals**
5. **All configurations under git version control** with clear commit history

---

## Notes & Observations

### Architecture Decisions Made (Good Ones)
- LCC Tower boards for occupancy detection (clean, modular, works well)
- MQTT + ESP32 for servo control (scalable, WiFi-based, flexible)
- JMRI layout editor for visual representation
- Tortoise Switches for high-reliability turnouts in critical areas (Gordonsville)
- DispatcherPro for automation (proper signaling + interlocking)

### Deviations from Byron's Plan (Smart Adaptations)
- Arsenal yard expansion (addresses operational needs)
- Extended VAL staging (better train length handling)
- Fork Union connector (ties VAL to lower level)
- Richmond replacing original main staging (better space utilization, industry focus)
- Lower-level main staging (vertical organization improvement)

### Design Patterns to Maintain
- Semantic versioning for generators and master data
- Comprehensive test coverage
- Git version control for everything
- Professional engineering discipline in hobby project
- Modular/scalable infrastructure

---

## Document Status

- **Last Updated:** 2025-01-20
- **Next Update:** After retrieving current JMRI profile and photographs
- **Owner:** Brian Whitacre
- **Reviewer:** Claude (AI Assistant)

**To Complete This Document:**
1. [ ] Provide current JMRI profile export
2. [ ] Provide photographs of built areas
3. [ ] Clarify signal architecture requirements
4. [ ] Provide Fork Union block/turnout inventory
5. [ ] Define DispatcherPro transit strategy
