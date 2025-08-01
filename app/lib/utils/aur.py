import os

from app.lib.utils.config import default_config
from app.lib.utils.logger import setup_logger
from app.lib.utils.system import default_system


class Aur:
    def __init__(self, logger=None, config=None, system=None) -> None:
        self.logger = logger or setup_logger
        self.config = config or default_config
        self.system = system or default_system

    def configure_chaotic_aur(self):
        self.system.arbitraty_command(["sudo", "pacman-key", "--init"])
        self.system.arbitraty_command(["sudo", "pacman-key", "--recv-key", "3056513887B78AEB", "--keyserver", "keyserver.ubuntu.com"])
        self.system.arbitraty_command(["sudo", "pacman-key", "--lsign-key", "3056513887B78AEB"])
        self.system.arbitraty_command(["sudo", "pacman", "-U", "https://cdn-mirror.chaotic.cx/chaotic-aur/chaotic-keyring.pkg.tar.zst"])
        self.system.arbitraty_command(["sudo", "pacman", "-U", "https://cdn-mirror.chaotic.cx/chaotic-aur/chaotic-mirrorlist.pkg.tar.zst"])
        
        with open("/tmp/chaotic-aur-config", "w") as f:
            f.write("\n[chaotic-aur]\nInclude = /etc/pacman.d/chaotic-mirrorlist\n")
        
        self.system.arbitraty_command("sudo tee -a /etc/pacman.conf < /tmp/chaotic-aur-config")
        os.remove("/tmp/chaotic-aur-config")

__all__ = ["default_aur"]

default_aur: Aur = Aur()