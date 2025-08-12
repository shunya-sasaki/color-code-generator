"""This module, defines a class GradientColorGenerator.

GradientColorGenerator is used to generate gradient colors.
"""

from decimal import ROUND_HALF_UP
from decimal import Decimal

from ccg.models import Color


class GradientColorGenerator:
    """Class to generate gradient colors.

    Methods:
        grad_color: generate gradient color
            from the given color_name and ratio.
        grad_colors: generate gradient colors for all color names.
    """

    @classmethod
    def grad_color(
        cls, color: Color, ratio: float = 1.0, base_number: int = 500
    ) -> Color:
        """Generate gradient color from the given color_name and ratio.

        Args:
            color (Color): Base color object.
            ratio (float, optional): ratio of the gradient.
                Positive values generate lighter colors,
                negative values generate darker colors.
                1.0 means the color is white,
                -1.0 means the color is black.
                Defaults to 1.0.
            base_number (int): Base color number. Defaults to 500.

        Returns:
            Color: gradient color object.
        """
        r, g, b = color.rgb
        if ratio >= 0:
            delta_r = 255 - r
            delta_g = 255 - g
            delta_b = 255 - b
            grad_r = cls._round(r + delta_r * (ratio))
            grad_g = cls._round(g + delta_g * (ratio))
            grad_b = cls._round(b + delta_b * (ratio))
        else:
            delta_r = r
            delta_g = g
            delta_b = b
            grad_r = cls._round(r - delta_r * (-ratio))
            grad_g = cls._round(g - delta_g * (-ratio))
            grad_b = cls._round(b - delta_b * (-ratio))
        grad_color_name = cls._round((1 - ratio) * base_number)
        grad_color = Color(
            name=f"{color.name}-{grad_color_name}",
            rgb=(grad_r, grad_g, grad_b),
        )
        return grad_color

    @classmethod
    def grad_colors(
        cls,
        color: Color,
        ratios: list[float] = [
            -0.90,
            -0.80,
            -0.60,
            -0.40,
            -0.20,
            0.0,
            0.20,
            0.40,
            0.60,
            0.80,
            0.90,
        ],
        base_number: int = 500,
    ) -> list[Color]:
        """Generate light gradient colors for specified ratios.

        Args:
            color (Color): Base color object.
            ratios (float, optional): List of ratios for the gradient.
            base_number (int): Base color number. Defaults to 500.

        Returns:
            list[Color]: List of gradient color objects.
        """
        colors = [
            cls.grad_color(color, ratio, base_number) for ratio in ratios
        ]
        return colors

    @classmethod
    def multi_grad_colors(
        cls,
        colors: list[Color],
        ratios: list[float] = [
            -0.90,
            -0.80,
            -0.60,
            -0.40,
            -0.20,
            0.0,
            0.20,
            0.40,
            0.60,
            0.80,
            0.90,
        ],
        base_number: int = 500,
        exlude_color_names: list[str] = ["white", "black"],
    ) -> list[Color]:
        """Generate multiple gradient colors."""
        grad_colors = []
        for color in colors:
            if color.name in exlude_color_names:
                continue
            grad_colors.extend(cls.grad_colors(color, ratios, base_number))
        return grad_colors

    @classmethod
    def _round(cls, value) -> int:
        rounded_value = Decimal(value).quantize(
            Decimal("1"), rounding=ROUND_HALF_UP
        )
        return int(rounded_value)
