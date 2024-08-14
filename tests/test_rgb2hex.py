from ccg.hexcolor import HEX_COLORS
from ccg.rgbcolor import RGB_COLORS


class TestRgb2Hex:

    def test_rgb2hex(self):
        for rgb, hex_target in zip(RGB_COLORS, HEX_COLORS):
            r, g, b = rgb
            hex_code = f"#{r:02x}{g:02x}{b:02x}"
            assert rgb.rgb2hex() == hex_code
