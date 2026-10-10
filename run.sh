#!/bin/bash

while true; do
    clear
    echo "========================================"
    echo "      数学アート生成プログラム ランチャー"
    echo "========================================"
    echo "  1. ドラゴン曲線 (dragon-curve.py)"
    echo "  2. ゴールドバッハ彗星 (goldbach-comet.py)"
    echo "  3. クリフォードのアトラクター (clifford-attractor.py)"
    echo "  4. ローレンツのアトラクター (lorenz-attractor.py)"
    echo "  5. バラ曲線 (rose-curve.py)"
    echo "  6. ジュリア集合 (julia-set.py)"
    echo "  7. マンデルブロ集合 (mandelbrot-set.py)"
    echo "  8. リサージュ図形 (lissajous-curve.py)"
    echo "  9. エノン・アトラクター (henon-attractor.py)"
    echo " 10. レスラーのアトラクター (rossler-attractor.py)"
    echo " 11. ド・ジョン・アトラクター (dejong-attractor.py)"
    echo " 12. 相沢のアトラクター (aizawa-attractor.py)"
    echo " 13. 終了"
    echo "========================================"
    read -p "実行する番号を選んでください (1〜13): " choice

    case $choice in
        1)
            echo ""
            echo "[dragon-curve.py] を実行しています ..."
            python3 dragon-curve.py
            ;;
        2)
            echo ""
            echo "[goldbach-comet.py] を実行しています ..."
            python3 goldbach-comet.py
            ;;
        3)
            echo ""
            echo "[clifford-attractor.py] を実行しています ..."
            python3 clifford-attractor.py
            ;;
        4)
            echo ""
            echo "[lorenz-attractor.py] を実行しています ..."
            python3 lorenz-attractor.py
            ;;
        5)
            echo ""
            echo "[rose-curve.py] を実行しています ..."
            python3 rose-curve.py
や            ;;
        6)
            echo ""
            echo "[julia-set.py] を実行しています ..."
            python3 julia-set.py
            ;;
        7)
            echo ""
            echo "[mandelbrot-set.py] を実行しています ..."
            python3 mandelbrot-set.py
            ;;
        8)
            echo ""
            echo "[lissajous-curve.py] を実行しています ..."
            python3 lissajous-curve.py
            ;;
        9)
            echo ""
            echo "[henon-attractor.py] を実行しています ..."
            python3 henon-attractor.py
            ;;
        10)
            echo ""
            echo "[rossler-attractor.py] を実行しています ..."
            python3 rossler-attractor.py
            ;;
        11)
            echo ""
            echo "[dejong-attractor.py] を実行しています ..."
            python3 dejong-attractor.py
            ;;
        12)
            echo ""
            echo "[aizawa-attractor.py] を実行しています ..."
            python3 aizawa-attractor.py
            ;;
        13)
            echo "終了します。"
            exit 0
            ;;
        *)
            echo ""
            echo "無効な番号です。もう一度選んでください。"
            ;;
    esac

    echo ""
    read -p "Enterキーを押すとメニューに戻ります..."
done