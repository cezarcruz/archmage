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
        self._configure_fontconfig()

    def _configure_git_config(self) -> None:
        git_config_file = self.files.get_asset_path(".gitconfig", FilesType.GIT)
        self.files.install_asset_in_home(git_config_file, ".gitconfig")
    
    def _configure_fontconfig(self) -> None:
        self.files.create_dir(FilesType.FONTCONFIG.value)
        fonts_file = self.files.get_asset_path("fonts.conf", FilesType.FONTCONFIG)
        self.files.install_asset_in_home(fonts_file, FilesType.FONTCONFIG.value + "/fonts.conf")

__all__ = ["default_home"]
default_home: Home = Home()
