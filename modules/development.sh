#!/bin/bash

prepare_intellij_home() {

  show_info "Preparing IntelliJ home directory..."

  if isNotDryRun; then
    sudo mkdir /opt/jetbrains
    sudo chown -R "$USER" /opt/jetbrains
  else
    show_info "sudo mkdir /opt/jetbrains"
    show_info "sudo chown -R $USER /opt/jetbrains"
  fi

}
