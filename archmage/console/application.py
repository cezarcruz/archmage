import os
import sys

from archmage.lib.utils.logger import setup_logger
from archmage.lib.utils.config import default_config
from archmage.lib.utils.system import default_system

class Application:
    def __init__(self, logger=None, config=None, system=None):
        self.logger = logger or setup_logger(__name__)
        self.config = config or default_config
        self.system = system or default_system

    def run(self) -> None:
        self.logger.info("Running the application...")

        self.cleaning_screen()
        self.check_sudo()
        self.print_welcome()
        self.show_dry_run_warning()

        self.system.update()
        self.system.configure_language()

    def check_sudo(self):
        if os.getuid() == 0:
            self.logger.error("This script should not be run as root. Please run it as a regular user.")
            sys.exit(1)

    def cleaning_screen(self) -> None:
        os.system("clear" if os.name == "posix" else "cls")

    def show_dry_run_warning(self) -> None:
        if self.config.is_dry_run():
            self.logger.warning("This is a dry run. No changes will be made to the system.")
            self.logger.warning("To perform actual changes, set DRY_RUN to False in the script.")

    def print_welcome(self) -> None:
        self.logger.info("Welcome to the Arch Linux setup script!")
        self.logger.info("This script will guide you through the post install setup process.")
        self.logger.info("Please follow the instructions carefully.")
