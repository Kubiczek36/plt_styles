# script to copy matplotlib styles from folder ./styles to matplotlib stylelib folder
# Author: Jakub Dokulil

import os
import shutil

# get current working directory
cwd = os.getcwd()

# get path to styles folder
styles_path = os.path.join(cwd, 'styles')

# get path to matplotlib stylelib folder

# for mac
if os.name == 'posix':
    home = os.path.expanduser('~')
    envs_path = os.path.join(home, 'opt', 'anaconda3', 'envs')
    # path to matplotlib stylelib folder

# for windows
elif os.name == 'nt':
    home = os.path.expanduser('~')
    envs_path = os.path.join(home, 'AppData', 'Local', 'anaconda3', 'envs')

# get list of all environments
envs = os.listdir(envs_path)

styles_paths =  [ ]
# mac path
if os.name == 'posix':
    for env in envs:
        lib_path = os.path.join(envs_path, env, 'lib')
        # find folder beginning with python3.*****
        for folder in os.listdir(lib_path):
            if folder.startswith('python3'):
                styles_paths.append(os.path.join(lib_path, folder, 'site-packages', 'matplotlib'))

# windows path
elif os.name == 'nt':
    for env in envs:
        lib_path = os.path.join(envs_path, env, 'Lib')
        # find folder beginning with python3.*****
        for folder in os.listdir(lib_path):
            if folder.startswith('python3'):
                styles_paths.append(os.path.join(lib_path, env, 'Lib', 'site-packages', 'matplotlib'))

# copy styles to matplotlib stylelib folder
for styles_path in styles_paths:
    for style in os.listdir(styles_path):
        if style.endswith('.mplstyle'):
            # copy style to stylelib folder in case overwrite is needed
            shutil.copy(os.path.join(styles_path, style), os.path.join(styles_path, 'mpl_stylelib'))
            # copy style to stylelib folder in case overwrite is not needed
            shutil.copy(os.path.join(styles_path, style), os.path.join(styles_path, 'mpl_stylelib'))