#!/bin/bash

set -e
# Solicita senha sudo no início para garantir privilégios ao longo do script
sudo -v

print_welcome() {
  echo "Welcome to the Arch Linux setup script!"
}

clear
print_welcome

# Variables
KDE_PLASMA_APPS=(
  "spectacle"
  "xdg-desktop-portal-gtk"
  "flatpak"
  "partitionmanager"
  "okular"
  "geoclue"
  "elisa"
  "dragon"
  "filelight"
  "inter-font"
  "gwenview"
)

GNOME_APPS=(
  "papers"
  "nautilus-python"
  "adw-gtk-theme"
  "ghostty"
)

FONTS=(
  "ttf-jetbrains-mono"
  "ttf-roboto"
)

BASE_PACKAGES=(
  "firefox"
  "docker"
  "docker-compose"
  "git"
  "go"
  "btop"
  "neovim"
  "reflector"
  "ttf-jetbrains-mono"
  "pacman-contrib"
  "bat"
  "pkgstats"
  "fish"
  "ttf-roboto"
  "fuse"
  "less"
)

# Utils

# Function to check if a package is installed
is_installed() {
  pacman -Qi "$1" &>/dev/null
}

# Function to check if a package is installed
is_group_installed() {
  pacman -Qg "$1" &>/dev/null
}

# Function to install packages using pacman
install_packages() {
  local packages=("$@")
  local to_install=()

  for pkg in "${packages[@]}"; do
    if ! is_installed "$pkg" && ! is_group_installed "$pkg"; then
      to_install+=("$pkg")
    fi
  done

  if [ ${#to_install[@]} -ne 0 ]; then
    printf '\nInstaling: %s' "${to_install[*]}"
    #sudo pacman -S --noconfirm "${to_install[@]}"
  else
    printf '\nAll packages are already installed.\n'  
  fi
}

isKde() {
  [ "$DESKTOP_SESSION" = "plasma" ]
}

update_system() {
  printf "\nUpdating system..."
  sudo pacman -Syu --noconfirm
}

install_base_packages() {
  printf "\nInstalling base packages..."
  install_packages "${BASE_PACKAGES[@]}"

  printf "\nInstalling fonts..."
  install_packages "${FONTS[@]}"
}

configure_language() {
  printf "\nConfiguring language settings..."
  printf "\npt_BR.UTF-8 UTF-8\n" | sudo tee -a /etc/locale.gen
  sudo locale-gen

  if isKde; then
    printf "\nLC_TIME=pt_BR.UTF-8\n" | sudo tee -a /etc/locale.conf
  fi
  
  printf "\nLC_CTYPE=pt_BR.UTF-8\n" | sudo tee -a /etc/locale.conf

}

main() {
  #update_system
  #configure_language
  install_base_packages

  if [ "$DESKTOP_SESSION" = "plasma" ]; then
    printf "\nDetected KDE Plasma desktop environment. Can you confirm this?"
    printf " (y/n): "
    read -r response
    if [ "$response" = "y" ]; then
      printf "\nProceeding with KDE Plasma setup..."
      install_packages "${KDE_PLASMA_APPS[@]}"
    else
      printf "\nSetupping GNOME desktop environment instead."
      install_packages "${GNOME_APPS[@]}"
    fi
  fi

}

main

# install_intellij() {
#     sudo mkdir /opt/jetbrains
#     sudo chown -R "$USER" /opt/jetbrains
# }

# configure_docker() {
#     sudo usermod -aG docker "$USER" #mantain to remove another moment
# }

# install_flatpaks() {
#     flatpak install flathub com.valvesoftware.Steam com.mattjakeman.ExtensionManager -y
# }

# enable_services() {
#     sudo systemctl enable docker
#     sudo systemctl enable reflector.timer
#     sudo systemctl enable fstrim.timer
#     sudo systemctl enable paccache.timer
#     #sudo systemctl enable pkgstats.timer
# }

# configure_aur() {
#     sudo pacman-key --init
#     sudo pacman-key --recv-key 3056513887B78AEB --keyserver keyserver.ubuntu.com
#     sudo pacman-key --lsign-key 3056513887B78AEB

#     sudo pacman -U 'https://cdn-mirror.chaotic.cx/chaotic-aur/chaotic-keyring.pkg.tar.zst'
#     sudo pacman -U 'https://cdn-mirror.chaotic.cx/chaotic-aur/chaotic-mirrorlist.pkg.tar.zst'

#     printf "\n[chaotic-aur]\nInclude = /etc/pacman.d/chaotic-mirrorlist\n" | sudo tee -a /etc/pacman.conf

# }

# install_aur_packages() {
#     sudo pacman -Syu visual-studio-code-bin --noconfirm
# }

# download_intellij() {
#     wget -nv -O idea.tar.gz "https://download.jetbrains.com/idea/ideaIC-2024.3.5.tar.gz"
#     tar -xzf idea.tar.gz
#     mv idea-IC-243.26053.27/* /opt/intellij/
#     rm -rf idea-IC-243.26053.27
# }

# configure_home() {
#     cp .gitconfig ~/ #warning: where is my email?
#     mkdir -p ~/.config/fontconfig
#     cp ./fontconfig/fonts.conf ~/.config/fontconfig/
#     cp .mise.toml ~/
#     cp -r .ssh ~/
# }

# configure_mise() {
#     sudo pacman -Syu mise --noconfirm
#     #curl https://mise.run | sh
#     #echo "$HOME/.local/bin/mise activate fish | source" >> ~/.config/fish/config.fish
# }

# configure_load_disk() {
#     sudo cp 50-udisks.rules /etc/polkit-1/rules.d/
# }

# install_base_packages
# install_gnome_packages

# configure_home
# configure_docker
# #download_intellij
# install_intellij
# configure_aur
# install_aur_packages
# enable_services
# install_flatpaks

# configure_load_disk
# configure_mise

# sudo pacman -R htop nano epiphany gnome-tour gnome-console --noconfirm
