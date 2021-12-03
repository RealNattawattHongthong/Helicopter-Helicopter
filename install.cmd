@echo off
echo Checking Python !
python --version
timeout 2 >null
del null
echo Install pygame 
pip install pygame
echo The program will run.. Please wait 
timeout 2 >null
del null
python main.py