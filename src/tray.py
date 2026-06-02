# Group 1: Tray Class
# See README.md for the class contract and required methods

#This code is owned by Evan and Cameron

class Tray:
    """
    trays.csv:
    tray_id,meal_type,compartment_a,compartment_b,compartment_c,target_a_g,target_b_g,target_c_g
    T001,protein_bowl,rice,chicken,vegetables,120,90,60
    T002,protein_bowl,rice,chicken,vegetables,120,90,60
    T003,veggie_bowl,rice,tofu,vegetables,110,80,75
    T004,curry_meal,rice,curry,vegetables,130,100,50
    T005,curry_meal,rice,curry,vegetables,130,100,50

    Behavior:
    - When built from CSV, `recipe` is the three compartment ingredient names.
    - `compartments` starts with zero grams for each ingredient in the recipe.
    - `add_food()` should reject unknown compartments and should update the tray state.
    - The tray can use a status such as `empty`, `in_progress`, or `complete`.
    - `total_error()` should compute error for every ingredient in `targets`.
    """
    @classmethod
    def from_csv(cls, row: dict) -> Tray: 
        """
        Parse one CSV row and build a tray with a recipe list and a targets dict.

        Args:
            row: Dict with keys tray_id, meal_type, compartment_a, compartment_b, 
                compartment_c, target_a_g, target_b_g, target_c_g

        Returns:
            Tray object initialized from the CSV row
        """
        recipe = [row["compartment_a"], row["compartment_b"], row["compartment_c"]]
        targets = {
            row["compartment_a"]: int(row["target_a_g"]),
            row["compartment_b"]: int(row["target_b_g"]),
            row["compartment_c"]: int(row["target_c_g"])
        }
        return cls(row["tray_id"], row["meal_type"], recipe, targets)
    
    def __init__(self, tray_id: str, meal_type: str, recipe: list, targets: dict):
        """
        Store tray metadata, build a compartments dict, and set initial status.

        Args:
            tray_id: Unique identifier for the tray (e.g. "T001")
            meal_type: Type of meal (e.g. "protein_bowl")
            recipe: List of ingredient names in the order of compartments (e.g. ["rice", "chicken", "vegetables"])
            targets: Dict mapping ingredient name → target grams (e.g. {"rice": 120, "chicken": 90, "vegetables": 60})
        """
        self.tray_id = tray_id
        self.meal_type = meal_type
        self.recipe = recipe
        self.targets = targets
        self.compartments = {compartment: 0 for compartment in recipe}
        self.status = "empty"

    def add_food(self, compartment: str, grams: int) -> int:
        """""
        Add grams to a named compartment, update the state, and return 
        the new total.

        Args:
            compartment: Name of the compartment to add food to (e.g. "rice")
            grams: Amount of food to add in grams (e.g. 50)

        Returns:
            New total grams in the specified compartment after adding (e.g. 170)
        """""
        self.compartments[compartment] += grams
        if all(self.compartments[comp] >= self.targets[comp] for comp in self.compartments.keys()):
            self.status = "complete"
        else: 
            self.status = "in progress"
        return grams

    def total_error(self) -> int:
        """
        Compare actual weight to each target and return the summed 
        absolute error.

        Returns:
            Total difference between actual and target weights across all compartments (e.g. 30)
        """
        total_error = 0
        for compartment in self.compartments:
            error = abs(self.compartments[compartment] - self.targets[compartment])
            total_error += error
        return total_error

    def to_json(self) -> dict:
        """
        Returns: 
            A dictionary with tray_id, meal_type, recipe, targets, 
            compartments, total_error, and status.
        """
        tray = {
            "tray_id": self.tray_id,
            "meal_type": self.meal_type,
            "recipe": self.recipe,
            "targets": self.targets,
            "compartments": self.compartments,
            "total_error": self.total_error(),
            "status": self.status
        }
        return tray    