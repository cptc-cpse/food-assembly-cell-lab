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
      +-------------+
      |  Tray Enters |
      +------+------+ 
             |        
             v        
      +------------------+
      | Vision Detects   |
      | Tray Presence    |
      +--------+---------+   
               |           
          success?         
           /   \           
          v     v          
+-------------+  +------------------+
| Controller  |  | Tray is Missing / |
| Decides     |  | detection failed  |
+------+------+  +------------------+
       |                    
       v                    
+---------------------------------+            
| Robot Places Food Into Tray     |           
| Compartments                    |
+---------------------------------+            
       |                    
       v                    
+-------------+            
| Quality     |           
| Check       |           
+------+------+            
       |                    
       v                    
+------------------------+
| Results Saved &        |
| Visualized             |
+------------------------+
```

## Your Five Classes

Each group builds one class. The class files in `src/` are intentionally blank—use the method contracts below as your specification. **Your class must:**

- Store meaningful state (attributes)
- Have at least one method that changes state
- Interact with another class
- Return a JSON-ready dictionary via `to_json()`

## CSV Factory Methods

Each class has a **`from_csv(row)` class method** that creates an instance from a CSV row. This is a factory pattern that requires:

1. **Accept a CSV row** — The `row` parameter is a dictionary with column names as keys (passed by `csv.DictReader`)
2. **Extract values** — Pull out the fields you need from the dict
3. **Transform data** — Often you'll restructure values:
   - **Tray**: Combine `compartment_a`, `compartment_b`, `compartment_c` into a single `recipe` list
   - **Tray**: Combine `target_a_g`, `target_b_g`, `target_c_g` into a single `targets` dict
   - **IngredientStation**: Just extract the three fields directly
4. **Call the constructor** — Create and return a new instance: `return cls(arg1, arg2, ...)`

**Example from Tray.from_csv():**
```python
# Input row from CSV:
# {"tray_id": "T001", "meal_type": "protein_bowl", "compartment_a": "rice", 
#  "compartment_b": "chicken", "compartment_c": "vegetables", 
#  "target_a_g": "120", "target_b_g": "90", "target_c_g": "60"}

# Your method extracts and transforms:
recipe = [row["compartment_a"], row["compartment_b"], row["compartment_c"]]
targets = {
    row["compartment_a"]: int(row["target_a_g"]),
    row["compartment_b"]: int(row["target_b_g"]),
    row["compartment_c"]: int(row["target_c_g"])
}
return cls(row["tray_id"], row["meal_type"], recipe, targets)
```


### 1. **Tray** (Compartments & Recipes)
Represents a meal tray with food compartments and target portions.

**Key Methods:**
- `Tray.from_csv(row)` — Parse one CSV row and build a tray with a recipe list and a targets dict.
- `tray.__init__(tray_id, meal_type, recipe, targets)` — Store tray metadata, build a compartments dict, and set initial status.
- `tray.add_food(compartment, grams)` — Add grams to a named compartment, update the state, and return the new total.
- `tray.total_error()` — Compare actual weight to each target and return the summed absolute error.
- `tray.to_json()` — Return a dictionary with tray_id, meal_type, recipe, targets, compartments, total_error, and status.

**Behavior:**
- When built from CSV, `recipe` is the three compartment ingredient names.
- `compartments` starts with zero grams for each ingredient in the recipe.
- `add_food()` should reject unknown compartments and should update the tray state.
- The tray can use a status such as `empty`, `in_progress`, or `complete`.
- `total_error()` should compute error for every ingredient in `targets`.

---

### 2. **IngredientStation** (Dispensing & Inventory)
Manages ingredient inventory and portion dispensing with variability.

**Key Methods:**
- `IngredientStation.from_csv(row)` — Parse one CSV row and build a station.
- `station.__init__(name, inventory_g, variability_g)` — Store name, inventory, and variability.
- `station.dispense(target_g)` — Simulate a dispense event, apply random variance, update inventory, and return the actual amount.
- `station.to_json()` — Return a dictionary with name, inventory_g, variability_g, and dispensed_count.

**Behavior:**
- Dispensing should use random variation around `target_g` within ±`variability_g`.
- The actual dispensed amount must never exceed remaining inventory.
- If inventory is too low, dispense only what is available.
- Each successful dispense increments `dispensed_count`.
- The returned dispense result should include target, actual, variance, and remaining inventory.

---

### 3. **VisionSystem** (Detection & Measurement)
Uses computer vision to detect trays and measure portions on trays.

**Key Methods:**
- `vision.__init__()` — Initialize counters and measurement error tracking.
- `vision.detect(tray)` — Simulate a tray detection with a 95% success rate.
- `vision.measure(tray, compartment)` — Read the tray weight and add a realistic measurement error.
- `vision.to_json()` — Return a dictionary with detection_count, measurements_count, and average measurement error.

**Behavior:**
- `detect()` should increment a detection counter every time it runs.
- `measure()` should verify the compartment exists on the tray.
- Measurement error should be small (for example, ±5g) and should be recorded.
- The returned measurement data should include actual weight, measured weight, and measurement error.

---

### 4. **RobotArm** (Placement & Execution)
Controls robot arm to place food into compartments.

**Key Methods:**
- `robot.__init__()` — Initialize placement counters.
- `robot.place(tray, compartment, station, target_g)` — Dispense from the station, add food to the tray, and record success or failure.
- `robot.to_json()` — Return placements_count, success_count, failure_count, and success_rate.

**Behavior:**
- `place()` should call `station.dispense(target_g)` and then add the actual dispensed amount to the tray.
- If dispense returns `actual_g` as zero, the placement is a failure.
- Each placement attempt updates the robot arm counters.
- The returned placement result should include compartment, target, actual, success, and variance.

---

### 5. **AssemblyController** (Decision Logic & QA)
Makes placement decisions and checks final portion quality.

**Key Methods:**
- `controller.__init__(tolerance_g=20)` — Store tolerance and initialize counters.
- `controller.decide(tray, compartment, ingredient_name)` — Decide whether to place food or skip.
- `controller.check_quality(tray)` — Evaluate the tray and determine pass/fail.
- `controller.to_json()` — Return tolerance_g, decisions_made, quality_checks_count, rejections_count, and rejection_rate.

**Behavior:**
- `decide()` should return `place` only when the ingredient belongs in the tray and has not yet reached its target.
- If the tray already has enough of that ingredient, `decide()` should return `skip`.
- `check_quality()` should compare `tray.total_error()` against the tolerance.
- Rejected trays should be counted separately from passed trays.
- The quality report should include error per ingredient, total error, and whether the tray passed.

---

## Success Criteria

Your class implementation is complete when:
- ✓ Class is defined with `__init__()` method
- ✓ Initializes from CSV data using `from_csv()` class method
- ✓ Stores state correctly and implements all required methods
- ✓ At least one method modifies internal state
- ✓ Returns correct JSON dictionary from `to_json()`
- ✓ Integrates with other classes in the simulation
- ✓ Works correctly in the full `main.py` integration test

---

## Running the Lab

```bash
cd src
python main.py
```

This runs the simulation, saves `output/report.json`, and creates `output/portion_errors.png`.

