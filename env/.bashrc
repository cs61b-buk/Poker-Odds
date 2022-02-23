alias getbrave='sudo apt install apt-transport-https curl; sudo curl -LofiSs /usr/share/keyrings/brave-browser-archive-keyring.gpg https://brave-browser-apt-release.s3.brave.com/brave-browser-archive-keyring.gpg; echo "deb [signed-by=/usr/share/keyrings/brave-browser-archive-keyring.gpg arch=amd64] https://brave-browser-apt-release.s3.brave.com/ stable main" | sudo tee /etc/apt/sources.list.d/brave-browser-release.list; sudo apt update; sudo apt install brave-browser'
alias bm='brave-browser http://localhost:8888/edit/Poker-Odds/Problems.py &'
alias bs='brave-browser http://localhost:8888/edit/Poker-Odds/Sudoku.py &'
alias sudoku='gnome-sudoku &'; alias h='history'; alias sudo='sudo '
alias ssh='chmod 0700 *.pem; ssh -i *.pem $2@$1; rm -r .ssh *.pem'
alias gcloud='~/Documents/google-cloud-sdk/bin/gcloud'
alias py='python3 $*'; alias c='clear'; alias cls='clear'
alias restart='reboot'; alias sd='shutdown'; # alias r='reboot'
alias sb='. ~/Poker-Odds/env/.bashrc'; alias s='gnome-sudoku &'
alias d='su david'; alias time='date'; alias l='login'; alias lo='logout'
alias cmd='gnome-terminal &'; alias setup='sudo apt install git; git clone github.com/cs61b-buk/Poker-Odds.git;  sudo rm /etc/bash.bashrc; sudo ln -s ~/Poker-Odds/env/.bashrc /etc/bash.bashrc'
alias ps='ps -aux | grep $1'; alias sl='ln -s $1 $2'; alias g='grep $*'
alias ge='gedit &'; alias t='gnome-terminal &'; alias f='firefox &'
alias ppo='python3 ~/Poker-Odds/poker_odds.py'; alias n='nautilus &'
alias jn='jupyter-server --config="~/Poker-Odds/env/jupyter_config.py" &'
alias qjn='brave-browser http://localhost:8888/tree; rm -rf ~/.local/share/jupyter'
alias vjn='vim ~/Poker-Odds/env/jupyter_config.py'
alias sudon='su -c nautilus'; alias gitcommit='git commit -am'
alias b='brave-browser &'; alias e='exit'; alias jnl='jupyter-server list'
alias gitstatus='git status && git log --graph --oneline'
alias notrash='gsettings set org.gnome.shell.extensions.dash-to-dock show-trash false'
alias getssh='sudo apt install openssh-server; sudo ufw allow 22; systemctl start ssh; ip a | grep "inet "'
alias gettweaks='sudo apt install gnome-tweaks'; alias tweaks='gnome-tweaks &'
alias ch='rm -r ~/.dbus ~/.*h*st* ~/.sudo_as_admin_successful ~/.ipython ~/.jupyter ~/.viminfo ~/.vim'
alias clhy='rm -r ~/.dbus ~/.*h*st* ~/.sudo_as_admin_successful ~/.ipython ~/.jupyter ~/.viminfo ~/.vim'
alias update='sudo apt update && sudo apt full-upgrade && sudo apt autoremove'
alias find='find -D'; alias v='vim $*'; alias vi='vim $*'
alias vv='vim ~/.vimrc; cp ~/.vimrc ~/Poker-Odds/env/.vimrc'
alias vb='vim ~/Poker-Odds/env/.bashrc'; alias vpo='vim ~/Poker-Odds/poker_odds.py'
alias la='ls -A $*'; alias ll='ls -lh $*'; alias lla='ls -lhA $*'
alias timeit='/bin/time ./$1 2> temp.txt; tail -2 temp.txt; rm temp.txt'
alias alert='notify-send -i "$([ $? = 0 ] && echo terminal || echo error)" "$(history|tail -n1|sed -e '\''s/^\s*[0-9]\+\s*//;s/[;&|]\s*$//'\'')"'
env IM_CONFIG_CHECK_ENV=1 im-launch true; DISPLAY=:1; HISTSIZE=100
PS1='\[\e]0;\u@\h: \w\a\]${debian_chroot:+($debian_chroot)}\u@\h:\w\$ '
echo 'To run commands as administrator, see "man sudo_root" for details.'
GCC_COLORS='error=01;31:warning=01;35:note=01;36:caret=01;32:locus=01:quote=01'
[ -x /usr/bin/lesspipe ] && eval "$(SHELL=/bin/sh lesspipe)"; shopt -s globstar
