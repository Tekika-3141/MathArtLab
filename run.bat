@echo off
chcp 65001 > nul
:menu
cls
echo ========================================
echo       数学アート生成プログラム ランチャー
echo ========================================
echo  1. ドラゴン曲線 (dragon-curve.py)
echo  2. ゴールドバッハ彗星 (goldbach-comet.py)
echo  3. クリフォードのアトラクター (clifford-attractor.py)
echo  4. ローレンツのアトラクター (lorenz-attractor.py)
echo  5. バラ曲線 (rose-curve.py)
echo  6. ジュリア集合 (julia-set.py)
echo  7. マンデルブロ集合 (mandelbrot-set.py)
echo  8. リサージュ図形 (lissajous-curve.py)
echo  9. エノン・アトラクター (henon-attractor.py)
echo 10. レスラーのアトラクター (rossler-attractor.py)
echo 11. ド・ジョン・アトラクター (dejong-attractor.py)
echo 12. 相沢のアトラクター (aizawa-attractor.py)
echo 13. 終了
echo ========================================
set /p choice="実行する番号を選んでください (1〜13): "

if "%choice%"=="1" (
    echo.
    echo [dragon-curve.py] を実行しています ...
    py dragon-curve.py
    goto end
)
if "%choice%"=="2" (
    echo.
    echo [goldbach-comet.py] を実行しています ...
    py goldbach-comet.py
    goto end
)
if "%choice%"=="3" (
    echo.
    echo [clifford-attractor.py] を実行しています ...
    py clifford-attractor.py
    goto end
)
if "%choice%"=="4" (
    echo.
    echo [lorenz-attractor.py] を実行しています ...
    py lorenz-attractor.py
    goto end
)
if "%choice%"=="5" (
    echo.
    echo [rose-curve.py] を実行しています ...
    py rose-curve.py
    goto end
)
if "%choice%"=="6" (
    echo.
    echo [julia-set.py] を実行しています ...
    py julia-set.py
    goto end
)
if "%choice%"=="7" (
    echo.
    echo [mandelbrot-set.py] を実行しています ...
    py mandelbrot-set.py
    goto end
)
if "%choice%"=="8" (
    echo.
    echo [lissajous-curve.py] を実行しています ...
    py lissajous-curve.py
    goto end
)
if "%choice%"=="9" (
    echo.
    echo [henon-attractor.py] を実行しています ...
    py henon-attractor.py
    goto end
)
if "%choice%"=="10" (
    echo.
    echo [rossler-attractor.py] を実行しています ...
    py rossler-attractor.py
    goto end
)
if "%choice%"=="11" (
    echo.
    echo [dejong-attractor.py] を実行しています ...
    py dejong-attractor.py
    goto end
)
if "%choice%"=="12" (
    echo.
    echo [aizawa-attractor.py] を実行しています ...
    py aizawa-attractor.py
    goto end
)
if "%choice%"=="13" (
    exit
)

echo.
echo 無効な番号です。もう一度選んでください。
pause
goto menu

:end
echo.
pause
goto menu