import datetime
import os
from subprocess import Popen
import time

def check_urls():

    current_directory = os.getcwd()
    current_time = str(datetime.datetime.now()).replace(':','-').replace(' ', '-')

    file_path_cmd = f"{current_directory}\\{current_time}_dns.cmd"
    file_path_dns = f"{current_directory}\\{current_time}_dns.txt"
    file_path_urls = f"{current_directory}\\{current_time}_urls.txt"


    with open(file_path_cmd, "w+") as current_cmd:
        current_cmd.write(f"ipconfig /displaydns > {file_path_dns}")

    Popen([file_path_cmd])
    time.sleep(1)

    with open(file_path_dns, "r") as current_dns:
        all_lines = current_dns.readlines()
        all_urls = []
        for line in all_lines:
            if 'Record Name' in line:
                all_urls.append(line)
        with open(file_path_urls, "w+") as urls:
            for url in set(all_urls):
                urls.write(url)
