"""
Greet a person on the command line with a message.

@author: Jannik Stebani
"""
import argparse
import random

from typing import TypeAlias 

from rich.console import Console
from rich.panel import Panel
from rich.text import Text
from rich.align import Align
from rich.padding import Padding

Message: TypeAlias = str

def cli() -> argparse.ArgumentParser:
    """
    CLI parser for greeting a person with different styles.
    """
    parser = argparse.ArgumentParser(description="Greet a person.")
    parser.add_argument(
        'style', type=str, choices=['plain', 'ornamental', 'fancy'], default='plain',
        help='Set the style of the greeting'
    )
    parser.add_argument('name', type=str, help='Name of the person to greet')
    return parser


def perform_plain_greeting(name: str) -> None:
    """
    Plainly greet a person with a message.

    Parameters
    ----------
    name : str
        Name of the person to greet.

    Returns
    -------
    None
        This function prints a simple greeting message to the console.
    """
    message: str = f'Hello, {name}!'
    print(message)


def perform_ornamental_greeting(name: str) -> None:
    """
    Perform an ornamental greeting.
    
    Parameters
    ----------
    name : str
        Name of the person to greet.

    Returns
    -------
    None
        This function prints a decorative greeting message to the console.
    """
    console = Console()
    
    # Create the main greeting text with styling
    greeting_text = Text()
    greeting_text.append('✨ Welcome, ', style='bold magenta')
    greeting_text.append(name, style='bold gold1')
    greeting_text.append(' ✨', style='bold magenta')
    
    # Create a subtitle with decorative elements
    subtitle = Text()
    subtitle.append('🌟 ', style='yellow')
    subtitle.append('May your day be filled with joy and wonder', style='italic cyan')
    subtitle.append(' 🌟', style='yellow')
    
    # Combine greeting and subtitle with proper spacing
    content = Text()
    content.append(greeting_text)
    content.append('\n\n')
    content.append(subtitle)
    
    centered_content = Align.center(content)
    padded_content = Padding(centered_content, (1, 2))
    
    panel = Panel(
        padded_content,
        title='🎉 Greetings 🎉',
        title_align='center',
        border_style='bright_blue',
        padding=(0, 1),
        expand=False
    )
    # Print the ornamental greeting
    console.print()
    console.print(panel)
    console.print()


def perform_fancy_greeting(name: str) -> None:
    """
    Alternative version with more elaborate styling and random elements.
    
    Parameters
    ----------
    name : str
        Name of the person to greet.

    Returns
    -------
    None
        This function prints a fancy greeting message to the console.
    """
    console = Console()
    decorations = ['✨', '🌟', '💫', '⭐', '🎆', '🎇', '✴️', '🔆']
    colors = ['red', 'green', 'blue', 'magenta', 'cyan', 'yellow', 'bright_red', 'bright_green']
    
    # Select random elements
    decoration = random.choice(decorations)
    color = random.choice(colors)
    
    # Create ornate greeting
    greeting = Text()
    greeting.append(f'{decoration} ', style=f'bold {color}')
    greeting.append('Greetings and Salutations Fellow Scientist', style='bold white')
    greeting.append(f' {decoration}\n', style=f'bold {color}')
    greeting.append(f'Dear {name}', style=f'bold {color}')
    
    # Create decorative message
    message = Text()
    message.append('━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━', style='dim white')
    message.append('\n')
    message.append('Welcome to this moment of Pytorial in 2025!\n', style='italic bright_cyan')
    message.append('Live long and prosper 🖖!', style='italic bright_cyan')
    message.append('\n')
    message.append('━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━', style='dim white')
    
    # Combine content
    full_content = Text()
    full_content.append(greeting)
    full_content.append('\n\n')
    full_content.append(message)
    
    # Create panel with dynamic styling
    panel = Panel(
        Align.center(full_content),
        title=f'{decoration} Ornamental Greeting {decoration}',
        title_align='center',
        border_style=color,
        padding=(1, 2),
        expand=False
    )
    
    console.print()
    console.print(panel)
    console.print()


def greet() -> None:
    parser = cli()
    args = parser.parse_args()
    name = args.name.strip()
    if args.style == 'plain':
        perform_plain_greeting(name)
    elif args.style == 'ornamental':
        perform_ornamental_greeting(name)
    elif args.style == 'fancy':
        perform_fancy_greeting(name)
    else:
        parser.print_help()
        raise ValueError(
            f'Unknown style: {args.style}. Please choose \'plain\', \'rich\', or \'fancy\'.'
        )