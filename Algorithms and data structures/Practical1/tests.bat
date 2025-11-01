@echo off
setlocal enabledelayedexpansion

:: ------------------------------------------------------------
:: CONFIGURATION
:: ------------------------------------------------------------
set "SAMPLES_DIR=samples-grading" <-- Change this to what directory you downloaded from DOMJudge
set "RUN_CMD=python main.py"   :: <-- Change this if your program is different

:: ------------------------------------------------------------
:: PROGRAM
:: ------------------------------------------------------------

set /a total=0
set /a passed=0

if not exist "%SAMPLES_DIR%" (
    echo Directory "%SAMPLES_DIR%" not found.
    exit /b 1
)

for %%F in (%SAMPLES_DIR%\*.in) do (
    set /a total+=1
    set "infile=%%~fF"
    set "base=%%~nF"
    set "dir=%%~dpF"
    set "expected=%%~dpF%%~nF.ans"
    set "actual=%%~dpF%%~nF.tmp"
    set "difffile=%%~dpF%%~nF.diff"

    echo ------------------------------------------------------------
    echo Test: !base!

    if not exist "!expected!" (
        echo EXPECTED OUTPUT MISSING: "!expected!"
        echo FAIL: !base!
    ) else (
        :: Run the configured command
        !RUN_CMD! < "!infile!" > "!actual!"

        :: Compare outputs
        fc "!expected!" "!actual!" > "!difffile!" 2>&1

        if errorlevel 2 (
            echo ERROR comparing files for !base!
            type "!difffile!"
        ) else if errorlevel 1 (
            echo FAIL: !base!
            type "!difffile!"
        ) else (
            echo PASS: !base!
            set /a passed+=1
        )
    )

    del "!actual!"
    del "!difffile!"
)

set /a failed=total-passed
echo.
echo ------------------------------------------------------------
echo Total: %total%  Passed: %passed%  Failed: %failed%

endlocal
exit /b 0
