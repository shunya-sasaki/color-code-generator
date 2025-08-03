"""This module define an abstract class Exporter."""

from abc import ABC
from abc import abstractmethod

from ccg.models import Color


class Exporter(ABC):
    """Abstract class to export color data to a file."""

    @abstractmethod
    def export_to_file(self, colors: list[Color], file_name: str) -> None:
        """Export color data to a file.

        Args:
            file_name (str): The name of the file to export to.
            colors (Color): A list of Color objects to export.
        """
        pass
