import os
import argparse

def generate() :
    
    argument = argparse.ArgumentParser()
    argument.add_argument('c', help='Create new core module')
    argument.add_argument('core', help='Create new core module')
    argument.add_argument('f', help='Create new feature module')
    argument.add_argument('feature', help='Create new feature module')
    argument.add_argument('s', help='Create new subsystem module')
    argument.add_argument('subsystem', help='Create new subsystem module')
    argument.add_argument('tp', help='Create new third party module')
    argument.add_argument('thirdpart', help='Create new third party module')
    # TODO: Need to find automatically kredivo android folder in next version.
    # findFolder = subprocess.run(['find', '/Users/', '-type', 'd', '-name', '\"Kredivo\"', "-ipath", "*Kredivo_Android", "-maxdepth ", "2", '2>/dev/null'], stdout=subprocess.PIPE)

    # folderPath = input("Where is your Android project path?\n")

    # try:
    #     listFolder = os.listdir(folderPath)
    # except:
    #     print("Path is invalid!")
    #     return

    # isValidProject = is_valid_android_project(listFolder)

    # if not isValidProject:
    #     print("Your path isn't a valid Android Project!")
        # return
    return
    


def is_valid_android_project(path):
    isValidAndroidProject = False
    for gradleFile in path:
        if "gradle" not in gradleFile:
            continue

        isValidAndroidProject = True
        break
    
    return isValidAndroidProject

def available_options():
    return ['c', 'core', 'f', 'feature', 's', 'subsystem', 'tp', 'thirdparty', '--help']