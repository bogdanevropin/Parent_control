import time

from install_smth import install_by_cmd

try:
	import psutil
except ModuleNotFoundError:
	install_by_cmd("psutil", True)

try:
	import pyautogui
except ModuleNotFoundError:
	install_by_cmd("pyautogui", True)


def battery_checker_time():
	battery = psutil.sensors_battery()
	
	# ends function and return nothing if there is no battery
	if battery is None:
		return 0
	while True:
		plugged = battery.power_plugged
		percent = int(battery.percent)
		if not plugged and (percent < 90 or percent < 30):
			pyautogui.alert("Plug in your pc !")
			return time.time()
