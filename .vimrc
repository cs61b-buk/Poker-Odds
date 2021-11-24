set nu
syntax on
cmap c color
cmap !q q!
cmap !Q q!
set showmode
nnoremap p N
inoremap <C-/> <C-c>/
nnoremap <C-/> <CR>i
inoremap <C-p> <C-c>Ni
inoremap <C-n> <C-c>ni
nnoremap <C-y> :w silent !python OneDrive\Desktop\TrueSkill_2.py<CR>
inoremap <C-y> <Esc>:w silent !python OneDrive\Desktop\TrueSkill_2.py<CR>gi
nnoremap <C-s> :update<CR>
inoremap <C-s> <Esc>:update<CR>gi
inoremap <C-z> <Esc>:u<CR>gi
nnoremap <C-z> :u<CR>
cmap m messages
set backspace=indent,eol,start
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
nnoremap P p
nnoremap W w
nnoremap çQ q
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
nnoremap <Enter> :nohl<CR><C-l><Enter>
nnoremap r <C-r>
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
nnoremap <C-o> <C-w>o
nnoremap + <C-W>+
nnoremap = <C-W>=
nnoremap - <C-W>-
nnoremap <space> zz
nnoremap n nzz
nnoremap N Nzz
nnoremap tt :tabm
nnoremap td :tabclose<CR>
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
inoremap <C-l> <Esc>li
inoremap <C-h> <Esc>hi
vnoremap < <gv
vnoremap > >gv
vnoremap gy "+y
vnoremap // y/<C-r>"<CR>
cnoreabbrev W w
cnoreabbrev Q q
cnoreabbrev A a
cnoreabbrev X x
cnoreabbrev Sh sh
cnoreabbrev sH sh
cnoreabbrev SH sh
color morning
set display=lastline
