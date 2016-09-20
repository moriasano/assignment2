""" Varies utility functions """
import os
from hashlib import (md5, sha256, sha512)

PASSWORDS = "phpbb.txt"
HASH_ALGS = {
    # Entries are in the form:
    # "Shadow file code": ("Mechanism_name", hash_function)
    "0": ("DES", None),
    "1": ("MD5", md5),
    "2": ("Blowfish", None),
    "2a": ("eksBlowfish", None),
    "5": ("SHA256", sha256),
    "6": ("SHA512", sha512)
}


def welcome():
    """ Prints the welcome screen """
    print("  ____  _               _                ____                _    ")
    print(" / ___|| |__   __ _  __| | _____      __/ ___|_ __ __ _  ___| | __")
    print(" \___ \| '_ \ / _` |/ _` |/ _ \ \ /\ / / |   | '__/ _` |/ __| |/ /")
    print("  ___) | | | | (_| | (_| | (_) \ V  V /| |___| | | (_| | (__|   < ")
    print(" |____/|_| |_|\__,_|\__,_|\___/ \_/\_/  \____|_|  \__,_|\___|_|\_\ ")
    print("\n")
    print("                                                   Mori Asano 2016")
    for _ in range(2):
        print "\n"
    print "Current using the %s dictionary." % PASSWORDS


def get_sc_params():
    """
    Prompt the user for the 'Shadow Crack' params
    :return: shadow file path, username
    """
    loop = True
    while loop:
        file_path = input("Enter the file path for the shadow file:")
        if os.access(file_path, os.F_OK):
            if os.access(file_path, os.R_OK):
                loop = False
            print("That file path cannot be read. Check the file privileges.")
        print("That file path does not exist. Try again.")

    user_name = input("Who's password are we cracking? Enter the username:")
    return file_path, user_name

