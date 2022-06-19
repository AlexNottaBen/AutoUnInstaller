#! /usr/bin/python3
# -*- coding: utf-8 -*-
import os
import sys
import random

#os.system("title AutoInstaller")

def WhatItIs(ProgrammeName):
    print("==================== UnInstall " + ProgrammeName + " ====================")

def Cleaner(RootPassword):
    print("==================== Cleaning ====================")
    print("> autoremove")
    os.system('echo %s|sudo -S %s' % (RootPassword, "sudo apt autoremove --yes"))
    print("> autoclean")
    os.system('echo %s|sudo -S %s' % (RootPassword, "sudo apt autoclean --yes"))
    print("> clean")
    os.system('echo %s|sudo -S %s' % (RootPassword, "sudo apt clean --yes"))


def SimpleUnInstall(RootPassword,ProgrammeName):
    os.system('echo %s|sudo -S %s' % (RootPassword, "sudo apt remove " + ProgrammeName + " --yes"))

def SnapSimpleUnInstall(RootPassword,ProgrammeName):
    os.system('echo %s|sudo -S %s' % (RootPassword, "sudo snap remove " + ProgrammeName))# No "--yes"

def DoThis(RootPassword,Command):
    os.system('echo %s|sudo -S %s' % (RootPassword,Command))


def Logo():
    print("######################################")
    print("#            AutoUnInstaller         #")
    print("######################################")
    print("By AlexNottaBen")

def ClearScreen():
    os.system("clear")

#Begin
ClearScreen()
Logo()
RootPassword = input("Input Root Password > ")
ClearScreen()
Logo()
print("1 - Simple Clean")
print("2 - Delete All Programs!")
print("3 - Delete Selected Programs!")
print("4 - Delete Unused Programs!")

if True:
	UninstallFlashPlayer = "0"
	UninstallVLC = "0"
	UninstallGIMP = "0"
	UninstallMyPaint = "0"
	UninstallInkScape = "0"
	Uninstallblender = "0"
	UninstallSweetHome3D = "0"
	UninstallCaffeine = "0"
	UninstallCajaDrobBox = "0"
	UninstallTimeShift = "0"
	UninstallKdenline = "0"
	UninstallOpenShot = "0"
	UninstallAudacity = "0"
	UninstallGrubCustomizer = "0"
	UninstallVBOX = "0"
	UninstallNotepadplusplus = "0"
	UninstallWine = "0"
	UninstallPlayOnLinux = "0"
	UninstallThunderBird = "0"
	UninstallFireFox = "0"
	UninstallChromium = "0"
	UninstallEdge = "0"
	UninstallChrome = "0"
	UninstallTor = "0"
	UninstallVSC = "0"
	UninstallSublimeText = "0"
	UninstallAtom = "0"
	UninstallLibreOffice = "0"
	UninstallOnlyOffice = "0"
	UninstallWPSOffice = "0"
	UninstallMSFonts = "0"
	UninstallGnomeSoftWare = "0"
	UninstallSynaptic = "0"
	UninstallBleachBit = "0"
	UninstallCheese = "0"
	UninstallGparted = "0"
	UninstallQbitTorrent = "0"
	UninstallTransmission = "0"
	UninstallSSR = "0"
	UninstallOBS = "0"
	UninstallSteam = "0"
	UninstallZoom = "0"
	UninstallViber = "0"
	UninstallPidgin = "0"
	UninstallTelegram = "0"
	UninstallTeams = "0"
	UninstallSkype = "0"
	UninstallFileZilla = "0"
	UninstallLutris = "0"
	UninstallPeaZip = "0"
	UninstallQuodlibet = "0"
	UninstallKolourPaint = "0"
	UninstallParole = "0"
	UninstallClipIt = "0"
	UninstallConky = "0"
	UninstallFeatherpad = "0"


