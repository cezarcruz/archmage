from app.lib.utils.desktop import default_desktop
from app.lib.utils.logger import setup_logger
from app.lib.utils.system import default_system

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
    "noto-fonts",
    "ttf-liberation",
]

PACKAGES_TO_REMOVE: list[str] = [
    "htop",
    "nano",
    "epiphany",
    "gnome-tour",
    "gnome-console",
    "gnu-free-fonts"
]


class BasePackages:
    def __init__(self, logger=None, system=None, desktop=None):
        self.logger = logger or setup_logger(__name__)
        self.system = system or default_system
        self.desktop = desktop or default_desktop

    def install_base_packages(self) -> None:
        self.system.install_packages(BASE_PACKAGES)
        self.system.install_packages(BASE_FONTS_PACKAGES)

        if self.desktop.is_kde():
            self.system.install_packages(KDE_PLASMA_APPS)
        else:
            self.system.install_packages(GNOME_APPS)

    def remove_unnused_packages(self) -> None:
        self.system.remove_packages(PACKAGES_TO_REMOVE)


default_base_packages: BasePackages = BasePackages()
