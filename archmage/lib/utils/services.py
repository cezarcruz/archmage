from archmage.lib.utils.config import default_config
from archmage.lib.utils.logger import setup_logger
from archmage.lib.utils.system import default_system

SERVICE_LIST: list[str] = ["docker", "reflector.timer", "fstrim.timer", "paccache.timer"]


class Services:
    def __init__(self, system=None, config=None, logger=None) -> None:
        self.system = system or default_system
        self.config = config or default_config
        self.logger = logger or setup_logger(__name__)

    def start_common_services(self):

        if self.config.is_dry_run():
            self.logger.info(f"enabling services {SERVICE_LIST}")
            return

        for service in SERVICE_LIST:
            self.system.enable_service(service)


__all__ = ["default_services"]
default_services: Services = Services()
