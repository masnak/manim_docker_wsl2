from manim import *

class UnitCircleScene(Scene): # Sceneクラスを継承する新しいクラスを定義します。
    def construct(self): # 主要なシーン構築メソッドを定義します。
        # XY平面を描画
        axes = Axes( # Axesオブジェクトを作成します。
            x_range=[-1.5, 1.5, 1], # X軸の範囲を設定します。
            y_range=[-1.5, 1.5, 1], # Y軸の範囲を設定します。
            axis_config={"color": WHITE}, # 軸の設定を設定します。
        )
        self.add(axes) # XY平面をシーンに追加します。

        # 単位円を描画
        circle = Circle(radius=1, color=WHITE) # 単位円を作成します。
        self.add(circle) # 単位円をシーンに追加します。

        # X軸とY軸の交点の座標を描画
        points = [Dot(axes.coords_to_point(x, 0), color=WHITE) for x in [-1, 1]] # X軸とY軸の交点の座標を作成します。
        points += [Dot(axes.coords_to_point(0, y), color=WHITE) for y in [-1, 1]] # X軸とY軸の交点の座標を作成します。
        self.add(*points) # X軸とY軸の交点の座標をシーンに追加します。

        # 動点を描画
        moving_dot = Dot(color=YELLOW) # 動点を作成します。
        self.add(moving_dot) # 動点をシーンに追加します。

        # 動点を円上で動かすアニメーション
        self.play(MoveAlongPath(moving_dot, circle, run_time=5, rate_func=linear)) # 動点を円上で動かすアニメーションを再生します。

        # この場面を保持
        self.wait()

# ドキュメンテーションの作成
"""
クラス名：UnitCircleScene
機能：XY平面に単位円を描き、動点を円上で反時計回りに動かす
詳細：
- `axes`はXY平面の座標軸
- `circle`は単位円
- `points`はX軸とY軸の交点
- `moving_dot`は動点、黄色で表示
- `MoveAlongPath`で動点を円上で動かす
"""

# manim -p -ql unit_circle.py UnitCircle