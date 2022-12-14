pip --version
IF %ERRORLEVEL% NEQ 0 (
  echo You don't have pip installed, installing it for you...
  python -m ensurepip --default-pip >NUL
)

echo Installing required module: playsound.
pip install playsound >NUL
echo Installing required module: win10toast
pip install win10toast >NUL

set /p question="Launch PVA now? (type y/n) "
if /i "%question%"=="y" (
  python PVA-Windows.py >NUL
)
