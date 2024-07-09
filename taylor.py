# manim -p -ql taylor.py TaylorSeriesSin

from manim import *
import math

class TaylorSeriesSin(Scene):
    def construct(self):
        # Define the Taylor series terms for sin(x)
        def taylor_series_sin(x, n):
            terms = [
                (-1)**k * x**(2*k+1) / math.factorial(2*k+1) for k in range(n)
            ]
            return sum(terms)

        # Set up the axes
        axes = Axes(
            x_range=[-3.5, 3.5, 1],
            y_range=[-1.5, 1.5, 0.5],
            axis_config={"color": BLUE}
        )

        # Labels for the axes
        x_label = axes.get_x_axis_label("x")
        y_label = axes.get_y_axis_label("y")

        # Plot the sin(x) function
        sin_graph = axes.plot(lambda x: math.sin(x), color=RED, use_smoothing=True)

        # Plot the first term of the Taylor series
        first_term_graph = axes.plot(lambda x: taylor_series_sin(x, 1), color=GREEN)

        # Plot the first two terms of the Taylor series
        first_two_terms_graph = axes.plot(lambda x: taylor_series_sin(x, 2), color=YELLOW)

        # Plot the first three terms of the Taylor series
        first_three_terms_graph = axes.plot(lambda x: taylor_series_sin(x, 3), color=ORANGE)

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

        # Keep the final graph on screen for a while
        self.wait(2)