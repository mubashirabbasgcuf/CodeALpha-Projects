# creating a text base Hangman game 
# Project no 1
import random
# imported necessary library 
# it will help us to import random words from the list
# we can also import txt file which would have all the words but i have made a list in words
words = [
    "Apple", "Bicycle", "Computer", "Dragon", "Elephant", "Forest", "Guitar", "Hospital", "Island", "Jacket",
    "Kangaroo", "Laptop", "Mountain", "Notebook", "Orange", "Pillow", "Quicksand", "Rainbow", "Suitcase", "Tornado",
    "Umbrella", "Volcano", "Waterfall", "Xylophone", "Yacht", "Zebra", "Airplane", "Bakery", "Castle", "Dinosaur",
    "Engine", "Flower", "Garage", "Helicopter", "Igloo", "Jellyfish", "Keychain", "Lighthouse", "Marshmallow",
    "Necklace", "Oxygen", "Pirate", "Quarantine", "River", "Satellite", "Telephone", "Universe", "Vampire", "Window",
    "X-ray", "Yearbook", "Zipper", "Avocado", "Balloon", "Chocolate", "Dentist", "Elevator", "Frisbee", "Garden",
    "Hamburger", "Iceberg", "Jellybean", "Kite", "Lizard", "Motorcycle", "Necklace", "Ocean", "Pancake", "Quicksilver",
    "Rocket", "Spider", "Telescope", "Unicorn", "Vacation", "Whistle", "Xenon", "Yardstick", "Zeppelin", "Acrobat",
    "Blender", "Cactus", "Dolphin", "Earphone", "Funnel", "Grapefruit", "Handkerchief", "Insect", "Juice", "Keyboard",
    "Luggage", "Mummy", "Narwhal", "Ostrich", "Pancake", "Quilt", "Robot", "Sandwich", "Teapot", "Umbrella", "Violin",
    "Wagon", "Xylophone", "Yarn", "Zebra", "Arrow", "Bookstore", "Camera", "Doctor", "Envelope", "Fence", "Globe", 
    "Hat", "Ice", "Jam", "Kangaroo", "Lamp", "Magnet", "Necklace", "Octopus", "Pizza", "Quokka", "Refrigerator", 
    "Socks", "Tree", "Umbrella"
]
# this is the list of thw words which we will use in our game 

word = random.choice(words)
# liisting the total number of chances which we want to allow the user 
# upon 7 incorrect entries the game will be end 
total_chances = 7
guessed_words = "-" * len(word)
# this is the variable which will store the guessed word by the user
guessed_letters = set()
# this is the variable which will store the letters which are already guessed by the user
# we are using set data type because it will not allow duplicate values
# main logic
while total_chances != 0:
    letter = input("Guess a letter: ").lower()
    if letter in guessed_letters:
        print("You already guessed this letter. Try another one.")
        continue
    guessed_letters.add(letter)

    if letter in word:
        for index in range(len(word)):
            if word[index] == letter:
                guessed_words = guessed_words[:index] + letter + guessed_words[index+1:]
        print(guessed_words)
        if guessed_words == word:
            print("You won!")
            break
    else:
        # upon every wrong word guess a chance will be lossed
        total_chances -= 1
        print("Remaining chances:", total_chances)
else:
    print("Game over. The word was:", word)
    print("Game over. You lose.")
    print("All chances finished.")