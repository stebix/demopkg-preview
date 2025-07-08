"""
Demonstration of console spinners using Rich for the FhG Pytorial.

@author: Jannik Stebani
"""
from time import sleep
from rich.console import Group
from rich.live import Live
from rich.text import Text
from rich.spinner import Spinner, SPINNERS

def spinner() -> None:
    """
    Demonstration of various spinners using Rich.
    """
    all_spinners = Group(
        *[
            Spinner(spinner_name, text=Text(repr(spinner_name), style="green"))
            for spinner_name in sorted(SPINNERS.keys())
        ]
    )
    with Live(all_spinners, refresh_per_second=20):
        while True:
            sleep(0.1)