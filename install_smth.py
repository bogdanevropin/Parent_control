import os


def install_by_cmd(module_name, t_or_f):
	# if t_or_f is True installs
	# creating (in any case) cmd file for manual installing
	current_directory = os.getcwd()
	
	# making unic (by date) path for .cmd command file
	installer_cmd = f"{current_directory}\\{module_name}_import_ERROR.cmd"
	
	# saving command in .cmd file for installing needed module that is not installed yet
	with open(installer_cmd, "w+") as current_install:
		current_install.write(f"pip install {module_name}")
	# installs if t_or_f == True
	if t_or_f:
		# installs automatic if subprocess installed yet
		try:
			from subprocess import Popen
			Popen([installer_cmd])
		except ModuleNotFoundError:
			install_by_cmd("subprocess", False)
		