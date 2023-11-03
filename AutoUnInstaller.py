#! /usr/bin/python3
# -*- coding: utf-8 -*-

from random import randrange
from os import system as execute
from getpass import getpass as input_password


def what_it_is(program_name):
    print("==================== uninstall " + program_name + " ====================")


def do_clean(root_password):
    print("==================== Cleaning ====================")
    print("> autoremove")
    execute("echo %s|sudo -S %s" % (root_password, "sudo apt autoremove --yes"))
    print("> autoclean")
    execute("echo %s|sudo -S %s" % (root_password, "sudo apt autoclean --yes"))
    print("> clean")
    execute("echo %s|sudo -S %s" % (root_password, "sudo apt clean --yes"))


def apt_remove(root_password, program_name):
    execute(
        "echo %s|sudo -S %s"
        % (root_password, "sudo apt remove " + program_name + " --yes")
    )


def snap_remove(root_password, program_name):
    execute(
        "echo %s|sudo -S %s" % (root_password, "sudo snap remove " + program_name)
    )  # No "--yes"


def execure_as_root(root_password, command):
    execute("echo %s|sudo -S %s" % (root_password, command))


def logo():
    print("######################################")
    print("#            Autouninstall_er         #")
    print("######################################")
    print("By AlexNottaBen")


def clear_screen():
    execute("clear")


# Begin
clear_screen()
logo()
root_password = input_password("Input Root Password > ")
clear_screen()
logo()
print("1 - Simple Clean")
print("2 - Delete All Programs!")
print("3 - Delete Selected Programs!")
print("4 - Delete Unused Programs!")

if True:
    uninstall_FlashPlayer = "0"
    uninstall_VLC = "0"
    uninstall_GIMP = "0"
    uninstall_MyPaint = "0"
    uninstall_InkScape = "0"
    uninstall_blender = "0"
    uninstall_SweetHome3D = "0"
    uninstall_Caffeine = "0"
    uninstall_CajaDrobBox = "0"
    uninstall_TimeShift = "0"
    uninstall_Kdenline = "0"
    uninstall_OpenShot = "0"
    uninstall_Audacity = "0"
    uninstall_GrubCustomizer = "0"
    uninstall_VBOX = "0"
    uninstall_Notepadplusplus = "0"
    uninstall_Wine = "0"
    uninstall_PlayOnLinux = "0"
    uninstall_ThunderBird = "0"
    uninstall_FireFox = "0"
    uninstall_Chromium = "0"
    uninstall_Edge = "0"
    uninstall_Chrome = "0"
    uninstall_Tor = "0"
    uninstall_VSC = "0"
    uninstall_SublimeText = "0"
    uninstall_Atom = "0"
    uninstall_LibreOffice = "0"
    uninstall_OnlyOffice = "0"
    uninstall_WPSOffice = "0"
    uninstall_MSFonts = "0"
    uninstall_GnomeSoftWare = "0"
    uninstall_Synaptic = "0"
    uninstall_BleachBit = "0"
    uninstall_Cheese = "0"
    uninstall_Gparted = "0"
    uninstall_QbitTorrent = "0"
    uninstall_Transmission = "0"
    uninstall_SSR = "0"
    uninstall_OBS = "0"
    uninstall_Steam = "0"
    uninstall_Zoom = "0"
    uninstall_Viber = "0"
    uninstall_Pidgin = "0"
    uninstall_Telegram = "0"
    uninstall_Teams = "0"
    uninstall_Skype = "0"
    uninstall_FileZilla = "0"
    uninstall_Lutris = "0"
    uninstall_PeaZip = "0"
    uninstall_Quodlibet = "0"
    uninstall_KolourPaint = "0"
    uninstall_Parole = "0"
    uninstall_ClipIt = "0"
    uninstall_Conky = "0"
    uninstall_Featherpad = "0"


