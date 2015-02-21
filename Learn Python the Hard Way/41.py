from sys import exit
from random import randint

def death():
	quips = ["you died. you kinda suck.", "nice job, you died...ass.", "such a loser.", "i have a small puppy that's better at this."]

	print quips[randint(0, len(quips)-1)]
	exit(1)


def central_corridor():
	print "the gothons of planet have invaded your ship and destroyed"
	print "your crew. youre the only one."
	print "mission is to get ....."

	action = raw_input("> ")

	if action == "shoot!":
		print "quick draw"
		return 'death'

	elif action == "dodge!":
		print 'you dodged!'
		return 'death'

	elif action == "tell a joke":
		print "telling a joke"
		return 'laser_weapon'

	else:
		print "DOES NOT COMPUTE"
		return 'central_corridor'

def laser_weapon():
	print "...."
	code = '%d%d%d' % (randint(1,9), randint(1,9), randint(1,9))
	guess = raw_input("[keypad]> ")
	guesses = 0

	while guess != code and guesses < 10:
		print "BZZZZED"
		guesses += 1
		guess = raw_input("[keypad]> ")

	if guess == code:
		print "..."
		return 'the bridge'
	else:
		print "..."
		return 'death'

def the_bridge():
	print "..."

	if action == "throw bomb":
		print "paniced and threw bomb"
		return 'death'

	elif action == "slowly place bomb":
		print "bomb placed"
		return 'escape_pod'
	else:
		print "DOES NOT COMPUTE"
		return 'the bridge'

def escape_pod():
	print "..."

	good_pod = randint(1,5)
	guesses = raw_input("[pod #]> ")

	if int(guess) != good_pod:
		print 'you jumped into pod'
		return 'death'
	else:
		print "..."
		exit(0)

ROOMS = {
	'death': death,
	'central_corridor': central_corridor,
	'laser_weapon': laser_weapon,
	'the_bridge': the_bridge,
	'escape_pod': escape_pod
}

def runner(map, start):
	next = start

	while True:
		room = map[next]
		print "\n----------"
		next = room()

runner(ROOMS, 'central_corridor')