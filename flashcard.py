import random
import time
import os

FLASHCARD_FILENAME = "cards.txt"


def clear_terminal():
    # print('\n' * 100) # if you want to run the script in IDLE
    os.system("cls" if os.name == "nt" else "clear")


def show_menu():
    clear_terminal()
    print("\n#### Welcome ###")
    print("1- Same Order (Question -> Answer)\n2- Revers Order (Answer -> Question)\n3- Random Order\n4- EXIT\n")


def show_flashcard(question, answer):
    clear_terminal()
    print("\nPress \"Enter\" key to reveal the answer .. (Put q to quit)\n")
    choice = ""
    # Loop to keep showing cards until the user exit the loop by putting 'q'
    while choice != "q":
        with open(FLASHCARD_FILENAME, "r") as f:
            # choice a random line from the file and then remove the \n that been created by readlines()
            card = random.choice(f.readlines()).strip()
        sentence = card.split(" : ")  # separate the question from the answer and put them in a list
        print(f"\n{sentence[question]}\n")
        choice = input().lower()
        clear_terminal()
        print("\nPress \"Enter\" key to reveal the answer .. (Put q to quit)\n\n")
        print(f"{sentence[question]}\n{sentence[answer]}\n")
        time.sleep(1)


def show_flashcard_randomly():
    clear_terminal()
    print("\nPress \"Enter\" key to reveal the answer .. (Put q to quit)\n")
    choice = ""
    while choice != "q":
        with open(FLASHCARD_FILENAME, "r") as f:
            card = random.choice(f.readlines()).strip()
        sentence = card.split(" : ")
        question = random.randrange(2)
        if question == 0:
            answer = 1
        else:
            answer = 0

        print(f"\n{sentence[question]}\n")
        choice = input().lower()
        clear_terminal()
        print("\nPress \"Enter\" key to reveal the answer .. (Put q to quit)\n\n")
        print(f"{sentence[question]}\n{sentence[answer]}\n")
        time.sleep(1)


def main():
    show_menu()
    choose = input("Put the number that you want: ")
    while True:
        if choose in ('1', '2', '3', '4'):
            break
        show_menu()
        print("\tWRONG INPUT!\n")
        choose = input("Put the number that you want: ")

    if choose == "1":
        show_flashcard(0, 1)
    elif choose == "2":
        show_flashcard(1, 0)
    elif choose == "3":
        show_flashcard_randomly()
    clear_terminal()
    print("\n\nThank you for using me .. Come back soon :)\n\n")


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        clear_terminal()
        raise SystemExit




