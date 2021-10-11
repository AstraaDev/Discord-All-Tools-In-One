@echo off

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
echo ev.club/ ^| http://astraadev.club/ ^| http://astraadev.club/ ^| http://astraadev.club/ ^| http://astraadev.club/ ^| http://as
echo ------------------------------------------------------------------------------------------------------------------------
echo.
echo [+] ADDITIONAL INFORMATION:
echo.
echo             [!] Hardware acceleration must be enabled for it to work.
echo             [!] Crash videos can get you banned in some Discord servers.
echo             [!] FFmpeg needs to be installed for this to work!
pause >nul

WHERE ffmpeg
IF %ERRORLEVEL% NEQ 0 echo ffmpeg wasn't found. Please make sure it is installed correctly. && pause && exit
color e
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
echo ev.club/ ^| http://astraadev.club/ ^| http://astraadev.club/ ^| http://astraadev.club/ ^| http://astraadev.club/ ^| http://as
echo ------------------------------------------------------------------------------------------------------------------------
echo.
set /p filepath=[#] Enter path to video file (or drag and drop the video here) : 
echo.

set timestamp=1
set /p timestamp=[#] Enter the time when the video should crash (in seconds) : 
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
echo ev.club/ ^| http://astraadev.club/ ^| http://astraadev.club/ ^| http://astraadev.club/ ^| http://astraadev.club/ ^| http://as
echo ------------------------------------------------------------------------------------------------------------------------
echo.
echo [#] Getting video duration...
ffprobe -i %filepath% -show_entries format=duration -v quiet -of csv="p=0" > tmpfile
set /p duration= < tmpfile
del tmpfile
ping 127.0.0.1 -n 3 > NUL
cls

echo [#] Splitting video...
ffmpeg -i %filepath% -ss 0 -t %timestamp% part1.mp4
ffmpeg -i %filepath% -ss %timestamp% -t %duration% part2.mp4

echo [#] Changing video properties...
ffmpeg -i part2.mp4 -pix_fmt yuv444p part2_new.mp4
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
echo ev.club/ ^| http://astraadev.club/ ^| http://astraadev.club/ ^| http://astraadev.club/ ^| http://astraadev.club/ ^| http://as
echo ------------------------------------------------------------------------------------------------------------------------
echo.
echo [#] Creating file list...
echo file part1.mp4> file_list.txt
echo file part2_new.mp4>> file_list.txt
ping 127.0.0.1 -n 3 > NUL
cls

echo [#] Creating output file...
ffmpeg -f concat -safe 0 -i file_list.txt -codec copy temp/crasher.mp4
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
echo ev.club/ ^| http://astraadev.club/ ^| http://astraadev.club/ ^| http://astraadev.club/ ^| http://astraadev.club/ ^| http://as
echo ------------------------------------------------------------------------------------------------------------------------
echo.
echo [#] Cleaning up old files...
del part1.mp4
del part2.mp4
del part2_new.mp4
del file_list.txt
ping 127.0.0.1 -n 3 > NUL
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
echo ev.club/ ^| http://astraadev.club/ ^| http://astraadev.club/ ^| http://astraadev.club/ ^| http://astraadev.club/ ^| http://as
echo ------------------------------------------------------------------------------------------------------------------------
echo.
echo [#] Output video created! It is located at "%CD%\temp\crasher.mp4"
pause >nul
