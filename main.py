#!/usr/bin/env python3

import os
import sys
from lib.utils.logger import setup_logger


def cleaning_screen():
    os.system('clear' if os.name == 'posix' else 'cls')

def print_welcome():
    logger.info("Welcome to the Arch Linux setup script!")
    logger.info("This script will guide you through the post install setup process.")
    logger.info("Please follow the instructions carefully.")

def main():
    # check if the script is run with root privileges
    if os.getuid() == 0:
        logger.error("This script should not be run as root. Please run it as a regular user.")
        sys.exit(1)

    cleaning_screen()
    print_welcome()

if __name__ == "__main__":
    logger = setup_logger(__name__)
    main()
