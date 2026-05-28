# COVA Prototype Geography, Operations, and Timetable Simulator Notes

*C&O Railway, Virginia Division — August/October 1943*

---

## Prototype Territory

### The "X" — Why This Location

The layout models the most operationally significant piece of the C&O during WWII:
the convergence of four traffic corridors near Lindsay and Gordonsville, Virginia.

```
              Washington, D.C.
                    │
               Washington Sub
                    │
    Clifton Forge ──┼── (main line) ──┼── Mineral/Arsenal ── Richmond/Newport News
    / Staunton    Gordonsville       (Piedmont Sub, east)
                    │
                Lindsay (VAL junction)
                    │
               Virginia Air Line
                    │
            Fork Union / Strathmore
                    │
           Richmond / Newport News
           (alternate southern route)
```

The short Lindsay→Gordonsville segment was the **busiest piece of the C&O during
the war years** because it carried:
- All main line traffic (east–west)
- All northbound VAL traffic merging at Lindsay onto the main line
- Passenger train sections splitting and combining at Charlottesville
- Coal loads heading north to Washington and beyond via the Washington Sub
- Coal empties returning from Newport News/Tidewater via both the main line and VAL

---

## Layout Geography

### What Is Modeled

**Main line (east to west):**
```
East staging  ←→  Arsenal (at Mineral)  ←→  Gordonsville  ←→  Lindsay  ←→
  [magic gap]  ←→  Charlottesville  ←→  Crozet  ←→  Greenwood  ←→  Afton  ←→
  North Mountain  ←→  West staging
```

**Washington Sub (north from Gordonsville):**
```
Gordonsville  →  Washington Sub staging  [represents Washington D.C.]
```

**Virginia Air Line (south from Lindsay):**
```
Lindsay  →  [intermediate stations]  →  Fork Union  →  VAL staging
                                                        [represents Strathmore
                                                         / Richmond via Air Line]
```

### Key Locations

**Charlottesville** — on-layout. The split/combine point for named passenger trains.
Eastbound GW/FFV/Sportsman sections depart separately from here; westbound sections
arrive separately and are conceptually combined for the run west. The large passenger
station is the primary human-interest vignette of the layout.

**Lindsay** — on-layout, explicitly modeled. The Virginia Air Line junction. Between
Charlottesville and Gordonsville on the main line. All VAL traffic joins the main
line here before the Gordonsville junction.

**Gordonsville** — on-layout, the primary railfan viewing location. Two-way junction:
main line passes through east–west; Washington Sub branches north. The C&O station
had tracks on two sides (Washington Sub on one side, main line / Piedmont on the
other). The Gordonsville North Wye handles turning movements.

**Arsenal (at Mineral)** — on-layout, slightly east of Gordonsville on the main line.
A wartime ordnance/ammunition depot. Served by local freight switcher jobs.
Has a gate, a plant track, and a warehouse track (three distinct spots).

**Fork Union** — on-layout. Intermediate station on the Virginia Air Line with
actual switching work (team tracks, local industry).

**Afton** — on-layout. Represents the Blue Ridge crossing. Significant grade requiring
helper operations westbound. Helper pocket nearby.

### Selective Compression / "Magic Gaps"

- Between **Crozet and Charlottesville**: some main line distance compressed
- **VAL south of Fork Union** to Strathmore: represented by VAL staging
- **Main line east of Mineral** to Richmond city line: represented by east staging
- The staging endpoints are designed so trains can run in all appropriate directions
  without excessive re-staging between sessions

### Staging Endpoints and What They Represent

| Staging | Represents | Primary traffic |
|---|---|---|
| West staging | Waynesboro / Staunton / Clifton Forge and west | Main line through freights, passenger trains, helpers returning |
| Washington Sub staging | Washington D.C. and north (via RF&P connection) | Coal loads northbound, passenger Washington sections |
| East staging | Louisa / Richmond direction via Piedmont Sub | Coal empties, through freights, passenger Virginia sections |
| VAL staging | Strathmore / Richmond via Air Line | VAL coal, VAL passenger sections, locals |

---

## Prototype Trains and Traffic

### Named Passenger Trains (public timetable, October 1943)

All three named trains have **Washington** and **Virginia sections** that split
(eastbound) or combine (westbound) at **Charlottesville**.

| Train | Name | Washington Section | Virginia Section |
|---|---|---|---|
| 1 / 2 | George Washington | All-Pullman, NY–Cincinnati via Washington | Newport News–Cincinnati via Air Line or Piedmont |
| 3 / 4 | Fast Flying Virginian (FFV) | Washington section | Virginia section |
| 5 / 47 | The Sportsman | Washington section | Virginia section |

**At Gordonsville** (eastbound): each Washington section takes the Washington Sub
northward; each Virginia section continues east on the main line (or via Lindsay
to VAL) toward the Virginia coast. Two trains in close succession.

