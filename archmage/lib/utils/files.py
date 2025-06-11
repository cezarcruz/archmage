import os
import shutil
from enum import Enum
from pathlib import Path

from archmage.lib.utils.config import default_config
from archmage.lib.utils.logger import setup_logger


class FilesType(Enum):
    GIT = "git"
    FONTCONFIG = ".config/fontconfig"
    MISE = "mise"
    KITTY = ".config/kitty"
    ETC = "etc"
    FISH = ".config/fish"
    HOME = ""


PROJECT_ROOT_DIR = str(Path(__file__).parent.parent.parent.parent)
PROJECT_RESOURCE_DIR = PROJECT_ROOT_DIR + "/resources/"
HOME_DIR = str(Path.home()) + "/"


class Files:
    def __init__(self, config=None, logger=None) -> None:
        self.config = config or default_config
        self.logger = logger or setup_logger(__name__)

    def get_asset_path(self, file_name: str, file_type: FilesType) -> str:
        return PROJECT_RESOURCE_DIR + file_type.value + "/" + file_name

    def install_asset_in_home(self, path_origin: str, path_destination: str) -> None:
        destination = HOME_DIR + path_destination

        if self.config.is_dry_run():
            self.logger.info(f"copying from {path_origin} to {destination}")
            return

        shutil.copy2(path_origin, destination)

    def install_asset(self, path_origin: str, path_destination: str) -> None:
        pass

    def create_dir(self, path_destination: str):
        path = HOME_DIR + path_destination

        if self.config.is_dry_run():
            self.logger.info(f"creating dir: {path}")
            return

        os.makedirs(path, exist_ok=True)

    def append_to_file(self, path_destination: str, content: list[str]) -> None:
        destination = HOME_DIR + path_destination

        if self.config.is_dry_run():
            self.logger.info(f"appending {content} to {destination}")
            return

        with open(destination, "a") as file:
            file.writelines(content)


__all__ = ["default_files"]
default_files: Files = Files()
