#!/usr/bin/env python3
"""
Autre script pour appeler les fonctions
du script principal, version 1.

Par: Fabrice Morin
"""
import main as bonjour


def main():
    """
    Fonction principale
    """
    bonjour.bonjour('Morin F. alias FM')
    bonjour.compter(8, 0.5)


if __name__ == '__main__':
    main()
