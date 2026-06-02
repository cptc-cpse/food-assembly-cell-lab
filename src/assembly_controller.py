SKIP = "skip"
PLACE = "place"
class AssemblyController:
    def __init__(self, tolerance_g=20):
        self.tolerance_g = int(tolerance_g)
        self.decisions_made = 0
        self.quality_checks_count = 0
        self.reject_count = 0


    def decide(self, tray, ingredient_name):
        if ingredient_name not in tray.recipe:
            return SKIP
        
        current_g = tray.compartments.get(ingredient_name, 0)
        target_g = tray.recipe.get(ingredient_name, 0)
        if current_g >= target_g - self.tolerance_g:
            print("skipped due to sufficient ingredient already present")
            return SKIP

        return PLACE
    
    def check_quality(self, tray):
        self.quality_checks_count += 1

        total_error = tray.total_error()
        passed = total_error <= self.tolerance_g

        if not passed:
            self.reject_count += 1
        
        error_per_compartment = {
            compartment: abs(tray.compartments.get(compartment, 0) - target_g)
            for compartment, target_g in tray.recipe.items()
        }

        return {
            "tray_id": tray.id,
            "passed": passed,
            "total_error": total_error,
            "error_per_compartment": error_per_compartment,
            "tolerance_g": self.tolerance_g
        }
    
    def to_json(self):
        rejection_rate += 0

        if self.quality_checks_count > 0:
            rejection_rate = self.reject_count / self.quality_checks_count

        return {
            "tolerance_g": self.tolerance_g,
            "decisions_made": self.decisions_made,
            "quality_checks_count": self.quality_checks_count,
            "reject_count": self.reject_count,
            "rejection_rate": rejection_rate
        }
    