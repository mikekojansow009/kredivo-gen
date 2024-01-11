from kredivo_generator.actions.base_action import BaseAction

class Feature(BaseAction):
        def __init__(self, folder):
            super().__init__('feature', folder)