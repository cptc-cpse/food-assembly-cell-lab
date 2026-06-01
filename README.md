# AI Food Assembly Cell Lab

A Programming for Industry 4.0 activity where students build an AI-powered food assembly robot.

## Directory Structure

```
food-assembly-cell-lab/
├── README.md           (This file)
├── src/                (All Python source code)
│   ├── main.py         (Integration script with TODOs)
│   ├── tray.py         (Group 1: Tray class)
│   ├── ingredient_station.py  (Group 2: IngredientStation class)
│   ├── vision_system.py       (Group 3: VisionSystem class)
│   ├── robot_arm.py    (Group 4: RobotArm class)
│   └── assembly_controller.py (Group 5: AssemblyController class)
├── data/               (Input CSV files)
│   ├── trays.csv
│   └── ingredients.csv
└── output/             (Output files - created by main.py)
    ├── report.json     (Generated simulation results)
    └── portion_errors.png (Generated visualization)
```

## Activity Overview

This lab simulates an automated food assembly system. Students work in **5 groups**, each building one Python class that represents a component of the robot. By the end, the classes integrate into a complete simulation.

### System Flow

```
Tray Enters → Vision Detects → Controller Decides → Robot Places → Quality Check → Results Saved & Visualized
```

## Your Five Classes

Each group builds one class. **Your class must:**

- Store meaningful state (attributes)
- Have at least one method that changes state
- Interact with another class
- Return a JSON-ready dictionary via `to_json()`

### 1. **Tray** (Compartments & Recipes)
Represents a meal tray with food compartments and target portions.

**Key Methods:**
- `Tray.from_csv(row)` — Create from CSV row
- `tray.recipe` — List of ingredient names
- `tray.targets` — Target grams per compartment
- `tray.add_food(compartment, grams)` — Add food to a compartment
- `tray.total_error()` — Calculate total error vs. targets
- `tray.to_json()` — Return JSON representation

**State:** tray_id, meal_type, compartments (dict), targets (dict), current food weights

---

### 2. **IngredientStation** (Dispensing & Inventory)
Manages ingredient inventory and portion dispensing with variability.

**Key Methods:**
- `IngredientStation.from_csv(row)` — Create from CSV row
- `station.dispense(target_g)` — Dispense portion (adds random variability)
- `station.to_json()` — Return JSON representation

**State:** name, inventory_g, variability_g, dispensed_count

---

### 3. **VisionSystem** (Detection & Measurement)
Uses computer vision to detect and measure portions on trays.

**Key Methods:**
- `vision.detect(tray)` — Detect if tray is present (return True/False)
- `vision.measure(tray, compartment)` — Measure current weight in a compartment
- `vision.to_json()` — Return JSON representation

**State:** detection_count, measurement_errors (tracking accuracy)

---

### 4. **RobotArm** (Placement & Execution)
Controls robot arm to place food into compartments.

**Key Methods:**
- `robot.place(tray, compartment, station, target_g)` — Place food from station into tray compartment
- `robot.to_json()` — Return JSON representation

**State:** placements_count, success_count, failure_count

---

### 5. **AssemblyController** (Decision Logic & QA)
Makes placement decisions and checks final portion quality.

**Key Methods:**
- `controller.decide(tray, compartment, ingredient_name)` — Return "place" or "skip"
- `controller.check_quality(tray)` — Check if portions meet tolerance
- `controller.to_json()` — Return JSON representation

**State:** tolerance_g, decisions_made, quality_checks_count, rejections_count

---

## Expected Files

- **data/trays.csv** — Input meal tray specifications
- **data/ingredients.csv** — Input ingredient inventory & variability
- **output/report.json** — Final simulation results (generated)
- **output/portion_errors.png** — Graph of portion errors per tray (generated)

## Success Criteria

Your class is working if:
- ✓ Initializes from CSV data
- ✓ Stores and updates state correctly
- ✓ Implements all required methods
- ✓ Returns correct JSON dictionary
- ✓ Integrates with other classes in the simulation
- ✓ Passes the integration test in `main.py`

## Stretch Ideas

- Add quality tolerance parameters to your class
- Track historical data (e.g., average dispensing error)
- Add logging or debug output
- Implement a rollback method if a tray fails
- Add statistical analysis (min/max/mean error)
- Extend CSV parsing to handle optional fields

## Running the Lab

```bash
cd src
python main.py
```

This runs the simulation, saves `output/report.json`, and creates `output/portion_errors.png`.

---

**Group Assignment:**
- Group 1: Edit `src/tray.py` (Tray class)
- Group 2: Edit `src/ingredient_station.py` (IngredientStation class)
- Group 3: Edit `src/vision_system.py` (VisionSystem class)
- Group 4: Edit `src/robot_arm.py` (RobotArm class)
- Group 5: Edit `src/assembly_controller.py` (AssemblyController class)

Work together on `src/main.py` to integrate all classes.