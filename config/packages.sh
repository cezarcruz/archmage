#!/bin/bash

KDE_PLASMA_APPS=(
  "spectacle"
  "xdg-desktop-portal-gtk"
  "flatpak"
  "partitionmanager"
  "okular"
  "geoclue"
  "dragon"
  "filelight"
  "inter-font"
  "gwenview"
  "haruna"
  "kcalc"
)

GNOME_APPS=(
  "papers"
  "nautilus-python"
  "adw-gtk-theme"
  "ghostty"
)

FONTS=(
  "ttf-jetbrains-mono"
  #"ttf-roboto"
  "noto-fonts"
  "ttf-liberation"
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
  "mise"
  "rsync"
  "kitty"
  "eza"
)

AUR_PACKAGES=(
  "visual-studio-code-bin"
)

FLATPAK_PACKAGES=(
  "com.valvesoftware.Steam"
  #"com.mattjakeman.ExtensionManager" only for GNOME
)

export KDE_PLASMA_APPS
export GNOME_APPS
export FONTS
export BASE_PACKAGES
export AUR_PACKAGES
export FLATPAK_PACKAGES

