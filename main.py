#!/usr/bin/env python3

"""
Script principal.

Par: Fabrice Morin
"""
import time


def bonjour(name):
    """
    Pour Saluer
    :param name: Nom de la personne à saluer.
    """
    print(f'Bonjour, {name}')


def compter(nb, secs=0.25):
    """
    Pour compter progressivement.
    :param nb: jusqu'ou compter
    :param secs: intervalle de temps entre les nombres
    """
    print(f"Je sais compter jusqu'à {nb}:", end=' ', flush=True)
    for i in range(1, nb + 1):
        time.sleep(secs)
        print(i, end=' ', flush=True)
    print()


def main():
    """
    Fonction principale du script
    """
    bonjour('Fabrice M.')
    compter(5)
    compter(10)


if __name__ == '__main__':
    main()
