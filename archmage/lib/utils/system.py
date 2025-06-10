import subprocess

from archmage.lib.utils.config import default_config
from archmage.lib.utils.logger import setup_logger

UPDATE_COMMAND = ["sudo", "pacman", "-Syu"]
INSTALL_COMMAND = ["sudo", "pacman", "-S"]
REMOVE_COMMAND = ["sudo", "pacman", "-Rs"]
CHECK_INSTALLED_COMMAND = ["sudo", "pacman", "-Qi"]
CHECK_GROUP_INSTALLED_COMMAND = ["sudo", "pacman", "-Qg"]
ENABLEBING_SERVICE_COMMAND = ["sudo", "systemctl", "enable"]
INSTALL_FLATPAKS_COMMAND = ["flatpak", "install", "flathub"]
PACMAN_NO_INTERACTION_COMMAND = ["--noconfirm"]
FLATPAK_NO_INTERACTION_COMMAND = ["-y"]


# TODO Revisit this.
class System:
    def __init__(self, logger=None, config=None):
        self.logger = logger or setup_logger(__name__)
        self.config = config or default_config

    def update(self) -> None:
        self.arbitraty_command(UPDATE_COMMAND)

    # TODO: thinking about to change to receive list
    def enable_service(self, service: str) -> None:
        command = ENABLEBING_SERVICE_COMMAND + [service]
        self.arbitraty_command(command)

    def install_packages(self, package_list: list[str]) -> None:
        self.arbitraty_command(INSTALL_COMMAND + package_list + PACMAN_NO_INTERACTION_COMMAND)

    # TODO: check packs already installed
    def install_flatpaks(self, package_list: list[str]) -> None:
        command = INSTALL_FLATPAKS_COMMAND + package_list + FLATPAK_NO_INTERACTION_COMMAND
        self.arbitraty_command(command)

    def remove_packages(self, package_list: list[str]) -> None:
        self.arbitraty_command(REMOVE_COMMAND + package_list + PACMAN_NO_INTERACTION_COMMAND)

    # TODO turn private
    def arbitraty_command(self, command: list[str] | str) -> None:
        if self.config.is_dry_run():
            self.logger.info(f"Running arbitrary command {command}")
            return

        try:
            self.logger.info(f"Running {command}")
            subprocess.run(command)
        except subprocess.CalledProcessError as e:
            self.logger.error(f"Error running arbitrary command {command}: {e}")

    def _get_packages_not_installed(self, package_list: list[str]) -> list[str]:
        if self.config.is_dry_run():
            return package_list

        packages_not_installed: list[str] = list(filter(self._is_installed, package_list))
        return list(filter(self._is_group_installed, packages_not_installed))

    def _is_installed(self, package_name: str) -> bool:
        self.logger.info(f"running {CHECK_INSTALLED_COMMAND + [package_name]}")
        return False

    def _is_group_installed(self, package_name: str) -> bool:
        self.logger.info(f"running {CHECK_GROUP_INSTALLED_COMMAND + [package_name]}")
        return False


__all__ = ["default_system"]

default_system: System = System()
