#!/usr/bin/env python3

import os
import sys

from lib.utils.logger import setup_logger
from lib.utils.config import config
from lib.utils.system import system 

class App:
    def __init__(self):
        self.logger = setup_logger(__name__)

    def run(self):
        self.logger.info("Running the application...")
        self.cleaning_screen()

        if os.getuid() == 0:
            self.logger.error("This script should not be run as root. Please run it as a regular user.")
            sys.exit(1)
    
        config.parse_args()

        self.print_welcome()
        self.show_dry_run_warning()

        system.update()
    
    def cleaning_screen(self):
        os.system('clear' if os.name == 'posix' else 'cls')

    def show_dry_run_warning(self):
        if config.is_dry_run():
            self.logger.warning("This is a dry run. No changes will be made to the system.")
            self.logger.warning("To perform actual changes, set DRY_RUN to False in the script.")

    def print_welcome(self):
        self.logger.info("Welcome to the Arch Linux setup script!")
        self.logger.info("This script will guide you through the post install setup process.")
        self.logger.info("Please follow the instructions carefully.")

if __name__ == "__main__":
    app = App()
    app.run()
