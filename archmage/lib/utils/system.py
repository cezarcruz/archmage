import subprocess

from archmage.lib.utils.config import default_config
from archmage.lib.utils.desktop import default_desktop
from archmage.lib.utils.logger import setup_logger

UPDATE_COMMAND = ["sudo", "pacman", "-Syu"]
INSTALL_COMMAND = ["sudo", "pacman", "-S"]
CHECK_INSTALLED_COMMAND = ["sudo", "pacman", "-Qi"]
CHECK_GROUP_INSTALLED_COMMAND = ["sudo", "pacman", "-Qg"]

# TODO Revisit this.


class System:
    def __init__(self, logger=None, config=None, desktop=None):
        self.logger = logger or setup_logger(__name__)
        self.config = config or default_config
        self.desktop = desktop or default_desktop

    def update(self) -> None:
        self.logger.info(f"Running {UPDATE_COMMAND}")

        if self.config.is_dry_run():
            return

        try:
            subprocess.run(UPDATE_COMMAND, check=True)
        except subprocess.CalledProcessError as e:
            self.logger.error(f"Error updating system: {e}")

    def install_package(self, package_list: list[str]) -> None:
        packages_not_installed = self._get_packages_not_installed(package_list)

        if len(packages_not_installed) != 0:
            packages_to_install: str = "".join(package_list)
            if self.config.is_not_dry_run():
                try:
                    subprocess.run(INSTALL_COMMAND + [packages_to_install], check=True)
                except subprocess.CalledProcessError as e:
                    self.logger.error(f"Error updating system: {e}")
            else:
                self.logger.info(f"{INSTALL_COMMAND} {packages_to_install}")
        else:
            self.logger.info(f"all packages are installed {package_list}")

    def _get_packages_not_installed(self, package_list: list[str]) -> list[str]:
        packages_not_installed: list[str] = list(
            filter(self._is_installed, package_list)
        )
        return list(filter(self._is_group_installed, packages_not_installed))

    def _is_installed(self, package_name: str) -> bool:
        try:
            subprocess.run(
                CHECK_INSTALLED_COMMAND + [package_name],
                stdout=subprocess.DEVNULL,
                stderr=subprocess.DEVNULL,
                check=True,
            )
            return True
        except subprocess.CalledProcessError:
            return False

    def _is_group_installed(self, package_name: str) -> bool:
        try:
            subprocess.run(
                CHECK_GROUP_INSTALLED_COMMAND + [package_name],
                stdout=subprocess.DEVNULL,
                stderr=subprocess.DEVNULL,
                check=True,
            )
            return True
        except subprocess.CalledProcessError:
            return False


__all__ = ["default_system"]

default_system: System = System()
