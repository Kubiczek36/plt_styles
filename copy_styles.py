# script to copy matplotlib styles from folder ./styles to matplotlib stylelib folder
# Author: Jakub Dokulil

import os
import shutil

logo = r"""
|           ____  _       _
|          |  _ \| | ___ | |_
|          | |_) | |/ _ \| __|
|     *    |  __/| | (_) | |_
|   *   *  |_|  _|_|\___/ \__|
|  *     *               ___| |_ _   _| | ___  ___
| *       *          *  / __| __| | | | |/ _ \/ __|
⏊______________________ \__ \ |_| |_| | |  __/\__ \
            *       * * |___/\__|\__, |_|\___||___/
              *   *
                *

"""

print(logo)

print(80 * "=")
print("Script to copy created matplotlib styles to matplotlib stylelib folder")
print(80 * "=")

# get current working directory
cwd = os.getcwd()

# get path to styles folder
my_styles_path = os.path.join(cwd, 'styles')

# print styles in the folder
my_styles = os.listdir(my_styles_path)

print("\nStyles in the folder: ")

for i in range(len(my_styles)):
    print("{}. {}".format(i + 1, my_styles[i]))

# get path to matplotlib stylelib folder
# ------------------------------------------

# for mac
if os.name == 'posix':
    home = os.path.expanduser('~')
    envs_path = os.path.join(home, 'opt', 'anaconda3', 'envs')
    # path to matplotlib stylelib folder

# for windows
elif os.name == 'nt':
    home = os.path.expanduser('~')
    envs_path = os.path.join(home, 'AppData', 'Local', 'anaconda3', 'envs')

print("\nPath to folder with environments: {}".format(envs_path))

# get list of all environments
envs = os.listdir(envs_path)

# delete folders that begin with .
envs = [env for env in envs if not env.startswith('.')]

print("\nList of environments: ")

for i in range(len(envs)):
    print("{}. {}".format(i + 1, envs[i]))

env_styles_paths = []
# empty list of booleans size of envs
matplotli_in_env = []

for env in envs:
    matplotli_in_env.append(False)

# mac path
if os.name == 'posix':
    for env in envs:
        lib_path = os.path.join(envs_path, env, 'lib')
        # find folder beginning with python3.*****
        for folder in os.listdir(lib_path):
            if folder.startswith('python3'):
                # test if matplotlib folder exists
                if 'matplotlib' in os.listdir(
                        os.path.join(lib_path, folder, 'site-packages')):
                    env_styles_paths.append(
                        os.path.join(lib_path, folder, 'site-packages',
                                     'matplotlib', 'mpl-data', 'stylelib'))
                    matplotli_in_env[envs.index(env)] = True
                # else:
                #     env_styles_paths.append('')

# windows path
elif os.name == 'nt':
    for env in envs:
        lib_path = os.path.join(envs_path, env, 'Lib')
        # find folder beginning with python3.*****
        for folder in os.listdir(lib_path):
            if folder.startswith('python3'):
                # test if matplotlib folder exists
                if 'matplotlib' in os.listdir(
                        os.path.join(lib_path, folder, 'site-packages')):
                    env_styles_paths.append(
                        os.path.join(lib_path, folder, 'site-packages',
                                     'matplotlib', 'mpl-data', 'stylelib'))
                    matplotli_in_env[envs.index(env)] = True

print("\nMatplotlib found in environments: ")

for i in range(len(matplotli_in_env)):
    print("{}. \t {} \t {}".format(i + 1, envs[i], matplotli_in_env[i]))

# copy my styles to matplotlib stylelib folder
# --------------------------------------------
print("\nCopying styles to matplotlib stylelib folder: ")

print("\nenv_styles_paths length: ", len(env_styles_paths))

for i in range(len(env_styles_paths)):
    print(i)
    # print("\nEnvironment: {}".format(envs[i]))
    print("Path: {}".format(env_styles_paths[i]))
    for style in my_styles:
        shutil.copy(
            os.path.join(my_styles_path, style),
            env_styles_paths[i])
        print("Copied {}".format(style))