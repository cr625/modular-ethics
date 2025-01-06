# main.py
import yaml
from ethical_models.decision_engine import DecisionEngine

# Load configuration
with open("config/config.yaml", "r") as f:
    config = yaml.safe_load(f)

# Initialize decision engine
decision_engine = DecisionEngine()

# Dynamically load disciplines
for discipline in config["disciplines"]:
    theory_of_good = __import__(discipline["theory_of_good"], fromlist=[""]).__dict__[discipline["theory_of_good"].split(".")[-1]]()
    theory_of_right = __import__(discipline["theory_of_right"], fromlist=[""]).__dict__[discipline["theory_of_right"].split(".")[-1]]()
    decision_engine.register_discipline(discipline["name"], theory_of_good, theory_of_right)

# Example usage
action = {"type": "apply_tourniquet"}
context = {"injury": "major_bleeding", "vitals": {"pain_level": 7}}
decision = decision_engine.decide("physicians", action, context)
print(decision)
