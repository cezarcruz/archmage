#!/bin/bash

configure_chaotic_aur() {

  show_info "\nConfiguring Chaotic AUR..."

  if isNotDryRun; then
    sudo pacman-key --init
    sudo pacman-key --recv-key 3056513887B78AEB --keyserver keyserver.ubuntu.com
    sudo pacman-key --lsign-key 3056513887B78AEB

    sudo pacman -U 'https://cdn-mirror.chaotic.cx/chaotic-aur/chaotic-keyring.pkg.tar.zst'
    sudo pacman -U 'https://cdn-mirror.chaotic.cx/chaotic-aur/chaotic-mirrorlist.pkg.tar.zst'

    printf "\n[chaotic-aur]\nInclude = /etc/pacman.d/chaotic-mirrorlist\n" | sudo tee -a /etc/pacman.conf
  else
    show_info "sudo pacman-key --init"
    show_info "pacman-key --recv-key 3056513887B78AEB --keyserver keyserver.ubuntu.com"
    show_info "pacman-key --lsign-key 3056513887B78AEB"
    show_info "pacman -U 'https://cdn-mirror.chaotic.cx/chaotic-aur/chaotic-keyring.pkg.tar.zst'"
    show_info "pacman -U 'https://cdn-mirror.chaotic.cx/chaotic-aur/chaotic-mirrorlist.pkg.tar.zst'"
  fi

}

install_aur_packages() {
  install_packages "${AUR_PACKAGES[@]}"
}