Answer = input("Answer > ")
if Answer == "1":
    uninstall_FlashPlayer = "0"
    uninstall_VLC = "0"
    uninstall_GIMP = "0"
    uninstall_MyPaint = "0"
    uninstall_InkScape = "0"
    uninstall_blender = "0"
    uninstall_SweetHome3D = "0"
    uninstall_Caffeine = "0"
    uninstall_CajaDrobBox = "0"
    uninstall_TimeShift = "0"
    uninstall_Kdenline = "0"
    uninstall_OpenShot = "0"
    uninstall_Audacity = "0"
    uninstall_GrubCustomizer = "0"
    uninstall_VBOX = "0"
    uninstall_Notepadplusplus = "0"
    uninstall_Wine = "0"
    uninstall_PlayOnLinux = "0"
    uninstall_ThunderBird = "0"
    uninstall_FireFox = "0"
    uninstall_Chromium = "0"
    uninstall_Edge = "0"
    uninstall_Chrome = "0"
    uninstall_Tor = "0"
    uninstall_VSC = "0"
    uninstall_SublimeText = "0"
    uninstall_Atom = "0"
    uninstall_LibreOffice = "0"
    uninstall_OnlyOffice = "0"
    uninstall_WPSOffice = "0"
    uninstall_MSFonts = "0"
    uninstall_GnomeSoftWare = "0"
    uninstall_Synaptic = "0"
    uninstall_BleachBit = "0"
    uninstall_Cheese = "0"
    uninstall_Gparted = "0"
    uninstall_QbitTorrent = "0"
    uninstall_Transmission = "0"
    uninstall_SSR = "0"
    uninstall_OBS = "0"
    uninstall_Steam = "0"
    uninstall_Zoom = "0"
    uninstall_Viber = "0"
    uninstall_Pidgin = "0"
    uninstall_Telegram = "0"
    uninstall_Teams = "0"
    uninstall_Skype = "0"
    uninstall_FileZilla = "0"
    uninstall_Lutris = "0"
    uninstall_PeaZip = "0"
    uninstall_Quodlibet = "0"
    uninstall_KolourPaint = "0"
    uninstall_ClipIt = "0"
    uninstall_Conky = "0"
    uninstall_Featherpad = "0"
    uninstall_Clementine = "0"
    uninstall_Foliate = "0"
    uninstall_Galculator = "0"
    uninstall_Geany = "0"
    uninstall_GKrellM = "0"
    uninstall_gMTP = "0"
    uninstall_GNOMEPPP = "0"
    uninstall_gscan2pdf = "0"
    uninstall_GSmartControl = "0"
    uninstall_GtkHash = "0"
    uninstall_HexChat = "0"
    uninstall_IconBrowser = "0"
    uninstall_IDeviceMounter = "0"
    uninstall_Guvcview = "0"
    uninstall_Quodlibet = "0"


if Answer == "2":
    Code = int(randrange(11111, 99999))
    print("Enter this " + str(Code))
    InputCode = input("Input > ")
    if InputCode != str(Code):
        exit()
    print("Delete All!")
    uninstall_FlashPlayer = "1"
    uninstall_VLC = "1"
    uninstall_GIMP = "1"
    uninstall_MyPaint = "1"
    uninstall_InkScape = "1"
    uninstall_blender = "1"
    uninstall_SweetHome3D = "1"
    uninstall_Caffeine = "1"
    uninstall_CajaDrobBox = "1"
    uninstall_TimeShift = "1"
    uninstall_Kdenline = "1"
    uninstall_OpenShot = "1"
    uninstall_Audacity = "1"
    uninstall_GrubCustomizer = "1"
    uninstall_VBOX = "1"
    uninstall_Notepadplusplus = "1"
    uninstall_Wine = "1"
    uninstall_PlayOnLinux = "1"
    uninstall_ThunderBird = "1"
    uninstall_FireFox = "1"
    uninstall_Chromium = "1"
    uninstall_Edge = "1"
    uninstall_Chrome = "1"
    uninstall_Tor = "1"
    uninstall_VSC = "1"
    uninstall_SublimeText = "1"
    uninstall_Atom = "1"
    uninstall_LibreOffice = "1"
    uninstall_OnlyOffice = "1"
    uninstall_WPSOffice = "1"
    uninstall_MSFonts = "0"
    uninstall_GnomeSoftWare = "1"
    uninstall_Synaptic = "1"
    uninstall_BleachBit = "1"
    uninstall_Cheese = "1"
    uninstall_Gparted = "1"
    uninstall_QbitTorrent = "1"
    uninstall_Transmission = "1"
    uninstall_SSR = "1"
    uninstall_OBS = "1"
    uninstall_Steam = "1"
    uninstall_Zoom = "1"
    uninstall_Viber = "1"
    uninstall_Pidgin = "1"
    uninstall_Telegram = "1"
    uninstall_Teams = "1"
    uninstall_Skype = "1"
    uninstall_FileZilla = "1"
    uninstall_Lutris = "1"
    uninstall_PeaZip = "1"
    uninstall_Quodlibet = "1"
    uninstall_KolourPaint = "1"
    uninstall_ClipIt = "1"
    uninstall_Conky = "1"
    uninstall_Featherpad = "1"
    uninstall_Clementine = "1"
    uninstall_Foliate = "1"
    uninstall_Galculator = "1"
    uninstall_Geany = "1"
    uninstall_GKrellM = "1"
    uninstall_gMTP = "1"
    uninstall_GNOMEPPP = "1"
    uninstall_gscan2pdf = "1"
    uninstall_GSmartControl = "1"
    uninstall_GtkHash = "1"
    uninstall_HexChat = "1"
    uninstall_IconBrowser = "1"
    uninstall_IDeviceMounter = "1"
    uninstall_Guvcview = "1"
    uninstall_Quodlibet = "1"