Answer = input("Answer > ")
if Answer == "1":
	UninstallFlashPlayer = "0"
	UninstallVLC = "0"
	UninstallGIMP = "0"
	UninstallMyPaint = "0"
	UninstallInkScape = "0"
	Uninstallblender = "0"
	UninstallSweetHome3D = "0"
	UninstallCaffeine = "0"
	UninstallCajaDrobBox = "0"
	UninstallTimeShift = "0"
	UninstallKdenline = "0"
	UninstallOpenShot = "0"
	UninstallAudacity = "0"
	UninstallGrubCustomizer = "0"
	UninstallVBOX = "0"
	UninstallNotepadplusplus = "0"
	UninstallWine = "0"
	UninstallPlayOnLinux = "0"
	UninstallThunderBird = "0"
	UninstallFireFox = "0"
	UninstallChromium = "0"
	UninstallEdge = "0"
	UninstallChrome = "0"
	UninstallTor = "0"
	UninstallVSC = "0"
	UninstallSublimeText = "0"
	UninstallAtom = "0"
	UninstallLibreOffice = "0"
	UninstallOnlyOffice = "0"
	UninstallWPSOffice = "0"
	UninstallMSFonts = "0"
	UninstallGnomeSoftWare = "0"
	UninstallSynaptic = "0"
	UninstallBleachBit = "0"
	UninstallCheese = "0"
	UninstallGparted = "0"
	UninstallQbitTorrent = "0"
	UninstallTransmission = "0"
	UninstallSSR = "0"
	UninstallOBS = "0"
	UninstallSteam = "0"
	UninstallZoom = "0"
	UninstallViber = "0"
	UninstallPidgin = "0"
	UninstallTelegram = "0"
	UninstallTeams = "0"
	UninstallSkype = "0"
	UninstallFileZilla = "0"
	UninstallLutris = "0"
	UninstallPeaZip = "0"
	UninstallQuodlibet = "0"
	UninstallKolourPaint = "0"
	UninstallClipIt = "0"
	UninstallConky = "0"
	UninstallFeatherpad = "0"
	UninstallClementine = "0"
	UninstallFoliate = "0"
	UninstallGalculator = "0"
	UninstallGeany = "0"
	UninstallGKrellM = "0"
	UninstallgMTP = "0"
	UninstallGNOMEPPP = "0"
	Uninstallgscan2pdf = "0"
	UninstallGSmartControl = "0"
	UninstallGtkHash = "0" 
	UninstallHexChat = "0" 
	UninstallIconBrowser = "0" 
	UninstallIDeviceMounter = "0"
	UninstallGuvcview = "0" 
	UninstallQuodlibet = "0" 


if Answer == "2":
	Code = int(random.randrange(11111, 99999))
	print("Enter this " + str(Code))
	InputCode = input("Input > ")
	if InputCode != str(Code):
		exit()
	print("Delete All!")
	UninstallFlashPlayer = "1"
	UninstallVLC = "1"
	UninstallGIMP = "1"
	UninstallMyPaint = "1"
	UninstallInkScape = "1"
	Uninstallblender = "1"
	UninstallSweetHome3D = "1"
	UninstallCaffeine = "1"
	UninstallCajaDrobBox = "1"
	UninstallTimeShift = "1"
	UninstallKdenline = "1"
	UninstallOpenShot = "1"
	UninstallAudacity = "1"
	UninstallGrubCustomizer = "1"
	UninstallVBOX = "1"
	UninstallNotepadplusplus = "1"
	UninstallWine = "1"
	UninstallPlayOnLinux = "1"
	UninstallThunderBird = "1"
	UninstallFireFox = "1"
	UninstallChromium = "1"
	UninstallEdge = "1"
	UninstallChrome = "1"
	UninstallTor = "1"
	UninstallVSC = "1"
	UninstallSublimeText = "1"
	UninstallAtom = "1"
	UninstallLibreOffice = "1"
	UninstallOnlyOffice = "1"
	UninstallWPSOffice = "1"
	UninstallMSFonts = "0"
	UninstallGnomeSoftWare = "1"
	UninstallSynaptic = "1"
	UninstallBleachBit = "1"
	UninstallCheese = "1"
	UninstallGparted = "1"
	UninstallQbitTorrent = "1"
	UninstallTransmission = "1"
	UninstallSSR = "1"
	UninstallOBS = "1"
	UninstallSteam = "1"
	UninstallZoom = "1"
	UninstallViber = "1"
	UninstallPidgin = "1"
	UninstallTelegram = "1"
	UninstallTeams = "1"
	UninstallSkype = "1"
	UninstallFileZilla = "1"
	UninstallLutris = "1"
	UninstallPeaZip = "1"
	UninstallQuodlibet = "1"
	UninstallKolourPaint = "1"
	UninstallClipIt = "1"
	UninstallConky = "1"
	UninstallFeatherpad = "1"
	UninstallClementine = "1"
	UninstallFoliate = "1"
	UninstallGalculator = "1"
	UninstallGeany = "1"
	UninstallGKrellM = "1"
	UninstallgMTP = "1"
	UninstallGNOMEPPP = "1"
	Uninstallgscan2pdf = "1"
	UninstallGSmartControl = "1"
	UninstallGtkHash = "1" 
	UninstallHexChat = "1" 
	UninstallIconBrowser = "1" 
	UninstallIDeviceMounter = "1"
	UninstallGuvcview = "1" 
	UninstallQuodlibet = "1" 


