# Group 1: Tray Class
# Represents a meal tray with food compartments and target portions.

class Tray:
    """
    A meal tray with compartments for different food items.
    Tracks target portions and actual portions placed.
    """
    
    def __init__(self, tray_id, meal_type, recipe, targets):
        """
        Initialize a tray.
        
        Args:
            tray_id: Unique identifier (e.g., "T001")
            meal_type: Type of meal (e.g., "protein_bowl")
            recipe: List of ingredient names (e.g., ["rice", "chicken", "vegetables"])
            targets: Dict of target grams per ingredient (e.g., {"rice": 120, "chicken": 90})
        """
        # TODO: Store tray_id, meal_type, recipe, targets
        # TODO: Initialize compartments dict (maps ingredient name → grams placed so far)
        # TODO: Initialize status as "pending" or similar
        pass
    
    @classmethod
    def from_csv(cls, row):
        """
        Create a Tray from a CSV row.
        
        Row format (from trays.csv):
        tray_id, meal_type, compartment_a, compartment_b, compartment_c, 
        target_a_g, target_b_g, target_c_g
        
        Example row:
        "T001,protein_bowl,rice,chicken,vegetables,120,90,60"
        
        Args:
            row: Dict or list from CSV (with keys: tray_id, meal_type, 
                 compartment_a, compartment_b, compartment_c, target_a_g, target_b_g, target_c_g)
        
        Returns:
            Tray object
        """
        # TODO: Parse row dict
        # TODO: Extract tray_id, meal_type
        # TODO: Extract compartment names (compartment_a, _b, _c) → recipe list
        # TODO: Extract target grams (target_a_g, _b_g, _c_g) → targets dict
        # TODO: Return new Tray(...)
        pass
    
    def add_food(self, compartment, grams):
        """
        Add food (weight) to a compartment.
        
        Args:
            compartment: Ingredient name (e.g., "rice")
            grams: Weight in grams to add
        
        Returns:
            New total weight in that compartment
        """
        # TODO: Update the compartment weight in self.compartments
        # TODO: Return the new total weight
        pass
    
    def total_error(self):
        """
        Calculate total error across all compartments.
        
        Error for a compartment = |actual - target|
        Total error = sum of all compartment errors
        
        Returns:
            Total error in grams (float)
        """
        # TODO: Loop through recipe
        # TODO: Get target for each ingredient from self.targets
        # TODO: Get actual from self.compartments
        # TODO: Sum absolute differences
        # TODO: Return total
        pass
    
    def to_json(self):
        """
        Return a JSON-ready dictionary representation.
        
        Returns:
            Dict with keys: tray_id, meal_type, recipe, targets, compartments, total_error, status
        """
        # TODO: Return a dict with all tray state
        # Example:
        # {
        #     "tray_id": "T001",
        #     "meal_type": "protein_bowl",
        #     "recipe": ["rice", "chicken", "vegetables"],
        #     "targets": {"rice": 120, "chicken": 90, "vegetables": 60},
        #     "compartments": {"rice": 118, "chicken": 92, "vegetables": 59},
        #     "total_error": 5.0,
        #     "status": "complete"
        # }
        pass
