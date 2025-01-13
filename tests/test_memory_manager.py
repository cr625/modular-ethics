import pytest
from event_motor.memory_manager import MemoryManager

def test_memory_manager_persistent_state():
    memory_manager = MemoryManager()

    # Initial state
    scene_1 = {
        "state": {
            "environment": {"location": "market"},
            "supplies": [{"type": "Bandage", "quantity": 2}],
            "characters": [{"id": "Shooter", "name": "Alderson"}],
        },
        "persist_characters": True,
    }

    updated_scene_1 = memory_manager.update_state(scene_1)

    # Check if persistent state was updated
    assert memory_manager.persistent_state["environment"] == {"location": "market"}
    assert memory_manager.persistent_state["supplies"] == [{"type": "Bandage", "quantity": 2}]
    assert len(memory_manager.persistent_state["characters"]) == 1

    # Scene 2 doesn't provide environment; it should persist from Scene 1
    scene_2 = {
        "state": {
            "supplies": [{"type": "Tourniquet", "quantity": 1}],
            "characters": [{"id": "Shooter", "name": "Alderson", "injured": True}],
        },
        "persist_characters": True,
    }

    updated_scene_2 = memory_manager.update_state(scene_2)

    # Verify persistence
    assert updated_scene_2["state"]["environment"] == {"location": "market"}
    assert updated_scene_2["state"]["supplies"] == [{"type": "Tourniquet", "quantity": 1}]
    assert len(updated_scene_2["state"]["characters"]) == 1

def test_memory_manager_character_merge():
    memory_manager = MemoryManager()

    # Scene 1 with characters
    scene_1 = {
        "state": {
            "characters": [
                {"id": "Victim", "name": "Babson", "status": "Injured"},
                {"id": "Shooter", "name": "Alderson", "status": "Critical"},
            ],
        },
        "persist_characters": True,
    }

    memory_manager.update_state(scene_1)

    # Scene 2 updates a single character
    scene_2 = {
        "state": {
            "characters": [
                {"id": "Victim", "name": "Babson", "status": "Stable"},
            ],
        },
        "persist_characters": True,
    }

    updated_scene_2 = memory_manager.update_state(scene_2)

    # Verify characters are merged correctly
    assert len(updated_scene_2["state"]["characters"]) == 2
    assert any(char["status"] == "Stable" for char in updated_scene_2["state"]["characters"])
