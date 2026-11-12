COLOURS = {
    "green": "\033[92m",
    "blue": "\033[94m",
    "red": "\033[91m",
    "orange": "\033[38;5;208m",
    "yellow": "\033[93m",
    "cyan": "\033[96m",
    "purple": "\033[38;5;93m",
    "brown": "\033[38;5;94m",
    "gold": "\033[38;5;220m",
    "lime": "\033[38;5;46m",
    "magenta": "\033[95m",
    "reset": "\033[0m",
    "crimson": "\033[38;2;220;20;60m",
    "darkred": "\033[38;2;139;0;0m",
    "violet": "\033[38;2;143;0;255m",
}

RAINBOW = [
    "\033[91m",
    "\033[38;5;208m",
    "\033[93m",
    "\033[92m",
    "\033[96m",
    "\033[94m",
    "\033[95m"
]


def draw_rainbow(text: str) -> str:
    coloreated_chars: str = ""
    for i, char in enumerate(text):
        color_ansi = RAINBOW[i % len(RAINBOW)]
        coloreated_chars += f"{color_ansi}{char}{COLOURS['reset']}"
    return coloreated_chars
