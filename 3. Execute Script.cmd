@echo off
echo Executant script...
python script.py
if %errorlevel% equ 0 (
  echo 
) else (
  echo ### Error executant el script ### Errors comuns poden ser que l'arxiu no es digui "llista" / "llista.csv" o que el format hagi canviat. Els camps haurien de ser "Numero/Classe", "Nom i cognoms" i "Serveis".
)
pause
