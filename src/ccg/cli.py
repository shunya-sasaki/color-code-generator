"""Entry point for the CCG application."""

from argparse import ArgumentParser

from ccg import GradientColorGenerator
from ccg.exporter import CssExporter
from ccg.exporter import VsCodeCodeSnippetsExporter
from ccg.models import AppConfig


def run() -> None:
    """Run the CCG application."""
    parser = ArgumentParser(description="CCG Application")
    parser.add_argument(
        "--output",
        "-o",
        type=str,
        default="color",
        help="Output file name (without suffix).",
    )
    parser.add_argument(
        "--config",
        type=str,
        default="config.json",
        help="Path to the configuration file.",
    )
    parser.add_argument(
        "--without-css",
        action="store_true",
        default=False,
        help="Generate CSS file.",
    )
    parser.add_argument(
        "--without-vscode-snippets",
        action="store_true",
        default=False,
        help="Generate VS Code snippets file.",
    )

    args = parser.parse_args()
    config = AppConfig.from_jsonfile(args.config)
    default_colors = config.colors
    ratios = config.ratios

    grad_generator = GradientColorGenerator()
    grad_colors = grad_generator.multi_grad_colors(
        default_colors, ratios=ratios
    )
    for color in grad_colors:
        print(f"{color.name}: {color.hex}, {color.rgb}")
    output_colors = default_colors + grad_colors

    if not args.without_vscode_snippets:
        VsCodeCodeSnippetsExporter.export_to_file(
            output_colors, f"{args.output}.code-snippets"
        )
    if not args.without_css:
        CssExporter.export_to_file(output_colors, f"{args.output}.css")
