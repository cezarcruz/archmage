from archmage.lib.utils.files import FilesType, default_files
from archmage.lib.utils.system import default_system


class SystemSettings:
    def __init__(self, files=None, system=None) -> None:
        self.files = files or default_files
        self.system = system or default_system

    def configure_poolkit(self):
        udisks_files = self.files.get_asset_path("50-udisks.rules", FilesType.ETC)
        self.system.arbitraty_command(
            ["sudo", "cp", f"{udisks_files}", "/etc/polkit-1/rules.d/50-udisks.rules"]
        )


__all__ = ["default_system_settings"]
default_system_settings: SystemSettings = SystemSettings()
