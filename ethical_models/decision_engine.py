# Orchestrates decisions across multiple disciplines

# ethical_models/decision_engine.py
class DecisionEngine:
    def __init__(self):
        self.theories_of_good = {}
        self.theories_of_right = {}

    def register_discipline(self, discipline_name, theory_of_good, theory_of_right):
        self.theories_of_good[discipline_name] = theory_of_good
        self.theories_of_right[discipline_name] = theory_of_right

    def decide(self, discipline_name, action, context):
        if discipline_name not in self.theories_of_good or discipline_name not in self.theories_of_right:
            raise ValueError(f"Discipline '{discipline_name}' not registered.")
        
        goodness = self.theories_of_good[discipline_name].evaluate_goodness(action, context)
        permissibility = self.theories_of_right[discipline_name].evaluate_permissibility(action, context)
        
        return {
            "discipline": discipline_name,
            "action": action["type"],
            "goodness": goodness,
            "permissibility": permissibility
        }
