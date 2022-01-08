set nu
syntax on
cmap !q q!
cmap !Q q!
nnoremap p N
nnoremap :p :N
set showmode
inoremap <C-a> <Esc>:w! ! sudo tee % > /dev/null<CR>i
nnoremap <C-a> :w! ! sudo tee % > /dev/null<CR>
inoremap <C-c> <Esc>:color<CR>gi
nnoremap <C-c> :color<CR>
inoremap <C-s> <Esc>:update<CR>gi
nnoremap <C-s> :update<CR>
inoremap <C-z> <Esc>:u<CR>gi
nnoremap <C-z> :u<CR>
inoremap <C-r> <Esc>:r<CR>gi
nnoremap <C-r> :r<CR>
set backspace=indent,eol,start
inoremap <C-g> <Esc>:messages<CR>gi
nnoremap <C-g> :messages<CR>
filetype plugin indent on
set autowrite
set virtualedit=onemore
set history=1000
set undolevels=1000
noremap <buffer> <silent> <S-l> vg<Home>
noremap <buffer> <silent> <S-h> vg<End>
noremap <buffer> <silent> <S-k> vgk
noremap <buffer> <silent> <S-j> vgj
set undoreload=10000
set tabpagemax=15
set linespace=0
set showmatch
set incsearch
set winminheight=0
set ignorecase
set smartcase
set wildmenu
set shiftwidth=4
set tabstop=4
set softtabstop=4
set pastetoggle=<F12>
nnoremap A a
nnoremap Q q
nnoremap aq qa
nnoremap AQ qa
nnoremap qw wq
nnoremap QW wq
set autoread
set textwidth=80
set laststatus=2
set statusline=%F
set statusline+=%=
set statusline+=%m
set statusline+=\ %Y
set statusline+=\ %3l/%L[%3p%%]
inoremap <Enter> <Esc>:nohl<CR>gi<CR>
nnoremap <Enter> :nohl<CR><CR>
set hlsearch
set expandtab
set tabstop=4
set shiftwidth=4
set nobackup
set noswapfile
let mapleader=","
nnoremap ; :
nnoremap hs sp
nnoremap vs vsp
nnoremap <C-j> j
nnoremap <C-k> k
nnoremap <C-l> l
nnoremap <C-h> h
nnoremap < <<
nnoremap > >>
nnoremap Y v$y
nnoremap gy "+yy
nnoremap - _
nnoremap c( ci(
nnoremap c[ ci[
nnoremap c< ci<
nnoremap c{ ci{
nnoremap c" ci"
nnoremap c' ci'
inoremap <C-j> <Esc>ji
inoremap <C-k> <Esc>ki
inoremap <C-h> <Esc>hi
inoremap <C-l> <Esc>li
cnoreabbrev W w
cnoreabbrev Q q
cnoreabbrev A a
cnoreabbrev X x
cnoreabbrev Sh sh
cnoreabbrev sH sh
cnoreabbrev SH sh
nnoremap cm :color morning
nnoremap cd :color default
set display=lastline
