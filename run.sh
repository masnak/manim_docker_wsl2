#!/bin/bash

# 実行スクリプト

# DISPLAY環境変数の設定
DISPLAY_VAR=${DISPLAY}

# Manimのスクリプトファイルのパスを設定
MANIM_SCRIPT_PATH="/manim/simple_circle.py"

# Dockerコンテナの実行
docker run -it --rm \
    -e DISPLAY=$DISPLAY_VAR \
    -v /tmp/.X11-unix:/tmp/.X11-unix \
    -v $(pwd):/manim \
    manim-docker manim -p -ql ${MANIM_SCRIPT_PATH} SimpleCircle

echo "Manimの実行が完了しました。"