if Answer == "3":
    print("==================== Set Basic Setting ====================")
    uninstall_FlashPlayer = input("uninstall FlashPlayer (No = 0/Yes = 1): = ")
    print("==================== uninstall Programs ====================")
    uninstall_VLC = input("VLC - MediaPlayer (No = 0/Yes = 1): = ")
    uninstall_GIMP = input("GIMP - Raster Graphic Editor (No = 0/Yes = 1): = ")
    uninstall_MyPaint = input("MyPaint - Raster Graphic Editor (No = 0/Yes = 1): = ")
    uninstall_InkScape = input("InkScape - Vector Graphic Editor (No = 0/Yes = 1): = ")
    uninstall_blender = input("Blender - 3D Editor (No = 0/Yes = 1): = ")
    uninstall_SweetHome3D = input("Sweet Home 3D - 3D Home Editor (No = 0/Yes = 1): = ")
    uninstall_Caffeine = input("Caffeine - Deactive sleep mode (No = 0/Yes = 1): = ")
    uninstall_FileZilla = input("FileZilla - FTP Client (No = 0/Yes = 1): = ")
    uninstall_CajaDrobBox = input(
        "Caja DrobBox - Alternative One Drive (No = 0/Yes = 1): = "
    )
    uninstall_TimeShift = input(
        "TimeShift - Alternative Time Machine (No = 0/Yes = 1): = "
    )
    uninstall_Kdenline = input("Kdenline - Video Editor (No = 0/Yes = 1): = ")
    uninstall_OpenShot = input("OpenShot - Open Video Editor (No = 0/Yes = 1): = ")
    uninstall_Audacity = input("Audacity - Open Audio Editor (No = 0/Yes = 1): = ")
    uninstall_GrubCustomizer = input(
        "Grub Customizer - For Grub Customition (No = 0/Yes = 1): = "
    )
    uninstall_VBOX = input("Virtual Box - Virtual Computer (No = 0/Yes = 1): = ")
    uninstall_Notepadplusplus = input("Notepad++ - Text Editor (No = 0/Yes = 1): = ")
    uninstall_Wine = input("Wine - Windows API (No = 0/Yes = 1): = ")
    uninstall_PlayOnLinux = input(
        "PlayOnLinux - For Run Windows Apps (No = 0/Yes = 1): = "
    )
    uninstall_Lutris = input("Lutris - For Run Windows Games (No = 0/Yes = 1): = ")
    uninstall_ThunderBird = input("ThunderBird - Open Mail Client(No = 0/Yes = 1): = ")
    uninstall_FireFox = input("FireFox - Open Web-broweser(No = 0/Yes = 1): = ")
    uninstall_Chromium = input("Chromium - Open Web-broweser(No = 0/Yes = 1): = ")
    uninstall_Edge = input("Edge[dev] - Web-broweser by Microsoft (No = 0/Yes = 1): = ")
    uninstall_Chrome = input(
        "Google Chrome - Web-broweser by Google (No = 0/Yes = 1): = "
    )
    uninstall_Tor = input(
        "Tor Browser - Web-broweser by Tor Project (No = 0/Yes = 1): = "
    )
    uninstall_VSC = input(
        "Visual Studio Code - Development Environment (No = 0/Yes = 1): = "
    )
    uninstall_SublimeText = input("Sublime Text - Text Editor (No = 0/Yes = 1): = ")
    uninstall_Atom = input("Atom - Text Editor (No = 0/Yes = 1): = ")
    uninstall_LibreOffice = input(
        "Libre Office - OpenSource Office (No = 0/Yes = 1): = "
    )
    uninstall_OnlyOffice = input("Only Office - OpenSource Office (No = 0/Yes = 1): = ")
    uninstall_WPSOffice = input("WPS Office - Chinese Office (No = 0/Yes = 1): = ")
    uninstall_Synaptic = input("Synaptic - Package Manager (No = 0/Yes = 1): = ")
    uninstall_BleachBit = input(
        "BleachBit - Alternative Piriform Cdo_clean (No = 0/Yes = 1): = "
    )
    uninstall_Cheese = input("Cheese - Camera (No = 0/Yes = 1): = ")
    uninstall_GnomeSoftWare = input("Gnome SoftWare - Snap Store (No = 0/Yes = 1): = ")
    uninstall_Gparted = input("Gparted - Disk Utility (No = 0/Yes = 1): = ")
    uninstall_QbitTorrent = input("Qbittorrent - Torrent Client  (No = 0/Yes = 1): = ")
    uninstall_Transmission = input(
        "Transmission - Torrent Client  (No = 0/Yes = 1): = "
    )
    uninstall_SSR = input(
        "Simple Screen Recorder - Screen Recorder  (No = 0/Yes = 1): = "
    )
    uninstall_OBS = input("OBS Studio - Screen Recorder  (No = 0/Yes = 1): = ")
    uninstall_Steam = input(
        "Steam - Center For Games and Software (No = 0/Yes = 1): = "
    )
    uninstall_Zoom = input("Zoom - For Vidio Rings (No = 0/Yes = 1): = ")
    uninstall_Viber = input("Viber - For Chating (No = 0/Yes = 1): = ")
    uninstall_Pidgin = input("Pidgin - For Chating (No = 0/Yes = 1): = ")
    uninstall_Telegram = input("Telegram - For Chating (No = 0/Yes = 1): = ")
    uninstall_Teams = input("Microsoft Teams - For Study (No = 0/Yes = 1): = ")
    uninstall_Skype = input("Microsoft Skype - For Vidio Rings (No = 0/Yes = 1): = ")
    uninstall_PeaZip = input("PeaZip - Alternative WinRaR (No = 0/Yes = 1): = ")
    uninstall_GrubCustomizer = input(
        "Grub Customizer - For Edit Grub (No = 0/Yes = 1): = "
    )
    uninstall_Quodlibet = input("Quod Libet - MediaPlayer (No = 0/Yes = 1): = ")

    Code = int(randrange(11111, 99999))
    print("Enter this " + str(Code))
    InputCode = input("Input > ")
    if InputCode != str(Code):
        exit()

