from manim import *

class ComplexPlaneScene(Scene):
    def construct(self):
        # シーンの背景色を黒に設定
        self.camera.background_color = BLACK

        # 実数軸と虚数軸を描画
        plane = ComplexPlane().add_coordinates()

        # 単位円を定義
        unit_circle = Circle(radius=1, color=WHITE)

        # アニメーションの定義
        self.play(Create(plane))      # 実数軸と虚数軸を描画
        self.play(Create(unit_circle)) # 単位円を描画

        # グリッドと単位円を画面いっぱいに拡大
        self.play(
            plane.animate.scale(3.5),
            unit_circle.animate.scale(3.5)
        )

        # 点滅しながら動く点を描画
        moving_dot = Dot(color=YELLOW)
        moving_dot.move_to(unit_circle.point_from_proportion(0))
        self.add(moving_dot)

        # 点を2周させるアニメーションを定義
        self.play(
            MoveAlongPath(moving_dot, unit_circle, rate_func=linear).set_run_time(4),
            MoveAlongPath(moving_dot, unit_circle, rate_func=linear).set_run_time(4)
        )

        # アニメーションを再生
        self.wait(2)

if __name__ == "__main__":
    from manim import config, tempconfig
    config.pixel_height = 720
    config.pixel_width = 1280
    config.frame_rate = 30
    config.background_color = BLACK
    with tempconfig({
        "quality": "low_quality"
    }):
        scene = ComplexPlaneScene()
        scene.render()