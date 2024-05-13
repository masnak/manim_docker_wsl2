from manim import *

class UnitCircleScene(Scene):
    def construct(self):
        # XY平面を描画
        axes = Axes(
            x_range=[-1.5, 1.5, 1],
            y_range=[-1.5, 1.5, 1],
            axis_config={"color": WHITE},
        )
        self.add(axes)

        # 単位円を描画
        circle = Circle(radius=1, color=WHITE)
        self.add(circle)

        # X軸とY軸の交点の座標を描画
        points = [Dot(axes.coords_to_point(x, 0), color=WHITE) for x in [-1, 1]]
        points += [Dot(axes.coords_to_point(0, y), color=WHITE) for y in [-1, 1]]
        self.add(*points)

        # 動点を描画
        moving_dot = Dot(color=YELLOW)
        self.add(moving_dot)

        # 動点を円上で動かすアニメーション
        self.play(MoveAlongPath(moving_dot, circle, run_time=5, rate_func=linear))

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