from manim import *

class SimpleCircle(Scene):
    def construct(self):
        # 円を作成
        circle = Circle(color=BLUE, fill_opacity=0.5)
        # テキストを作成
        text = Text("Hello Manim!", font_size=42)
        # 円の中心にテキストを配置
        text.move_to(circle.get_center())

        # 円とテキストをシーンに追加
        self.add(circle, text)
        # アニメーション：円とテキストを右に移動
        self.play(circle.animate.shift(RIGHT*3), text.animate.shift(RIGHT*3))
        # アニメーションの保持
        self.wait(2)