if Answer == "3":
	print("==================== Set Basic Setting ====================")
	UninstallFlashPlayer = input("UnInstall FlashPlayer (No = 0/Yes = 1): = ")
	print("==================== UnInstall Programs ====================")
	UninstallVLC = input("VLC - MediaPlayer (No = 0/Yes = 1): = ")
	UninstallGIMP = input("GIMP - Raster Graphic Editor (No = 0/Yes = 1): = ")
	UninstallMyPaint = input("MyPaint - Raster Graphic Editor (No = 0/Yes = 1): = ")
	UninstallInkScape = input("InkScape - Vector Graphic Editor (No = 0/Yes = 1): = ")
	Uninstallblender = input("Blender - 3D Editor (No = 0/Yes = 1): = ")
	UninstallSweetHome3D = input("Sweet Home 3D - 3D Home Editor (No = 0/Yes = 1): = ")
	UninstallCaffeine = input("Caffeine - Deactive sleep mode (No = 0/Yes = 1): = ")
	UninstallFileZilla = input("FileZilla - FTP Client (No = 0/Yes = 1): = ")
	UninstallCajaDrobBox = input("Caja DrobBox - Alternative One Drive (No = 0/Yes = 1): = ")
	UninstallTimeShift = input("TimeShift - Alternative Time Machine (No = 0/Yes = 1): = ")
	UninstallKdenline = input("Kdenline - Video Editor (No = 0/Yes = 1): = ")
	UninstallOpenShot = input("OpenShot - Open Video Editor (No = 0/Yes = 1): = ")
	UninstallAudacity = input("Audacity - Open Audio Editor (No = 0/Yes = 1): = ")
	UnInstallGrubCustomizer = input("Grub Customizer - For Grub Customition (No = 0/Yes = 1): = ")
	UninstallVBOX = input("Virtual Box - Virtual Computer (No = 0/Yes = 1): = ")
	UninstallNotepadplusplus = input("Notepad++ - Text Editor (No = 0/Yes = 1): = ")
	UninstallWine = input("Wine - Windows API (No = 0/Yes = 1): = ")
	UninstallPlayOnLinux = input("PlayOnLinux - For Run Windows Apps (No = 0/Yes = 1): = ")
	UninstallLutris = input("Lutris - For Run Windows Games (No = 0/Yes = 1): = ")
	UninstallThunderBird = input("ThunderBird - Open Mail Client(No = 0/Yes = 1): = ")
	UninstallFireFox = input("FireFox - Open Web-broweser(No = 0/Yes = 1): = ")
	UninstallChromium = input("Chromium - Open Web-broweser(No = 0/Yes = 1): = ")
	UninstallEdge = input("Edge[dev] - Web-broweser by Microsoft (No = 0/Yes = 1): = ")
	UninstallChrome = input("Google Chrome - Web-broweser by Google (No = 0/Yes = 1): = ")
	UninstallTor = input("Tor Browser - Web-broweser by Tor Project (No = 0/Yes = 1): = ")
	UninstallVSC = input("Visual Studio Code - Development Environment (No = 0/Yes = 1): = ")
	UninstallSublimeText  = input("Sublime Text - Text Editor (No = 0/Yes = 1): = ")
	UninstallAtom = input("Atom - Text Editor (No = 0/Yes = 1): = ")
	UninstallLibreOffice = input("Libre Office - OpenSource Office (No = 0/Yes = 1): = ")
	UninstallOnlyOffice = input("Only Office - OpenSource Office (No = 0/Yes = 1): = ")
	UninstallWPSOffice = input("WPS Office - Chinese Office (No = 0/Yes = 1): = ")
	UninstallSynaptic = input("Synaptic - Package Manager (No = 0/Yes = 1): = ")
	UninstallBleachBit = input("BleachBit - Alternative Piriform CCleaner (No = 0/Yes = 1): = ")
	UninstallCheese = input("Cheese - Camera (No = 0/Yes = 1): = ")
	UninstallGnomeSoftWare = input("Gnome SoftWare - Snap Store (No = 0/Yes = 1): = ")
	UninstallGparted = input("Gparted - Disk Utility (No = 0/Yes = 1): = ")
	UninstallQbitTorrent = input("Qbittorrent - Torrent Client  (No = 0/Yes = 1): = ")
	UninstallTransmission = input("Transmission - Torrent Client  (No = 0/Yes = 1): = ")
	UninstallSSR = input("Simple Screen Recorder - Screen Recorder  (No = 0/Yes = 1): = ")
	UninstallOBS = input("OBS Studio - Screen Recorder  (No = 0/Yes = 1): = ")
	UninstallSteam = input("Steam - Center For Games and Software (No = 0/Yes = 1): = ")
	UninstallZoom = input("Zoom - For Vidio Rings (No = 0/Yes = 1): = ")
	UninstallViber = input("Viber - For Chating (No = 0/Yes = 1): = ")
	UninstallPidgin = input("Pidgin - For Chating (No = 0/Yes = 1): = ")
	UninstallTelegram = input("Telegram - For Chating (No = 0/Yes = 1): = ")
	UninstallTeams = input("Microsoft Teams - For Study (No = 0/Yes = 1): = ")
	UninstallSkype = input("Microsoft Skype - For Vidio Rings (No = 0/Yes = 1): = ")
	UninstallPeaZip = input("PeaZip - Alternative WinRaR (No = 0/Yes = 1): = ")
	UninstallGrubCustomizer = input("Grub Customizer - For Edit Grub (No = 0/Yes = 1): = ")
	UninstallQuodlibet = input("Quod Libet - MediaPlayer (No = 0/Yes = 1): = ")

	Code = int(random.randrange(11111, 99999))
	print("Enter this " + str(Code))
	InputCode = input("Input > ")
	if InputCode != str(Code):
		exit()

