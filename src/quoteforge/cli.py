#!/usr/bin/env python3
import json, click
from pathlib import Path
from rich.console import Console
from .calc import build_quote, render_text
console = Console()
@click.group()
@click.version_option()
def main(): pass
@main.command()
@click.argument('file')
@click.option('--tax', default=0.0, type=float)
@click.option('--discount', default=0.0, type=float)
@click.option('--title', default='Quote')
def build(file, tax, discount, title):
    items = json.loads(Path(file).read_text())
    q = build_quote(items, tax, discount)
    console.print(render_text(q, title))
if __name__ == '__main__': main()
