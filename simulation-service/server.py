from concurrent import futures
import grpc
from service_pb2_grpc import SimulationServiceServicer, add_SimulationServiceServicer_to_server
import service_pb2

# Import modules (e.g., EnvironmentAssessment, SimulationHandler)
from environment.assessment import EnvironmentAssessment
from simulation.handler import SimulationHandler
from reasoning.goodness import GoodnessAssessment
from reasoning.rightness import RightnessAssessment
from decision.decision import EthicalDecisionMaking

class SimulationService(SimulationServiceServicer):
    def __init__(self):
        self.env_assessment = EnvironmentAssessment()
        self.simulation_handler = SimulationHandler()
        self.goodness_assessment = GoodnessAssessment()
        self.rightness_assessment = RightnessAssessment()
        self.decision_maker = EthicalDecisionMaking()

    def RunSimulation(self, request, context):
        # Step 1: Assess the environment
        raw_data = {"scenario_id": request.scenario_id, "parameters": dict(request.parameters)}
        structured_data = self.env_assessment.assess(raw_data)

        # Step 2: Run the simulation
        simulation_results = self.simulation_handler.run_simulation(structured_data)

        # Step 3: Evaluate goodness
        goodness_result = self.goodness_assessment.evaluate(simulation_results)

        # Step 4: Evaluate rightness
        rightness_result = self.rightness_assessment.evaluate(
            structured_data["parameters"].get("action", "default_action"),
            simulation_results
        )

        # Step 5: Make ethical decision
        decision = self.decision_maker.decide(goodness_result, rightness_result)

        # Step 6: Return the result
        return service_pb2.SimulationResponse(
            status="SUCCESS",
            result=decision["decision"]
        )

def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    add_SimulationServiceServicer_to_server(SimulationService(), server)
    server.add_insecure_port("[::]:50051")
    print("Server is running on port 50051...")
    server.start()
    server.wait_for_termination()

if __name__ == "__main__":
    serve()
