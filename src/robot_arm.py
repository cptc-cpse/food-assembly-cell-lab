# Group 4: RobotArm Class
# TODO: Implement the RobotArm class here
# See README.md for the class contract and required methods

# this code is owned by Rachel

class RobotArm:

    def __init__(self):
        self.placement_count = 0
        self.success_count = 0
        self.failure_count = 0

    def place(self, tray, compartment, station, target_g):
        """
        Simulate placing an ingredient on the tray.
        
        Args:
            tray: Tray object
            ingredient: Name of the ingredient to place
            station: IngredientStation object to get the ingredient from
            target: Target grams to place
            """
        self.placement_count += 1
        dispense_results = station.dispense(target_g)
        actual_grams = dispense_results['actual_g']
        success = actual_grams > 0

        if success:
            tray.add_food(compartment, actual_grams)
            self.success_count += 1
        else:
            self.failure_count += 1
        return {
            "compartment": compartment,
            "target_g": target_g,
            "success": success,
            # TODO: variabnce
        }
    
    def to_json(self):
        success_rate = 0
        if self.placement_count > 0:
            success_rate = self.success_count / self.placement_count
        return {
            "placement_count": self.placement_count,
            "success_count": self.success_count,
            "failure_count": self.failure_count,
            "success_rate": success_rate
        }