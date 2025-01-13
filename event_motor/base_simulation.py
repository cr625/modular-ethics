from models.itm_schema import Scenario
import yaml

def parse_scenario(file_path: str) -> Scenario:
    """Parse a scenario file and validate against the schema."""
    import yaml
    with open(file_path, "r") as f:
        scenario_data = yaml.safe_load(f)
    return Scenario.parse_obj(scenario_data)

print("Scenario model loaded.")