#!/bin/bash

sync_packages() {
  show_info "Synchronizing package databases..."

  if isNotDryRun; then
    sudo pacman -Syy
  fi

}

update_system() {
  show_info "Updating system..."

  if isNotDryRun; then
    sudo pacman -S --noconfirm
  fi
}

install_packages() {
  local packages=("$@")
  local to_install=()

  for pkg in "${packages[@]}"; do
    if ! is_installed "$pkg" && ! is_group_installed "$pkg"; then
      to_install+=("$pkg")
    fi
  done

  if [ ${#to_install[@]} -ne 0 ]; then
    show_info 'Instaling: %s' "${to_install[*]}"
    if isNotDryRun; then
      sudo pacman -S --noconfirm "${to_install[@]}"
    fi
  else
    show_info 'All packages are already installed.'  
  fi
}

configure_language() {
  show_info "Configuring language settings..."

  if isNotDryRun; then
    printf "\npt_BR.UTF-8 UTF-8\n" | sudo tee -a /etc/locale.gen
    sudo locale-gen

    if isKde; then
      printf "\nLC_TIME=pt_BR.UTF-8\n" | sudo tee -a /etc/locale.conf
    fi

    printf "\nLC_CTYPE=pt_BR.UTF-8\n" | sudo tee -a /etc/locale.conf
  else
    show_info "printf pt_BR.UTF-8 UTF-8"

    if isKde; then
      show_info "printf LC_TIME=pt_BR.UTF-8"
    fi

    show_info "printf LC_CTYPE=pt_BR.UTF-8"
  fi
}
