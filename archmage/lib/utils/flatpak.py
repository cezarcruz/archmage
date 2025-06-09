from archmage.lib.utils.logger import setup_logger
from archmage.lib.utils.system import default_system

FLATPAK_PACKAGES: list[str]=[
  "com.valvesoftware.Steam"
  #"com.mattjakeman.ExtensionManager" only for GNOME
]

class Flatpak:
    def __init__(self, logger=None, system=None) -> None:
        self.logger = logger or setup_logger(__name__)
        self.system = system or default_system

    def install_flatpaks(self):
        self.logger.info("Installing Flatpak packages...")
        self.system.install_flatpaks(FLATPAK_PACKAGES)

__all__ = ["default_flatpak"]

default_flatpak: Flatpak = Flatpak()