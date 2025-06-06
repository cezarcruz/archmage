#!/bin/bash
enable_services() {

  show_info "\nEnabling system services..."

  if isNotDryRun; then
    sudo systemctl enable docker
    sudo systemctl enable reflector.timer
    sudo systemctl enable fstrim.timer
    sudo systemctl enable paccache.timer
  else
    show_info "sudo systemctl enable docker"
    show_info "sudo systemctl enable reflector.timer"
    show_info "sudo systemctl enable fstrim.timer"
    show_info "sudo systemctl enable paccache.timer"
  fi

}
