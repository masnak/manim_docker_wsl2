# ベースイメージの指定
FROM python:3.9-slim

# 必要なパッケージのインストール
RUN apt-get update && apt-get install -y \
    pkg-config \
    gcc \
    g++ \
    libcairo2-dev \
    libpango1.0-dev \
    librsvg2-dev \
    xdg-utils \
    texlive \
    texlive-latex-extra \
    texlive-fonts-recommended \
    ffmpeg && rm -rf /var/lib/apt/lists/*  # ffmpegを追加し、コメントをこの行に移動

# 必要なPythonパッケージのインストール
RUN pip install manim \
    importlib_metadata  # importlib_metadataを追加

# 作業ディレクトリの設定
WORKDIR /manim

# スクリプトファイルのコピー
COPY . /manim

# エントリポイントの設定
ENTRYPOINT ["manim"]

# X11ソケットの使用を許可（Dockerコンテナ内でGUIを有効にする）
# ENV DISPLAY=host.docker.internal:0.0

# ビルド
# docker build -t manim-docker .

# 実行
# docker run -it --rm -e DISPLAY=$DISPLAY -v /tmp/.X11-unix:/tmp/.X11-unix -v $(pwd):/manim manim-docker manim -p -ql /manim/simple_circle.py SimpleCircle


# bash login
# docker run -it --rm -e DISPLAY=$DISPLAY -v /tmp/.X11-unix:/tmp/.X11-unix -v $(pwd):/manim --entrypoint /bin/bash manim-docker

# docker container内部で実行
# manim -p -ql simple_circle.py SimpleCircle
# manim -p -ql sine_curve_unit_circle.py SineCurveUnitCircle
# manim -p -ql sine_curve_unit_circle.py SineCurveUnitCircle -n 100
# manim -p -ql sin_cos2.py SineCosine2
# manim -p -ql sine_cosine.py SineCosine
# manim -p -ql unit_circle.py UnitCircle

