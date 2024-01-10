from actions.base_action import BaseAction

class Subsystem(BaseAction):
    def __init__(self, folder):
        super().__init__('subsystem', folder)