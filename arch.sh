#!/bin/bash
set -e
sudo -v

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"

export SCRIPT_DIR
export DRY_RUN=true

# Load all modules
source "$SCRIPT_DIR/modules/core.sh"
source "$SCRIPT_DIR/modules/colors.sh"
source "$SCRIPT_DIR/modules/system.sh"
source "$SCRIPT_DIR/modules/packages.sh"
source "$SCRIPT_DIR/modules/desktop.sh"
source "$SCRIPT_DIR/modules/services.sh"
source "$SCRIPT_DIR/modules/aur.sh"
source "$SCRIPT_DIR/modules/flatpak.sh"
source "$SCRIPT_DIR/modules/user_config.sh"
source "$SCRIPT_DIR/modules/development.sh"

# Load configuration settings
source "$SCRIPT_DIR/config/settings.sh"

# Main function to execute the script
main() {
  clear
  print_welcome

  if ! isNotDryRun; then
    show_dry_run_warning
  fi

  sync_packages
  update_system
  configure_language
  install_base_packages

  setup_desktop_environment
  enable_services
  configure_chaotic_aur
  install_aur_packages
  install_flatpaks
  
  configure_user_home
  configure_mise
  configure_load_disk
  prepare_intellij_home
  garbage_collector
  
  show_success "Setup completed successfully!"

}

main

##################### END #############
