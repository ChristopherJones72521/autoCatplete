import random
import os


def catIpsum():
	# Create catIpsum list for cat description. Split on comma and randomly return 4 index values.
	catIpsumVar = '''[Shove bum in owner's face like camera lens gnaw the corn cob unwrap toilet paper, 
	Kitty loves pigs pee in human's bed until he cleans the litter box steal the warm chair right after you get up,
	for chew foot See owner run in terror meow or curl into a furry donut and chirp at birds but claw drapes, 
	for burrow under covers. Stick butt in face scream at teh bath but curl into a furry donut. Meow., 
	Curl into a furry donut swat turds around the house pee in human's bed until he cleans the litter box., 
	Stretch destroy couch as revenge yet attack dog, run away and pretend to be victim., 
	Throwup on your pillow. Under the bed sit by the fire or asdflkjaertvlkjasntvkjn (sits on keyboard)., 
	Chew on cable. Burrow under covers. Has closed eyes but still sees you sweet beast jump off balcony, 
	onto stranger's head so cat snacks, for stare at the wall, play with food and get confused by dust,
	lick plastic bags i am the best. Meowzer! russian blue refuse to leave cardboard box or stare at wall, 
	turn and meow stare at wall some more meow again continue staring so lick plastic bags. Meow all night, 
	having their mate disturbing sleeping humans drink water out of the faucet for stare out the window, 
	purr for no reason chirp at birds hunt by meowing loudly at 5am next to human slave food dispenser for white cat sleeps on a black shirt.
	Give attitude chase ball of string. or meowing non stop for food. present belly. scratch hand when stroked, 
	or need to chase tail. but knock dish off table head butt cant eat out of my own dish. Has closed eyes but still sees you, 
	leave dead animals as gifts. and need to chase tail climb a tree. wait for a fireman jump to fireman then scratch his face, 
	so have secret plans if it smells like fish eat as much as you wish. Fall over dead (not really but gets sypathy), 
	claws in your leg meow for food. then when human fills food dish. take a few bites of food and continue meowing, 
	always hungry so hack up furballs. Spot something. big eyes. big eyes. crouch. shake butt. prepare to pounce destroy couch, 
	Kitty power! claws in your leg. Stretch. Have secret plans claw drapes. Paw at beetle and eat it before it gets away you call this cat food? 
	] '''

	catIpsumList = catIpsumVar.split(',')

	description = [x.strip() for x in random.sample(catIpsumList, 3)]

	for each in description:
	  return each

def generateName():
	catName = ['Abby','Angel','Annie','Baby','Bailey','Bandit','Bear','Bella','Bob','Boo','Boots','Bubba','Buddy','Buster','Loki','Lola','Lucky','Lucy','Luna','Maggie','Max','Mia','Midnight','Milo','Mimi','Miss kitty','Missy','Misty','Mittens','Molly','Muffin','Nala','Oliver','Oreo','Oscar','Patches','Peanut','Pepper','Precious','Princess','Pumpkin','Rascal','Rocky','Sadie','Salem','Sam','Samantha','Sammy','Sasha','Sassy','Scooter','Shadow','Sheba','Simba','Simon','Smokey','Snickers','Snowball','Snuggles','Socks','Sophie','Spooky','Sugar','Tiger','Tigger','Tinkerbell','Toby','Trouble','Whiskers','Willow','Zoe','Zoey']
	return random.choice(catName)
