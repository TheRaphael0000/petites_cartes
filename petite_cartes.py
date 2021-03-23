import json
import glob
import os
import sys
import random
import curses
import argparse
import itertools
import time
import math


def quiz(w, cards):
    L = curses.LINES
    l = L // 2
    C = curses.COLS
    c = C // 2

    card_no = 0
    while True:
        random.shuffle(cards)
        for card in cards:
            card_no += 1
            count = f"{str(card_no)}/{str(len(cards))}"

            w.box()
            w.addstr(L - 2, C - 2 - len(str(count)), count, curses.A_DIM)
            lines = [i - math.floor(len(card) / 2) for i in range(len(card))]
            for i, word in enumerate(card):
                w.addstr(l + lines[i], c - len(word) // 2, word)
                w.getkey()
            w.clear()


def posivite_int(t):
    try:
        t = int(t)
    except:
        raise TypeError
    if t <= 0:
        raise ValueError
    return t


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("-f", "--file", type=str)
    parser.add_argument("-o", "--offset", default=0, type=posivite_int)
    parser.add_argument("-s", "--size", default=10, type=posivite_int)
    parser.add_argument("-r", "--random", action="store_true")

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
        quiz(w, cards)
    except KeyboardInterrupt:
        curses.curs_set(True)
        curses.endwin()
