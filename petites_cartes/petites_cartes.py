import json
import glob
import os
import sys
import random
import argparse
import itertools
import time
import math
import statistics

try:
    import curses
except ModuleNotFoundError:
    print("""
    Couldn't import curses module,
    Please install another terminal .-.""")
    exit()


def quiz(w, cards, reverse):
    L = curses.LINES
    l = L // 2
    C = curses.COLS
    c = C // 2

    words_lens = [len(word) for word in itertools.chain(*cards)]
    x_pos = c - int(statistics.mean(words_lens)) // 2

    card_no = 0
    while True:
        random.shuffle(cards)
        for card in cards:
            if reverse:
                card = card[::-1]

            card_no += 1
            count = f"{str(card_no)}/{str(len(cards))}"

            w.box()
            w.addstr(L - 2, C - 2 - len(str(count)), count, curses.A_DIM)
            lines = [i - math.floor(len(card) / 2) for i in range(len(card))]
            for i, word in enumerate(card):
                w.addstr(l + lines[i], x_pos, word)
                w.getkey()
            w.clear()

def view(w, cards):
    cols = len(cards[0])
    L = curses.LINES
    l = L // 2
    C = curses.COLS
    c = C // 2

    la = L - 2
    ca = C - 2

    col_width = ca//cols
    len_cols = [max([len(card[i]) for card in cards]) for i in range(cols)]

    w.box()
    for i, card in enumerate(cards):
        for j, word in enumerate(card):
            w.addstr(i + 1, len_cols[j] + 2*j, word)
    key = w.getkey()




def posivite_int(t):
    try:
        t = int(t)
    except:
        raise TypeError
    if t <= 0:
        raise ValueError
    return t


def petites_cartes():
    parser = argparse.ArgumentParser()
    parser.add_argument("-f", "--file", type=str)
    parser.add_argument("-o", "--offset", default=0, type=posivite_int)
    parser.add_argument("-s", "--size", default=10, type=posivite_int)
    parser.add_argument("-r", "--reverse", action="store_true")
    parser.add_argument("-v", "--view", action="store_true")

    args = parser.parse_args()

    if args.file is None:
        jsons = glob.glob("*.json")
        try:
            file = jsons[0]
        except:
            print("No .json file in this directory.")
            exit(-1)
    else:
        file = args.file

    cards = json.load(open(file))
    cards = cards[args.offset:args.offset + args.size]

    try:
        w = curses.initscr()
        curses.noecho()
        curses.curs_set(False)
        if args.view:
            view(w, cards)
        else:
            quiz(w, cards, args.reverse)
    except KeyboardInterrupt:
        pass
    finally:
        curses.curs_set(True)
        curses.endwin()
