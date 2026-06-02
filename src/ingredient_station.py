# Group 2: IngredientStation Class
# TODO: Implement the IngredientStation class here
# See README.md for the class contract and required methods

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
        return cls(row["station_id"], row["ingredient_name"])
    
    def __init__(self, station_id: str, ingredient: str):
        """
        Store station metadata and set a fixed dispense amount.
        """
        self.station_id = station_id
        self.ingredient = ingredient
        self.dispense_amount = 10  # Fixed amount in grams for simplicity

    def dispense(self) -> int:
        """""
        Return the fixed amount of grams for the ingredient.
        """""
        return self.dispense_amount