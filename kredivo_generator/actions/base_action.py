import os

from kredivo_generator.kredivo_config import Config
from pathlib import Path

class BaseAction:
    dependencyList = ''

    def __init__(self, rootFolder, folder):
        self.folder = folder
        self.rootFolder = rootFolder
        self.config = Config()

    def make(self):
        realFolder = self.folder

        if '.' in realFolder:
            realFolder = ''
            splitString = self.folder.split('.')

            for string in splitString:
                realFolder += string + '/'

        path = self.config.get_value(self.config.androidProjectConfig) + '/' + self.rootFolder + '/' + realFolder + '/src'

        javaPath = path + '/main/java'

        packageName = self.config.get_value(self.config.androidPackageConfig) + '.' + self.rootFolder + '.' + self.folder

        os.makedirs(path)
        os.makedirs(javaPath)
        
        self.create_build_gradle(path, packageName)
        self.make_sub_child(javaPath, packageName)
        self.replace_settings_gradle()


    def make_sub_child(self, javaPath, packageName):
        subpath = packageName.replace('.', '/')

        fullPath = javaPath + '/' + subpath

        os.makedirs(fullPath)

        print(fullPath)

    def create_build_gradle(self, projectPath, packageName):
        gradlePath = projectPath + '/build.gradle.kts'

        Path(gradlePath).touch()

        sampleGradle = open(os.getcwd() + '/kredivo_generator/sample/sample-build-gradle.sample', 'r').read()

        result = sampleGradle.replace('[[DEPEDENCIY_LIST]]', self.dependencyList)
        result = result.replace('[[PACKAGE_NAME]]', packageName)

        with open(gradlePath, 'w') as file:
            file.write(result)


    def replace_settings_gradle(self):
        settingPath = self.config.get_value(self.config.androidProjectConfig) + '/settings.gradle.kts'

        replaceDot = self.folder.replace('.', ':')

        format = ':' + self.rootFolder + ':' + replaceDot

        content = 'include(\"' + format + '\")'

        with open(settingPath, 'a') as file:
            file.write('\n' + content)