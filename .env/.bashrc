PS1="\[\e]0;\u@\h: \w\a\]${debian_chroot:+($debian_chroot)}\u@\h:\w\$"
alias sudoku='gnome-sudoku &'; alias h='history'; alias s='gnome-sudoku &'
alias py='python3'; alias python='python3'; alias c='clear'
alias pso='python3 ~/Poker-Odds/poker_odds.py'; alias sb='. ~/.bashrc'
alias setup='sudo apt install git && git clone github.com/cs61b-buk/Poker-Odds.git && sudo rm /etc/bash.bashrc && ln -s ~/Poker-Odds/.bashrc ~/.bashrc && sudo ln -s ~/.bashrc /etc/bash.bashrc'
alias ps='ps -aux | grep $1'; alias sl='ln -s $1 $2'; alias g='grep'
alias ge='gedit &'; alias t='gnome-terminal . &'; alias f='firefox &'
alias st='sudo gnome-terminal .'; alias n='nautilus . &'
alias b='brave-browser &'; HISTSIZE=100; shopt -s globstar
alias gitstats='git status && git log --graph --oneline'
alias nostarred='brave-browser https://askubuntu.com/questions/1194319/can-the-starred-folder-in-the-left-pane-of-files-nautilus-be-removed#1248774'
alias notrash='gsettings set org.gnome.shell.extensions.dash-to-dock show-trash false'
alias ssh='sudo apt install openssh-server; sudo ufw allow 22; systemctl start ssh; ip a | grep "inet "'
[ -x /usr/bin/lesspipe ] && eval "$(SHELL=/bin/sh lesspipe)"
alias e='exit'; alias cls='clear'; alias desk='sudo apt install gnome-tweaks'
alias nodesk='sudo apt remove gnome-tweaks'; shopt -s checkwinsize
alias update='sudo apt update && sudo apt full-upgrade && sudo apt autoremove && sudo rm -r /var/lib/snapd'
alias r='rm -r ~/.*hist* ~/.sudo_as_admin_successful ~/.viminfo ~/.vim'
alias v='vim'; alias vi='vim'; alias vv='vim ~/.vimrc'
alias vb='vim ~/.bashrc'; alias vpo='vim ~/Poker-Odds/poker_odds.py'
export GCC_COLORS='error=01;31:warning=01;35:note=01;36:caret=01;32:locus=01:quote=01'
alias la='ls -A'; alias ll='ls -lh'; alias lla='ls -lhA'
alias alert='notify-send --urgency=low -i "$([ $? = 0 ] && echo terminal || echo error)" "$(history|tail -n1|sed -e '\''s/^\s*[0-9]\+\s*//;s/[;&|]\s*alert$//'\'')"'
echo 'To run commands as administrator, see "man sudo_root" for details.'
