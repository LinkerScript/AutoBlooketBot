import webbot
import os
import sys
import time
import random
os.system('pip3 install pyautogui')
print(chr(27)+'[2j')
print('\033c')
print('\x1bc')
driver = webbot.Browser()
driver.go_to('blooket.com/play')
code = input("The game id: ")
bots = int(input("Enter the amount of bots you want (Only 1 to 50): "))
while True:
  if bots >= 51:
    print ("Please only 1 to 50 bots!")
    time.sleep(1)
    sys.stdout.write("\033[F")
    sys.stdout.write("\033[K")
    sys.stdout.write("\033[F")
    sys.stdout.write("\033[K")
    bots = int(input("Enter the amount of bot you want (Only 1 to 50): "))
  else:
    if bots <= 50:
      break
bot = bots - 1
tab = 1
botall = bots
botconect = 0
for i in range(0,bot):
  driver.type(code)
  driver.type(driver.Key.ENTER)
  time.sleep(1)
  discname1 = ['saucy', 'momma', 'mecha', 'earth', 'barbed', 'prehistoric', 'old','cosmic', 'metallic', 'neat', 'supa', 'haunted', 'ruthless', 'clueless', 'rough', 'killer', 'spooky', 'retro', 'ancient', 'strange', 'astro', 'baren', 'burned', 'chared', 'crap', 'cranky', 'crummy', 'croaked', 'dead', 'daring', 'drunk', 'droopy', 'dank', 'drowned', 'enraged', 'angry', 'good', 'garnished', 'groaning', 'happy', 'hopeful', 'graceful', 'gentle', 'hairy', 'inteligent', 'intergallactic', 'jelly filled', 'jumping', 'kind', 'limp', 'blind', 'lumpy', 'insane', 'meek', 'nocternal', 'artifcial', 'perfect', 'quirky', 'petty', 'rocky', 'sad', 'sorrowful', 'useless', 'sickly', 'unbeatable', 'zesty', 'acrobatic', 'buttered', 'burpy', ]
  noun = ['chair', 'tortoise', 'fruit', 'paper', 'gecko', 'giraffe', 'mountain', 'boy', 'urinal', 'pencil','toenail', 'pug', 'wrangler', 'garbage', 'tugboat', 'bladder', 'viper', 'chicken', 'gnome', 'slayer', 'apple', 'artichoke', 'butter', 'bladder', 'cat', 'coop', 'carp', 'dome', 'door', 'horse', 'dart', 'fart', 'farie', 'garlic', 'goop', 'gunk', 'guild', 'hoop', 'harp', 'handle', 'house', 'cow', 'cake', 'cookie', 'largo', 'armor', 'bow', 'map', 'mayonaise', 'egg', 'napkin', 'octopus', 'park', 'pancake', 'punk', 'queen', 'rock', 'salmon', 'sock', 'syrup', 'tophat', 'viking', 'hipopotomous']
  discname2 = ['saucy', 'momma', 'mecha', 'earth', 'barbed', 'prehistoric', 'old','cosmic', 'metallic', 'neat', 'supa', 'haunted', 'ruthless', 'clueless', 'rough', 'killer', 'spoopy', 'retro', 'ancient', 'strange', 'astro', 'baren', 'burned', 'chared', 'crap', 'cranky', 'crummy', 'croaked', 'dead', 'daring', 'drunk', 'droopy', 'dank', 'drowned', 'enraged', 'angry', 'good', 'garnished', 'groaning', 'happy', 'hopeful', 'graceful', 'gentle', 'hairy', 'inteligent', 'intergallactic', 'jelly filled', 'jumping', 'kind', 'limp', 'blind', 'lumpy', 'insane', 'meek', 'nocternal', 'artifcial', 'perfect', 'quirky', 'petty', 'rocky', 'sad', 'sorrowful', 'useless', 'sickly', 'unbeatable', 'zesty', 'acrobatic', 'buttered', 'burpy',]
  noun2 = ['chair', 'tortoise', 'fruit', 'paper', 'gecko', 'giraffe', 'mountain', 'boy', 'urinal', 'pencil','toenail', 'pug', 'wrangler', 'garbage', 'tugboat', 'bladder', 'viper', 'chicken', 'gnome', 'slayer', 'apple', 'artichoke', 'butter', 'bladder', 'cat', 'coop', 'carp', 'dome', 'door', 'horse', 'dart', 'fart', 'farie', 'garlic', 'goop', 'gunk', 'guild', 'hoop', 'harp', 'handle', 'house', 'cow', 'cake', 'cookie', 'largo', 'armor', 'bow', 'map', 'mayonaise', 'egg', 'napkin', 'octopus', 'park', 'pancake', 'punk', 'queen', 'rock', 'salmon', 'sock', 'syrup', 'tophat', 'viking', 'hipopotomous',]
  rand1 = random.choice(discname1)
  rand2 = random.choice(noun)
  username = (random.choice(discname2) + ' ' + random.choice(discname1) + ' ' + random.choice(noun) + ' ' + random.choice(noun2))
  input_elements = driver.find_elements(xpath='//input')
  driver.type(username)
  driver.type(driver.Key.ENTER)
  time.sleep(0.5)


  botconect = botconect + 1
  time.sleep(3)
  driver.go_to('blooket.com/play')
