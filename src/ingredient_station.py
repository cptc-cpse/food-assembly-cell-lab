# Group 2: IngredientStation Class
# Manages ingredient inventory and portion dispensing with variability.

import random

class IngredientStation:
    """
    A station that dispenses a single ingredient (e.g., rice, chicken).
    Tracks inventory and adds realistic variability to portions.
    """
    
    def __init__(self, name, inventory_g, variability_g):
        """
        Initialize an ingredient station.
        
        Args:
            name: Ingredient name (e.g., "rice")
            inventory_g: Starting inventory in grams
            variability_g: Standard variability in grams (±variability around target)
        """
        # TODO: Store name, inventory_g, variability_g
        # TODO: Initialize dispensed_count = 0
        pass
    
    @classmethod
    def from_csv(cls, row):
        """
        Create an IngredientStation from a CSV row.
        
        Row format (from ingredients.csv):
        name, starting_inventory_g, portion_variability_g
        
        Example row:
        "rice,3000,5"
        
        Args:
            row: Dict or list from CSV (with keys: name, starting_inventory_g, portion_variability_g)
        
        Returns:
            IngredientStation object
        """
        # TODO: Parse row dict
        # TODO: Extract name, starting_inventory_g, portion_variability_g
        # TODO: Return new IngredientStation(...)
        pass
    
    def dispense(self, target_g):
        """
        Dispense a portion from this station.
        
        Adds random variability to simulate real-world inconsistency:
        actual_amount = target_g ± random value between 0 and variability_g
        
        Reduces inventory by the actual amount dispensed.
        
        Args:
            target_g: Target portion size in grams
        
        Returns:
            Dict with keys: ingredient_name, target_g, actual_g, variance_g
            Example: {"ingredient": "rice", "target": 120, "actual": 118, "variance": -2}
        """
        # TODO: Generate random variability (e.g., random.uniform(-variability_g, +variability_g))
        # TODO: Calculate actual_g = target_g + variance
        # TODO: Ensure actual_g is never negative
        # TODO: Reduce self.inventory_g by actual_g
        # TODO: Increment self.dispensed_count
        # TODO: Return dict with ingredient, target, actual, variance
        pass
    
    def to_json(self):
        """
        Return a JSON-ready dictionary representation.
        
        Returns:
            Dict with keys: name, inventory_g, variability_g, dispensed_count
        """
        # TODO: Return a dict with all station state
        # Example:
        # {
        #     "name": "rice",
        #     "inventory_g": 2880,
        #     "variability_g": 5,
        #     "dispensed_count": 10
        # }
        pass
