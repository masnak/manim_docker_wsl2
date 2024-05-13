from manim import *  # Manimライブラリをインポートします。

class SineCurveUnitCircle(Scene):  # Sceneクラスを継承する新しいクラスを定義します。
    # heejin_parkによる貢献、https://infograph.tistory.com/230から引用
    def construct(self):  # 主要なシーン構築メソッドを定義します。
        self.show_axis()  # 軸を表示するメソッドを呼び出します。
        self.show_circle()  # 単位円を表示するメソッドを呼び出します。
        self.move_dot_and_draw_curve()  # 点を動かして曲線を描画するメソッドを呼び出します。
        self.wait()  # アニメーションの最後に待機します。

    def show_axis(self):  # 軸を表示するメソッドを定義します。
        x_start = np.array([-6,0,0])  # X軸の開始点を設定します。
        x_end = np.array([6,0,0])  # X軸の終了点を設定します。
        y_start = np.array([-4,-2,0])  # Y軸の開始点を設定します（ここは間違っているかもしれません）。
        y_end = np.array([-4,2,0])  # Y軸の終了点を設定します。

        x_axis = Line(x_start, x_end)  # X軸をLineオブジェクトとして作成します。
        y_axis = Line(y_start, y_end)  # Y軸をLineオブジェクトとして作成します。
        self.add(x_axis, y_axis)  # 作成した軸をシーンに追加します。
        self.add_x_labels()  # X軸のラベルを追加するメソッドを呼び出します。

        self.origin_point = np.array([-4,0,0])  # 原点の位置を設定します。
        self.curve_start = np.array([-3,0,0])  # 曲線の開始位置を設定します。

    def add_x_labels(self):  # X軸のラベルを追加するメソッドを定義します。
        x_labels = [  # ラベルのリストを作成します。
            MathTex("\pi"), MathTex("2 \pi"),
            MathTex("3 \pi"), MathTex("4 \pi"),
        ]
        for i in range(len(x_labels)):  # ラベルを配置します。
            x_labels[i].next_to(np.array([-1 + 2*i, 0, 0]), DOWN)  # 各ラベルを適切な位置に配置します。
            self.add(x_labels[i])  # ラベルをシーンに追加します。

    def show_circle(self):  # 単位円を表示するメソッドを定義します。
        circle = Circle(radius=1)  # 単位円を作成します。
        circle.move_to(self.origin_point)  # 単位円を原点の位置に移動します。
        self.add(circle)  # 単位円をシーンに追加します。
        self.circle = circle  # 単位円をインスタンス変数に保持します。

    def move_dot_and_draw_curve(self):
        orbit = self.circle
        origin_point = self.origin_point

        dot = Dot(radius=0.08, color=YELLOW)
        dot.move_to(orbit.point_from_proportion(0))
        self.t_offset = 0
        rate = 0.25

        def go_around_circle(mob, dt):
            self.t_offset += (dt * rate)
            # print(self.t_offset)
            mob.move_to(orbit.point_from_proportion(self.t_offset % 1))

        def get_line_to_circle():
            return Line(origin_point, dot.get_center(), color=BLUE)

        def get_line_to_curve():
            x = self.curve_start[0] + self.t_offset * 4
            y = dot.get_center()[1]
            return Line(dot.get_center(), np.array([x,y,0]), color=YELLOW_A, stroke_width=2 )


        self.curve = VGroup()
        self.curve.add(Line(self.curve_start,self.curve_start))
        def get_curve():
            last_line = self.curve[-1]
            x = self.curve_start[0] + self.t_offset * 4
            y = dot.get_center()[1]
            new_line = Line(last_line.get_end(),np.array([x,y,0]), color=YELLOW_D)
            self.curve.add(new_line)

            return self.curve

        dot.add_updater(go_around_circle)

        origin_to_circle_line = always_redraw(get_line_to_circle)
        dot_to_curve_line = always_redraw(get_line_to_curve)
        sine_curve_line = always_redraw(get_curve)

        self.add(dot)
        self.add(orbit, origin_to_circle_line, dot_to_curve_line, sine_curve_line)
        self.wait(8.5)

        dot.remove_updater(go_around_circle)