if Answer == "4":
	UninstallFlashPlayer = "0"
	UninstallVLC = "0"
	UninstallGIMP = "0"
	UninstallMyPaint = "0"
	UninstallInkScape = "0"
	Uninstallblender = "0"
	UninstallSweetHome3D = "0"
	UninstallCaffeine = "0"
	UninstallCajaDrobBox = "0"
	UninstallTimeShift = "0"
	UninstallKdenline = "0"
	UninstallOpenShot = "0"
	UninstallAudacity = "0"
	UninstallGrubCustomizer = "0"
	UninstallVBOX = "0"
	UninstallNotepadplusplus = "0"
	UninstallWine = "0"
	UninstallPlayOnLinux = "0"
	UninstallThunderBird = "0"
	UninstallFireFox = "0"
	UninstallChromium = "0"
	UninstallEdge = "0"
	UninstallChrome = "0"
	UninstallTor = "0"
	UninstallVSC = "0"
	UninstallSublimeText = "0"
	UninstallAtom = "0"
	UninstallLibreOffice = "0"
	UninstallOnlyOffice = "0"
	UninstallWPSOffice = "0"
	UninstallMSFonts = "0"
	UninstallGnomeSoftWare = "0"
	UninstallSynaptic = "0"
	UninstallBleachBit = "0"
	UninstallCheese = "0"
	UninstallGparted = "0"
	UninstallQbitTorrent = "0"
	UninstallTransmission = "1"
	UninstallSSR = "0"
	UninstallOBS = "0"
	UninstallSteam = "0"
	UninstallZoom = "0"
	UninstallViber = "0"
	UninstallPidgin = "1"
	UninstallTelegram = "0"
	UninstallTeams = "0"
	UninstallSkype = "0"
	UninstallFileZilla = "0"
	UninstallLutris = "0"
	UninstallPeaZip = "0"
	UninstallParole = "1"
	#UninstallRistretto = "0" Warning! Uninstall Ristretto with more xfce programs!
	UninstallQuodlibet = "1"
#====
	UninstallClipIt = "1"
	UninstallConky = "1"
	UninstallFeatherpad = "1"
	UninstallClementine = "1"
	UninstallFoliate = "1"
	UninstallGalculator = "1"
	UninstallGeany = "1"
	UninstallGKrellM = "1"
	UninstallgMTP = "1"
	UninstallGNOMEPPP = "1"
	Uninstallgscan2pdf = "1"
	UninstallGSmartControl = "1"
	UninstallGtkHash = "1" 
	UninstallHexChat = "1" 
	UninstallIconBrowser = "1" 
	UninstallIDeviceMounter = "1"
	UninstallGuvcview = "1" 
	UninstallQuodlibet = "1" 


