from app.lib.utils.desktop import default_desktop
from app.lib.utils.logger import setup_logger
from app.lib.utils.system import default_system


class Language:
    def __init__(self, logger=None, config=None, desktop=None, system=None):
        self.logger = logger or setup_logger(__name__)
        self.desktop = desktop or default_desktop
        self.system = system or default_system

    def configure_language(self) -> None:
        self.logger.info("Configuring system language...")

        self.system.arbitraty_command(
            'printf "\npt_BR.UTF-8 UTF-8\n" | sudo tee -a /etc/locale.gen'
        )
        self.system.arbitraty_command(["sudo", "locale-gen"])

        if self.desktop.is_kde():
            self.system.arbitraty_command(
                'printf "\nLC_TIME=pt_BR.UTF-8\n" | sudo tee -a /etc/locale.conf'
            )

        self.system.arbitraty_command(
            'printf "\nLC_CTYPE=pt_BR.UTF-8\n" | sudo tee -a /etc/locale.conf'
        )


__all__ = ["default_language"]

default_language: Language = Language()
