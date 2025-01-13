from event_motor.scenario_parser import parse_scenario

if __name__ == "__main__":
    scenario_file = "scenarios/dryrun-adept-eval-MJ2.yaml" 
    scenario_data = parse_scenario(scenario_file)

    # Display updated scenario data for verification
    import pprint
    pprint.pprint(scenario_data)
