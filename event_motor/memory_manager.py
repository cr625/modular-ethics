class MemoryManager:
    def __init__(self):
        # Initialize persistent state
        self.persistent_state = {
            "environment": None,
            "supplies": None,
            "characters": []
        }

    def update_state(self, scene_dict):
        """
        Update the scene's state with persistent data.
        If `persist_characters` is enabled, merge character data.
        """
        state = scene_dict.get("state", {})

        # Update environment
        if "environment" in state:
            self.persistent_state["environment"] = state["environment"]
        elif "environment" in self.persistent_state:
            state["environment"] = self.persistent_state["environment"]

        # Update supplies
        if "supplies" in state:
            self.persistent_state["supplies"] = state["supplies"]
        elif "supplies" in self.persistent_state:
            state["supplies"] = self.persistent_state["supplies"]

        # Update characters
        if scene_dict.get("persist_characters", False):
            new_characters = list(self.persistent_state.get("characters", []))
            for revised_character in state.get("characters", []):
                new_characters = [char for char in new_characters if char["id"] != revised_character["id"]]
                new_characters.append(revised_character)
            self.persistent_state["characters"] = new_characters
            state["characters"] = new_characters
        elif "characters" in state:
            self.persistent_state["characters"] = state["characters"]

        # Return the updated state
        scene_dict["state"] = state
        return scene_dict
