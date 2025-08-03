"""This module define Color."""

from __future__ import annotations

from typing import Any
from typing import ClassVar

from pydantic import BaseModel
from pydantic import ConfigDict

from ccg.utils import FormatConverter


class Color(BaseModel):
    """Color data model.

    Attributes:
        name (str): Name of the color.
        hex (str): Hexadecimal representation of the color.
        rgb (tuple[int, int, int]): RGB representation of the color.
    """

    model_config = ConfigDict(
        alias_generator=FormatConverter.snake_to_camel, populate_by_name=True
    )

    _DEFAULT_HEX: ClassVar[str] = ""
    _DEFAULT_RGB: ClassVar[tuple[int, int, int]] = (-1, -1, -1)

    name: str
    hex: str = _DEFAULT_HEX
    rgb: tuple[int, int, int] = _DEFAULT_RGB

    def model_post_init(self, context: Any) -> None:
        """Post-initialization."""
        super().model_post_init(context)
        if self.hex != self._DEFAULT_HEX and self.rgb != self._DEFAULT_RGB:
            raise ValueError("Either hex or rgb must be provided.")
        if self.hex != self._DEFAULT_HEX and self.hex[0] != "#":
            self.hex = "#" + self.hex
        if self.hex == self._DEFAULT_HEX and self.rgb != self._DEFAULT_RGB:
            r, g, b = self.rgb
            hex_r = f"{r:02x}"
            hex_g = f"{g:02x}"
            hex_b = f"{b:02x}"
            self.hex = f"#{hex_r}{hex_g}{hex_b}"
        elif self.hex != self._DEFAULT_HEX and self.rgb == self._DEFAULT_RGB:
            hex_r = self.hex[1:3]
            hex_g = self.hex[3:5]
            hex_b = self.hex[5:7]
            r = int(hex_r, 16)
            g = int(hex_g, 16)
            b = int(hex_b, 16)
            self.rgb = (r, g, b)
