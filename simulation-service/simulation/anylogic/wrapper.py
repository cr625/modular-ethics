import subprocess
import json

class AnyLogicWrapper:
    def __init__(self, jar_path="simulation/anylogic/model.jar"):
        self.jar_path = jar_path

    def run_simulation(self, inputs):
        """
        Runs the AnyLogic Java model and captures its outputs.
        :param inputs: Dictionary of parameters to pass to the model.
        :return: Dictionary of simulation results.
        """
        # Convert inputs to JSON string
        input_json = json.dumps(inputs)

        try:
            # Run the AnyLogic model using Java
            result = subprocess.run(
                ["java", "-jar", self.jar_path, input_json],
                capture_output=True,
                text=True,
                check=True
            )
            # Parse the JSON output from the AnyLogic model
            output = json.loads(result.stdout)
            return output
        except subprocess.CalledProcessError as e:
            print(f"Error running AnyLogic model: {e}")
            return None
