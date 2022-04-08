import os
import datetime

from install_smth import install_by_cmd

try:
    # for executing files
    import subprocess
except ModuleNotFoundError:
    install_by_cmd("subprocess", False)
    

def shutdown_by_cmd():
    # shutting down pc by cmd
    current_directory = os.getcwd()
    current_date = str(datetime.datetime.now().date()).replace(':', '-').replace(' ', '-')
    
    # making unic (by date) path for .cmd command file
    shutdown_path_cmd = f"{current_directory}\\{current_date}_shutdown.cmd"
    
    # saving command in .cmd file for shutting-down
    with open(shutdown_path_cmd, "w+") as current_cmd:
        current_cmd.write(f"shutdown /s > {shutdown_path_cmd}")
    # executing command for shutting-down
    subprocess.Popen([shutdown_path_cmd])
