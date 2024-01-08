import os
import argparse
from android_project import AndroidProject
from pathlib import Path
from kredivo_config import Config

def generate() :
    argument = argparse.ArgumentParser()
    argument.add_argument('-c', '--core', help='Create new core module')
    argument.add_argument('-f', '--feature', help='Create new feature module')
    argument.add_argument('-s', '--subsystem', help='Create new subsystem module')
    argument.add_argument('-tp', '--thirdparty', help='Create new third party module')

    args = argument.parse_args()
    # TODO: Need to find automatically kredivo android folder in next version.
    # findFolder = subprocess.run(['find', '/Users/', '-type', 'd', '-name', '\"Kredivo\"', "-ipath", "*Kredivo_Android", "-maxdepth ", "2", '2>/dev/null'], stdout=subprocess.PIPE)

    cnfPath = os.path.dirname(__file__) + "/generator.cnf"

    androidProject = AndroidProject(cnfPath)

    if os.path.isfile(cnfPath) == False:
        Path(cnfPath).touch()

    readFile = open(cnfPath, "r").read()

    if not readFile or androidProject.is_project_path_exists() == False:
        folderPath = input_android_project()

        androidProject.validate(folderPath)

    androidProject.input_package_if_needed()

def input_android_project():
    return input("Where is your Android project path?\n")


generate()