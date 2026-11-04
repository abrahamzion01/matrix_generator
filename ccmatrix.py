
import argparse
import curses
import random
import string
import time


COLORS = {
    "green": curses.COLOR_GREEN,
    "red": curses.COLOR_RED,
    "blue": curses.COLOR_BLUE,
    "white": curses.COLOR_WHITE,
    "yellow": curses.COLOR_YELLOW,
    "cyan": curses.COLOR_CYAN,
    "magenta": curses.COLOR_MAGENTA,
    "black": curses.COLOR_BLACK,
}

RAINBOW = [
    "green", "red", "blue", "yellow",
    "cyan", "magenta", "white"
]


def get_characters(use_katakana):
    if use_katakana:
        return [chr(i) for i in range(0xFF66, 0xFF9E)]

    return string.ascii_letters + string.digits


def create_streams(width, height, base_delay):
    streams = []

    for column in range(width):
        streams.append({
            "column": column,
            "row": random.randint(-height, 0),
            "trail": [],
            "max_length": random.randint(5, 15),
            "interval": base_delay * random.uniform(0.6, 1.4),
            "next_move": time.monotonic() + random.uniform(0, 2),
        })

    return streams


def main(stdscr, args):
    curses.curs_set(0)
    stdscr.nodelay(True)
    stdscr.keypad(True)

    height, width = stdscr.getmaxyx()

    use_colors = curses.has_colors()

    if use_colors:
        curses.start_color()

        for number, name in enumerate(COLORS, start=1):
            curses.init_pair(
                number,
                COLORS[name],
                curses.COLOR_BLACK
            )

    color_numbers = {
        name: number
        for number, name in enumerate(COLORS, start=1)
    }

    delay_level = args.delay
    base_delay = 0.04 + delay_level * 0.04

    streams = create_streams(width, height, base_delay)

    characters = get_characters(args.katakana)

    rainbow_position = 0
    paused = False

    while True:
        now = time.monotonic()
        

        new_height, new_width = stdscr.getmaxyx()

        if new_height != height or new_width != width:
            height, width = new_height, new_width
            streams = create_streams(width, height, base_delay)

        key = stdscr.getch()
        if key == ord(" "):
            paused = not paused
            if key == ord("q"):
                break

        if paused:
            curses.napms(50)
            continue

        now = time.monotonic()

        if key == curses.KEY_RESIZE:
            continue

        if args.screensaver and key != -1:
            break

        if not args.screensaver and key == ord("q"):
            break

        if ord("0") <= key <= ord("9"):
            delay_level = int(chr(key))
            base_delay = 0.04 + delay_level * 0.04

            for stream in streams:
                stream["interval"] = (
                    base_delay * random.uniform(0.6, 1.4)
                )

        stdscr.erase()

        for stream in streams:
            if now >= stream["next_move"]:

                character = random.choice(characters)

                stream["trail"].append(
                    (stream["row"], character)
                )

                if len(stream["trail"]) > stream["max_length"]:
                    stream["trail"].pop(0)

                stream["row"] += 1

                stream["next_move"] = (
                    now + stream["interval"]
                )

                if stream["row"] > height + 10:
                    stream["row"] = random.randint(-height, 0)
                    stream["trail"] = []
                    stream["interval"] = (
                        base_delay * random.uniform(0.6, 1.4)
                    )

            trail = stream["trail"]
            column = stream["column"]

            for index, (trail_row, character) in enumerate(trail[:-1]):

                if not (0 <= trail_row < height):
                    continue

                if args.rainbow:
                    color_name = RAINBOW[
                        (index + rainbow_position) % len(RAINBOW)
                    ]
                else:
                    color_name = args.color

                if use_colors:
                    attribute = curses.color_pair(
                        color_numbers[color_name]
                    )
                    if args.bold:
                        attribute |= curses.A_BOLD

                    if index < 3:
                        attribute |= curses.A_BOLD
                    elif index >= 7:
                        attribute |= curses.A_DIM
                else:
                        attribute = curses.A_NORMAL
                try:
                    stdscr.addstr(
                        trail_row,
                        column,
                        character,
                        attribute
                    )
                except curses.error:
                    pass

            if trail:
                head_row, head_character = trail[-1]

                if 0 <= head_row < height:
                    attribute = (
                        curses.color_pair(color_numbers["white"])
                        if use_colors else curses.A_NORMAL
                    )
                    if args.bold:
                        attribute |= curses.A_BOLD

                    try:
                        stdscr.addstr(
                            head_row,
                            column,
                            head_character,
                            attribute
                        )
                    except curses.error:
                        pass

        stdscr.refresh()

        rainbow_position += 1

        curses.napms(30)


def parse_arguments():
    parser = argparse.ArgumentParser(
        description="Matrix Falling Text Generator"
    )

    parser.add_argument(
        "-s",
        "--screensaver",
        action="store_true",
        help="Exit when any key is pressed"
    )

    parser.add_argument(
        "-u",
        "--delay",
        type=int,
        choices=range(0, 11),
        default=4,
        help="Animation delay level from 0 to 10 (default: 4)"
    )

    color_group = parser.add_mutually_exclusive_group()

    color_group.add_argument(
        "-C",
        "--color",
        choices=COLORS.keys(),
        default="green",
        help="Choose the trail colour"
    )

    color_group.add_argument(
        "-r",
        "--rainbow",
        action="store_true",
        help="Enable rainbow trail colours"
    )

    parser.add_argument(
        "-c",
        "--katakana",
        action="store_true",
        help="Use half-width Katakana characters"
    )
    parser.add_argument(
    "-b",
    "--bold",
    action="store_true",
    help="Display bold falling characters"
    )

    return parser.parse_args()


if __name__ == "__main__":
    arguments = parse_arguments()

    try:
        curses.wrapper(main, arguments)
    except KeyboardInterrupt:
        pass
