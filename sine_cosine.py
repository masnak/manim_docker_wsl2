from manim import *

class TrigonometricGraphScene(Scene):
    def construct(self):
        # 座標軸の設定
        axes = Axes(
            x_range=[-1.5 * PI, 1.5 * PI, PI / 2],
            y_range=[-1.5, 1.5, 0.5],
            x_length=7,
            y_length=5,
            axis_config={"color": BLUE},
        )

        # 座標軸にラベルを直接追加
        labels = [
            MathTex("-\pi").next_to(axes.c2p(-PI, 0), DOWN),
            MathTex("-\pi/2").next_to(axes.c2p(-PI/2, 0), DOWN),
            MathTex("0").next_to(axes.c2p(0, 0), DOWN),
            MathTex("\pi/2").next_to(axes.c2p(PI/2, 0), DOWN),
            MathTex("\pi").next_to(axes.c2p(PI, 0), DOWN)
        ]

        self.add(axes, *labels)

        # グラフの描画
        sin_curve = axes.plot(lambda x: np.sin(x), color=GREEN)
        cos_curve = axes.plot(lambda x: np.cos(x), color=RED)

        # sin関数とcos関数のグラフにラベルを追加
        sin_label = axes.get_graph_label(sin_curve, label="sin(x)", x_val=-PI, direction=UP)
        cos_label = axes.get_graph_label(cos_curve, label="cos(x)", x_val=-PI/2, direction=UP)

        # グラフのアニメーション
        self.play(Create(sin_curve), Create(cos_curve), run_time=4)
        self.play(Write(sin_label), Write(cos_label), run_time=1)
        self.wait(1)

