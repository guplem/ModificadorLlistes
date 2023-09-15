@echo off
echo Instalando pandas para Python...
pip install pandas
if %errorlevel% equ 0 (
  echo ### PANDAS SE HA INSTALADO CORRECTAMENTE. ###
) else (
  echo ### ERROR INSTALANDO PANDAS. ###
)
pause
