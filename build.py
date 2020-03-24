#!/usr/bin/env python3
import subprocess
from pathlib import Path

FILENAME = "README.md"
TEMPLATE_ARG = "--template=template.html"


def build(infile: Path):
    directory: Path = infile.parent
    outfile = directory / "index.html"
    command = ["pandoc", "-s", str(infile), "-o", str(outfile), TEMPLATE_ARG]
    subprocess.run(command)
    print(f"{infile} -> {directory}/")


for path in Path(".").rglob("README.md"):
    build(path)
