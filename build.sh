#!/bin/bash

# ビルドスクリプト

# Dockerイメージのビルド
docker build -t manim-docker .

echo "Dockerイメージのビルドが完了しました。"