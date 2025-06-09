import os
import sys

from archmage.lib.utils.aur import default_aur
from archmage.lib.utils.base_packages import default_base_packages
from archmage.lib.utils.config import default_config
from archmage.lib.utils.flatpak import default_flatpak
from archmage.lib.utils.home import default_home
from archmage.lib.utils.language import default_language
from archmage.lib.utils.logger import setup_logger
from archmage.lib.utils.services import default_services
from archmage.lib.utils.system import default_system


class Application:
    def __init__(
        self,
        logger=None,
        config=None,
        system=None,
        packages=None,
        language=None,
        services=None,
        aur=None,
        flatpak=None,
        home=None
    ):
        self.logger = logger or setup_logger(__name__)
        self.config = config or default_config
        self.system = system or default_system
        self.language = language or default_language
        self.packages = packages or default_base_packages
        self.services = services or default_services
        self.aur = aur or default_aur
        self.flatpak = flatpak or default_flatpak
        self.home = home or default_home

    def run(self) -> None:
        self.logger.info("Running the application...")

        self.cleaning_screen()
        self.check_sudo()
        self.print_welcome()
        self.show_dry_run_warning()

        self.system.update()
        self.language.configure_language()
        self.packages.install_base_packages()
        self.services.start_common_services()
        self.aur.configure_chaotic_aur()
        self.flatpak.install_flatpaks()
        self.home.configure_user_home()

    def check_sudo(self):
        if os.getuid() == 0:
            self.logger.error(
                "This script should not be run as root. Please run it as a regular user."
            )
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
