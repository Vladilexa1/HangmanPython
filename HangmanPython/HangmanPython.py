# -*- coding: cp1251 -*-
import random
import os, sys



def random_word():
    with open('words.txt', 'r') as file:
        lines = file.read().splitlines()
        for line in lines:
            line.strip()
    return random.choice(lines).lstrip()

def clear():
    os.system("cls")


def check_valid_symbol(symbol):
    if 1073 <= ord(symbol) <= 1103:
        return True
    else:
        return False


def start_new_game(word):
    clear()
    print(word)
    count_mistake = 0
    print_gallows(count_mistake)
    result = ""
    for l in word:
        result += "*"
    writenSymbol = ""
    while count_mistake != 6:
        print(result)
        print(f"������: - {count_mistake}") 
        input_letter = input("������� �����: ").lower()
       
        if not check_valid_symbol(input_letter):
            print("��� �� �����!")
            continue

        if input_letter in writenSymbol:
            print("�� ������� ��� �����!")
            continue
        writenSymbol += input_letter
        i = 0
        new_result = ""
        
        while len(word) > i:
            if input_letter == word[i]: 
                new_result += input_letter
            elif result[i] == "*":
                new_result += "*"
            else:
                new_result += result[i]
            i += 1
            if result == new_result:
                count_mistake += 1
                print_gallows(count_mistake)
        
        
        result = new_result 
        if result == word:
            print("�� ��������!")
            return
            

def print_gallows(coumt_mistake):
    gallows = [
        """    +---+
    |   |
        |
        |
        |
        |
  =========""",
  """    +---+
    |   |
    O   |
        |
        |
        |
  =========""",
"""    +---+
    |   |
    O   |
    |   |
        |
        |
  =========""", 
"""    +---+
    |   |
    O   |
   /|   |
        |
        |
  =========""",
"""    +---+
    |   |
    O   |
   /|\  |
        |
        |
  =========""","""    +---+
    |   |
    O   |
   /|\  |
   /    |
        |
  =========""", """    +---+
    |   |
    O   |
   /|\  |
   / \  |
        |
  ========="""]
    print(gallows[coumt_mistake])


while True:
    print("������ ����� ����?", "�/�")
    state = input().lower()
    if state == "�":
        start_new_game(random_word())
    else: 
        print("�������� �����!")
        break





