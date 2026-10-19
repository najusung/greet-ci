"""Command-line greeting program."""

import sys


def greet(name: str) -> str:
    """Return a greeting for the given name."""
    return f"Hello, {name}!"


def main(argv: list[str] | None = None) -> None:
    """Print a greeting using the first command-line argument."""
    args = sys.argv[1:] if argv is None else argv
    name = args[0] if args else "world"
    print(greet(name))


def test_greet() -> None:
    assert greet("Hee") == "Hello, Hee!"


if __name__ == "__main__":
    main()
