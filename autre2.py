#!/usr/bin/env python3
"""
Autre script pour appeler les fonctions
du script principal, version 2.

Par: Fabrice Morin
"""

from main import bonjour
from main import compter


def main():
    """
    Fonction principale du script
    """
    bonjour('Morin F.')
    compter(3)


if __name__ == '__main__':
    main()
