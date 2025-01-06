# Base class for Theory of Good (Professional Ethics)

class TheoryOfGood:
    def evaluate_goodness(self, action, context):
        """
        Evaluates the goodness of an action based on professional ethics.
        :param action: The action to evaluate.
        :param context: Contextual information (e.g., casualty, environment).
        :return: A score or qualitative assessment of goodness.
        """
        raise NotImplementedError("Subclasses must implement this method")
    