import os

from pathlib import Path

class Config:
    androidProjectConfig = "android_project_path"
    androidPackageConfig = "android_package_name"
    configPath = os.path.dirname(__file__) + "/generator.cnf"

    def get_value(self, id):
        file = open(self.configPath, 'r').read()
        splitFile = file.split('\n')

        for string in splitFile:
            if id in string:
                return string.replace(id + "=", "")
        
        return ""

    def append_file(self, id, value):
        with open(self.configPath, 'a') as file:
            file.write(id + "=" + value + "\n")

    def is_value_exists(self, id):
        if not self.get_value(id):
            return False
        
        return True
    
    def create_config_if_needed(self):
        if os.path.isfile(self.configPath) == False:
            self.create_config()

    def create_config(self):
        Path(self.configPath).touch()

    def clear(self):
        open(self.configPath, 'w').close()