import os
import argparse
from kredivo_generator.android_project import AndroidProject
from pathlib import Path
from kredivo_generator.kredivo_config import Config
from kredivo_generator.actions.base_action import BaseAction
from kredivo_generator.actions.core import Core
from kredivo_generator.actions.feature import Feature
from kredivo_generator.actions.subsystem import Subsystem
from kredivo_generator.actions.thirdparty import ThirdParty

def generate() :
    argument = argparse.ArgumentParser()
    argument.add_argument('-c', '--core', type=str, help='Create new core module')
    argument.add_argument('-f', '--feature', type=str, help='Create new feature module')
    argument.add_argument('-s', '--subsystem', type=str, help='Create new subsystem module')
    argument.add_argument('-tp', '--thirdparty', type=str, help='Create new third party module')
    argument.add_argument('--clear', action='store_true', help='Clear config')

    args = argument.parse_args()
    # TODO: Need to find automatically kredivo android folder in next version.
    # findFolder = subprocess.run(['find', '/Users/', '-type', 'd', '-name', '\"Kredivo\"', "-ipath", "*Kredivo_Android", "-maxdepth ", "2", '2>/dev/null'], stdout=subprocess.PIPE)

    config = Config()
    androidProject = AndroidProject()

    if args.clear == True:
        config.clear()
        return

    config.create_config_if_needed()
    
    readFile = open(config.configPath, "r").read()

    if not readFile or androidProject.is_project_path_exists() == False:
        folderPath = input_android_project()

        androidProject.validate(folderPath)

    androidProject.input_package_if_needed()

    action = False

    if args.core:
        coreAction = Core(args.core)
        coreAction.make()

        action = True
    
    if args.feature:
        options = ['domain', 'presentation', 'data', 'shared', 'all']
        
        inputMessage = 'Which module do you need to create?\n'

        for index, item in enumerate(options):
            inputMessage += f'{index + 1}. {item}\n'

        inputMessage += 'Answer : '

        answer = int(input(inputMessage))

        if answer > len(options):
            print("Incorrect answer!")
            return


        featureAction = Feature(args.feature + '.' + options[answer - 1])
        featureAction.make()

        action = True
    
    if args.subsystem:
        subsystemAction = Subsystem(args.subsystem)
        subsystemAction.make()

        action = True
    
    if args.thirdparty:
        thirdpartyAction = ThirdParty(args.thirdparty)
        thirdpartyAction.make()

        action = True
    
    if action == False:
        argument.print_help()

def input_android_project():
    return input("Where is your Android project path?\n")


# generate()