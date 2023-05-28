## Vundle

Vim plugin manager to install, update and manage configured plugins.

https://github.com/VundleVim/Vundle.vim

## ALE (Asynchronous Lint Engine)

Plugin for providing linting (syntax checking adn semantic errors).

https://github.com/dense-analysis/ale

## Color Schemes

### Zenburn

https://github.com/jnurmine/Zenburn

## .vimrc

```.vimrc
 set nocompatible              " be iMproved, required
 51 filetype off                  " required
 50
 49 " set the runtime path to include Vundle and initialize
 48 set rtp+=~/.vim/bundle/Vundle.vim
 47 call vundle#begin()
 46 " alternatively, pass a path where Vundle should install plugins
 45 "call vundle#begin('~/some/path/here')
 44
 43 " let Vundle manage Vundle, required
 42 Plugin 'VundleVim/Vundle.vim'
 41 Plugin 'jnurmine/Zenburn'
 40 Plugin 'vim-syntastic/syntastic'
 39 Plugin 'nvie/vim-flake8'
 38 " All of your Plugins must be added before the following line
 37 call vundle#end()            " required
 36 filetype plugin indent on    " required
 35
 34 set relativenumber
 33 set smartindent
 32 set tabstop=4
 31 set shiftwidth=4
 30 set textwidth=79
 29 set softtabstop=4
 28 set expandtab
 27
 26 inoremap {<cr> {<cr>}<c-o><s-o>
 25 inoremap [<cr> [<cr>]<c-o><s-o>
 24 inoremap (<cr> (<cr>)<c-o><s-o>
 23
 22 nnoremap <C-J> <C-W><C-J>
 21 nnoremap <C-K> <C-W><C-K>
 20 nnoremap <C-L> <C-W><C-L>
 19 nnoremap <C-H> <C-W><C-H>
 18
 17 set number
 16 set ruler
 15 set encoding=utf-8
 14 colors zenburn
 13
 12 set fileformat=unix
 11 let python_highlight_all=1
 10 syntax on
  9
  8 set statusline+=%#warningmsg#
  7 set statusline+=%{SyntasticStatuslineFlag()}
  6 set statusline+=%*
  5
  4 let g:syntastic_always_populate_loc_list = 1
  3 let g:syntastic_auto_loc_list = 1
  2 let g:syntastic_check_on_open = 1
  1 let g:syntastic_check_on_wq = 0
53  let $PATH.=':' . $HOME . '/.vim/bundle/syntastic/'
```