if Answer == "4":
    uninstall_FlashPlayer = "0"
    uninstall_VLC = "0"
    uninstall_GIMP = "0"
    uninstall_MyPaint = "0"
    uninstall_InkScape = "0"
    uninstall_blender = "0"
    uninstall_SweetHome3D = "0"
    uninstall_Caffeine = "0"
    uninstall_CajaDrobBox = "0"
    uninstall_TimeShift = "0"
    uninstall_Kdenline = "0"
    uninstall_OpenShot = "0"
    uninstall_Audacity = "0"
    uninstall_GrubCustomizer = "0"
    uninstall_VBOX = "0"
    uninstall_Notepadplusplus = "0"
    uninstall_Wine = "0"
    uninstall_PlayOnLinux = "0"
    uninstall_ThunderBird = "0"
    uninstall_FireFox = "0"
    uninstall_Chromium = "0"
    uninstall_Edge = "0"
    uninstall_Chrome = "0"
    uninstall_Tor = "0"
    uninstall_VSC = "0"
    uninstall_SublimeText = "0"
    uninstall_Atom = "0"
    uninstall_LibreOffice = "0"
    uninstall_OnlyOffice = "0"
    uninstall_WPSOffice = "0"
    uninstall_MSFonts = "0"
    uninstall_GnomeSoftWare = "0"
    uninstall_Synaptic = "0"
    uninstall_BleachBit = "0"
    uninstall_Cheese = "0"
    uninstall_Gparted = "0"
    uninstall_QbitTorrent = "0"
    uninstall_Transmission = "1"
    uninstall_SSR = "0"
    uninstall_OBS = "0"
    uninstall_Steam = "0"
    uninstall_Zoom = "0"
    uninstall_Viber = "0"
    uninstall_Pidgin = "1"
    uninstall_Telegram = "0"
    uninstall_Teams = "0"
    uninstall_Skype = "0"
    uninstall_FileZilla = "0"
    uninstall_Lutris = "0"
    uninstall_PeaZip = "0"
    uninstall_Parole = "1"
    # uninstall_Ristretto = "0" Warning! uninstall Ristretto with more xfce programs!
    uninstall_Quodlibet = "1"
    # ====
    uninstall_ClipIt = "1"
    uninstall_Conky = "1"
    uninstall_Featherpad = "1"
    uninstall_Clementine = "1"
    uninstall_Foliate = "1"
    uninstall_Galculator = "1"
    uninstall_Geany = "1"
    uninstall_GKrellM = "1"
    uninstall_gMTP = "1"
    uninstall_GNOMEPPP = "1"
    uninstall_gscan2pdf = "1"
    uninstall_GSmartControl = "1"
    uninstall_GtkHash = "1"
    uninstall_HexChat = "1"
    uninstall_IconBrowser = "1"
    uninstall_IDeviceMounter = "1"
    uninstall_Guvcview = "1"
    uninstall_Quodlibet = "1"


