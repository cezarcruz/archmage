#!/usr/bin/env python3

"""
This script is used to set up the environment for the application.
"""

import os
import sys
from utils.logger import setup_logger

def main():
    
    # check if the script is run with root privileges
    if os.getuid() == 0:
        logger.error("This script should not be run as root. Please run it as a regular user.")
        sys.exit(1)

if __name__ == "__main__":
    logger = setup_logger(__name__)
    main()
