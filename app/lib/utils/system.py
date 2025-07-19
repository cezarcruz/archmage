import subprocess

from app.lib.utils.config import default_config
from app.lib.utils.logger import setup_logger

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
        packages_to_install = self._get_packages_not_installed(package_list)
        if not packages_to_install:
            self.logger.info("All packages are already installed.")
            return

        command = INSTALL_COMMAND + packages_to_install + PACMAN_NO_INTERACTION_COMMAND
        self.arbitraty_command(command)

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

            if isinstance(command, list):
                subprocess.run(command)
            else:
                subprocess.run(command, shell=True)
        except subprocess.CalledProcessError as e:
            self.logger.error(f"Error running arbitrary command {command}: {e}")

    def _get_packages_not_installed(self, package_list: list[str]) -> list[str]:
        if self.config.is_dry_run():
            return package_list

        self.logger.info("Checking for already installed packages...")
        return list(filter(self._is_installed, package_list))

    def _is_installed(self, package_name: str) -> bool:
        """Checks if a package is installed. Returns True if the package is NOT installed."""
        try:
            result = subprocess.run(
                ["pacman", "-Q", package_name],
                check=False,
                capture_output=True,
            )
            if result.returncode == 0:
                self.logger.info(f"Package '{package_name}' is already installed.")
                return False
            else:
                self.logger.info(
                    f"Package '{package_name}' is not installed, scheduling for installation."
                )
                return True
        except Exception as e:
            self.logger.error(
                f"An error occurred while checking if {package_name} is installed: {e}"
            )
            return False

    def _is_group_installed(self, package_name: str) -> bool:
        self.logger.info(f"running {CHECK_GROUP_INSTALLED_COMMAND + [package_name]}")
        return False


__all__ = ["default_system"]

default_system: System = System()
