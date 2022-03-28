import os
import datetime
from subprocess import Popen

def shutdown_by_cmd():

    current_directory = os.getcwd()
    current_time = str(datetime.datetime.now().date()).replace(':','-').replace(' ', '-')

    shutdown_path_cmd = f"{current_directory}\\{current_time}_shutdown.cmd"

    
    with open(shutdown_path_cmd, "w+") as current_cmd:
        current_cmd.write(f"ipconfig /displaydns > {shutdown_path_cmd}")

    Popen([shutdown_path_cmd])