**At Gordonsville** (westbound): two trains arrive in close succession — one from
the Washington Sub, one from the east — both continuing west to Charlottesville.

### Freight (Employee Timetable)

**Scheduled:**
- **#90 / #91**: Hot merchandise manifests, on schedule (employee timetable)
- **#410** (VAL local): 1-car local on the Air Line, runs south on the VAL. Has
  work at Fork Union and other stops. C&O practice: head-end caboose behind the
  locomotive, plus tail caboose.

**Extras (stochastic — not on timetable):**
- **Coal empties, eastbound/southbound**: Newport News direction, roughly hourly
  during war years. Modeled as Poisson process with historically-calibrated rate.
- **Coal loads, northbound**: From Newport News via VAL through Lindsay and
  Gordonsville, up the Washington Sub. 4–5 per day but irregular timing.
- **Mixed freight / merchandise extras**: Irregular; probability window across
  the operating day.

### Helper Operations (Afton Mountain)

Westbound trains requiring helpers get a pusher at the foot of the grade. Helpers
return eastbound light to the helper pocket after topping the grade. This is a
distinct traffic pattern on the west end of the layout. Helper assignment depends
on tonnage (variable consists) and grade rating.

---

## Consist Rules

### General Principles

C&O consists follow prototype practice for the era. Key rules:

**All freight trains:** caboose always on the tail end.

