from archmage.lib.utils.config import default_config
from archmage.lib.utils.desktop import default_desktop
from archmage.lib.utils.logger import setup_logger


class Language:
    def __init__(self, logger=None, config=None, desktop=None):
        self.logger = logger or setup_logger(__name__)
        self.config = config or default_config
        self.desktop = desktop or default_desktop

    def configure_language(self) -> None:
        self.logger.info("Configuring system language...")

        if self.config.is_dry_run():
            self.logger.info("printf pt_BR.UTF-8 UTF-8")

            if self.desktop.is_kde():
                self.logger.info("printf LC_TIME=pt_BR.UTF-8")

            self.logger.info("printf LC_CTYPE=pt_BR.UTF-8")


__all__ = ["default_language"]

default_language: Language = Language()
