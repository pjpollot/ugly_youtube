#!/usr/bin/env python3

import subprocess
import os 

from os import path
from shutil import copy

folder_path = path.dirname(__file__)
bin_path = path.join(folder_path, "bin")
# target directory: ~/bin
target_path = path.join(os.environ["HOME"], "bin")

pip_install_command = f"python3.9 -m pip install {folder_path}"


if __name__=="__main__":
    # first of all, install the current version of the package
    subprocess.call(pip_install_command, shell=True)
    # then add the bin files into the target folder
    bin_entities = os.listdir(bin_path)
    for bin_entity in bin_entities:
        bin_ent_path = path.join(bin_path, bin_entity)
        if path.isfile(bin_ent_path):
            dest_path = path.join(target_path, bin_entity)
            copy(src=bin_ent_path, dst=dest_path)
            print(f"Created {dest_path}")