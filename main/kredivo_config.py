class Config:
    androidProjectConfig = "android_project_path"
    androidPackageConfig = "android_package_name"

    def __init__(self, configPath):
        self.configPath = configPath

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