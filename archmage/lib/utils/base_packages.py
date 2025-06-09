from archmage.lib.utils.logger import setup_logger
from archmage.lib.utils.system import default_system

BASE_PACKAGES: list[str] = [
    "firefox",
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
    "eza",
]

BASE_FONTS_PACKAGES: list[str] = [
    "ttf-jetbrains-mono",
    # "ttf-roboto",
    "noto-fonts",
    "ttf-liberation",
]

PACKAGES_TO_REMOVE: list[str] = [
    "htop",
    "nano",
    "epiphany",
    "gnome-tour",
    "gnome-console",
]


class BasePackages:
    def __init__(self, logger=None, system=None):
        self.logger = logger or setup_logger(__name__)
        self.system = system or default_system

    def install_base_packages(self) -> None:
        self.system.install_packages(BASE_PACKAGES)
        self.system.install_packages(BASE_FONTS_PACKAGES)

    def remove_unnused_packages(self) -> None:
        self.system.remove_packages(PACKAGES_TO_REMOVE)


default_base_packages: BasePackages = BasePackages()
