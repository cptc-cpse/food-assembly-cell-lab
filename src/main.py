# Main Integration Script
# This file brings together all five classes to run the simulation.
# Most functions are TODOs for students to implement during the lab session.

import csv
import json
from pathlib import Path

from tray import Tray
# from ingredient_station import IngredientStation
from vision_system import VisionSystem
from robot_arm import RobotArm
from assembly_controller import AssemblyController

ROOT = Path(__file__).resolve()
DATA = ROOT / "data"
def load_csv(filename):
    """
    Load a CSV file and return list of dicts (one dict per row).
    
    Args:
        filename: Path to CSV file
    
    Returns:
        List of dicts, where each dict is one row
    """
    with open(filename, mode="r", encoding="utf-8") as file:
        return list(csv.DictReader(file))


def save_json(filename, data):
    """
    Save a dict or list as JSON to a file.
    
    Args:
        filename: Path to output JSON file
        data: Dict or list to save
    """
    # TODO: Open file for writing
    # TODO: Use json.dump() with indent=2 for readability
    # TODO: Close file
    pass


def create_trays(tray_rows):
    """
    Create Tray objects from CSV rows.
    
    Args:
        tray_rows: List of dicts from trays.csv
    
    Returns:
        List of Tray objects
    """
    return_list = []
    for tray_row in tray_rows:
        tray = Tray.from_csv(tray_row)
        return_list.append(tray)
    return return_list


def create_ingredient_stations(ingredient_rows):
    """
    Create IngredientStation objects from CSV rows.
    
    Args:
        ingredient_rows: List of dicts from ingredients.csv
    
    Returns:
        Dict mapping ingredient name → IngredientStation object
    """
    # return_dict = {}
    # for ingredient_row in ingredient_rows:
    #     station = IngredientStation.from_csv(ingredient_row)
    #     ingredient_name = ingredient_row["ingredient_name"]
    #     return_dict[ingredient_name] = station
    # return return_dict


def run_simulation(trays, stations, vision, robot, controller):
    """
    Run the main assembly simulation.
    
    For each tray:
    1. Vision detects the tray
    2. For each ingredient in the tray's recipe:
       a. Ask controller to decide ("place" or "skip")
       b. If "place", ask robot to place from the station
       c. Measure the result with vision
    3. After tray is done, check quality with controller
    
    Args:
        trays: List of Tray objects
        stations: Dict of ingredient_name → IngredientStation
        vision: VisionSystem object
        robot: RobotArm object
        controller: AssemblyController object
    
    Returns:
        List of events (dicts) tracking what happened during simulation
    """
    events = []
    
    # TODO: Loop through each tray
    #   TODO: Try to detect tray with vision.detect(tray)
    #   TODO: If not detected:
    #       - Record "missed_tray" event
    #       - Skip to next tray
    #   TODO: If detected:
    #       - Loop through tray.recipe
    #           - Get ingredient name
    #           - Get target grams from tray.targets[ingredient]
    #           - Get station from stations[ingredient]
    #           - Call controller.decide(tray, ingredient, ingredient)
    #           - If decision == "place":
    #               - Call robot.place(tray, ingredient, station, target)
    #               - Call vision.measure(tray, ingredient)
    #               - Record "portion_placed" event with placement and measurement info
    #           - Else (skip):
    #               - Record "portion_skipped" event
    #       - After all ingredients, call controller.check_quality(tray)
    #       - Record "tray_done" event with quality check result
    
    return events


def build_report(trays, stations, vision, robot, controller, events):
    """
    Build a comprehensive JSON report of the entire simulation.
    
    Args:
        trays: List of Tray objects (completed)
        stations: Dict of ingredient_name → IngredientStation
        vision: VisionSystem object
        robot: RobotArm object
        controller: AssemblyController object
        events: List of events from run_simulation
    
    Returns:
        Dict with keys: trays, stations, vision, robot, controller, events, summary
    """
    # TODO: Build report dict
    # TODO: Add "trays": [tray.to_json() for tray in trays]
    # TODO: Add "stations": {name: station.to_json() for name, station in stations.items()}
    # TODO: Add "vision": vision.to_json()
    # TODO: Add "robot": robot.to_json()
    # TODO: Add "controller": controller.to_json()
    # TODO: Add "events": events
    # TODO: Add "summary": dict with overall stats (total trays, detected, rejected, etc.)
    # TODO: Return report dict
    pass


def plot_portion_errors(events, filename):
    """
    Create a graph showing portion errors for each tray.
    
    X-axis: Tray IDs
    Y-axis: Total error in grams
    
    Args:
        events: List of events from run_simulation
        filename: Path to save PNG graph
    """
    import matplotlib.pyplot as plt
    
    # TODO: Extract tray_done events from events list
    # TODO: Build lists: tray_ids and errors
    # TODO: Create bar chart
    # TODO: Set labels: xlabel="Tray ID", ylabel="Total Error (g)", title="Portion Errors by Tray"
    # TODO: Add a horizontal line at y=tolerance to show target
    # TODO: Save figure to filename
    # TODO: Close figure
    pass


def main():
    """
    Main entry point. Orchestrate the entire lab activity.
    """
    print("=== AI Food Assembly Cell Lab ===\n")
    
    # Construct paths relative to project root
    project_root = Path(__file__).parent.parent
    data_dir = project_root / "data"
    output_dir = project_root / "output"
    
    # Load CSV data
    print("Loading tray and ingredient data...")
    # Load data/trays.csv and data/ingredients.csv
    tray_rows = load_csv(str(data_dir / "trays.csv"))
    ingredient_rows = load_csv(str(data_dir / "ingredients.csv"))

    # Create objects
    print("Creating objects from CSV data...")
    trays = create_trays(tray_rows)
    print(trays)
    # TODO: stations = create_ingredient_stations(ingredient_rows)
    vision = VisionSystem()
    robot = RobotArm()
    controller = AssemblyController(tolerance_g=20)
    
    # Run simulation
    print("Running simulation...")
    # events = run_simulation(trays, stations, vision, robot, controller)
    
    # Build report
    print("Building report...")
    # TODO: report = build_report(trays, stations, vision, robot, controller, events)
    
    # Save JSON report
    print("Saving output/report.json...")
    # TODO: save_json(str(output_dir / "report.json"), report)
    
    # Plot portion errors
    print("Creating output/portion_errors.png...")
    # TODO: plot_portion_errors(events, str(output_dir / "portion_errors.png"))
    
    print("\nDone! Check output/ folder for results.")


if __name__ == "__main__":
    main()
