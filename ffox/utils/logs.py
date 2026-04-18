import base64
import time

import colorama

from ffox.settings import DEBUG


def present_request(res, filter: list = [], tabs: int = 0):
    for key in res:
        if key in filter or not filter:
            if type(res[key]) is list:
                for elem in res[key]:
                    present_request(elem, tabs=tabs + 1)
            else:
                show(
                    "  " * tabs
                    + f"• {key}: {res[key] if key not in ['disk_path', 'path'] else base64.b64decode(res[key]).decode()}"
                )


def debug(text: str):
    if DEBUG:
        print(f"[{time.time()}] {text}")


def show(text: str):
    print(f"{colorama.Style.BRIGHT}{text}{colorama.Style.RESET_ALL}")


def log(text: str):
    print(f"[{time.time()}] {text}")


def warn(text: str):
    print(f"{colorama.Fore.YELLOW}{text}{colorama.Style.RESET_ALL}")


def error(text: str):
    print(f"{colorama.Fore.RED}{text}{colorama.Style.RESET_ALL}")


def success(text: str):
    print(f"{colorama.Fore.GREEN}{text}{colorama.Style.RESET_ALL}")


def secondary(text: str):
    print(f"{colorama.Style.DIM} | {text}{colorama.Style.RESET_ALL}")


def critical(text: str, code: int = 1):
    print(f"{colorama.Back.RED}{text}{colorama.Style.RESET_ALL}")
    exit(code)
