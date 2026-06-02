# Group 2: IngredientStation Class
# TODO: Implement the IngredientStation class here
# See README.md for the class contract and required methods
import random
class IngredientStation:
    """
    ingredient_stations.csv:
    station_id,ingredient_name
    rice
    chicken
    vegetables
    curry
    tofu

    Behavior:
    - When built from CSV, `ingredient` is the ingredient name.
    - `dispense()` should return a fixed amount of grams for the ingredient.
    """
    @classmethod
    def from_csv(cls, row: dict) -> IngredientStation: 
        """
        Parse one CSV row and build an ingredient station with an ingredient name.
        """
        return cls(row["ingredient_name"], row["starting_inventory_g"], row["portion_variability_g"])
    
    def __init__(self, name, inventory_g, variability_g):
        """
        Store station metadata and set a fixed dispense amount.
        """
        self.name = name
        self.inventory_g = int(inventory_g)
        self.variability_g = int(variability_g)
        self.dispense_count = 0

    def dispense(self, target_g) -> int:
        variance = random.randint(-self.variability_g, self.variability_g)
        actual_g = max(0, target_g + variance)
        actual_g = min(actual_g, self.inventory_g)

        self.inventory_g -= actual_g
        self.dispense_count += 1
        return {
            "target_g": target_g,
            "actual_g": actual_g,
            "variance": variance,
            "inventory_remaining_g": self.inventory_g
        }
    
    def to_json(self):
        return {
            "name": self.name,
            "inventory_g": self.inventory_g,
            "dispense_count": self.dispense_count,
            "inventory_remaining_g": self.inventory_g
        }