**C&O local freights** (including #410, Arsenal switcher jobs): **head-end caboose**
between the locomotive and the train body, PLUS tail caboose.
```
[Loco] → [Caboose] → [freight cars] → [Caboose]
```

**Through freight / coal trains:** no head-end caboose.
```
[Loco(s)] → [freight cars] → [Caboose]
```

**Passenger trains:** specific car order with positional constraints:
```
[Power] → [Baggage / Express] → [RPO] → [Coaches] → [Diner] → [Sleepers] → [Observation]
```
Observation car is always tail-end. Head-end equipment (baggage, RPO, express) is
always immediately behind the power.

### Consist Templates (sketch — to be refined)

```yaml
# Washington section (GW, FFV, Sportsman)
passenger-washington-section:
  power: {class: L-2 Mallet / T-1, count: 1}
  segments:
    - {role: baggage,     count: {min: 1, max: 2}}
    - {role: rpo,         count: 1}
    - {role: coach,       count: {min: 2, max: 3}}
    - {role: diner,       count: 1}
    - {role: sleeper,     count: {min: 2, max: 4}}
    - {role: observation, count: 1, position: tail}

# Virginia section (GW, FFV, Sportsman) — shorter consist
passenger-virginia-section:
  power: {class: similar}
  segments:
    - {role: baggage,     count: 1}
    - {role: coach,       count: {min: 2, max: 3}}
    - {role: diner,       count: 1}
    - {role: sleeper,     count: {min: 1, max: 3}}
    - {role: observation, count: 1, position: tail}

# Coal train (loaded, northbound)
coal-loaded:
  power: {class: H-7 articulated, count: 1}
  segments:
    - {role: hopper-loaded, count: {min: 80, max: 130, distribution: normal}}
    - {role: caboose, count: 1, position: tail}

# Coal train (empties, eastbound/southbound)
coal-empty:
  power: {class: H-7 or similar, count: 1}
  segments:
    - {role: hopper-empty, count: {min: 80, max: 130}}
    - {role: caboose, count: 1, position: tail}

# VAL local freight (#410 or similar)
local-freight-val:
  power: {class: K-4 Mikado, count: 1}
  segments:
    - {role: caboose, count: 1, position: head}   # C&O local practice
    - {role: freight-mixed, count: {min: 8, max: 20}}
    - {role: caboose, count: 1, position: tail}

# Hot manifest (#90/#91)
manifest-freight:
  power: {class: K-4 or similar, count: 1}
  segments:
    - {role: boxcar-merchandise, count: {min: 30, max: 60}}
    - {role: caboose, count: 1, position: tail}
```

---

## Timetable Simulator Architecture

### Concept

The goal is a **historical railroad scene simulator**, not a car-forwarding operations
system. The user is a railfan "sitting at Gordonsville on June 8, 1943 watching trains
go by" — not an operator managing car movements. OperationsPro's car-routing model
is not the primary driver.

### The Three Layers

1. **Historical timetable** (config file): fixed-schedule trains from employee and
   public timetables, with exact times at each modeled station. Source: C&O TT No. 132
   (August 1943, Richmond Division) and companion Clifton Forge Division timetable.

2. **Stochastic extras** (probability model): coal trains and miscellaneous freight
   that ran as extras, not on the timetable. Modeled as Poisson processes with
   historically-calibrated parameters (daily count, mean interval).

3. **Orchestrator script** (Jython/JMRI): watches the fast clock, launches DP Active
   Trains at pre-calculated staging departure times so trains arrive at Gordonsville
   on schedule.

### Launch Time Calculation

The simulator pins arrival times at **Gordonsville** (the primary viewing location),
not at arbitrary waypoints. For each scheduled train:

```
staging_launch_time = gordonsville_arrival_time - actual_running_time_from_staging
```

This offset is calibrated empirically (run the train, measure the time) and stored
per train path. The fast clock ratio is a preference setting — trains will appear
at Gordonsville on schedule regardless of ratio, because the launch offset absorbs
the difference.

DispatcherPro handles all meets, section allocation, and signal aspects after
launch. The orchestrator does not concern itself with traffic conflicts.

### Timetable Config Format (sketch)

```yaml
fast_clock_ratio: 4          # 1 real minute = 4 fast-clock minutes
reference_date: "1943-06-08"

trains:
  # Fixed-schedule named passenger trains
  - id: gw-1-washington
    name: "George Washington #1 — Washington Section"
    type: fixed
    direction: westbound
    gordonsville_arrive: "10:47"
    gordonsville_depart: "10:52"
    transit: washington-sub-to-main-westbound
    consist: passenger-washington-section

  - id: gw-1-virginia
    name: "George Washington #1 — Virginia Section"
    type: fixed
    direction: westbound
    gordonsville_arrive: "10:54"   # minutes behind Washington section
    gordonsville_depart: "10:58"
    transit: main-line-east-to-west
    consist: passenger-virginia-section

  # Stochastic coal extras
  - id: coal-empty-eastbound
    name: "Newport News coal empties"
    type: stochastic
    direction: eastbound
    distribution: poisson
    mean_interval_min: 60
    daily_max: 18
    transit: main-line-west-to-east
    consist: coal-empty

  - id: coal-loaded-northbound
    name: "Coal loads via VAL, northbound"
    type: stochastic
    direction: northbound
    distribution: uniform
    daily_count: {min: 4, max: 6}
    transit: val-to-washington-sub
    consist: coal-loaded
```

### DP / OP Integration

- **OperationsPro role**: optional / secondary. Could be used to track car locations
  for staging plausibility, but does NOT drive the schedule.
- **DispatcherPro**: activated programmatically from the orchestrator at launch time.
  Handles all traffic management (meets, holds, section allocation) autonomously.
- **The orchestrator gap**: no built-in JMRI tool bridges "it's time to run train X"
  to "activate DP Active Train for train X." This requires a Jython script watching
  the fast clock and calling the DP API. To be built.

### Manual Intervention

DispatcherPro allows switching an Active Train to manual mode. The user can take
control of a specific job (e.g., the Arsenal switcher, a Charlottesville switching
move) while automated trains continue running around them. No special architecture
needed — this is native DP behavior.

---

## Timetable Data Sources

| Source | Coverage | Status |
|---|---|---|
| C&O Public TT Oct 1943 (24 pages, color scan) | Named passenger trains: GW, FFV, Sportsman. Tables 4, 5 (main line), Table 7 (VAL) | Scanned, in `Timetables/` |
| C&O Employee TT No. 132, Aug 1943 — Richmond Division | Freight manifests, locals east of Charlottesville, Richmond Div. all trains | Scanned (b&w), in `Timetables/` |
| C&O Employee TT — Clifton Forge Division | All trains west of Charlottesville, helper operations over Afton | Physical copy; partial scan |

**Extraction plan**: use vision model (Claude) to extract structured YAML from
clean public timetable scans (Tables 4, 5, 7); manual verification; then cross-
reference employee TTs for freight schedules.

**Key data points needed per train**:
- Gordonsville time (arrive / depart)
- Charlottesville time (for split/combine timing)
- Direction and which sub (Washington Sub, main line east, VAL)
- Train class (scheduled vs. extra; passenger / freight class)

---

## Open Questions

- [ ] Exact prototype times at Gordonsville for all named trains (pending extraction)
- [ ] Employee TT freight train numbers and times on both divisions
- [ ] Helper pocket location on layout — is it at Waynesboro? Crozet? Exact staging?
- [ ] DP API: can Active Trains be created programmatically from Jython? (Needs verification)
- [ ] OP role: use it at all, or run purely timetable-driven without car-forwarding?
- [ ] Fast clock ratio: 4:1 tentative; calibrate against Gordonsville scene "feel"
- [ ] Consist details: exact car counts and classes for each named train section
  (can be sourced from C&O historical society / passenger car records for 1943)
- [ ] Vision system for staging bootstrapping: design TBD (see conversation notes)
- [ ] RFID choke-point locations for ongoing car tracking: TBD with layout completion
