"""Runner configuration package.

This is used to load test runners from the configuration file.
Runner configuration is expected to be in the format:
{
    runner_name: {
        "exe": path to nuke,
        "args": [list of arguments for nuke]
    }
}
"""

from __future__ import annotations

import itertools
import json
from typing import TYPE_CHECKING

from nuke_test_runner.runner import Runner, RunnerException

if TYPE_CHECKING:
    from pathlib import Path


def load_runners(filepath: Path) -> dict[str, Runner]:
    """Load all runners specified in the config file.

    Notes:
        If the file does not exist, an empty dictionary will be returned.

    Args:
        filepath: the config filepath.

    Returns:
        dictionary of runner name and loaded runner.
    """
    if not filepath.exists():
        return {}

    data = json.loads(filepath.read_text())

    result = {}
    for name, config in data.items():
        try:
            result[name] = Runner(config["exe"], config["args"])
        except RunnerException as err:  # noqa: PERF203
            print(f"Skipping config '{name}' because of Error: {err}")  # noqa: T201

    return result


def find_configuration(start_path: Path) -> Path | None:
    """Find a configuration file that is part of the current test.

    This will return the first configuration that is found.
    It will traverse the directories up to find a "runners.json".

    Args:
        start_path: the starting directory/file where the search begins.

    Returns:
        The found "runners.json" or None.
    """
    path = start_path.parent if start_path.is_file() else start_path

    for parent in itertools.chain([path], path.parents):
        config = parent / "runners.json"
        if config.exists():
            return config

    return None
