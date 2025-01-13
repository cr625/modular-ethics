import pytest
from event_motor.scenario_parser import parse_scenario

def test_parse_scenario(tmp_path):
    # Create a temporary YAML file
    scenario_content = """
    scenes:
      - id: Scene1
        state:
          environment:
            location: "market"
          supplies:
            - type: "Bandage"
              quantity: 2
          characters:
            - id: "Shooter"
              name: "Alderson"
        persist_characters: true
      - id: Scene2
        state:
          supplies:
            - type: "Tourniquet"
              quantity: 1
    """

    scenario_file = tmp_path / "scenario.yaml"
    scenario_file.write_text(scenario_content)

    # Parse the scenario
    parsed_data = parse_scenario(str(scenario_file))

    # Assertions
    assert "scenes" in parsed_data
    assert len(parsed_data["scenes"]) == 2
    assert parsed_data["scenes"][0]["state"]["environment"]["location"] == "market"
    assert parsed_data["scenes"][1]["state"]["supplies"] == [{"type": "Tourniquet", "quantity": 1}]
