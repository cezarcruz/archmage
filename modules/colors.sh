#!/bin/bash

show_question() {
  local blue=$'\033[0;94m'
  local nc=$'\033[0m'
  if [[ "${1:--e}" =~ ^(-e|-n)$ ]]; then
    echo "${1:--e}" "${blue}${*:2}${nc}"
  else
    echo -e "${blue}${*}${nc}"
  fi
}

show_info() {
  local green=$'\033[0;92m'
  local nc=$'\033[0m'
  if [[ "${1:--e}" =~ ^(-e|-n)$ ]]; then
    echo "${1:--e}" "${green}${*:2}${nc}"
  else
    echo -e "${green}${*}${nc}"
  fi
}

show_warning() {
  local yellow=$'\033[0;93m'
  local nc=$'\033[0m'
  if [[ "${1:--e}" =~ ^(-e|-n)$ ]]; then
    echo "${1:--e}" "${yellow}${*:2}${nc}"
  else
    echo -e "${yellow}${*}${nc}"
  fi
}

show_success() {
  local purple=$'\033[0;95m'
  local nc=$'\033[0m'
  if [[ "${1:--e}" =~ ^(-e|-n)$ ]]; then
    echo "${1:--e}" "${purple}${*:2}${nc}"
  else
    echo -e "${purple}${*}${nc}"
  fi
}

show_header() {
  local cyan=$'\033[0;96m'
  local nc=$'\033[0m'
  if [[ "${1:--e}" =~ ^(-e|-n)$ ]]; then
    echo "${1:--e}" "${cyan}${*:2}${nc}"
  else
    echo -e "${cyan}${*}${nc}"
  fi
}
