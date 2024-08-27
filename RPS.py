import random
import time

BL = '\033[94m'
WH = '\033[97m'
GR = '\033[92m'
RD = '\033[91m'
RS = '\033[0m'

rolls = ["Rock ✊", "Paper ✋", "Scissors ✌️"]
rolls_s = ["R", "P", "S"]
win = [("Rock ✊", "Scissors ✌️"), ("Paper ✋", "Rock ✊"), ("Scissors ✌️", "Paper ✋")]
(h_s, c_s) = (0, 0)


def check_file():
    try:
        with open('RPSResults.txt', 'r'):
            pass
    except:
        with open("RPSResults.txt", "w") as file:
            file.write("Rock-Paper-Scissors Game Results\n")
            file.write("==============================\n")


def roll():
    while True:
        h_ch = input(f"{BL}R{WH}ock ✊, {BL}P{WH}aper ✋ or {BL}S{WH}cissors ✌️: {RS}").upper()
        if h_ch in rolls_s:
            return {"R": "Rock ✊", "P": "Paper ✋", "S": "Scissors ✌️"}.get(h_ch)
        else:
            print(f"{RD}  > Please type {BL}R{RD}, {BL}P{RD}, or {BL}S{RD}.{RS}")


def comproll():
    return random.choice(rolls)


def ani():
    print(f"{WH}    Rock ✊... ", end='', flush=True)
    time.sleep(0.4)
    print("Paper ✋... ", end='', flush=True)
    time.sleep(0.4)
    print("Scissors ✌️... ", end='', flush=True)
    time.sleep(0.4)
    print(f"{BL}SHOOT!{RS}")
    print(f"    {name}: {BL}{h}{RS}  ||⚔️||  {BL}{c}{RS} :Computer")
    time.sleep(1)


def save_init():
    try:
        with open('RPSResults.txt', 'a', encoding='utf-8') as database:
            database.write(f"\nMatch: {name} vs Computer\n")
    except Exception as e:
        print(e)


def save_roll():
    try:
        with open('RPSResults.txt', 'a', encoding='utf-8') as database:
            database.write(f"\n    > {name}: {h}  ||⚔️||  {c} :Computer")
    except Exception as e:
        print(e)


def save_score():
    try:
        with open('RPSResults.txt', 'a', encoding='utf-8') as database:
            database.write(f"""\n    Scorecard:
        > {name} - {h_s} Point{'s' if h_s != 1 else ''}
        > Computer - {c_s} Point{'s' if c_s != 1 else ''}""")
    except Exception as e:
        print(e)

check_file()
name = input("Enter your name: ").capitalize()
if name == "":
    name = "Player"
save_init()
while True:
    h = roll()
    c = comproll()
    ani()
    if (h, c) in win:
        (w, l) = (name, "Computer")
        result = "win"
        h_s += 1
    elif (c, h) in win:
        (l, w) = (name, "Computer")
        result = "loss"
        c_s += 1
    else:
        (w, l) = (name, "Computer")
        result = "draw"
        h_s += 0.5
        c_s += 0.5
    save_roll()
    print(f"{RS}It's a Draw!{RS}" if result == "draw" else f"{GR}{w}{WH} wins against {RD}{l}{WH}!")
    time.sleep(2)
    print(f"""
    Scorecard:
        > {RS}{name} - {BL}{h_s} {WH}Point{'s' if h_s != 1 else ''}
        > {RS}Computer - {BL}{c_s} {WH}Point{'s' if c_s != 1 else ''}""")
    if input(f"{RS}Rematch? {BL}[y/n]: {RS}").upper() == "N":
        save_score()
        break
    else:
        pass
