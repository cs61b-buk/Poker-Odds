# This file is ~/.bashrc, executed by bash(1) for non-login shells:
# If not running interactively, don't do anything:
case $- in
    *i*) ;;
      *) return;;
esac
# Don't put duplicate lines or lines starting with space in the history:
HISTCONTROL=ignoreboth
# Append to the history file, don't overwrite it:
shopt -s histappend
# Aliases:
alias code='cd Poker-Odds'
alias rpo='python poker_odds.py'
alias vpo='vim poker_odds.py'
alias ps='ps -aux | grep $1'
alias vrc='vim .bashrc'
alias vv='vim .vimrc'
alias f='firefox'
alias n='nautilus'
alias b='brave-browser'
alias nostarred='brave-browser https://askubuntu.com/questions/1194319/can-the-starred-folder-in-the-left-pane-of-files-nautilus-be-removed#1248774'
alias notrash='gsettings set org.gnome.shell.extensions.dash-to-dock show-trash
false'
# For setting history length see HISTSIZE and HISTFILESIZE in bash(1):
HISTSIZE=1000
HISTFILESIZE=2000
# Check the window size after each command & update the values of LINES and COLUMNS:
shopt -s checkwinsize
# If set, the pattern "**" used in a pathname expansion context will
# match all files and zero or more directories and subdirectories:
shopt -s globstar
# Allow SSH connections and get SSH IP address:
alias ssh='sudo apt install openssh-server; sudo ufw allow 22; ip a | grep "inet "'
# Make less more friendly for non-text input files, see lesspipe(1):
[ -x /usr/bin/lesspipe ] && eval "$(SHELL=/bin/sh lesspipe)"
# Set variable identifying the chroot you work in (used in the prompt below):
if [ -z "${debian_chroot:-}" ] && [ -r /etc/debian_chroot ]; then
    debian_chroot=$(cat /etc/debian_chroot)
fi
# Enable color support of ls and also add handy aliases:
if [ -x /usr/bin/dircolors ]; then
    test -r ~/.dircolors && eval"$(dircolors -b ~/.dircolors)"||eval "$(dircolors -b)"
    alias ls='ls --color=auto'
    alias dir='dir --color=auto'
    alias vdir='vdir --color=auto'
    alias grep='grep --color=auto'
    alias fgrep='fgrep --color=auto'
    alias egrep='egrep --color=auto'
fi
# More aliases:
alias c='clear'
alias cls='clear'
alias desk='sudo apt install gnome-tweaks'
alias nodesk='sudo apt remove gnome-tweaks'
alias vi='vim'
alias v='vim'
alias e='exit'
# Colored GCC warnings and errors:
export GCC_COLORS='error=01;31:warning=01;35:note=01;36:caret=01;32:locus=01:quote=01'
# Some more ls aliases:
alias la='ls -A'
alias ll='ls -F'
alias lla='ls -FA'
# Add an "alert" alias for long running commands:
alias alert='notify-send --urgency=low -i "$([ $? = 0 ] && echo terminal || echo error)" "$(history|tail -n1|sed -e '\''s/^\s*[0-9]\+\s*//;s/[;&|]\s*alert$//'\'')"'
