import argparse

from app.lib.utils.logger import setup_logger


class Config:
    def __init__(self, dry_run: bool = True, logger=None):
        self._dry_run = dry_run
        self.logger = logger or setup_logger(__name__)
        self.parse_args()

    def parse_args(self, args=None) -> None:
        parser = self._create_argument_parser()
        parsed_args = parser.parse_args(args)
        self._dry_run = parsed_args.dry_run

    @classmethod
    def _create_argument_parser(cls) -> argparse.ArgumentParser:
        parser = argparse.ArgumentParser(
            description="A script to configure Arch Linux post-installation setup."
        )

        parser.add_argument(
            "-dry",
            "--dry-run",
            action="store_true",
            default=True,
            help="Run the script in dry run mode (no changes will be made) (default: True)",
        )

        parser.add_argument(
            "-no-dry",
            "--no-dry-run",
            dest="dry_run",
            action="store_false",
            help="Run the script in normal mode (changes will be made)",
        )

        return parser

    def is_dry_run(self) -> bool:
        return self._dry_run

    def is_not_dry_run(self) -> bool:
        return not self._dry_run


__all__ = ["default_config"]

default_config: Config = Config()
