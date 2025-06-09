import os


class Desktop:
    def __init__(self) -> None:
        pass

    def is_kde(self) -> bool:
        return os.environ["DESKTOP_SESSION"] == "plasma"

__all__ = ["default_desktop"]

default_desktop: Desktop = Desktop()