print("\n==================== Start ====================\n")

'''DoThis("")'''

'''
if UninstallMediaCodes == "1":
	WhatItIs("Media Codes")
	SimpleUnInstall(RootPassword,"ubuntu-restricted-extras")
'''

#Installs
if UninstallVLC == "1":
    WhatItIs("VLC")
    SimpleUnInstall(RootPassword,"vlc")

if UninstallGIMP == "1":
    WhatItIs("GIMP")
    SimpleUnInstall(RootPassword,"gimp")

if UninstallMyPaint == "1":
    WhatItIs("MyPaint")
    SimpleUnInstall(RootPassword,"mypaint")

if UninstallKolourPaint == "1":
    WhatItIs("KolourPaint")
    SimpleUnInstall(RootPassword,"kolourpaint")

if UninstallInkScape == "1":
    WhatItIs("InkScape")
    SimpleUnInstall(RootPassword,"inkscape")

if Uninstallblender == "1":
    WhatItIs("Blender")
    SimpleUnInstall(RootPassword,"blender")

if UninstallSweetHome3D == "1":
    WhatItIs("SweetHome3D")
    SimpleUnInstall(RootPassword,"sweethome3d")

if UninstallCaffeine == "1":
    WhatItIs("Caffeine")
    SimpleUnInstall(RootPassword,"caffeine")

if UninstallFileZilla == "1":
    WhatItIs("FileZilla")
    SimpleUnInstall(RootPassword,"filezilla")

if UninstallCajaDrobBox == "1":
    WhatItIs("Caja - DrobBox")
    SimpleUnInstall(RootPassword,"caja-dropbox")

if UninstallKdenline == "1":
    WhatItIs("Kdenline")
    SimpleUnInstall(RootPassword,"kdenlive")

if UninstallOpenShot == "1":
    WhatItIs("OpenShot")
    SimpleUnInstall(RootPassword,"openshot")

if UninstallAudacity == "1":
    WhatItIs("Audacity")
    SimpleUnInstall(RootPassword,"audacity")

if UninstallGrubCustomizer == "1":
    WhatItIs("GrubCustomizer")
    SimpleUnInstall(RootPassword,"grub-customizer")

if UninstallVBOX == "1":
    WhatItIs("Virtualbox")
    SimpleUnInstall(RootPassword,"virtualbox")

if UninstallNotepadplusplus == "1":
    WhatItIs("Notepad++")
    SnapSimpleUnInstall(RootPassword,"notepad-plus-plus")

if UninstallTelegram == "1":
    WhatItIs("Telegram")
    SnapSimpleUnInstall(RootPassword,"telegram-desktop")

if UninstallViber == "1":
    WhatItIs("Viber")
    SimpleUnInstall(RootPassword,"viber")
    
if UninstallPidgin == "1":
    WhatItIs("Pidgin")
    SimpleUnInstall(RootPassword,"pidgin")

if UninstallWine == "1":
    WhatItIs("Wine")
    SimpleUnInstall(RootPassword,"wine")

if UninstallGparted == "1":
    WhatItIs("Gparted")
    SimpleUnInstall(RootPassword,"gparted")

if UninstallPlayOnLinux == "1":
    WhatItIs("PlayOnLinux")
    SimpleUnInstall(RootPassword,"playonlinux")
    SimpleUnInstall(RootPassword,"winbind")
    SimpleUnInstall(RootPassword,"winetricks")

if UninstallLutris == "1":
    WhatItIs("Lutris")
    SimpleUnInstall(RootPassword,"lutris")

if UninstallSkype == "1":
    WhatItIs("MS Skype")
    DoThis(RootPassword,"sudo apt-get --purge remove skypeforlinux")
    SimpleUnInstall(RootPassword,"skypeforlinux")
    SnapSimpleUnInstall(RootPassword,"skypeforlinux")

if UninstallThunderBird == "1":
    WhatItIs("ThunderBird")
    SimpleUnInstall(RootPassword,"thunderbird")

if UninstallFireFox == "1":
    WhatItIs("FireFox")
    SimpleUnInstall(RootPassword,"firefox")

