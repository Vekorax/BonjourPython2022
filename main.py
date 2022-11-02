#!/usr/bin/env python3

import time


def print_hi(name):
    print(f'Bonjour, {name}')


def compter(nb):
    print(f"Je sais compter jusqu'à {nb}:", end=' ', flush=True)
    for i in range(1, nb + 1):
        time.sleep(0.25)
        print(i, end=' ', flush=True)
    print()


def main():
    print_hi('Fabrice M.')
    compter(5)
    compter(10)


if __name__ == '__main__':
    main()
