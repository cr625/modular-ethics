import grpc
import service_pb2
import service_pb2_grpc

def run():
    channel = grpc.insecure_channel("localhost:50051")
    stub = service_pb2_grpc.SimulationServiceStub(channel)

    # Example request
    request = service_pb2.SimulationRequest(
        scenario_id="scenario_1",
        parameters={"action": "test_action", "key": "value"}
    )
    response = stub.RunSimulation(request)
    print("Server Response:", response)

if __name__ == "__main__":
    run()
