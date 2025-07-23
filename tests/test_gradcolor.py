import pytest
from ccg.gradient import GradientColorGenerator
from ccg.rgbcolor import RGB_COLORS
from ccg.hexcolor import HEX_COLORS


class TestGradientColorGenerator:

    def test_grad_color_rgb(self):
        generator = GradientColorGenerator()
        for color_name, rgb_values in RGB_COLORS.items():
            r_target, g_target, b_target = rgb_values
            r, g, b = generator.grad_color(color_name, ratio=1.0)
            assert r == r_target
            assert g == g_target
            assert b == b_target

    def test_grad_color_hex(self):
        generator = GradientColorGenerator()
        for color_name, hex_target in HEX_COLORS.items():
            hex_value = generator.grad_color(
                color_name, ratio=1.0, return_type="hex"
            )
            assert hex_value == hex_target

    def test_grad_color_rgb_white(self):
        generator = GradientColorGenerator()
        for color_name in RGB_COLORS.keys():
            r, g, b = generator.grad_color(color_name, ratio=0)
            assert r == 255
            assert g == 255
            assert b == 255

    def test_grad_color_hex_white(self):
        generator = GradientColorGenerator()
        for color_name in HEX_COLORS.keys():
            hex_value = generator.grad_color(
                color_name, ratio=0, return_type="hex"
            )
            assert hex_value == "#ffffff"

    def test_grad_color_value_error(self):
        with pytest.raises(ValueError):
            generator = GradientColorGenerator()
            generator.grad_color("primary-gray", return_type="rgb")
            
