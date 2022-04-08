import wmi
import os
import datetime
import time
import shutil

from shutdown import shutdown_by_cmd

def apps_timer(controlled_times_str):

    time_now = datetime.datetime.now()
    current_date = time_now.date()

    time_now_forstop = str(datetime.datetime.now()).replace(':','-').replace(' ', '-')

    current_date_str = str(current_date)

    noncontrol = True
    current_directory = os.getcwd()

    file_path_c = f"{current_directory}\\{current_date_str}_current.txt"
    file_path_p = f"{current_directory}\\{current_date_str}_previous.txt"
    file_path_s = f"{current_directory}\\{time_now_forstop}_stop.txt"
    file_path_t =  f"{current_directory}\\{controlled_times_str}"

    controlled_processes = {}

    with open(file_path_t, "r") as today_data:
        for c_proc in today_data.readlines():
            key, value = c_proc.strip().split(":")
            controlled_processes[key] = int(value)

    all_processes = {}

    while noncontrol:

        start_time = time.time()
        check_file = os.path.exists(f"{current_directory}\\{current_date_str}_current.txt")
        current_processes = []

        if not check_file:   

            c = wmi.WMI ()

            for proc in c.Win32_Process():
                if proc.name not in current_processes:
                    current_processes.append(proc.name)
            for proc in current_processes:
                all_processes[proc] = 1

            with open(file_path_c, "w+") as today_data:
                for proc in all_processes:
                    today_data.write(f"{proc}:1\n")

        else:
            shutil.copy2(file_path_c, file_path_p)
            c = wmi.WMI ()

            with open(file_path_p, "r") as today_data:
                for line in today_data.readlines():
                    key, value = line.strip().split(":")
                    all_processes[key] = int(value)

            for controlled_proc in controlled_processes:
                try:
                    if all_processes[controlled_proc] > controlled_processes[controlled_proc]:
                        noncontrol = False
                        with open(file_path_s, "w+") as s:
                            s.write(f"stopped by app {controlled_proc} time {controlled_processes[controlled_proc]}")
                        break
                except KeyError:
                    continue
            else:
                for proc in c.Win32_Process():
                    if proc.name not in current_processes:
                        current_processes.append(proc.name)
                for proc in current_processes:
                    if proc not in all_processes:
                        all_processes[proc] = 1
                    else:
                        all_processes[proc] += 1
                with open(file_path_c, "w+") as today_data_new:
                    for proc in all_processes:
                        today_data_new.write(f"{proc}:{all_processes[proc]}\n")
        
        time.sleep(60 - (time.time() - start_time))
    
    shutdown_by_cmd()
    
        
