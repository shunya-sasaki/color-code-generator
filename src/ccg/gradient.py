"""In this module, we define a class GradientColorGenerator
to generate gradient colors.
"""

from typing import Literal
from typing import Tuple
from ccg.rgbcolor import RGB_COLORS


class GradientColorGenerator:
    """Class to generate gradient colors.

    Methods:
        grad_color: generate gradient color
            from the given color_name and ratio.
        grad_colors: generate gradient colors for all color names.
    """

    def grad_color(
        self,
        color_name: str = "primary-gray",
        ratio: float = 1.0,
        return_type: Literal["rgb", "hex"] = "rgb",
    ) -> Tuple[int, int, int] | str:
        """generate gradient color from the given color_name and ratio.

        Args:
            color_name (str, optional): color name.
                Defaults to "primary-gray".
            ratio (float, optional): ratio of the gradient color.
                Defaults to 1.0.
            return_type (Literal["rgb", "hex"], optional): return type.
                Defaults to "rgb".
        Returns:
            Tuple[int, int, int] | str: gradient color.
        """
        r, g, b = RGB_COLORS[color_name]
        delta_r = 255 - r
        delta_g = 255 - g
        delta_b = 255 - b
        grad_r = int(r + delta_r * (1 - ratio))
        grad_g = int(g + delta_g * (1 - ratio))
        grad_b = int(b + delta_b * (1 - ratio))
        match return_type:
            case "rgb":
                return grad_r, grad_g, grad_b
            case "hex":
                return f"#{grad_r:02x}{grad_g:02x}{grad_b:02x}"
            case _:
                raise ValueError("return_type must be either 'rgb' or 'hex'.")

    def grad_colors(self, return_type: Literal["rgb", "hex"] = "rgb"):
        """generate gradient colors for all color names

        Args:
            return_type (Literal["rgb", "hex"], optional): return type.
                Defaults to "rgb".
        """
        dict_colors: dict[str, str | tuple[int, int, int]] = {}
        ratios = [0.2, 0.4, 0.6, 0.8, 1.0]
        n_ratio = len(ratios)
        for color_name in RGB_COLORS.keys():
            for i_ratio, ratio in enumerate(ratios):
                dict_colors[f"{color_name}-{int(ratio*100):02d}"] = (
                    self.grad_color(
                        color_name=color_name,
                        ratio=ratio,
                        return_type=return_type,
                    )
                )
                if i_ratio == n_ratio - 1:
                    dict_colors[color_name] = dict_colors[f"{color_name}-100"]
        return dict_colors
