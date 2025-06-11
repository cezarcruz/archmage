#!/bin/bash
# This script sets up environment variables for the application

load_settings() {
  show_info "Setting up environment variables..."

  if file_exists "$SCRIPT_DIR/.env"; then
    show_info "Loading environment variables from .env file..."
  else
    show_error ".env file not found in $SCRIPT_DIR"
    exit 1
  fi

  # shellcheck disable=SC1091
  source "$SCRIPT_DIR/.env"
  show_info "EMAIL=$EMAIL"
}
