# Group 5: AssemblyController Class
# Makes placement decisions and checks final portion quality.

class AssemblyController:
    """
    The main controller that makes decisions about when to place food.
    Implements quality control by checking if portions are within tolerance.
    """
    
    def __init__(self, tolerance_g=20):
        """
        Initialize the assembly controller.
        
        Args:
            tolerance_g: Acceptable error in grams per portion (default 20)
        """
        # TODO: Store tolerance_g
        # TODO: Initialize decisions_made = 0
        # TODO: Initialize quality_checks_count = 0
        # TODO: Initialize rejections_count = 0
        pass
    
    def decide(self, tray, compartment, ingredient_name):
        """
        Decide whether to place food in a compartment.
        
        Simple logic: Always return "place" for now.
        (Students can add logic: skip if compartment already full, or skip if low inventory, etc.)
        
        Args:
            tray: Tray object
            compartment: Ingredient name (e.g., "rice")
            ingredient_name: Ingredient name (should match compartment)
        
        Returns:
            String: "place" or "skip"
        """
        # TODO: Increment self.decisions_made
        # TODO: For now, always return "place"
        # TODO: (Later: add logic to skip if target already met, or if ingredient is low, etc.)
        pass
    
    def check_quality(self, tray):
        """
        Check if a tray's portions meet quality standards.
        
        A tray passes if:
        - Each compartment's error is within tolerance_g
        - Total error is within (tolerance_g * number of compartments)
        
        Args:
            tray: Completed Tray object
        
        Returns:
            Dict with keys: tray_id, passed, error_per_compartment, total_error, tolerance_g
            Example:
            {
                "tray_id": "T001",
                "passed": True,
                "error_per_compartment": {"rice": 5, "chicken": 2, "vegetables": 1},
                "total_error": 8,
                "tolerance_g": 20
            }
        """
        # TODO: Increment self.quality_checks_count
        # TODO: Get tray.total_error()
        # TODO: Build error_per_compartment dict
        # TODO: Check if total_error <= tolerance_g * len(tray.recipe)
        # TODO: If not passed, increment self.rejections_count
        # TODO: Return dict with tray_id, passed, error_per_compartment, total_error, tolerance_g
        pass
    
    def to_json(self):
        """
        Return a JSON-ready dictionary representation.
        
        Returns:
            Dict with keys: tolerance_g, decisions_made, quality_checks_count, rejections_count, rejection_rate
        """
        # TODO: Return a dict with controller state
        # TODO: Calculate rejection_rate as rejections_count / quality_checks_count
        # TODO: Handle division by zero (return 0.0 if no checks yet)
        # Example:
        # {
        #     "tolerance_g": 20,
        #     "decisions_made": 15,
        #     "quality_checks_count": 5,
        #     "rejections_count": 0,
        #     "rejection_rate": 0.0
        # }
        pass
