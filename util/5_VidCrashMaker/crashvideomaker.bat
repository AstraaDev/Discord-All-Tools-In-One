@echo off
setlocal enabledelayedexpansion
pushd %~dp0
chcp 65001 >nul

title Video Crash Maker - Made by Astraa
set Version=1.0

set "AllowedExtentions=gif webm mp4 mkv png jpg"
set "ffmpeg=ffmpeg.exe"


color e
echo.
echo                          _    ___     __           ______                __       ______         
echo                         ^| ^|  / (_)___/ /__  ____  / ____/________ ______/ /_     / ____/__  ____ 
echo                         ^| ^| / / / __  / _ \/ __ \/ /   / ___/ __ `/ ___/ __ \   / / __/ _ \/ __ \
echo                         ^| ^|/ / / /_/ /  __/ /_/ / /___/ /  / /_/ (__  ) / / /  / /_/ /  __/ / / /
echo                         ^|___/_/\__,_/\___/\____/\____/_/   \__,_/____/_/ /_/   \____/\___/_/ /_/ 
echo.
echo.
echo ------------------------------------------------------------------------------------------------------------------------
echo adev ^| https://dsc.gg/astraadev ^| https://dsc.gg/astraadev ^| https://dsc.gg/astraadev ^| https://dsc.gg/astraadev ^| https
echo ------------------------------------------------------------------------------------------------------------------------
echo.
echo [+] ADDITIONAL INFORMATION:
echo.
echo             [#] Hardware acceleration must be enabled for it to work.
echo             [#] Crash videos can get you banned in some Discord servers.
echo             [#] If ffmpeg is not installed, it will be installed automatically. Plz do not delete.
pause >nul

:: <DOWNLOAD DEPENDENCIES>

echo.
if not exist "ffmpeg.exe" echo [#] Downloading ffmpeg:
if not exist "ffmpeg.exe" curl -#fkLo "!ffmpeg!" "https://github.com/agamsol/VideoCrash/raw/main/ffmpeg.exe"

:: </DOWNLOAD DEPENDENCIES>

:PROVIDE_FILE
if not defined SecondTime (
    set SecondTime=true
    set "Args=%*"
) else set Args=
set VideoFile=
set Output=
set VideoExt=
cls
if defined Args (
    echo --^> !Args!
    set VideoFile=!Args!
) else set /p "VideoFile= [#] Enter path to video file (or drag and drop the video here) : "

for /f "delims=" %%a in ("!VideoFile!") do (
    set "VideoFile=%%~a"
    set "Output=%%~na"
    set VideoExt=%%~xa
)

if not exist "!VideoFile!" (
    echo.
    echo [#] ERROR: Couldn't find the video specified
    timeout /t 3 /nobreak >nul
    goto :PROVIDE_FILE
)

echo !AllowedExtentions! | findstr /c:"!VideoExt:.=!">nul || (
    echo.
    echo [#] ERROR: You only can convert the following file formats: !AllowedExtentions: =%grey%, %brightblue%!
    timeout /t 5 /nobreak >nul
    goto :PROVIDE_FILE
)

cls
echo [#] Changing Pixel Format...
ffmpeg -i "!VideoFile!" -pix_fmt yuv444p video.webm -y >nul 2>&1

cls
echo [#] Generating Your File...
(
    echo file video.webm
    echo file black.webm
)>"merge-list.txt"

ffmpeg -f concat -i merge-list.txt -codec copy "crasher.mp4" -y >nul 2>&1

cls
echo [#] Cleaning files...
del /s /q "video.webm" "merge-list.txt" >nul 2>&1

cls
echo.
echo                          _    ___     __           ______                __       ______         
echo                         ^| ^|  / (_)___/ /__  ____  / ____/________ ______/ /_     / ____/__  ____ 
echo                         ^| ^| / / / __  / _ \/ __ \/ /   / ___/ __ `/ ___/ __ \   / / __/ _ \/ __ \
echo                         ^| ^|/ / / /_/ /  __/ /_/ / /___/ /  / /_/ (__  ) / / /  / /_/ /  __/ / / /
echo                         ^|___/_/\__,_/\___/\____/\____/_/   \__,_/____/_/ /_/   \____/\___/_/ /_/ 
echo.
echo.
echo ------------------------------------------------------------------------------------------------------------------------
echo adev ^| https://dsc.gg/astraadev ^| https://dsc.gg/astraadev ^| https://dsc.gg/astraadev ^| https://dsc.gg/astraadev ^| https
echo ------------------------------------------------------------------------------------------------------------------------
echo.
echo [#] Success, The File has been Successfully Generated. Located at "output/crasher.webm"
timeout /t 3 /nobreak >nul