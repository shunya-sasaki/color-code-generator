from typing import Literal, Tuple
from ccg.rgbcolor import RGB_COLORS


class GradientColorGenerator:

    def grad_color(
        self,
        color_name: Literal[
            "primary-gray",
            "accent",
            "white",
            "black",
            "dark-yellow",
            "light-yellow",
            "dark-blue",
            "middle-blue",
            "light-blue",
            "dark-green",
            "light-green",
            "dark-purple",
            "light-purple",
            "gray",
            "dark-blue-gray1",
            "dark-blue-gray2",
            "dark-blue-gray3",
        ] = "primary-gray",
        ratio: float = 1.0,
        return_type: Literal["rgb", "hex"] = "rgb",
    ) -> Tuple[int, int, int] | str:
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
