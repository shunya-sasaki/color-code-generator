"""This module defines a class CssExporter."""

from ccg.exporter.exporter import Exporter
from ccg.models import Color


class CssExporter(Exporter):
    """Export color data to CSS format."""

    @classmethod
    def export_to_file(
        cls, colors: list[Color], file_name: str = "colors.css"
    ) -> None:
        """Export color data to a CSS file.

        Args:
            file_name (str): The name of the file to export to.
            colors (list[Color]): A list of Color objects to export.
        """
        with open(file_name, "w", encoding="utf-8") as fout:
            fout.write(":root {\n")
            for color in colors:
                fout.write(f"  --{color.name}: {color.hex};\n")
            fout.write("}")
