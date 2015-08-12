'''
Quick and dirty mass srcds update system for TCAdmin 1
'''
import sys, os, subprocess, time

premadeArgs = "{0} +login anonymous +force_install_dir {1}/{2} +app_update 4020 validate +quit"
steamCMDPath = ""
checkGModFilepath ="{0}/{1}/garrysmod/lua/autorun/developer_functions.lua"
	
def GrabAllLinks(path):
	validDirectories = []

	print("Scanning for viable GMod installations...")
	print("WARNING: Make sure all servers this is being ran for are turned OFF before attempting to update!")
	print("Unexpected behaviour may happen otherwise!")

	dirs = os.listdir(path)
	
	for item in dirs:
		if os.path.exists(checkGModFilepath.format(path, item)):
			validDirectories.append(premadeArgs.format(steamCMDPath, path,item))

	print("We have " + str(len(validDirectories)) + " gmod installations. Make sure the total is correct!")
	print("Press Y to continue.")

	response = input()

	if str.lower(response) != "y":
		return

	for path in validDirectories:
		subprocess.Popen(path)
		

if __name__ == '__main__':
	args = sys.argv
	steamCMDPath = args[1]
	path = args[2]

	if len(args) > 1 and args[1] != None:
		GrabAllLinks(path)



