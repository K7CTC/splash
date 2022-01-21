import time
from console import console
from rich.text import Text

def move(r, c):
    print(f'\033[{r};{c}H', end='')

def logo_generator(shade):
    logo = [
        f'[grey{shade}]╭─────────╮  ╭─╮  ╭─────────╮  ╭─────────╮  ╭─────────╮[/]',
        f'[grey{shade}]╰──────╮  │  ╰─╯  ╰─────────╯  ╰──────╮  │  │ ╭───────╯[/]',
        f'[grey{shade}]╭──────╯  │  ╭─╮  ╭───────╮    ╭──────╯  │  │ ╰───────╮[/]',
        f'[grey{shade}]│ ╭───────╯  │ │  │ ╭─────╯    │ ╭────╮  ⎨  ╰──────╮  │[/]',
        f'[grey{shade}]│ │          │ │  │ ╰───────╮  │ │    │  │  ╭──────╯  │[/]',
        f'[grey{shade}]╰─╯          ╰─╯  ╰─────────╯  ╰─╯    ╰──╯  ╰─────────╯[/]'
    ]
    return logo

def header(title):
    #console.print(f'[header1] [header3]≡[/] {title}[/][header2]█▉▊▋▌▍▎▏[/]')

    console.print(f' ≣ {title} ❱❯❭ ')


def frame():
    console.print('[bright_cyan]┎[/][bright_blue]──[/][blue]────────────────────── ─── ── ─ ─  ─[/]')
    console.print('[bright_blue]┃[/]')
    console.print('[blue]┃[/]')
    console.print('[blue]│[/]')
    console.print('[blue]│[/]')
    console.print('[blue]│[/]')
    console.print('[blue]│[/]')
    console.print('[blue]│[/]')
    console.print('[blue]│[/]')
    console.print('[blue]│[/]')
    console.print('[blue]│[/]')
    console.print('[blue]│[/]')
    console.print('[blue]│[/]')
    console.print('[blue]│[/]')
    console.print()
    console.print('[blue]│[/]')
    console.print()
    console.print()
    console.print('[blue]│[/]')
    console.print()
    console.print()
    console.print()
    #console.print("[header1] This is the footer                                                      Status [/]")
    console.print('[bright_cyan]─[/][bright_blue]─[/][blue]─[[/][white] 105[/][bright_blue] of [/][white]200 [/][blue]]────────────────────────────────────────────────────[[/][white]  53[/][bright_blue]% [/][blue]]─[/][bright_blue]─[/][bright_cyan]─[/]')


    # print('\033[3;3H', end='')
    # console.print('Canvas Course ID................................[999999]', end='')

    # print('\033[4;3H', end='')
    # console.print('Canvas Course Name..............................[Spring 2022 ADVS-2120-AB1 XL]', end='')

    # print('\033[5;3H', end='')
    # console.print('LTI Context ID Exists...........................[TRUE]', end='')

    # # print('\033[6;3H', end='')
    # # console.print(This is a test', end='')

    # print('\033[7;3H', end='')
    # console.print('Instructor A Number.............................[A01234567]', end='')

    # print('\033[8;3H', end='')
    # console.print('Instructor Name.................................[John Jhonson]', end='')

    # # print('\033[9;3H', end='')
    # # console.print('This is a test', end='')

    # print('\033[10;3H', end='')
    # console.print('Facilitator A Number............................[A76543210]', end='')

    # print('\033[11;3H', end='')
    # console.print('Facilitator Name................................[Johnson JoHanssen]', end='')

    # # print('\033[12;3H', end='')
    # # console.print('This is a test', end='')

    # print('\033[13;3H', end='')
    # console.print('Zoom Meeting ID.................................[98564571524526]', end='')

    # # print('\033[14;3H', end='')
    # # console.print('This is a test', end='')

    # print('\033[1;1H', end='')