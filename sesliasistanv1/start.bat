@echo off
title Sesli Asistan Uygulaması

rem Python yüklü olduğundan emin olun
where python >nul 2>nul
if %errorlevel% neq 0 (
    echo Python yüklü değil. Lütfen yükleyin ve PATH'e ekleyin.
    pause
    exit
)

rem Gerekli Python paketlerini yükleyin
pip install SpeechRecognition pyttsx3 pygame

rem Sesli asistan uygulamasını başlat
python "C:\Users\MONSTER\Desktop\jarvis asistant\main.py"

rem Kapatıldığında ekranda bir mesaj görüntüle
echo Sesli Asistan uygulaması kapatıldı.
pause


echo __        _______ _     ____ ___  __  __ _____    __  __ ____       ____ ___ _     _____ _  __
\ \      / / ____| |   / ___/ _ \|  \/  | ____|  |  \/  |  _ \     | __ )_ _| |   | ____| |/ /
 \ \ /\ / /|  _| | |  | |  | | | | |\/| |  _|    | |\/| | |_) |    |  _ \| || |   |  _| | ' / 
  \ V  V / | |___| |__| |__| |_| | |  | | |___   | |  | |  _ < _   | |_) | || |___| |___| . \ 
   \_/\_/  |_____|_____\____\___/|_|  |_|_____|  |_|  |_|_| \_(_)  |____/___|_____|_____|_|\_\
