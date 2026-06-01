# CSV Data Reference

This folder contains the input data files used by the assembly cell simulation.

## trays.csv
- `tray_id`: Unique identifier for each tray.
- `meal_type`: Name of the meal plan or recipe type.
- `compartment_a`: Ingredient name for tray compartment A.
- `compartment_b`: Ingredient name for tray compartment B.
- `compartment_c`: Ingredient name for tray compartment C.
- `target_a_g`: Target grams for the ingredient in compartment A.
- `target_b_g`: Target grams for the ingredient in compartment B.
- `target_c_g`: Target grams for the ingredient in compartment C.

Each row represents one tray to assemble in the simulation. The row defines:
- the tray identity used for reporting,
- the meal type for labeling,
- the three ingredients the tray should receive,
- the target portion weight for each ingredient.

The logic uses this row to build a `Tray` with a recipe list and a targets dict. The robot and controller refer to this recipe when deciding which ingredient goes into each compartment.

## ingredients.csv
- `ingredient_name`: Name of the ingredient station.
- `starting_inventory_g`: How many grams of that ingredient are available at the start.
- `portion_variability_g`: The maximum dispense variation in grams around the target portion.

Each row represents one ingredient station in the system. The row defines:
- which ingredient the station holds,
- how much inventory is available for all trays,
- how much randomness the station adds to each dispense.

The logic uses this row to build an `IngredientStation` that supplies food during placement. The robot calls `station.dispense(target_g)` and the actual amount delivered is based on the station’s inventory and variability.
