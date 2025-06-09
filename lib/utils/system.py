import subprocess

from .config import config
from .logger import setup_logger

UPDATE_COMMAND = ['sudo', 'pacman', '-Syu']

class System:
    def __init__(self):
        self.logger = setup_logger(__name__)
        self.config = config

    def update(self):

        self.logger.info(f"Running {UPDATE_COMMAND}")
        
        if self.config.is_dry_run():
            return

        try:
            subprocess.run(UPDATE_COMMAND, check=True)
        except subprocess.CalledProcessError as e:
            self.logger.error(f"Error updating system: {e}")

__all__ = ['system']

system: System = System()
