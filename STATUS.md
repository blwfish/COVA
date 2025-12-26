# COVA Layout Project Status

**Last Updated:** 2025-12-26

## Project Overview

3D model of Brian's COVA (Charlottesville, Orange & Virginia Air-Line) model railroad layout, converted from 3rdPlanIt DXF export.

## As-Built vs As-Planned Differences

The 3rdPlanIt DXF represents Byron's original plan. Significant changes have been made during construction:

### Currently Built & Operational

| Area | Plan Status | As-Built Changes |
|------|-------------|------------------|
| **Arsenal** | In plan | Expanded from 1 to 2-track yard (becoming 3-track) |
| **Gordonsville Yard** | In plan | Built as planned; passing siding half-built, wired, NOT in JMRI |
| **Lindsay to Woolen Mills** | In plan | Built as planned, operational |
| **VAL Staging** | 3 tracks, 1 block each | Extended to 3 tracks × 2 blocks = 6 blocks; PLUS 2-foot helper pocket |
| **VAL Exit Connector** | In plan | Built, wired, NOT in JMRI (~18" before helix) |
| **Fork Union Connector** | NOT in plan | NEW: Hidden under layout, ~3-5 blocks, wired, NOT in JMRI |
| **Temporary Staging** | NOT in plan | 2-track reverse loop (will be removed when main staging built) |

### Planned But NOT Yet Built

| Area | Notes |
|------|-------|
| **Helix** | NOT BUILT - Fork Union ends ~18" short of helix connection |
| **Richmond Area** | NOT BUILT - Will replace original main staging location |
| **Main Staging (Lower Level)** | NOT BUILT - Being moved down one level for Richmond |
| **Pages 2 & 3 Unbuilt** | ~43+ blocks not yet built (Charlottesville, Lyndhurst, etc.) |
| **Upper Deck** | NOT BUILT - geometry in model but track not laid |

### Areas Removed/Relocated from Plan

| Original Plan | Change |
|---------------|--------|
| Main staging (original location) | Replaced by Richmond area |
| Original staging topology | Moved to lower level, topology TBD |

## JMRI Configuration State

### Current JMRI Inventory (March 2025 export)

| Item | Count | Notes |
|------|-------|-------|
| **Blocks** | 28 | IB:AUTO:0001-0028 (skipping 0020, 0023) |
| **Turnouts** | 23 | 11 MQTT (ESP32), 12 SPROG (Tortoise) |
| **LCC Sensors** | 17 | 4 Tower Boards (C4, C5, F2, F3) |
| **MQTT Sensors** | 5 | Pushbuttons |
| **Routes** | 4+ | Basic routes defined |

### JMRI Block Assignments by Area

| Area | Blocks | Status |
|------|--------|--------|
| Arsenal | 0001-0003 | Operational |
| Gordonsville | 0004-0006, 0027-0028 | Operational |
| Lindsay | 0009, 0018-0019 | Operational |
| VAL Staging | 0010-0017 | Operational (but may need update for extensions) |
| Piedmont | 0021 | Operational |
| Louisa | 0026 | Operational |
| Staging (temp) | 0007-0008, 0022, 0024-0025 | Operational |

### Missing from JMRI

- Fork Union blocks (wired, tested, not in JMRI)
- VAL helper pocket block
- Gordonsville passing siding (half-built)
- Arsenal yard expansion (ST210+ turnouts lack user names)
- Signal masts (not yet designed)

## 3D Model State (`cova_layout_3d.FCStd`)

### Completed

- Full track geometry imported from DXF at correct elevations
- Double-track helix (30"/32.5" radius, ~4 turns) connecting decks
- Helix connections to approach tracks (Shape905, Shape158, Shape952, Shape679)
- Main deck benchwork surface (from Lower_Bench_Outline)
- Room walls extruded to 8'
- Two turntables with pits and bridges (Charlottesville @ 46.5", Afton @ 72")
- 14 clearance points highlighted in red
- 12 location labels added
- Track color-coded by layer/railroad

### Elevations (as-drawn)

| Level | Elevation | Description |
|-------|-----------|-------------|
| VAL Staging | 38.5" | Under-layout staging |
| Main Deck | 46.5" - 48" | C&O visible layout |
| Main Staging | 46.5" | Below main deck |
| Helix Bottom | 48" | Connects to main staging |
| Upper Deck | 65" - 72" | Mountain subdivision |
| Helix Top | 65" | Connects to upper deck |

**Note:** As-drawn elevations differ from as-built (VAL staging measured at 40", main deck 48-49").

### Location Labels

- Gordonsville, Woolen Mills, Arsenal Gate
- Charlottesville (turntable), Lindsay, VAL Branch
- Southern Crossing / Union Station
- Main Staging, Greenwood, Crozet
- Afton (upper turntable), VAL Staging

### Track Color Coding

| Color | Layer | Description |
|-------|-------|-------------|
| Blue | C_O | C&O main line |
| Green | Upr_Track | Upper deck |
| Purple | staging | Main staging |
| Orange | VAL, VAL_staging, VAL_ramps | Virginia Air Line |
| Red | SOU, Interchange | Southern Railway |
| Gray | hidden | Hidden track |
| Brown | structures | Structure footprints |
| Light Gray | Backdrops | Backdrop outlines |

### Object Organization

Groups created:
- Labels (12 objects)
- Helixes (2 objects)
- Ramps (3 objects)
- Turntables (4 objects)
- Walls (78 objects)
- Benchwork (2 objects)

## Files

| File | Description |
|------|-------------|
| `cova_layout_3d.FCStd` | Main FreeCAD 3D model |
| `cova_layout_analysis.md` | Layer-by-layer analysis report |
| `cova_layer_data.json` | Full object data with geometry |
| `cova_layer_summary.csv` | Layer statistics |
| `COVA_JMRI_Automation_Project_Doc.md` | JMRI automation requirements |
| `COVA_JMRI_Current_Analysis_March2025.md` | JMRI config analysis |

## TODO - FreeCAD Model Updates for JMRI

### Priority 1: Turnout Locations
- [ ] Identify and mark all 23 current turnouts in model
- [ ] Label with JMRI system names (ST200, M2TVAL-*, etc.)
- [ ] Color-code: MQTT (ESP32) vs SPROG (Tortoise)

### Priority 2: Block Boundaries
- [ ] Mark 28 current JMRI block boundaries
- [ ] Label with block names (Arsenal, Gordonsville-South-Turnout, etc.)
- [ ] Identify block boundaries for unbuilt areas

### Priority 3: As-Built Updates
- [ ] Add Fork Union connector (not in original DXF)
- [ ] Update VAL staging to show extended blocks + helper pocket
- [ ] Mark Arsenal yard expansion
- [ ] Note temporary staging (to be removed)

### Priority 4: Sensor Zones
- [ ] Visualize LCC Tower Board coverage areas
- [ ] Group by board (C4, C5, F2, F3)

## Hardware Infrastructure

### Occupancy Detection
- RRcir-kits LCC Tower boards
- 4 boards: C4 (Gordonsville), C5 (Staging), F2 (VAL), F3 (VAL extended)

### Turnout Control
- **Tortoises (16):** Gordonsville + Arsenal, via 2× SwitchIt8, DCC/SPROG
- **ESP32 + SG90 servos:** All remaining (~45+), via MQTT

### DCC
- SPROG command station
- Expandable to 3 additional boosters

## Source Data

- Original: `bw_5_18_1-13-22.3pi` (3rdPlanIt format)
- Exported: `all-layers-fixed.dxf` (AutoCAD 2000 format, codepage fixed)
- Units: Inches (scaled to mm in FreeCAD)
- JMRI Profile: `/Users/blw/Library/Preferences/JMRI/CO_in_Virginia.jmri/`
