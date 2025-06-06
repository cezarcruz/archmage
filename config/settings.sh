#!/bin/bash
# This script sets up environment variables for the application

load_settings() {
  show_info "Setting up environment variables..."
  # shellcheck disable=SC1091
  source "$SCRIPT_DIR/.env"
  show_info "EMAIL=$EMAIL"
}



