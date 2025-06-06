#!/bin/bash

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"

export SCRIPT_DIR
export DRY_RUN=true

source "$SCRIPT_DIR/modules/colors.sh"

##################### END #############
