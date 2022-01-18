from rich.console import Console
from rich.theme import Theme

default_theme = Theme.read('theme.txt')

console = Console(theme=default_theme)