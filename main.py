#!/usr/bin/env python3

import time


def bonjour(name):
    print(f'Bonjour, {name}')


def compter(nb, secs=0.25):
    print(f"Je sais compter jusqu'à {nb}:", end=' ', flush=True)
    for i in range(1, nb + 1):
        time.sleep(secs)
        print(i, end=' ', flush=True)
    print()


def main():
    bonjour('Fabrice M.')
    compter(5)
    compter(10)


if __name__ == '__main__':
    main()
