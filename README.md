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

Aiming to support vim-clang-format plugin you should install clang-format

```bash
# Example in Fedora OS
$ sudo dnf install clang -y
```

Based on https://www.quora.com/How-can-I-configure-Vim-to-use-the-Google-C++-coding-style-guide
To follow Google's style, in the root of your project, create a .clang-format file with the following command:

```bash
clang-format -style=google -dump-config > .clang-format
```

You need setting up the .vimrc with the clang-format.py from:
https://raw.githubusercontent.com/llvm-mirror/clang/master/tools/clang-format/clang-format.py

Download the clang-format.py, and then setting up in the vimrc at line 467 and 468
with the full path to the clang-format.py in your computer

Have fun :)
