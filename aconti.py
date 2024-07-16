# manim -p -ql aconti.py AnalyticContinuation

from manim import *

class AnalyticContinuation(Scene):
    def construct(self):
        title = Text("解析接続の解説", font_size=48)
        self.play(Write(title))
        self.wait(2)
        self.play(FadeOut(title))

        plane = ComplexPlane().add_coordinates()
        self.play(Create(plane))
        self.wait(1)

        func_label = MathTex(r"f(z) = \frac{1}{1 - z}", font_size=36)
        func_label.to_edge(UP)
        self.play(Write(func_label))
        self.wait(1)

        # First series expansion
        series1 = MathTex(
            r"f(z) = 1 + z + z^2 + z^3 + \cdots \quad \text{for} \ |z| < 1",
            font_size=36
        )
        series1.next_to(func_label, DOWN)
        self.play(Write(series1))
        self.wait(2)

        # Highlight the unit circle
        unit_circle = Circle(radius=1, color=YELLOW)
        self.play(Create(unit_circle))
        self.wait(1)

        # Second series expansion
        series2 = MathTex(
            r"f(z) = -\frac{1}{z} - \frac{1}{z^2} - \frac{1}{z^3} - \cdots \quad \text{for} \ |z| > 1",
            font_size=36
        )
        series2.next_to(series1, DOWN)
        self.play(Write(series2))
        self.wait(2)

        # Highlight the annulus region
        annulus_outer = Circle(radius=2, color=BLUE)
        annulus_inner = Circle(radius=1, color=BLACK, fill_opacity=1)
        annulus = VGroup(annulus_inner, annulus_outer)
        self.play(Create(annulus_outer))
        self.wait(1)

        # Explanation text
        explanation = Text(
            "解析接続は異なる領域での関数の拡張です",
            font_size=36
        )
        explanation.next_to(series2, DOWN)
        self.play(Write(explanation))
        self.wait(3)

        # Fade out all
        self.play(
            FadeOut(series1),
            FadeOut(series2),
            FadeOut(explanation),
            FadeOut(annulus),
            FadeOut(unit_circle),
            FadeOut(plane),
            FadeOut(func_label)
        )

        # Closing text
        closing_text = Text(
            "解析接続を用いて関数の定義域を拡張することができます",
            font_size=36
        )
        self.play(Write(closing_text))
        self.wait(3)

        self.play(FadeOut(closing_text))