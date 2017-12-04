#!/usr/bin/env python

import sys
import os

os.system("sudo dnf install python-pip")
os.system("sudo dnf install git")
os.system("sudo pip install powerline-status")
os.system("wget https://github.com/powerline/powerline/raw/develop/font/PowerlineSymbols.otf")
os.system("wget https://github.com/powerline/powerline/raw/develop/font/10-powerline-symbols.conf")
os.system("sudo mv PowerlineSymbols.otf /usr/share/fonts/")
os.system("sudo fc-cache -vf /usr/share/fonts/")
os.system("sudo mv 10-powerline-symbols.conf /etc/fonts/conf.d/")

"""
 Manually
 >> Step 4: Setting Powerline for Bash Shell and Vim Statuslines
 export TERM="screen-256color"
 >> Get location
 pip show powerline-status
 >> Add on .bashrc
 powerline-daemon -q
 POWERLINE_BASH_CONTINUATION=1
 POWERLINE_BASH_SELECT=1
 . /usr/lib/python2.7/dist-packages/powerline/bindings/bash/powerline.sh
 >> Enable Powerline for Vim
 set  rtp+=/usr/lib/python2.7/dist-packages/powerline/bindings/vim/
 set laststatus=2
 set t_Co=256
"""

