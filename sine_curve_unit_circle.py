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

    def move_dot_and_draw_curve(self): # 点を動かして曲線を描画するメソッドを定義します。
        orbit = self.circle # 単位円を軌道として設定します。
        origin_point = self.origin_point # 原点の位置を取得します。

        dot = Dot(radius=0.08, color=YELLOW) # 点を作成します。
        dot.move_to(orbit.point_from_proportion(0)) # 点を単位円の原点に移動します。
        self.t_offset = 0 # 時間オフセットを設定します。
        rate = 0.25 # レートを設定します。

        def go_around_circle(mob, dt): # 点を円周上を動かす関数を定義します。
            self.t_offset += (dt * rate) # 時間オフセットを更新します。
            # print(self.t_offset)
            mob.move_to(orbit.point_from_proportion(self.t_offset % 1)) # 点を円周上を動かします。

        def get_line_to_circle(): # 点と円の間の線を取得する関数を定義します。
            return Line(origin_point, dot.get_center(), color=BLUE) # 点と円の間の線を作成して返します。

        def get_line_to_curve(): # 点と曲線の間の線を取得する関数を定義します。
            x = self.curve_start[0] + self.t_offset * 4 # 線のX座標を計算します。
            y = dot.get_center()[1] # 線のY座標を計算します。
            return Line(dot.get_center(), np.array([x,y,0]), color=YELLOW_A, stroke_width=2 ) # 点と曲線の間の線を作成して返します。


        self.curve = VGroup() # 曲線を格納するVGroupを作成します。
        self.curve.add(Line(self.curve_start,self.curve_start)) # 曲線の開始点を追加します。
        def get_curve(): # 曲線を取得する関数を定義します。
            last_line = self.curve[-1] # 最後の線を取得します。
            x = self.curve_start[0] + self.t_offset * 4 # 線のX座標を計算します。
            y = dot.get_center()[1] # 線のY座標を計算します。
            new_line = Line(last_line.get_end(),np.array([x,y,0]), color=YELLOW_D) # 新しい線を作成します。
            self.curve.add(new_line) # 新しい線を曲線に追加します。

            return self.curve # 曲線を返します。

        dot.add_updater(go_around_circle) # 点を円周上を動かすアップデータを追加します。

        origin_to_circle_line = always_redraw(get_line_to_circle) # 原点と円の間の線を常に再描画します。
        dot_to_curve_line = always_redraw(get_line_to_curve) # 点と曲線の間の線を常に再描画します。
        sine_curve_line = always_redraw(get_curve) # 曲線を常に再描画します。

        self.add(dot) # 点をシーンに追加します。
        self.add(orbit, origin_to_circle_line, dot_to_curve_line, sine_curve_line) # 軌道、線、曲線をシーンに追加します。
        self.wait(8.5) # 8.5秒間待機します。

        dot.remove_updater(go_around_circle) # 点のアップデータを削除します。
