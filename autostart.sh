#!/bin/sh

# Systray network
nm-applet &

# Systray bluetooth
blueman-applet &

# Systray Optimus manager
optimus-manager-qt &

# Numlock systray
numlockx on &

# Set default layout
setxkbmap -layout us -variant altgr-intl

# Dunst
dunst &

# Dual Screen
xrandr --output eDP-1 --primary --mode 1366x768 --pos 1920x0 --rotate normal --output HDMI-1 --off --output DP-1 --mode 1920x1080 --pos 0x0 --rotate
normal

# Background
feh --bg-scale ~/Pictures/fondo.jpg
