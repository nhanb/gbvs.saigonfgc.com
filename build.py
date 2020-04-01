#!/usr/bin/env python3
import subprocess
from pathlib import Path

FILENAME = "index.md"
TEMPLATE_ARG = "--template=template.html"
VNDATE_FILTER_ARG = "--lua-filter=./filters/vndate.lua"


def build(infile: Path):
    directory: Path = infile.parent
    outfile = directory / "index.html"
    command = [
        "pandoc",
        "-s",
        str(infile),
        "-o",
        str(outfile),
        TEMPLATE_ARG,
        VNDATE_FILTER_ARG,
    ]
    subprocess.run(command)
    print(f"{infile} -> {directory}/")


for path in Path(".").rglob(FILENAME):
    build(path)
