"""This is a temporary file that reads the launch file to identify the
current number of robots in the launch"""

def getRobots():

	numRobots = 0
	fname = open('launch.launch', 'r+')

	with fname as f:
		for line in f:
			if 'robot_' in line:
				numRobots += 1
	fname.close()
	return numRobots
			
num = getRobots()
print(num)

