from archmage.lib.utils.logger import setup_logger


class Flatpak:
    def __init__(self, logger=None) -> None:
        self.logger = logger or setup_logger(__name__)

    def install_flatpaks(self):
        self.logger.info("Installing Flatpak packages...")

default_flatpak: Flatpak = Flatpak()