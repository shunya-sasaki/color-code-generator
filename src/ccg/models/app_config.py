"""Application configuration model."""

from __future__ import annotations

import json
from pathlib import Path
from typing import Literal

from pydantic import BaseModel
from pydantic import ConfigDict

from ccg.models.color import Color
from ccg.utils import FormatConverter


class AppConfig(BaseModel):
    """Application configuration model.

    Args:
        colors (list[Color]): List of color object.
            Each color object contains the name, hex or rgb.
        ratios (list[float]): List of ratios for generating gradient colors.
        log_level (Literal["debug", "info", "warning", "error"]):
            Logging level for the application.
    """

    model_config = ConfigDict(
        alias_generator=FormatConverter.snake_to_camel, populate_by_name=True
    )
    colors: list[Color] = [
        Color(name="white", hex="#ffffff"),
        Color(name="black", hex="#000000"),
        Color(name="red", hex="#ff0000"),
        Color(name="green", hex="#00ff00"),
        Color(name="blue", hex="#0000ff"),
    ]
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
    ]

    log_level: Literal["debug", "info", "warning", "error"] = "info"

    @classmethod
    def from_json(cls, config_json: dict) -> AppConfig:
        """Create an AppConfig instance from a JSON dictionary."""
        config = AppConfig.model_validate(config_json)
        return config

    @classmethod
    def from_jsonfile(cls, config_file: str) -> AppConfig:
        """Create an AppConfig instance from a JSON file."""
        if not Path(config_file).exists():
            raise FileNotFoundError(
                f"Configuration file {config_file} not found."
            )
        with open(config_file, "r") as file:
            config_json = json.load(file)
        return cls.from_json(config_json)

    def to_jsonfile(self, config_file: str = "config.json") -> None:
        """Save the AppConfig instance to a JSON file."""
        json_str = self.model_dump_json(indent=2, by_alias=True)
        with open(config_file, "w") as fout:
            fout.write(json_str)