if UninstallChromium == "1":
    WhatItIs("Chromium")
    SnapSimpleUnInstall(RootPassword,"chromium")
    SimpleUnInstall(RootPassword,"chromium")
'''
    DoThis(RootPassword,"sudo apt-get remove chromium --purge --yes")
    DoThis(RootPassword,"sudo rm -rf ~/.config/chromium")
    DoThis(RootPassword,"sudo rm -rf ~/.cache/chromium")
    DoThis(RootPassword,"sudo rm -rf /etc/chromium")
'''
if UninstallEdge == "1":
    WhatItIs("MS Edge")
    SimpleUnInstall(RootPassword,"microsoft-edge-*")
    SimpleUnInstall(RootPassword,"microsoft-edge-dev")
    
if UninstallChrome == "1":
    WhatItIs("Google Chrome")
    DoThis(RootPassword,"sudo apt-get purge google-chrome-stable --yes")


if UninstallTor == "1":
    WhatItIs("Tor Browser")
    # '''letterboxing'''
    SimpleUnInstall(RootPassword,"torbrowser-launcher")

if UninstallFlashPlayer == "1":
	WhatItIs("Flash Player")
	SimpleUnInstall(RootPassword,"adobe-flashplugin")
	SimpleUnInstall(RootPassword,"browser-plugin-freshplayer-pepperflash")

if UninstallTimeShift == "1":
	WhatItIs("TimeShift")
	SimpleUnInstall(RootPassword,"timeshift")

if UninstallPeaZip == "1":
	WhatItIs("PeaZip")
	SimpleUnInstall(RootPassword,"peazip")

if UninstallVSC == "1":
	WhatItIs("Visual Studio Code")
	SimpleUnInstall(RootPassword,"code")

if UninstallSublimeText == "1":
     WhatItIs("Sublime Text")
     SnapSimpleUnInstall(RootPassword,"sublime-text")

if UninstallAtom == "1":
     WhatItIs("Atom")
     SimpleUnInstall(RootPassword,"atom")

if UninstallLibreOffice == "1":
    WhatItIs("LibreOffice")
    SimpleUnInstall(RootPassword,"--purge libreoffice-core")

if UninstallOnlyOffice == "1":
    WhatItIs("OnlyOffice")
    SimpleUnInstall(RootPassword,"onlyoffice-desktopeditors")
    SnapSimpleUnInstall(RootPassword,"onlyoffice-desktopeditors")
'''
    DoThis(RootPassword,"sudo docker stop documentserver")
    DoThis(RootPassword,"sudo docker rm documentserver")
    DoThis(RootPassword,"sudo docker ps -a")
    DoThis(RootPassword,"sudo docker rm -f $(sudo docker ps -aq)")
    DoThis(RootPassword,"rm -rvf /path/to/onlyoffice/data/directory")
    DoThis(RootPassword,"sudo docker rmi onlyoffice/documentserver")
    DoThis(RootPassword,"sudo docker rmi -f $(sudo docker images -aq)")
'''

if UninstallWPSOffice == "1":
    WhatItIs("WPSOffice")
    DoThis(RootPassword,"sudo apt-get purge wps-office --yes")
    DoThis(RootPassword,"sudo apt-get purge kingsoft-office --yes")
    DoThis(RootPassword,"sudo snap remove wps-office --yes")
    DoThis(RootPassword,"sudo apt-get purge --auto-remove wps-office --yes")

'''if UninstallMSFonts == "1":
	WhatItIs("Microsoft's Fonts")
	SimpleUnInstall(RootPassword,"ttf-mscorefonts-installer")
	SimpleUnInstall(RootPassword,"msttcorefonts")'''

if UninstallBleachBit == "1":
    SimpleUnInstall(RootPassword,"bleachbit")

if UninstallCheese == "1":
    SimpleUnInstall(RootPassword,"cheese")

if UninstallSynaptic == "1":
    WhatItIs("Synaptic Package Manager")
    SimpleUnInstall(RootPassword,"synaptic")
    SimpleUnInstall(RootPassword,"lxpolkit")
    SimpleUnInstall(RootPassword,"mate-polkit")
    SimpleUnInstall(RootPassword,"policykit-1-gnome")
    SimpleUnInstall(RootPassword,"lxqt-policykit")

if UninstallGnomeSoftWare =="1":
    WhatItIs("Gnome SoftWare")
    SimpleUnInstall(RootPassword,"gnome-software")

