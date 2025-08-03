"""This module define VsCodeCodeSnippetsExporter class."""

import json

from ccg.exporter.exporter import Exporter
from ccg.models import Color


class VsCodeCodeSnippetsExporter(Exporter):
    """Export color data to VS Code code snippets format."""

    def export_to_file(self, colors: list[Color], file_name: str) -> None:
        """Export color data to a VS Code code snippets file.

        Args:
            file_name (str): The name of the file to export to.
            colors (Color): A list of Color objects to export.
        """
        dict_out = {}
        for color in colors:
            dict_out = {
                color.name: {
                    "prefix": f"hex-{color.name}",
                    "body": color.hex,
                    "description": f"Color {color.name} in hex format.",
                }
            }
        with open(file_name, "w", encoding="utf-8") as fout:
            json.dump(dict_out, fout, indent=2)
