import os
import datetime
import time
# for installing modules by pip
from install_smth import install_by_cmd

# check processes in WMI
try:
    import wmi
except ModuleNotFoundError:
    install_by_cmd("WMI", True)
    
try:
    import shutil
except ModuleNotFoundError:
    install_by_cmd("shutil", True)

# from shutdown import shutdown_by_cmd
# for shutting-down by cmd

from urls_controller import check_urls
# for storing urls


def apps_timer(controlled_times_str, time_urls):
    # shutdown pc when today's time of using app from controlled_exe_times.txt is more than permitted
    
    # every minute apps_timer is checking current tasks (apps) and saving today's time of using this app
    # time of today's use writing in controlled_exe_times.txt by :
    # example
    
    # System Idle Process: 120
    # System: 120
    # Registry: 120
    # chrome.exe: 50
    # python.exe: 0
    
    # block pc if open python, after 50 min of chrome and pc after 120 min anyway
    
    cycles = 1
    # after {time_urls} min store urls
    
    # control is active
    non_control = True
    current_directory = os.getcwd()
    
    # creating unic paths by date
    current_date_str = str(datetime.datetime.now().date())
    file_path_c = f"{current_directory}\\apps\\{current_date_str}_current.txt"
    file_path_p = f"{current_directory}\\apps\\{current_date_str}_previous.txt"
    file_path_t = f"{current_directory}\\{controlled_times_str}"
    # creating unic path for storing stopped app
    time_now_for_stop = str(datetime.datetime.now()).replace(':', '-').replace(' ', '-')
    file_path_s = f"{current_directory}\\stopped_by\\{time_now_for_stop}_stop.txt"
    
    # saving all controlling processes
    controlled_processes = {}

    with open(file_path_t, "r") as control_times:
        for c_proc in control_times.readlines():
            key, value = c_proc.strip().split(":")
            controlled_processes[key] = int(value)
            
    # saving all processes
    all_processes = {}
    
    # first checking urls when log on
    check_urls()
    
    while non_control:
        # while user is permit using pc
        
        # storing time for calculating time of cycle and sleep till minute and rerun all
        start_time = time.time()
        # monitoring processes
        c = wmi.WMI()
        # saving current processes at the check time
        current_processes = []
        # checking previous data
        check_file = os.path.exists(file_path_c)
        if not check_file:   
            # if no file with today's apps we need to create it

            for proc in c.Win32_Process():
                if proc.name not in current_processes:
                    current_processes.append(proc.name)
            for proc in current_processes:
                all_processes[proc] = 1

            with open(file_path_c, "w+") as control_times:
                for proc in all_processes:
                    control_times.write(f"{proc}:1\n")

        else:
            shutil.copy2(file_path_c, file_path_p)
            c = wmi.WMI()

            with open(file_path_p, "r") as control_times:
                for line in control_times.readlines():
                    key, value = line.strip().split(":")
                    all_processes[key] = int(value)

            for controlled_proc in controlled_processes:
                try:
                    if all_processes[controlled_proc] > controlled_processes[controlled_proc]:
                        non_control = False
                        with open(file_path_s, "a+") as s:
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
        
        if cycles > time_urls:
            # storing urls every {time_urls} min
            cycles = 0
            check_urls()
        # sleeping other time till next minute
        cycles += 1
        # every 1 min checking apps
        minute = 60
        time.sleep(10 - (time.time() - start_time))
    
    # if non_control false pc shutting-down
    # shutdown_by_cmd()
    print("boooo")
    
        
