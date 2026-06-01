# Group 3: VisionSystem Class
# Uses computer vision to detect and measure portions on trays.

import random

class VisionSystem:
    """
    A computer vision system that detects tray presence and measures portion weights.
    Simulates real vision accuracy with occasional errors.
    """
    
    def __init__(self):
        """
        Initialize the vision system.
        """
        # TODO: Initialize detection_count = 0
        # TODO: Initialize measurements_count = 0
        # TODO: Initialize measurement_errors list (to track accuracy over time)
        pass
    
    def detect(self, tray):
        """
        Detect if a tray is present and readable.
        
        Simulates 95% detection accuracy (5% of trays might be missed).
        
        Args:
            tray: Tray object to detect
        
        Returns:
            Bool: True if tray detected, False if missed
        """
        # TODO: Increment self.detection_count
        # TODO: Generate random value 0-100
        # TODO: Return True if random >= 5 (95% success rate)
        # TODO: Return False otherwise (5% miss rate)
        pass
    
    def measure(self, tray, compartment):
        """
        Measure the current weight in a tray compartment.
        
        Adds small random measurement error (±5 grams).
        
        Args:
            tray: Tray object
            compartment: Ingredient name (e.g., "rice")
        
        Returns:
            Dict with keys: compartment, actual_g, measured_g, measurement_error_g
            Example: {"compartment": "rice", "actual": 120, "measured": 118, "error": -2}
        """
        # TODO: Increment self.measurements_count
        # TODO: Get actual weight from tray.compartments[compartment]
        # TODO: Generate random measurement error (±5 grams, e.g., random.uniform(-5, 5))
        # TODO: Calculate measured_g = actual + error
        # TODO: Store error in self.measurement_errors list
        # TODO: Return dict with compartment, actual, measured, error
        pass
    
    def to_json(self):
        """
        Return a JSON-ready dictionary representation.
        
        Returns:
            Dict with keys: detection_count, measurements_count, avg_measurement_error_g
        """
        # TODO: Return a dict with vision system state
        # TODO: Calculate avg_measurement_error_g as mean of self.measurement_errors
        # TODO: Handle empty list case (return 0.0 if no measurements yet)
        # Example:
        # {
        #     "detection_count": 5,
        #     "measurements_count": 15,
        #     "avg_measurement_error_g": 1.2
        # }
        pass
