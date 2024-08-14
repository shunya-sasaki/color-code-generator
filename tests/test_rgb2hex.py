from ccg.hexcolor import HEX_COLORS
from ccg.rgbcolor import RGB_COLORS


class TestRgb2Hex:

    def test_rgb2hex(self):
        for (rgb_name, rgb_values), (hex_name, hex_value) in zip(
            RGB_COLORS.items(), HEX_COLORS.items()
        ):
            assert rgb_name == hex_name
            r, g, b = rgb_values
            hex_code = f"#{r:02x}{g:02x}{b:02x}"
            assert hex_code == hex_value
