 # Base class for Theory of Right (Professional Standards)
 
class TheoryOfRight:
    def evaluate_permissibility(self, action, context):
        """
        Evaluates the permissibility of an action based on professional standards.
        :param action: The action to evaluate.
        :param context: Contextual information (e.g., casualty, environment).
        :return: A decision (e.g., permissible, impermissible, or conditional).
        """
        raise NotImplementedError("Subclasses must implement this method")