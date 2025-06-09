import subprocess

from archmage.lib.utils.config import default_config
from archmage.lib.utils.logger import setup_logger

UPDATE_COMMAND = ["sudo", "pacman", "-Syu"]
INSTALL_COMMAND = ["sudo", "pacman", "-S"]
CHECK_INSTALLED_COMMAND = ["sudo", "pacman", "-Qi"]
CHECK_GROUP_INSTALLED_COMMAND = ["sudo", "pacman", "-Qg"]
ENABLEBING_SERVICE_COMMAND = ["sudo", "systemctl", "enable"]


# TODO Revisit this.
class System:
    def __init__(self, logger=None, config=None):
        self.logger = logger or setup_logger(__name__)
        self.config = config or default_config

    def update(self) -> None:
        self.logger.info(f"Running {UPDATE_COMMAND}")

        if self.config.is_dry_run():
            return

        try:
            subprocess.run(UPDATE_COMMAND, check=True)
        except subprocess.CalledProcessError as e:
            self.logger.error(f"Error updating system: {e}")

    # TODO: thinking about to change to receive list
    def enable_service(self, service: str) -> None:
        self.logger.info(f"Enabling service: {service}")

        command = ENABLEBING_SERVICE_COMMAND + [service]

        if self.config.is_dry_run():
            self.logger.info(f"Running {command}")
            return

        try:
            subprocess.run(command, check=True)
        except subprocess.CalledProcessError as e:
            self.logger.error(f"Error enabling service: {e}")

    def install_package(self, package_list: list[str]) -> None:
        packages_not_installed = self._get_packages_not_installed(package_list)
        if len(packages_not_installed) != 0:
            packages_to_install: str = " ".join(package_list)
            if self.config.is_not_dry_run():
                try:
                    subprocess.run(INSTALL_COMMAND + [packages_to_install], check=True)
                except subprocess.CalledProcessError as e:
                    self.logger.error(f"Error updating system: {e}")
            else:
                self.logger.info(f"{INSTALL_COMMAND} {packages_to_install}")
        else:
            self.logger.info(f"All packages are installed {package_list}")

    def _get_packages_not_installed(self, package_list: list[str]) -> list[str]:
        if self.config.is_dry_run():
            return package_list

        packages_not_installed: list[str] = list(filter(self._is_installed, package_list))
        return list(filter(self._is_group_installed, packages_not_installed))

    def _is_installed(self, package_name: str) -> bool:
        try:
            subprocess.run(
                CHECK_INSTALLED_COMMAND + [package_name],
                check=True,
            )
            return True
        except subprocess.CalledProcessError:
            return False

    def _is_group_installed(self, package_name: str) -> bool:
        try:
            subprocess.run(
                CHECK_GROUP_INSTALLED_COMMAND + [package_name],
                check=True,
            )
            return True
        except subprocess.CalledProcessError:
            return False


__all__ = ["default_system"]

default_system: System = System()