driver.type(code)
driver.type(driver.Key.ENTER)
time.sleep(0.5)
discname1 = ['saucy', 'momma', 'mecha', 'earth', 'barbed', 'prehistoric', 'old','cosmic', 'metallic', 'neat', 'supa', 'haunted', 'ruthless', 'clueless', 'rough', 'killer', 'spooky', 'retro', 'ancient', 'strange', 'astro', 'baren', 'burned', 'chared', 'crap', 'cranky', 'crummy', 'croaked', 'dead', 'daring', 'drunk', 'droopy', 'dank', 'drowned', 'enraged', 'angry', 'good', 'garnished', 'groaning', 'happy', 'hopeful', 'graceful', 'gentle', 'hairy', 'inteligent', 'intergallactic', 'jelly filled', 'jumping', 'kind', 'limp', 'blind', 'lumpy', 'insane', 'meek', 'nocternal', 'artifcial', 'perfect', 'quirky', 'petty', 'rocky', 'sad', 'sorrowful', 'useless', 'sickly', 'unbeatable', 'zesty', 'acrobatic', 'buttered', 'burpy', ]
noun = ['chair', 'tortoise', 'fruit', 'paper', 'gecko', 'giraffe', 'mountain', 'boy', 'urinal', 'pencil','toenail', 'pug', 'wrangler', 'garbage', 'tugboat', 'bladder', 'viper', 'chicken', 'gnome', 'slayer', 'apple', 'artichoke', 'butter', 'bladder', 'cat', 'coop', 'carp', 'dome', 'door', 'horse', 'dart', 'fart', 'farie', 'garlic', 'goop', 'gunk', 'guild', 'hoop', 'harp', 'handle', 'house', 'cow', 'cake', 'cookie', 'largo', 'armor', 'bow', 'map', 'mayonaise', 'egg', 'napkin', 'octopus', 'park', 'pancake', 'punk', 'queen', 'rock', 'salmon', 'sock', 'syrup', 'tophat', 'viking', 'hipopotomous']
discname2 = ['saucy', 'momma', 'mecha', 'earth', 'barbed', 'prehistoric', 'old','cosmic', 'metallic', 'neat', 'supa', 'haunted', 'ruthless', 'clueless', 'rough', 'killer', 'spoopy', 'retro', 'ancient', 'strange', 'astro', 'baren', 'burned', 'chared', 'crap', 'cranky', 'crummy', 'croaked', 'dead', 'daring', 'drunk', 'droopy', 'dank', 'drowned', 'enraged', 'angry', 'good', 'garnished', 'groaning', 'happy', 'hopeful', 'graceful', 'gentle', 'hairy', 'inteligent', 'intergallactic', 'jelly filled', 'jumping', 'kind', 'limp', 'blind', 'lumpy', 'insane', 'meek', 'nocternal', 'artifcial', 'perfect', 'quirky', 'petty', 'rocky', 'sad', 'sorrowful', 'useless', 'sickly', 'unbeatable', 'zesty', 'acrobatic', 'buttered', 'burpy',]
noun2 = ['chair', 'tortoise', 'fruit', 'paper', 'gecko', 'giraffe', 'mountain', 'boy', 'urinal', 'pencil','toenail', 'pug', 'wrangler', 'garbage', 'tugboat', 'bladder', 'viper', 'chicken', 'gnome', 'slayer', 'apple', 'artichoke', 'butter', 'bladder', 'cat', 'coop', 'carp', 'dome', 'door', 'horse', 'dart', 'fart', 'farie', 'garlic', 'goop', 'gunk', 'guild', 'hoop', 'harp', 'handle', 'house', 'cow', 'cake', 'cookie', 'largo', 'armor', 'bow', 'map', 'mayonaise', 'egg', 'napkin', 'octopus', 'park', 'pancake', 'punk', 'queen', 'rock', 'salmon', 'sock', 'syrup', 'tophat', 'viking', 'hipopotomous',]
rand1 = random.choice(discname1)
rand2 = random.choice(noun)
username = (random.choice(discname2) + ' ' +random.choice(discname1) + ' ' + random.choice(noun) + ' ' + random.choice(noun2))
input_elements = driver.find_elements(xpath='//input')
driver.type(driver.Key.TAB)
driver.type(username)
driver.type(driver.Key.ENTER)
time.sleep(0.5)
 

botconect = botconect + 1
print (botconect ,"out of", bots ,"bots connected successfully")
tab = 0
timerun = 0
while True:
  tab = tab + 1
  driver.switch_to_tab(tab)
  while True:
    url = driver.get_current_url()
    if url == "https://kahoot.it/v2/gameblock":
      break
  input_elements = driver.find_elements(xpath='//input')
  pick = random.randint (1,4)
  if pick == 1:
    driver.type(driver.Key.TAB,into=input_elements[0].text)
    print("Kahoot.it bot picked: Red")
  if pick == 2:
    driver.type(driver.Key.TAB,into=input_elements[0].text)
    driver.type(driver.Key.TAB,into=input_elements[0].text)
    print("Kahoot.it bot picked: Blue")
  if pick == 3:
    driver.type(driver.Key.TAB,into=input_elements[0].text)
    driver.type(driver.Key.TAB,into=input_elements[0].text)
    driver.type(driver.Key.TAB,into=input_elements[0].text)
    print("Kahoot.it bot picked: Yellow")
  if pick == 4:
    driver.type(driver.Key.TAB,into=input_elements[0].text)
    driver.type(driver.Key.TAB,into=input_elements[0].text)
    driver.type(driver.Key.TAB,into=input_elements[0].text)
    driver.type(driver.Key.TAB,into=input_elements[0].text)
    print("Kahoot.it bot picked: Green")
  driver.type(driver.Key.ENTER,into=input_elements[0].text)
  timerun = timerun + 1
  if timerun == bots:
    tab = 0
    timerun = 0
    print("Next Question")
  exit = driver.get_current_url()
  if exit == "https://kahoot.it/v2/ranking":
    sys.exit(0)