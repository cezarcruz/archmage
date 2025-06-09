from archmage.lib.utils.config import default_config
from archmage.lib.utils.files import FilesType, default_files
from archmage.lib.utils.logger import setup_logger


class Home:
    def __init__(self, config=None, logger=None, files=None) -> None:
        self.config = config or default_config
        self.logger = logger or setup_logger(__name__)
        self.files = files or default_files

    def configure_user_home(self) -> None:
        self.logger.info("Configuring home directory...")
        self._configure_git_config()

    def _configure_git_config(self) -> None:
        git_config_file = self.files.get_asset_path(".gitconfig", FilesType.GIT)
        self.files.install_asset_in_home(git_config_file, ".gitconfig")


__all__ = ["default_home"]
default_home: Home = Home()
