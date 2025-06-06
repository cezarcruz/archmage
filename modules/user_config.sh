#!/bin/bash

configure_user_home() {

  show_info "Configuring home directory..."

  if isNotDryRun; then
    cp "$SCRIPT_DIR/.gitconfig" ~/ #warning: where is my email?
    mkdir -p ~/.config/fontconfig
    cp "$SCRIPT_DIR/fontconfig/fonts.conf" ~/.config/fontconfig/
    cp "$SCRIPT_DIR/.mise.toml" ~/
    cp -r "$SCRIPT_DIR/.ssh" ~/
    mkdir -p ~/.config/kitty
    cp "$SCRIPT_DIR/kitty/kitty.conf" ~/.config/kitty/
    cp "$SCRIPT_DIR/kitty/current-theme.conf" ~/.config/kitty/
  else
    show_info "cp $SCRIPT_DIR/.gitconfig ~/"
    show_info "mkdir -p $SCRIPT_DIR/.config/fontconfig"
    show_info "cp $SCRIPT_DIR/fontconfig/fonts.conf ~/.config/fontconfig/"
    show_info "cp $SCRIPT_DIR/.mise.toml ~/"
    show_info "cp -r $SCRIPT_DIR/.ssh ~/"
    show_info "mkdir -p $SCRIPT_DIR/.config/kitty"
    show_info "cp $SCRIPT_DIR/kitty/kitty.conf ~/.config/kitty/"
    show_info "cp $SCRIPT_DIR/kitty/current-theme.conf ~/.config/kitty/"
  fi

}

configure_fish() {
  show_info "Configuring Fish shell..."

  if ! is_installed "fish"; then
    show_error "Fish shell is not installed. Please install it first."
    return 1
  fi

  if isNotDryRun; then
    cat >> ~/.bashrc << 'EOF'

# Inicia o Fish shell automaticamente
if [[ $(ps --no-header --pid=$PPID --format=comm) != "fish" && -z ${BASH_EXECUTION_STRING} && ${SHLVL} == 1 ]]
then
	shopt -q login_shell && LOGIN_OPTION='--login' || LOGIN_OPTION=''
	exec fish $LOGIN_OPTION
fi
EOF
  fi

  if isNotDryRun; then
    mkdir -p ~/.config/fish
    cp "$SCRIPT_DIR/fish/config.fish" ~/.config/fish/
  else
    show_info "mkdir -p ~/.config/fish"
    show_info "cp $SCRIPT_DIR/fish/config.fish ~/.config/fish/"
  fi

}
