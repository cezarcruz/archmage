import argparse

from .logger import setup_logger

class Config:
    def __init__(self):
        self.dry_run = True
        self.logger = setup_logger(__name__)
    
    def parse_args(self):
        parser = argparse.ArgumentParser(
            description='A script to configure Arch Linux post-installation setup.'
        )

        parser.add_argument(
            '-dry',
            '--dry-run', 
            action='store_true', 
            default=True,
            help='Run the script in dry run mode (no changes will be made) (default: True)'
        )

        parser.add_argument(
            '-no-dry',
            '--no-dry-run', 
            dest='dry_run',
            action='store_false', 
            help='Run the script in normal mode (changes will be made)'
        )

        args = parser.parse_args()
        self.dry_run = args.dry_run

        return args
    
    def is_dry_run(self):
        return self.dry_run
    
    def is_not_dry_run(self):
        return not self.dry_run

__all__ = ['config']

config: Config = Config()
