from archmage.lib.utils.logger import setup_logger
from archmage.lib.utils.system import default_system

BASE_PACKAGES: list[str] = ["firefox",
  "docker",
  "docker-compose",
  "git",
  "go",
  "btop",
  "neovim",
  "reflector",
  "ttf-jetbrains-mono",
  "pacman-contrib",
  "bat",
  "pkgstats",
  "fish",
  "ttf-roboto",
  "fuse",
  "less",
  "mise",
  "rsync",
  "kitty",
  "eza"]

BASE_FONTS_PACKAGES: list[str] = ["ttf-jetbrains-mono",
  #"ttf-roboto",
  "noto-fonts",
  "ttf-liberation",]

class BasePackages:
    def __init__(self, logger=None, system=None):
        self.logger = logger or setup_logger(__name__)
        self.system = system or default_system

    def install_base_packages(self) -> None:
        self.logger.info("Installing base packages...")
        self.system.install_package(BASE_PACKAGES)
        self.logger.info("Installing fonts...")
        self.system.install_package(BASE_FONTS_PACKAGES)



default_base_packages: BasePackages = BasePackages()
