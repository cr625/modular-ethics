
from event_motor.memory_manager import MemoryManager
from event_motor.scenario_parser import parse_scenario

# Load the scenario file
scenario_file = "scenarios/dryrun-adept-eval-MJ2.yaml"
scenario = parse_scenario(scenario_file)

# Initialize and run the Event Motor
motor = EventMotor()
motor.run(scenario)
