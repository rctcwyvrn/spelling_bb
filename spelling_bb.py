import string
import random
letters = list(string.ascii_lowercase)
vowels = ["a", "e", "i", "o", "u"]
def get_words(filename):
    return [s.strip().lower() for s in open(filename).readlines()]

wordlist = get_words("words.txt")
wordlist.extend(get_words("additional_words.txt"))

print("Welcome to Lily's spelling 🐝")
print("1. Generate new game")
print("2. Load game from code")
choice = input("> ")

if choice == "1":
    center_letter = random.choice(vowels)
    letters.remove(center_letter)
    game_letters = random.sample(letters, k=6)
    game_letters.append(center_letter)
elif choice == "2":
    print("Input code")
    code = input("> ")
    if len(code) != 7:
        print("Invalid code")
        exit()
    game_letters = code
    center_letter = code[-1]
else:
    print("??? the options are 1 or 2")
    exit()

def valid_game_word(s):
    return (center_letter in s) and (all([c in game_letters for c in s]))

game_words = list(set(filter(valid_game_word, wordlist)))
game_words.sort()

def menu():
    half = " " * 2
    print(half + game_letters[0] + half + game_letters[1])
    print(game_letters[2] + half + game_letters[-1] + half + game_letters[3])
    print(half + game_letters[4] + half + game_letters[5])
    print(f"Current correct guesses = {successful}")
    print(f"Guessed: {len(successful)}/{len(game_words)}")

print(f"There are {len(game_words)} valid words for this game")
print(f"Game code: {''.join(game_letters)}")
# print(f"debug: {game_words}")

successful = []
while True:
    menu()
    guess = input("> ")
    if guess == "reveal_answer":
        print(f"The words are: {game_words}")
        break
    if guess in game_words and not guess in successful:
        print(f"{guess} is a valid word")
        successful.append(guess)
        successful.sort()
    else:
        print(f"{guess} is not a valid word or has already been guessed")