if UninstallQbitTorrent == "1":
    WhatItIs("qBittorrent")
    SimpleUnInstall(RootPassword,"qbittorrent")

if UninstallTransmission == "1":
    WhatItIs("Transmission")
    SimpleUnInstall(RootPassword,"transmission-daemon")
    DoThis(RootPassword,"sudo apt-get remove transmission-cli transmission-common transmission-daemon --yes")
    DoThis(RootPassword,"sudo apt-get purge transmission-cli transmission-common transmission-daemon --yes")
    DoThis(RootPassword,"sudo rm -fr /etc/transmission-daemon/")
    DoThis(RootPassword,"sudo apt-get autoremove transmission-cli transmission-common transmission-daemon --yes")

if UninstallSSR == "1":
    WhatItIs("Simple Screen Recorder")
    SimpleUnInstall(RootPassword,"simplescreenrecorder")

if UninstallOBS == "1":
    WhatItIs("OBS Studio")
    SimpleUnInstall(RootPassword,"obs-studio")

if UninstallZoom == "1":
    WhatItIs("Zoom")
    SimpleUnInstall(RootPassword,"zoom")

if UninstallSteam == "1":
    WhatItIs("Steam")
    SimpleUnInstall(RootPassword,"steam")

if UninstallTeams == "1":
    WhatItIs("MS Teams")
    SimpleUnInstall(RootPassword,"teams")

if UninstallParole == "1":
    WhatItIs("Parole")
    SimpleUnInstall(RootPassword,"parole")
'''
#Warning! Uninstall Ristretto with more xfce programs!
if UninstallRistretto == "1":
    WhatItIs("Ristretto")
    SimpleUnInstall(RootPassword,"ristretto")
'''
if UninstallQuodlibet == "1":
    WhatItIs("Quod Libet")
    SimpleUnInstall(RootPassword,"quodlibet")

if UninstallClipIt == "1":
    WhatItIs("ClipIt")
    SimpleUnInstall(RootPassword,"clipit")

if UninstallConky == "1":
    WhatItIs("Conky")
    SimpleUnInstall(RootPassword,"conky")

if UninstallFeatherpad == "1":
    WhatItIs("Featherpad")
    SimpleUnInstall(RootPassword,"featherpad")

if UninstallClementine == "1":
    WhatItIs("Clementine")
    SimpleUnInstall(RootPassword,"clementine")

if UninstallFoliate == "1":
    WhatItIs("Foliate")
    SimpleUnInstall(RootPassword,"foliate")

if UninstallGalculator == "1":
    WhatItIs("Galculator")
    SimpleUnInstall(RootPassword,"galculator")

if UninstallGeany == "1":
    WhatItIs("Geany")
    SimpleUnInstall(RootPassword,"geany")

if UninstallGKrellM == "1":
    WhatItIs("GKrellM")
    SimpleUnInstall(RootPassword,"gkrellm")

if UninstallgMTP == "1":
    WhatItIs("gMTP")
    SimpleUnInstall(RootPassword,"gmtp")

if UninstallGNOMEPPP == "1":
    WhatItIs("GNOMEPPP")
    SimpleUnInstall(RootPassword,"gnome-ppp")

if Uninstallgscan2pdf == "1":
    WhatItIs("gscan2pdf")
    SimpleUnInstall(RootPassword,"gscan2pdf")

if UninstallGSmartControl == "1":
    WhatItIs("GSmartControl")
    SimpleUnInstall(RootPassword,"gsmartcontrol")

if UninstallGtkHash == "1":
    WhatItIs("GtkHash")
    SimpleUnInstall(RootPassword,"gtkhash")

if UninstallHexChat == "1":
    WhatItIs("HexChat")
    SimpleUnInstall(RootPassword,"hexchat")

if UninstallIconBrowser == "1":
    WhatItIs("IconBrowser")
    SimpleUnInstall(RootPassword,"yad-icon-browser")#!

if UninstallIDeviceMounter == "1":
    WhatItIs("IDeviceMounter")
    SimpleUnInstall(RootPassword,"idevice-mounter")#!
    
if UninstallGuvcview == "1":
    WhatItIs("Guvcview")
    SimpleUnInstall(RootPassword,"guvcview")

Cleaner(RootPassword)

print("\n===================== End =====================")
isReboot = input("ReBoot? (No = 0/Yes = 1): = ")
if isReboot == "1":
    DoThis(RootPassword,"sudo shutdown -r now")
