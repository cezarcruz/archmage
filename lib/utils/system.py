import subprocess

from .config import config
from .logger import setup_logger

UPDATE_COMMAND = ['sudo', 'pacman', '-Syu']

class System:
    def __init__(self):
        self.logger = setup_logger(__name__)

    def update(self):

        self.logger.info(f"Running {UPDATE_COMMAND}")
        
        if config.is_dry_run():
            return

        try:
            subprocess.run(UPDATE_COMMAND, check=True)
        except subprocess.CalledProcessError as e:
            print(f"Error updating system: {e}")

system = System()
