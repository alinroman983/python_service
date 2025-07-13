#!/usr/bin/env python3
"""This script fetches weather information for a specified
location using the wttr.in service."""

import sys
import requests


def main():
    """Main fanction to fetch and display  weather information."""
    if len(sys.argv) == 2:
        location = sys.argv[1]
    else:
        print("Usage: python cli.py <location>")
        sys.exit(1)
    url = f"https://wttr.in/{location}"
    response = requests.get(url, timeout=10)
    print(response.text)


if __name__ == "__main__":
    main()
