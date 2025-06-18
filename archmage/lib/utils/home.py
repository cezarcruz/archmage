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
        self._configure_mise()
        self._configure_kitty()
        self._configure_ssh()
        self._configure_fish()

    def _configure_git_config(self) -> None:
        git_config_file = self.files.get_asset_path(".gitconfig", FilesType.GIT)
        self.files.install_asset_in_home(git_config_file, ".gitconfig")

    def _configure_fontconfig(self) -> None:
        self.files.create_dir(FilesType.FONTCONFIG.value)
        fonts_file = self.files.get_asset_path("fonts.conf", FilesType.FONTCONFIG)
        self.files.install_asset_in_home(fonts_file, FilesType.FONTCONFIG.value + "/fonts.conf")

    def _configure_mise(self) -> None:
        mise_config_file = self.files.get_asset_path(".mise.toml", FilesType.MISE)
        self.files.install_asset_in_home(mise_config_file, FilesType.HOME.value + ".mise.toml")

    def _configure_kitty(self) -> None:
        self.files.create_dir(FilesType.KITTY.value)
        kitty_config = self.files.get_asset_path("kitty.conf", FilesType.KITTY)
        kitty_theme = self.files.get_asset_path("current-theme.conf", FilesType.KITTY)
        self.files.install_asset_in_home(kitty_config, FilesType.KITTY.value + "/kitty.conf")
        self.files.install_asset_in_home(
            kitty_theme, FilesType.KITTY.value + "/current-theme.conf"
        )

    def _configure_ssh(self) -> None:
        self.logger.warning("_configure_ssh not implemented yet")

    def _configure_fish(self) -> None:
        content: list[str] = []
        content.append("\n")
        content.append("""
if [[ $(ps --no-header --pid=$PPID --format=comm) != "fish" && -z ${BASH_EXECUTION_STRING} && ${SHLVL} == 1 ]]
then
    shopt -q login_shell && LOGIN_OPTION='--login' || LOGIN_OPTION=''
    exec fish $LOGIN_OPTION
fi
""")

        self.files.append_to_file(".bashrc", content)
        self.files.create_dir(FilesType.FISH.value)
        fish_config_file = self.files.get_asset_path("config.fish", FilesType.FISH)
        self.files.install_asset_in_home(fish_config_file, FilesType.FISH.value + "/config.fish")


__all__ = ["default_home"]
default_home: Home = Home()
