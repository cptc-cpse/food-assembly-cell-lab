# Group 3: VisionSystem Class
# TODO: Implement the VisionSystem class here
# See README.md for the class contract and required methods

# Ian and Kevin team has stolen this file. This is ours now.

# **Key Methods:**
# - `vision.__init__()` — Initialize counters and measurement error tracking.
# - `vision.detect(tray)` — Simulate a tray detection with a 95% success rate.
# - `vision.measure(tray, compartment)` — Read the tray weight and add a realistic measurement error.
# - `vision.to_json()` — Return a dictionary with detection_count, measurements_count, and average measurement error.

# **Behavior:**
# - `detect()` should increment a detection counter every time it runs.
# - `measure()` should verify the compartment exists on the tray.
# - Measurement error should be small (for example, ±5g) and should be recorded.
# - The returned measurement data should include actual weight, measured weight, and measurement error.

# we are getting output from? : tray.to_json()` — Return a dictionary with tray_id, meal_type, recipe, targets, compartments, total_error, and status
# so a list of ordered dictionary?

import json
import random

from tray import Tray

class VisionSystem:

    def __init__(self):
        self.detection_count = 0
        self.measurements_count = 0
        self.measurement_error = 0

    # - `vision.detect(tray)` — Simulate a tray detection with a 95% success rate.
    # - `detect()` should increment a detection counter every time it runs.
    def detect(self, tray: Tray) -> bool:
        self.detection_count = self.detection_count + 1
        success_rate = random.random(0, 100)  # generates a random number between 0 and 100

        if success_rate >= 95: # simulate 95% success rate
            return True
        else :
            return False

    # - `vision.measure(tray, compartment)` — Read the tray weight and add a realistic measurement error.
    # - `measure()` should verify the compartment exists on the tray.
    def measure(self, tray: Tray, compartment: dict) :
        pass

    # - `vision.to_json()` — Return a dictionary with detection_count, measurements_count, and average measurement error.
    def to_json(self) :
        return_val = {
            "detection_count": self.detection_count,
            "measurements_count": self.measurements_count,  
            "average_measurement_error": self.measurement_error
        }
        return return_val
