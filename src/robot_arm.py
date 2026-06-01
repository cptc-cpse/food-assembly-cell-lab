# Group 4: RobotArm Class
# Controls robot arm to place food into compartments.

class RobotArm:
    """
    A robotic arm that places food from ingredient stations into tray compartments.
    Tracks placement attempts and success/failure rates.
    """
    
    def __init__(self):
        """
        Initialize the robot arm.
        """
        # TODO: Initialize placements_count = 0
        # TODO: Initialize success_count = 0
        # TODO: Initialize failure_count = 0
        pass
    
    def place(self, tray, compartment, station, target_g):
        """
        Place food from an ingredient station into a tray compartment.
        
        Steps:
        1. Dispense from the station (gets actual amount with variability)
        2. Add the dispensed amount to the tray
        3. Return success/failure status
        
        Args:
            tray: Tray object
            compartment: Ingredient name (e.g., "rice")
            station: IngredientStation object to dispense from
            target_g: Target portion size in grams
        
        Returns:
            Dict with keys: compartment, target_g, actual_g, success
            Example: {"compartment": "rice", "target": 120, "actual": 118, "success": True}
        """
        # TODO: Increment self.placements_count
        # TODO: Call station.dispense(target_g) to get dispensed amount
        # TODO: Call tray.add_food(compartment, actual_g) to add to tray
        # TODO: Check if station has enough inventory (actual_g <= station inventory before dispense)
        # TODO: Set success = True if placement succeeded, False if failed
        # TODO: Increment self.success_count or self.failure_count
        # TODO: Return dict with compartment, target_g, actual_g, success
        pass
    
    def to_json(self):
        """
        Return a JSON-ready dictionary representation.
        
        Returns:
            Dict with keys: placements_count, success_count, failure_count, success_rate
        """
        # TODO: Return a dict with robot arm state
        # TODO: Calculate success_rate as success_count / placements_count
        # TODO: Handle division by zero (return 0.0 if no placements yet)
        # Example:
        # {
        #     "placements_count": 15,
        #     "success_count": 14,
        #     "failure_count": 1,
        #     "success_rate": 0.933
        # }
        pass
