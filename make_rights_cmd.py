import os
# import glob


def check_rights():
	# create cmd file witch check all rights for source folder
	current_directory = os.getcwd()
	# disk of current directory C: for example
	current_disk = current_directory[0:2]
	# making path for .cmd command file
	rights_cmd = f"{current_directory}\\check_rights.cmd"
	
	# saving command in .cmd file for checking all rights for all users
	with open(rights_cmd, "w+") as current_rights:
		# move to next line
		nl = '\n'
		current_rights.write(current_disk + nl)
		current_rights.write(f"icacls {current_directory}{nl}")
		current_rights.write("cmd /k")


def rights_cmd_creator():
	# long annotation
	
	# command patterns for rights:
	#
	# icacls < filename > [ / grant[:r] < sid >: < perm > [...]]
	# [ / deny < sid >: < perm > [...]]
	# [ / remove[:g |:d]]
	# < sid > [...]] [ / t] [ / c] [ / l] [ / q]
	# [ / setintegritylevel < Level >: < policy > [...]]
	# icacls < directory >
	# [ / substitute < sidold > < sidnew > [...]]
	# [ / restore < aclfile > [ / c] [ / l] [ / q]]
	# type -> mask
	# dns command files-> '\\raw_data\\*_dns.cmd'
	# dns apps files-> '\\raw_data\\*_dns.txt'
	# urls apps files-> '\\urls\\*_urls.txt'
	#
	# Parameter	Description
	# <filename>	Specifies the file for which to display or modify DACLs.
	# <directory>	Specifies the directory for which to display or modify DACLs.
	# /t	Performs the operation on all specified files in the current directory and its subdirectories.
	# /c	Continues the operation despite any file errors. Error messages will still be displayed.
	# /l	Performs the operation on a symbolic link instead of its destination.
	# /q	Suppresses success messages.
	# [/save <ACLfile> [/t] [/c] [/l] [/q]]-
	# Stores DACLs for all matching files into an access control list
	# (ACL) file for later use with /restore.
	# [/setowner <username> [/t] [/c] [/l] [/q]]
	# Changes the owner of all matching files to the specified user.
	# [/findsid <sid> [/t] [/c] [/l] [/q]]
	# Finds all matching files that contain a DACL explicitly mentioning the specified security identifier (SID).
	# [/verify [/t] [/c] [/l] [/q]]
	# Finds all files with ACLs that are not canonical or have lengths inconsistent with access control entry (ACE) counts.
	# [/reset [/t] [/c] [/l] [/q]]	Replaces ACLs with default inherited ACLs for all matching files.
	# [/grant[:r] <sid>:<perm>[...]]
	# Grants specified user access rights. Permissions replace previously granted explicit permissions.
	# Not adding the :r, means that permissions are added to any previously granted explicit permissions.
	#
	# [/deny <sid>:<perm>[...]]
	# Explicitly denies specified user access rights.
	# An explicit deny ACE is added for the stated permissions and the same permissions in any explicit grant are removed.
	# [/remove[:g | :d]] <sid>[...] [/t] [/c] [/l] [/q]
	# Removes all occurrences of the specified SID from the DACL. This command can also use:
	# :g - Removes all occurrences of granted rights to the specified SID.
	# :d - Removes all occurrences of denied rights to the specified SID.
	# [/setintegritylevel [(CI)(OI)] <Level>:<Policy>[...]]
	# Explicitly adds an integrity ACE to all matching files. The level can be specified as:
	# l - Low
	# m- Medium
	# h - High
	# Inheritance options for the integrity ACE may precede the level and are applied only to directories.
	# [/substitute <sidold><sidnew> [...]]
	# Replaces an existing SID (sidold) with a new SID (sidnew). Requires using with the <directory> parameter.
	# /restore <ACLfile> [/c] [/l] [/q]
	# Applies stored DACLs from <ACLfile> to files in the specified directory.
	# Requires using with the <directory> parameter.
	# /inheritancelevel: [e | d | r]	Sets the inheritance level, which can be:
	# e - Enables inheritance
	# d - Disables inheritance and copies the ACEs
	# r - Disables inheritance and removes only inherited ACEs
	#
	# Remarks
	# SIDs may be in either numerical or friendly name form.
	# If you use a numerical form, affix the wildcard character * to the beginning of the SID.
	# This command preserves the canonical order of ACE entries as:
	# Explicit denials
	# Explicit grants
	# Inherited denials
	# Inherited grants
	# The <perm> option is a permission mask that can be specified in one of the following forms:
	# A sequence of simple rights (basic permissions):
	# F - Full access
	# M- Modify access
	# RX - Read and execute access
	# R - Read-only access
	# W - Write-only access
	# A comma-separated list in parenthesis of specific rights (advanced permissions):
	# D - Delete
	# RC - Read control (read permissions)
	# WDAC - Write DAC (change permissions)
	# WO - Write owner (take ownership)
	# S - Synchronize
	# AS - Access system security
	# MA - Maximum allowed
	# GR - Generic read
	# GW - Generic write
	# GE - Generic execute
	# GA - Generic all
	# RD - Read data/list directory
	# WD - Write data/add file
	# AD - Append data/add subdirectory
	# REA - Read extended attributes
	# WEA - Write extended attributes
	# X - Execute/traverse
	# DC - Delete child
	# RA - Read attributes
	# WA - Write attributes
	# Inheritance rights may precede either <perm> form:
	# (I) - Inherit. ACE inherited from the parent container.
	# (OI) - Object inherit. Objects in this container will inherit this ACE. Applies only to directories.
	# (CI) - Container inherit. Containers in this parent container will inherit this ACE. Applies only to directories.
	# (IO) - Inherit only. ACE inherited from the parent container, but does not apply to the object itself.
	# Applies only to directories.
	# (NP) - Do not propagate inherit. ACE inherited by containers and objects from the parent container,
	# but does not propagate to nested containers. Applies only to directories.
	
	# directory for saving RIGHTS.cmd
	current_directory = os.getcwd()
	rights_cmd_path = current_directory + "\\RIGHTS.cmd"
	
	# rights for source folder and subfolders and files
	commands = [
		"ghgh",
		"cmd / k"
	]
	with open(rights_cmd_path, "w") as rights_cmd:
		for line in commands:
			rights_cmd.write(line + '\n')
		

if __name__ == '__main__':
	check_rights()
	print("""
	input PC name, and controlled user in this form:
			""")
	
	
