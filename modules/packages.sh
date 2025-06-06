#!/bin/bash
install_base_packages() {
  show_info "Installing base packages..."
  install_packages "${BASE_PACKAGES[@]}"

  show_info "Installing fonts..."
  install_packages "${FONTS[@]}"
}
