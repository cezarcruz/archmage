#!/usr/bin/env python3

import os
import sys
from lib.utils.logger import setup_logger
from lib.utils.config import config
from lib.utils.system import system 

def show_dry_run_warning():
    if config.is_dry_run():
        logger.warning("This is a dry run. No changes will be made to the system.")
        logger.warning("To perform actual changes, set DRY_RUN to False in the script.")

def cleaning_screen():
    os.system('clear' if os.name == 'posix' else 'cls')

def print_welcome():
    logger.info("Welcome to the Arch Linux setup script!")
    logger.info("This script will guide you through the post install setup process.")
    logger.info("Please follow the instructions carefully.")

def main():
    cleaning_screen()

    # check if the script is run with root privileges
    if os.getuid() == 0:
        logger.error("This script should not be run as root. Please run it as a regular user.")
        sys.exit(1)
    
    config.parse_args()

    print_welcome()
    show_dry_run_warning()

    system.update()

if __name__ == "__main__":
    logger = setup_logger(__name__)    
    main()
