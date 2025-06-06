#!/bin/bash
setup_desktop_environment() {
  if [ "$DESKTOP_SESSION" = "plasma" ]; then
    show_question "\nDetected KDE Plasma desktop environment. Can you confirm this? (y/n):"
    read -r response
    if [ "$response" = "y" ]; then
      show_info "Proceeding with KDE Plasma setup..."
      install_packages "${KDE_PLASMA_APPS[@]}"
    else
      show_info "Setupping GNOME desktop environment instead."
      install_packages "${GNOME_APPS[@]}"
    fi
  fi

}
