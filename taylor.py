# manim -p -ql taylor.py TaylorSeriesSin

from manim import *
import math

class TaylorSeriesSin(Scene):
    def construct(self):
        # Taylor series for sin(x) up to the n-th term
        def taylor_series_sin(x, n):
            terms = [
                (-1)**k * x**(2*k+1) / math.factorial(2*k+1) for k in range(n)
            ]
            return sum(terms)

        # Set up the axes
        axes = Axes(
            x_range=[-2 * math.pi, 2 * math.pi, math.pi],  # x軸の範囲を-2πから2πに設定
            y_range=[-1.5, 1.5, 0.5],
            axis_config={"color": BLUE}
        )

        # Labels for the axes
        x_label = axes.get_x_axis_label("x")
        y_label = axes.get_y_axis_label("y")

        # Plot the sin(x) function
        sin_graph = axes.plot(lambda x: math.sin(x), color=RED, use_smoothing=True)

        # Plot the Taylor series terms
        first_term_graph = axes.plot(lambda x: taylor_series_sin(x, 1), color=GREEN)
        first_two_terms_graph = axes.plot(lambda x: taylor_series_sin(x, 2), color=YELLOW)
        first_three_terms_graph = axes.plot(lambda x: taylor_series_sin(x, 3), color=ORANGE)
        first_four_terms_graph = axes.plot(lambda x: taylor_series_sin(x, 4), color=PURPLE)
        first_five_terms_graph = axes.plot(lambda x: taylor_series_sin(x, 5), color=PINK)
        first_six_terms_graph = axes.plot(lambda x: taylor_series_sin(x, 6), color=BLUE)
        first_seven_terms_graph = axes.plot(lambda x: taylor_series_sin(x, 7), color=MAROON)
        first_eight_terms_graph = axes.plot(lambda x: taylor_series_sin(x, 8), color=TEAL)
        first_nine_terms_graph = axes.plot(lambda x: taylor_series_sin(x, 9), color=GOLD)

        # Add the axes and the sin(x) graph
        self.play(Create(axes), Create(sin_graph), Write(x_label), Write(y_label))
        self.wait(2)

        # Add the first term graph
        self.play(Create(first_term_graph))
        self.wait(2)

        # Add the first two terms graph
        self.play(Transform(first_term_graph, first_two_terms_graph))
        self.wait(2)

        # Add the first three terms graph
        self.play(Transform(first_term_graph, first_three_terms_graph))
        self.wait(2)

        # Add the first four terms graph
        self.play(Transform(first_term_graph, first_four_terms_graph))
        self.wait(2)

        # Add the first five terms graph
        self.play(Transform(first_term_graph, first_five_terms_graph))
        self.wait(2)

        # Add the first six terms graph
        self.play(Transform(first_term_graph, first_six_terms_graph))
        self.wait(2)

        # Add the first seven terms graph
        self.play(Transform(first_term_graph, first_seven_terms_graph))
        self.wait(2)

        # Add the first eight terms graph
        self.play(Transform(first_term_graph, first_eight_terms_graph))
        self.wait(2)

        # Add the first nine terms graph
        self.play(Transform(first_term_graph, first_nine_terms_graph))
        self.wait(2)

        # Keep the final graph on screen for a while
        self.wait(2)