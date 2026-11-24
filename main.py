#!/usr/bin/env python3
"""Charm the Commuter: Forecast a City That Isn't.

Writes one line of weather for the invented city Breezewick
to /output/entry.txt. Stdlib only, deterministic, no network,
no files read, no environment secrets.

The forecast is assembled from its broadcast parts so the
structure of a real forecast stays visible in the code:
place + day, the fair-weather lead, then the commuter's punchline.
"""

from pathlib import Path

# Broadcast parts, in spoken order.
CITY = "Breezewick"
LEAD = "sunny spells, a 40% chance of rain"
PUNCHLINE = "a 100% chance the bus is late again"

OUTPUT_PATH = Path("/output/entry.txt")


def build_entry() -> str:
    """Return the single forecast line for Breezewick."""
    return f"In {CITY} today: {LEAD}, and {PUNCHLINE}."


def write_entry(path: Path = OUTPUT_PATH) -> Path:
    """Write the forecast line plus a trailing newline, deterministically."""
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(build_entry() + "\n", encoding="utf-8", newline="\n")
    return path


def main() -> None:
    write_entry()


if __name__ == "__main__":
    main()
