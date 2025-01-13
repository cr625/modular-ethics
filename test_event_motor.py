from event_motor.scenario_parser import parse_scenario

def test_scenario_parsing():
    scenario_file = "scenarios/dryrun-adept-eval-MJ2.yaml"  # Adjust based on your structure
    parsed_scenario = parse_scenario(scenario_file)

    # Print parsed scenario for verification
    import pprint
    pprint.pprint(parsed_scenario)

if __name__ == "__main__":
    test_scenario_parsing()


