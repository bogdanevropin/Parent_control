from install_smth import install_by_cmd

try:
	# for notifications
	import pyautogui
except ModuleNotFoundError:
	install_by_cmd("pyautogui", True)


def eye_help_time(full_training):
	pyautogui.alert("Look in window for 1 min, close eyes")
	if full_training:
		pyautogui.alert("Make full training for eyes")
		