print("\n==================== Start ====================\n")

# Installs
if uninstall_VLC == "1":
    what_it_is("VLC")
    apt_remove(root_password, "vlc")

if uninstall_GIMP == "1":
    what_it_is("GIMP")
    apt_remove(root_password, "gimp")

if uninstall_MyPaint == "1":
    what_it_is("MyPaint")
    apt_remove(root_password, "mypaint")

if uninstall_KolourPaint == "1":
    what_it_is("KolourPaint")
    apt_remove(root_password, "kolourpaint")

if uninstall_InkScape == "1":
    what_it_is("InkScape")
    apt_remove(root_password, "inkscape")

if uninstall_blender == "1":
    what_it_is("Blender")
    apt_remove(root_password, "blender")

if uninstall_SweetHome3D == "1":
    what_it_is("SweetHome3D")
    apt_remove(root_password, "sweethome3d")

if uninstall_Caffeine == "1":
    what_it_is("Caffeine")
    apt_remove(root_password, "caffeine")

if uninstall_FileZilla == "1":
    what_it_is("FileZilla")
    apt_remove(root_password, "filezilla")

if uninstall_CajaDrobBox == "1":
    what_it_is("Caja - DrobBox")
    apt_remove(root_password, "caja-dropbox")

if uninstall_Kdenline == "1":
    what_it_is("Kdenline")
    apt_remove(root_password, "kdenlive")

if uninstall_OpenShot == "1":
    what_it_is("OpenShot")
    apt_remove(root_password, "openshot")

if uninstall_Audacity == "1":
    what_it_is("Audacity")
    apt_remove(root_password, "audacity")

if uninstall_GrubCustomizer == "1":
    what_it_is("GrubCustomizer")
    apt_remove(root_password, "grub-customizer")

if uninstall_VBOX == "1":
    what_it_is("Virtualbox")
    apt_remove(root_password, "virtualbox")

if uninstall_Notepadplusplus == "1":
    what_it_is("Notepad++")
    snap_remove(root_password, "notepad-plus-plus")

if uninstall_Telegram == "1":
    what_it_is("Telegram")
    snap_remove(root_password, "telegram-desktop")

if uninstall_Viber == "1":
    what_it_is("Viber")
    apt_remove(root_password, "viber")

if uninstall_Pidgin == "1":
    what_it_is("Pidgin")
    apt_remove(root_password, "pidgin")

if uninstall_Wine == "1":
    what_it_is("Wine")
    apt_remove(root_password, "wine")

if uninstall_Gparted == "1":
    what_it_is("Gparted")
    apt_remove(root_password, "gparted")

if uninstall_PlayOnLinux == "1":
    what_it_is("PlayOnLinux")
    apt_remove(root_password, "playonlinux")
    apt_remove(root_password, "winbind")
    apt_remove(root_password, "winetricks")

if uninstall_Lutris == "1":
    what_it_is("Lutris")
    apt_remove(root_password, "lutris")

