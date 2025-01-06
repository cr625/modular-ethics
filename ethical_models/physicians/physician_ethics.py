# Physician-specific ethics (Theory of Good)

from ethical_models.base.theory_of_good import TheoryOfGood

class PhysicianEthics(TheoryOfGood):
    def evaluate_goodness(self, action, context):
        if action["type"] == "apply_tourniquet":
            return {"goodness_score": 10, "reason": "Prevents fatal bleeding"}
        elif action["type"] == "administer_pain_meds":
            return {"goodness_score": 5, "reason": "Alleviates suffering"}
        return {"goodness_score": 0, "reason": "No significant ethical value"}
