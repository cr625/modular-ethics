 # Physician-specific standards (Theory of Right)
 
from ethical_models.base.theory_of_right import TheoryOfRight

class PhysicianStandards(TheoryOfRight):
    def evaluate_permissibility(self, action, context):
        if action["type"] == "apply_tourniquet" and context["injury"] == "major_bleeding":
            return {"decision": "permissible", "reason": "Aligned with TCCC standards"}
        elif action["type"] == "administer_pain_meds" and context["vitals"]["pain_level"] > 5:
            return {"decision": "permissible", "reason": "Pain level justifies medication"}
        return {"decision": "impermissible", "reason": "Action not justified"}
