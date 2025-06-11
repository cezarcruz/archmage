if status is-interactive
    # Commands to run in interactive sessions can go here
end

alias ls='eza -al --color=always --group-directories-first --icons'   # preferred listing
alias la='eza -a --color=always --group-directories-first --icons'    # all files and dirs
alias ll='eza -l --color=always --group-directories-first --icons'    # long format
alias lt='eza -aT --color=always --group-directories-first --icons'   # tree listing
alias grep='grep --color=auto'                                        # colorize grep output  

mise activate fish | source