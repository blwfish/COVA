# COVA Layout Project Status

**Last Updated:** 2025-12-26

## Project Overview

3D model of Brian's COVA (Charlottesville, Orange & Virginia Air-Line) model railroad layout, converted from 3rdPlanIt DXF export.

## Current State

### 3D Model (`cova_layout_3d.FCStd`)

**Completed:**
- Full track geometry imported from DXF at correct elevations
- Double-track helix (30"/32.5" radius, ~4 turns) connecting decks
- Helix connections to approach tracks (Shape905, Shape158, Shape952, Shape679)
- Main deck benchwork surface (from Lower_Bench_Outline)
- Room walls extruded to 8'
- Two turntables with pits and bridges (Charlottesville @ 46.5", Afton @ 72")
- 14 clearance points highlighted in red
- 12 location labels added

**Elevations (as-drawn):**
| Level | Elevation | Description |
|-------|-----------|-------------|
| VAL Staging | 38.5" | Under-layout staging |
| Main Deck | 46.5" - 48" | C&O visible layout |
| Main Staging | 46.5" | Below main deck |
| Helix Bottom | 48" | Connects to main staging |
| Upper Deck | 65" - 72" | Mountain subdivision |
| Helix Top | 65" | Connects to upper deck |

**Note:** As-drawn elevations differ slightly from as-built measurements.

### Location Labels
- Gordonsville
- Woolen Mills
- Arsenal Gate
- Charlottesville (turntable)
- Lindsay
- VAL Branch
- Southern Crossing / Union Station
- Main Staging
- Greenwood
- Crozet
- Afton (upper turntable)
- VAL Staging

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

## Known Issues / TODO

- [ ] Upper deck benchwork is hidden (rectangular approximation wasn't useful)
- [ ] Some ramp connections could use smoother curves
- [ ] Block boundaries not yet identified
- [ ] Turnout locations not specifically marked
- [ ] JMRI integration not started

## Source Data

- Original: `bw_5_18_1-13-22.3pi` (3rdPlanIt format)
- Exported: `all-layers-fixed.dxf` (AutoCAD 2000 format, codepage fixed)
- Units: Inches (scaled to mm in FreeCAD)

## Next Steps

1. Identify block boundaries for JMRI
2. Mark turnout locations
3. Extract track data for JMRI panel creation
4. Consider parametric reconstruction of key elements
