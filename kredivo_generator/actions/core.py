from kredivo_generator.actions.base_action import BaseAction

class Core(BaseAction):
    def __init__(self, folder):
        super().__init__('core', folder)