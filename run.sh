#!/bin/bash

# 現在のディスプレイ設定を取得
DISPLAY_SETTING=$DISPLAY

# カレントディレクトリを取得
CURRENT_DIR=$(pwd)

# Dockerコンテナを実行
docker run -it --rm \
    -e DISPLAY=$DISPLAY_SETTING \
    -v /tmp/.X11-unix:/tmp/.X11-unix \
    -v $CURRENT_DIR:/manim \
    --entrypoint /bin/bash manim-docker