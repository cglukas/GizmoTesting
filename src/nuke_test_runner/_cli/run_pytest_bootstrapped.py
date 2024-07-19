"""Script that gets executed by nuke to run tests.

This script will be run through the `Runner` class. It adds pytest to the available packages and executes
pytest with all provided arguments.
"""

# It is important here not to import anything package related,
# as this is not bootstrapped yet.

import argparse
import sys
from typing import NoReturn


def run_tests(packages_directory: str, test_directory: str, pytest_arguments: list[str]) -> NoReturn:
    """Run pytest with the provided arguments.

    Note:
        This function will exit the calling instance.

    Args:
        pytest_arguments:
    """
    sys.path.insert(packages_directory)
    import nuke_test_runner

    arguments = [test_directory]
    arguments.extend(pytest_arguments)
    sys.exit(nuke_test_runner.main(arguments))


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        prog="NukeTestBootstrapper",
        description="Internal CLI interface to wrap Nuke to run the tests.",
    )
    parser.add_argument("test_dir")
    parser.add_argument("packages_directory")
    parser.add_argument("pytest_args")
    args = parser.parse_args()

    run_tests(
        packages_directory=args.packages_directory, pytest_arguments=args.pytest_args, test_directory=args.test_dir
    )