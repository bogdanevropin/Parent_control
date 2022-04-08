import datetime
import os
import time

from install_smth import install_by_cmd

try:
    import subprocess
except ModuleNotFoundError:
    install_by_cmd("subprocess", False)


def check_urls():
    # create .txt file with urls from dns cash received by cmd command "displaydns"
    
    current_directory = os.getcwd()
    current_time = str(datetime.datetime.now()).replace(':', '-').replace(' ', '-')
    
    # saving unic(by time) paths for files that will contain command, dns cash, urls
    file_path_cmd = f"{current_directory}\\raw_data\\{current_time}_dns.cmd"
    file_path_dns = f"{current_directory}\\raw_data\\{current_time}_dns.txt"
    file_path_urls = f"{current_directory}\\urls\\{current_time}_urls.txt"
    
    # create .cmd file with commands for saving all dns cash
    with open(file_path_cmd, "w+") as current_cmd:
        # save dnss in file_path_dns from cmd
        current_cmd.write(f"ipconfig /displaydns > {file_path_dns}")
    
    # executing .cmd file for receiving dns cash
    subprocess.Popen([file_path_cmd])
    # waiting  while  file executing
    time.sleep(1)
    
    # reading dns cash from file
    with open(file_path_dns, "r") as current_dns:
        all_lines = current_dns.readlines()
        
        # save all urls (lines that contain 'Record Name' string)
        all_now_urls = []
        for line in all_lines:
            if 'Record Name' in line:
                # write only name
                all_now_urls.append(line.split(":")[1])
        
        # save all urls in file_path_urls (.txt)
        with open(file_path_urls, "w+") as urls:
            for url in set(all_now_urls):
                urls.write(url)