if uninstall_Skype == "1":
    what_it_is("MS Skype")
    execure_as_root(root_password, "sudo apt-get --purge remove skypeforlinux")
    apt_remove(root_password, "skypeforlinux")
    snap_remove(root_password, "skypeforlinux")

if uninstall_ThunderBird == "1":
    what_it_is("ThunderBird")
    apt_remove(root_password, "thunderbird")

if uninstall_FireFox == "1":
    what_it_is("FireFox")
    apt_remove(root_password, "firefox")

if uninstall_Chromium == "1":
    what_it_is("Chromium")
    snap_remove(root_password, "chromium")
    apt_remove(root_password, "chromium")
"""
    execure_as_root(root_password,"sudo apt-get remove chromium --purge --yes")
    execure_as_root(root_password,"sudo rm -rf ~/.config/chromium")
    execure_as_root(root_password,"sudo rm -rf ~/.cache/chromium")
    execure_as_root(root_password,"sudo rm -rf /etc/chromium")
"""
if uninstall_Edge == "1":
    what_it_is("MS Edge")
    apt_remove(root_password, "microsoft-edge-*")
    apt_remove(root_password, "microsoft-edge-dev")

if uninstall_Chrome == "1":
    what_it_is("Google Chrome")
    execure_as_root(root_password, "sudo apt-get purge google-chrome-stable --yes")


if uninstall_Tor == "1":
    what_it_is("Tor Browser")
    # '''letterboxing'''
    apt_remove(root_password, "torbrowser-launcher")

if uninstall_FlashPlayer == "1":
    what_it_is("Flash Player")
    apt_remove(root_password, "adobe-flashplugin")
    apt_remove(root_password, "browser-plugin-freshplayer-pepperflash")

if uninstall_TimeShift == "1":
    what_it_is("TimeShift")
    apt_remove(root_password, "timeshift")

if uninstall_PeaZip == "1":
    what_it_is("PeaZip")
    apt_remove(root_password, "peazip")

if uninstall_VSC == "1":
    what_it_is("Visual Studio Code")
    apt_remove(root_password, "code")

if uninstall_SublimeText == "1":
    what_it_is("Sublime Text")
    snap_remove(root_password, "sublime-text")

if uninstall_Atom == "1":
    what_it_is("Atom")
    apt_remove(root_password, "atom")

if uninstall_LibreOffice == "1":
    what_it_is("LibreOffice")
    apt_remove(root_password, "--purge libreoffice-core")

if uninstall_OnlyOffice == "1":
    what_it_is("OnlyOffice")
    apt_remove(root_password, "onlyoffice-desktopeditors")
    snap_remove(root_password, "onlyoffice-desktopeditors")
"""
    execure_as_root(root_password,"sudo docker stop documentserver")
    execure_as_root(root_password,"sudo docker rm documentserver")
    execure_as_root(root_password,"sudo docker ps -a")
    execure_as_root(root_password,"sudo docker rm -f $(sudo docker ps -aq)")
    execure_as_root(root_password,"rm -rvf /path/to/onlyoffice/data/directory")
    execure_as_root(root_password,"sudo docker rmi onlyoffice/documentserver")
    execure_as_root(root_password,"sudo docker rmi -f $(sudo docker images -aq)")
"""

if uninstall_WPSOffice == "1":
    what_it_is("WPSOffice")
    execure_as_root(root_password, "sudo apt-get purge wps-office --yes")
    execure_as_root(root_password, "sudo apt-get purge kingsoft-office --yes")
    execure_as_root(root_password, "sudo snap remove wps-office --yes")
    execure_as_root(root_password, "sudo apt-get purge --auto-remove wps-office --yes")

"""if uninstall_MSFonts == "1":
    what_it_is("Microsoft's Fonts")
    apt_remove(root_password,"ttf-mscorefonts-installer")
    apt_remove(root_password,"msttcorefonts")"""

if uninstall_BleachBit == "1":
    apt_remove(root_password, "bleachbit")

if uninstall_Cheese == "1":
    apt_remove(root_password, "cheese")

if uninstall_Synaptic == "1":
    what_it_is("Synaptic Package Manager")
    apt_remove(root_password, "synaptic")
    apt_remove(root_password, "lxpolkit")
    apt_remove(root_password, "mate-polkit")
    apt_remove(root_password, "policykit-1-gnome")
    apt_remove(root_password, "lxqt-policykit")

