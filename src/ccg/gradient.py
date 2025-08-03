"""This module, defines a class GradientColorGenerator.

GradientColorGenerator is used to generate gradient colors.
"""

from typing import Literal
from typing import Tuple

from ccg.models import Color
from ccg.rgbcolor import RGB_COLORS


class GradientColorGenerator:
    """Class to generate gradient colors.

    Methods:
        grad_color: generate gradient color
            from the given color_name and ratio.
        grad_colors: generate gradient colors for all color names.
    """

    @classmethod
    def grad_color(cls, color: Color, ratio: float = 1.0) -> Color:
        """Generate gradient color from the given color_name and ratio.

        Args:
            color (Color): Base color object.
            ratio (float, optional): ratio of the gradient.
                Defaults to 1.0.

        Returns:
            Color: gradient color object.
        """
        r, g, b = color.rgb
        delta_r = 255 - r
        delta_g = 255 - g
        delta_b = 255 - b
        grad_r = int(r + delta_r * (1 - ratio))
        grad_g = int(g + delta_g * (1 - ratio))
        grad_b = int(b + delta_b * (1 - ratio))
        grad_color = Color(
            name=f"{color.name}-{int((1 - ratio) * 100)}",
            rgb=(grad_r, grad_g, grad_b),
        )
        return grad_color

    @classmethod
    def grad_colors(
        cls,
        color: Color,
        ratios: list[float] = [0.2, 0.4, 0.6, 0.8],
    ) -> list[Color]:
        """Generate light gradient colors for specified ratios.

        Args:
            color (Color): Base color object.
            ratios (float, optional): List of ratios for the gradient.
                Defaults to [0.2, 0.4, 0.6, 0.8].

        Returns:
            list[Color]: List of gradient color objects.
        """
        colors = [cls.grad_color(color, ratio) for ratio in ratios]
        return colors
