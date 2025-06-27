import logging

from app.lib.utils.colors import Colors


class ColoredFormatter(logging.Formatter):
    COLORS = {
        "DEBUG": Colors.CYAN,
        "INFO": Colors.GREEN,
        "WARNING": Colors.YELLOW,
        "ERROR": Colors.RED,
        "CRITICAL": Colors.MAGENTA + Colors.BOLD,
    }

    def format(self, record):
        log_color = self.COLORS.get(record.levelname, Colors.WHITE)
        record.levelname = f"{log_color}{record.levelname}{Colors.RESET}"
        record.msg = f"{log_color}{record.msg}{Colors.RESET}"
        return super().format(record)


__all__ = ["setup_logger"]


def setup_logger(name=__name__, level=logging.INFO):
    handler = logging.StreamHandler()
    handler.setFormatter(ColoredFormatter("%(levelname)s: %(message)s"))

    logger = logging.getLogger(name)
    logger.setLevel(level)
    logger.addHandler(handler)
    logger.propagate = False

    return logger