if uninstall_GnomeSoftWare == "1":
    what_it_is("Gnome SoftWare")
    apt_remove(root_password, "gnome-software")

if uninstall_QbitTorrent == "1":
    what_it_is("qBittorrent")
    apt_remove(root_password, "qbittorrent")

if uninstall_Transmission == "1":
    what_it_is("Transmission")
    apt_remove(root_password, "transmission-daemon")
    execure_as_root(
        root_password,
        "sudo apt-get remove transmission-cli transmission-common transmission-daemon --yes",
    )
    execure_as_root(
        root_password,
        "sudo apt-get purge transmission-cli transmission-common transmission-daemon --yes",
    )
    execure_as_root(root_password, "sudo rm -fr /etc/transmission-daemon/")
    execure_as_root(
        root_password,
        "sudo apt-get autoremove transmission-cli transmission-common transmission-daemon --yes",
    )

if uninstall_SSR == "1":
    what_it_is("Simple Screen Recorder")
    apt_remove(root_password, "simplescreenrecorder")

if uninstall_OBS == "1":
    what_it_is("OBS Studio")
    apt_remove(root_password, "obs-studio")

if uninstall_Zoom == "1":
    what_it_is("Zoom")
    apt_remove(root_password, "zoom")

if uninstall_Steam == "1":
    what_it_is("Steam")
    apt_remove(root_password, "steam")

if uninstall_Teams == "1":
    what_it_is("MS Teams")
    apt_remove(root_password, "teams")

if uninstall_Parole == "1":
    what_it_is("Parole")
    apt_remove(root_password, "parole")
"""
#Warning! uninstall Ristretto with more xfce programs!
if uninstall_Ristretto == "1":
    what_it_is("Ristretto")
    apt_remove(root_password,"ristretto")
"""
if uninstall_Quodlibet == "1":
    what_it_is("Quod Libet")
    apt_remove(root_password, "quodlibet")

if uninstall_ClipIt == "1":
    what_it_is("ClipIt")
    apt_remove(root_password, "clipit")

if uninstall_Conky == "1":
    what_it_is("Conky")
    apt_remove(root_password, "conky")

if uninstall_Featherpad == "1":
    what_it_is("Featherpad")
    apt_remove(root_password, "featherpad")

if uninstall_Clementine == "1":
    what_it_is("Clementine")
    apt_remove(root_password, "clementine")

if uninstall_Foliate == "1":
    what_it_is("Foliate")
    apt_remove(root_password, "foliate")

if uninstall_Galculator == "1":
    what_it_is("Galculator")
    apt_remove(root_password, "galculator")

if uninstall_Geany == "1":
    what_it_is("Geany")
    apt_remove(root_password, "geany")

if uninstall_GKrellM == "1":
    what_it_is("GKrellM")
    apt_remove(root_password, "gkrellm")

if uninstall_gMTP == "1":
    what_it_is("gMTP")
    apt_remove(root_password, "gmtp")

if uninstall_GNOMEPPP == "1":
    what_it_is("GNOMEPPP")
    apt_remove(root_password, "gnome-ppp")

if uninstall_gscan2pdf == "1":
    what_it_is("gscan2pdf")
    apt_remove(root_password, "gscan2pdf")

if uninstall_GSmartControl == "1":
    what_it_is("GSmartControl")
    apt_remove(root_password, "gsmartcontrol")

if uninstall_GtkHash == "1":
    what_it_is("GtkHash")
    apt_remove(root_password, "gtkhash")

if uninstall_HexChat == "1":
    what_it_is("HexChat")
    apt_remove(root_password, "hexchat")

if uninstall_IconBrowser == "1":
    what_it_is("IconBrowser")
    apt_remove(root_password, "yad-icon-browser")  #!

if uninstall_IDeviceMounter == "1":
    what_it_is("IDeviceMounter")
    apt_remove(root_password, "idevice-mounter")  #!

if uninstall_Guvcview == "1":
    what_it_is("Guvcview")
    apt_remove(root_password, "guvcview")

do_clean(root_password)

print("\n===================== End =====================")
if int(input("ReBoot? (No = 0/Yes = 1): = ")):
    execure_as_root(root_password, "sudo shutdown -r now")
