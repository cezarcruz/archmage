#!/bin/bash

configure_user_home() {

  show_info "Configuring home directory..."

  if isNotDryRun; then
    cp .gitconfig ~/ #warning: where is my email?
    mkdir -p ~/.config/fontconfig
    cp ./fontconfig/fonts.conf ~/.config/fontconfig/
    cp .mise.toml ~/
    cp -r .ssh ~/
    mkdir -p ~/.config/kitty
    cp ./kitty/kitty.conf ~/.config/kitty/
    cp ./kitty/current-theme.conf ~/.config/kitty/
  else
    show_info "cp .gitconfig ~/"
    show_info "mkdir -p ~/.config/fontconfig"
    show_info "cp ./fontconfig/fonts.conf ~/.config/fontconfig/"
    show_info "cp .mise.toml ~/"
    show_info "cp -r .ssh ~/"
    show_info "mkdir -p ~/.config/kitty"
    show_info "cp ./kitty/kitty.conf ~/.config/kitty/"
    show_info "cp ./kitty/current-theme.conf ~/.config/kitty/"
  fi

}

# not needed, use fish config
configure_mise() {

  show_info "Configuring Mise..."

  if isNotDryRun; then    
    echo "mise activate fish | source" >> ~/.config/fish/config.fish    
  else
    show_info "echo \"mise activate fish | source\" >> ~/.config/fish/config.fish"
  fi
  
}
