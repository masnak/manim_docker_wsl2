from manim import *

class SineCosineAnimation(Scene):
    def construct(self):
        # 座標軸の設定
        axes = Axes(
            x_range=[-1, 1, 0.5],
            y_range=[-1, 1, 0.5],
            x_length=5,
            y_length=5,
            axis_config={"color": BLUE},
        )
        circle = Circle(radius=1, color=WHITE).move_to(axes.c2p(0,0))
        
        # 点の初期化
        dot = Dot(axes.c2p(1, 0), color=YELLOW)
        
        # ラインの初期化
        line_sin = always_redraw(lambda: Line(axes.c2p(0, 0), dot.get_center(), color=GREEN))
        line_cos = always_redraw(lambda: Line(dot.get_center(), axes.c2p(dot.get_x(), 0), color=RED))
        
        # パスの初期化
        path_sin = TracedPath(dot.get_center, stroke_color=GREEN, stroke_width=4)
        path_cos = TracedPath(lambda: axes.c2p(dot.get_x(), 0), stroke_color=RED, stroke_width=4)

        # 点の動きを定義
        def update_dot(mob, dt):
            mob.rotate_about_origin(-dt)
        
        # 点にアップデート関数を追加
        dot.add_updater(update_dot)
        
        # シーンにオブジェクトを追加
        self.add(axes, circle, dot, line_sin, line_cos, path_sin, path_cos)
        self.wait(10)  # 10秒間アニメーションを実行
        
        # アップデータを停止
        dot.remove_updater(update_dot)
