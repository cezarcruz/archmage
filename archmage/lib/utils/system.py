import subprocess

from .config import default_config
from .logger import setup_logger
from .desktop import default_desktop

UPDATE_COMMAND = ['sudo', 'pacman', '-Syu']

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
    
    def configure_language(self) -> None:
        self.logger.info("Configuring system language...")

        if self.config.is_dry_run():
            self.logger.info("printf pt_BR.UTF-8 UTF-8")

            if self.desktop.is_kde():
                self.logger.info("printf LC_TIME=pt_BR.UTF-8")

            self.logger.info("printf LC_CTYPE=pt_BR.UTF-8")


__all__ = ['default_system']

default_system: System = System()
