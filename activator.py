from app_and_urls_controller import apps_timer


if __name__ == "__main__":
    
    # control app time, saves urls
    # check battery percentage
    # first arg file with controlling apps times,
    # second is length in minutes of cycle that stores urls
    apps_timer('controlled_exe_times.txt', 0)
    