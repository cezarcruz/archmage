from archmage.lib.utils.config import default_config
from archmage.lib.utils.system import default_system

SERVICE_LIST: list[str] = [
    "docker",
    "reflector.timer",
    "fstrim.timer",
    "paccache.timer"
]

class Services:
    def __init__(self, system=None, config=None, logger=None) -> None:
        self.system = system or default_system
        self.config = config or default_config

    def start_common_services(self):       
        for service in SERVICE_LIST:
            self.system.enable_service(service)

__all__ = ["default_services"]
default_services: Services = Services()