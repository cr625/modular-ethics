import yaml
from event_motor.memory_manager import MemoryManager

def parse_scenario(file_path):
    """
    Parse the scenario YAML file and apply persistent state management.
    """
    with open(file_path, 'r') as file:
        scenario_data = yaml.safe_load(file)

    memory_manager = MemoryManager()

    # Iterate through scenes and update state
    for scene in scenario_data.get("scenes", []):
        scene = memory_manager.update_state(scene)

    return scenario_data
