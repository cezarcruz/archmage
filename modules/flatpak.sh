#!/bin/bash

install_flatpaks() {
  show_info "Installing Flatpak packages..."

  for pkg in "${FLATPAK_PACKAGES[@]}"; do
    if ! flatpak list | grep -q "$pkg"; then
      show_info "Installing Flatpak package: %s" "$pkg"

      if isNotDryRun; then
        flatpak install flathub "$pkg" -y      
      fi
    else
      show_warning "Flatpak package %s is already installed." "$pkg" #-- not working
    fi
  done

}
