from typing import Any, List, Dict
from datetime import datetime
from models.itm_schema import Scenario, Event  # Correct import of Scenario and Event


class ScenarioState:
    """Manages the current state of the scenario."""

    def __init__(self):
        self.variables: Dict[str, Any] = {}

    def apply_event(self, event: Event):
        """Update the state based on the event effects."""
        if not event.effects:
            return

        print(f"Applying event: {event.id}")
        for effect in event.effects:
            variable = effect.variable
            value = effect.value
            self.variables[variable] = value
            print(f"Updated {variable} to {value}")

    def __str__(self):
        """String representation of the current state."""
        return f"Current State: {self.variables}"


class EventTrace:
    """Tracks the progression of events."""

    def __init__(self):
        self.events: List[Dict[str, Any]] = []

    def add_event(self, event: Event, status: str):
        """Log an event in the trace."""
        trace_entry = {
            "event_id": event.id,
            "status": status,
            "timestamp": datetime.utcnow().isoformat(),
        }
        self.events.append(trace_entry)
        print(f"Event logged: {trace_entry}")

    def __str__(self):
        """String representation of the event trace."""
        return f"Event Trace: {self.events}"


class EventMotor:
    """Processes scenarios and manages state and event traces."""

    def __init__(self):
        self.state = ScenarioState()
        self.trace = EventTrace()

    def process_event(self, event: Event):
        """Process a single event."""
        print(f"Processing event: {event.id}")
        self.state.apply_event(event)
        self.trace.add_event(event, status="processed")

    def process_scene_events(self, scene):
        """Process all events in a given scene."""
        if not hasattr(scene, "events") or not scene.events:
            print(f"No events found in scene: {scene.id}")
            return

        print(f"Processing events for scene: {scene.id}")
        for event in scene.events:
            self.process_event(event)

    def run(self, scenario: Scenario):
        """Run the scenario step by step."""
        print(f"Starting scenario: {scenario.id}")

        # Access initial variables from first_scene
        if hasattr(scenario, "first_scene") and scenario.first_scene:
            initial_state = scenario.first_scene.variables
            for variable, value in initial_state.items():
                self.state.variables[variable] = value
            print("Initialized state from first_scene.")
        else:
            print("No initial state found in first_scene.")

        print(self.state)

        # Process events for each scene
        if hasattr(scenario, "scenes") and scenario.scenes:
            for scene in scenario.scenes:
                print(f"Entering scene: {scene.id}")
                self.process_scene_events(scene)
        else:
            print("No scenes found in the scenario.")

        print("Scenario completed!")
        print(self.state)
        print(self.trace)


# Utility Functions
import yaml
from pydantic import ValidationError

import yaml
from pydantic import ValidationError
from models.itm_schema import Scenario  # Update this to match your import path

def parse_scenario(file_path: str) -> Scenario:
    """Parse a YAML scenario file and validate it against the schema."""
    print(f"Loading scenario from: {file_path}")
    with open(file_path, "r") as f:
        scenario_data = yaml.safe_load(f)

    # Debug: Log the loaded scenario data
    print("Loaded scenario data:")
    print(scenario_data)

    try:
        scenario = Scenario.model_validate(scenario_data)  # Perform validation
        print("Scenario successfully parsed and validated.")
        return scenario
    except ValidationError as e:
        print("Validation errors encountered during parsing:")
        print(e.json())  # Print detailed validation errors
        raise
