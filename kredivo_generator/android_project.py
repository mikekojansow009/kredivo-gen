import os
from kredivo_generator.kredivo_config import Config

class AndroidProject:
    androidPackageName = "com.kredivocorp.kredivo"

    def __init__(self):
        self.config = Config()

    def validate(self, projectPath):
        try:
            listFolder = os.listdir(projectPath)
        except:
            print("Path is invalid!")
            return

        isValidProject = self.is_valid(listFolder)

        if not isValidProject:
            print("Your path isn't a valid Android Project!")
            return
        
        self.write_project_path_file(projectPath)

        self.input_package_if_needed()

    def is_valid(self, projectPath):
        isValidAndroidProject = False

        for gradleFile in projectPath:
            if "gradle" not in gradleFile:
                continue

            isValidAndroidProject = True
            break
        
        return isValidAndroidProject

    def is_project_path_exists(self):
        return self.config.is_value_exists(self.config.androidProjectConfig)

    def write_project_path_file(self, projectPath):
        self.config.append_file(self.config.androidProjectConfig, projectPath)

    def input_package_if_needed(self):
        if self.config.is_value_exists(self.config.androidPackageConfig) == False:
            self.input_package_name()

    def input_package_name(self):
        inputPackage = input("What is your default package name? (Default is " + self.androidPackageName + ")")

        if not inputPackage:
            inputPackage = self.androidPackageName

        self.config.append_file(self.config.androidPackageConfig, inputPackage)

    
    def get_package_name(self):
        return self.config.get_value(self.config.androidPackageConfig)
    
    def get_project_path(self):
        return self.config.get_value(self.config.androidPackageConfig)