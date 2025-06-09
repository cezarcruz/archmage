import os
import sys

from archmage.lib.utils.logger import setup_logger
from archmage.lib.utils.system import default_system

KDE_PLASMA_APPS = [
    "spectacle",
    "xdg-desktop-portal-gtk",
    "flatpak",
    "partitionmanager",
    "okular",
    "geoclue",
    "dragon",
    "filelight",
    "inter-font",
    "gwenview",
    "haruna",
    "kcalc",
]

GNOME_APPS = [
    "papers",
    "nautilus-python",
    "adw-gtk-theme",
    "ghostty",
]


# TODO: revisit this
class Desktop:
    def __init__(self, logger=None, system=None) -> None:
        self.logger = logger or setup_logger(__name__)
        self.system = system or default_system

    def is_kde(self) -> bool:
        return os.environ["DESKTOP_SESSION"] == "plasma"

    def setup_de(self) -> None:
        if self.is_kde():
            self.logger.info(
                "Detected KDE Plasma desktop environment. Can you confirm this? (y/n/q):"
            )
            response = input()

            if response == "q":
                sys.exit(0)
            else:
                self.logger.error(
                    "Invalid response. Please answer with 'y' or 'n' or 'q'."
                )
                sys.exit(1)

            if response == "y":
                self.logger.info("Proceeding with KDE Plasma setup...")
                self.system.install_package(KDE_PLASMA_APPS)
            else:
                self.logger.info("Setupping GNOME desktop environment instead.")
                self.system.install_package(GNOME_APPS)


__all__ = ["default_desktop"]

default_desktop: Desktop = Desktop()
