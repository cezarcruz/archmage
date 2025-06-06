#!/bin/bash
isNotDryRun() {
  [ "$DRY_RUN" = false ]
}

show_dry_run_warning() {
  show_warning "This is a dry run. No changes will be made to your system."
}

print_welcome() {
  show_header "Welcome to the Arch Linux setup script!"
}

# Função para verificar se um pacote está instalado
is_installed() {
  pacman -Qi "$1" &>/dev/null
}

is_group_installed() {
  pacman -Qg "$1" &>/dev/null
}

isKde() {
  [ "$DESKTOP_SESSION" = "plasma" ]
}
