from actions.base_action import BaseAction

class ThirdParty(BaseAction):
    def __init__(self, folder):
        super().__init__('third_party', folder)