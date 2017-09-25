# dotfilesvhb

## About

My personal configuration files.

## Install 

## Install Nerd Fonts

```bash
# Fedora or Ubuntu is in ~/.local/share/fonts
$ sudo su
$ cd /usr/share/fonts
$ wget https://github.com/ryanoasis/nerd-fonts/releases/download/v1.1.0/DroidSansMono.zip
$ mkdir DroidSansMono
$ unzip DroidSansMono.zip -d DroidSansMono/
$ fc-cache -f -v DroidSansMono

```
## Installing vimrc

Clone project and copy vimrc file to the user home directory:

```bash
$ git clone https://github.com/hbgit/dotfilesvhb.git
$ cp dotfilesvhb/vimrc ~/.vimrc
```

Clone Vundle plugin and install other plugins:

```bash
$ git clone https://github.com/VundleVim/Vundle.vim.git ~/.vim/bundle/Vundle.vim
$ vim +PluginInstall +qall
```

Have fun :)
