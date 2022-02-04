from operator import ne
import time
from console import console

def cursor_move(row, column):
    print(f'\033[{row};{column}H', end='')

def cursor_home():
    print(f'\033[H', end='\r')

def splash():
    console.clear()

    cursor_move(15,27)
    console.print('[grey70]C h r i s    C l e m e n t[/]')
    cursor_home()
    
    callsign_elements = [
        '▰▰   ▰▰',
        '▰▰  ▰▰ ',
        '▰▰▰▰▰',
        '▰▰▰▰▰▰▰',
        '▰    ▰▰',
        '    ▰▰',
        '   ▰▰',
        ' ▰▰▰▰▰▰',
        '▰▰',
        '▰▰▰▰▰▰▰▰',
        '   ▰▰'
    ]
    
    frame_delay = .03

    #K
    cursor_move(9, 16)
    console.print(callsign_elements[0], style='color(26)')
    cursor_home()
    time.sleep(frame_delay)
    cursor_move(10, 16)
    console.print(callsign_elements[1], style='color(32)')
    cursor_home()
    time.sleep(frame_delay)
    cursor_move(11, 16)
    console.print(callsign_elements[2], style='color(38)')
    cursor_home()
    time.sleep(frame_delay)
    cursor_move(12, 16)
    console.print(callsign_elements[1], style='color(32)')
    cursor_home()
    time.sleep(frame_delay)
    cursor_move(13, 16)
    console.print(callsign_elements[0], style='color(26)')
    cursor_home()
    time.sleep(frame_delay)
    
    #7
    cursor_move(13, 26)
    console.print(callsign_elements[6], style='color(26)')
    cursor_home()
    time.sleep(frame_delay)
    cursor_move(12, 26)
    console.print(callsign_elements[6], style='color(32)')
    cursor_home()
    time.sleep(frame_delay)
    cursor_move(11, 26)
    console.print(callsign_elements[5], style='color(38)')
    cursor_home()
    time.sleep(frame_delay)
    cursor_move(10, 26)
    console.print(callsign_elements[4], style='color(32)')
    cursor_home()
    time.sleep(frame_delay)
    cursor_move(9, 26)
    console.print(callsign_elements[3], style='color(26)')
    cursor_home()
    time.sleep(frame_delay)
    
    #C
    cursor_move(9, 36)
    console.print(callsign_elements[7], style='color(26)')
    cursor_home()
    time.sleep(frame_delay)
    cursor_move(10, 36)
    console.print(callsign_elements[8], style='color(32)')
    cursor_home()
    time.sleep(frame_delay)
    cursor_move(11, 36)
    console.print(callsign_elements[8], style='color(38)')
    cursor_home()
    time.sleep(frame_delay)
    cursor_move(12, 36)
    console.print(callsign_elements[8], style='color(32)')
    cursor_home()
    time.sleep(frame_delay)
    cursor_move(13, 36)
    console.print(callsign_elements[7], style='color(26)')
    cursor_home()
    time.sleep(frame_delay)
    
    #T
    cursor_move(13, 46)
    console.print(callsign_elements[10], style='color(26)')
    cursor_home()
    time.sleep(frame_delay)
    cursor_move(12, 46)
    console.print(callsign_elements[10], style='color(32)')
    cursor_home()
    time.sleep(frame_delay)
    cursor_move(11, 46)
    console.print(callsign_elements[10], style='color(38)')
    cursor_home()
    time.sleep(frame_delay)
    cursor_move(10, 46)
    console.print(callsign_elements[10], style='color(32)')
    cursor_home()
    time.sleep(frame_delay)
    cursor_move(9, 46)
    console.print(callsign_elements[9], style='color(26)')
    cursor_home()
    time.sleep(frame_delay)
    
    #C
    cursor_move(9, 57)
    console.print(callsign_elements[7], style='color(26)')
    cursor_home()
    time.sleep(frame_delay)
    cursor_move(10, 57)
    console.print(callsign_elements[8], style='color(32)')
    cursor_home()
    time.sleep(frame_delay)
    cursor_move(11, 57)
    console.print(callsign_elements[8], style='color(38)')
    cursor_home()
    time.sleep(frame_delay)
    cursor_move(12, 57)
    console.print(callsign_elements[8], style='color(32)')
    cursor_home()
    time.sleep(frame_delay)
    cursor_move(13, 57)
    console.print(callsign_elements[7], style='color(26)')
    cursor_home()
    time.sleep(frame_delay)
    
    time.sleep(.5)

    cursor_move(19,30)
    console.print('[grey70]Proudly presents...[/]')
    cursor_home()

    time.sleep(1.5)

    console.clear()
    
    time.sleep(1)

    def logo_print_line(line, color):
        lines = [
            '╭─────────╮  ╭─╮  ╭─────────╮  ╭─────────╮  ╭─────────╮',
            '╰──────╮  │  ╰─╯  ╰─────────╯  ╰──────╮  │  │ ╭───────╯',
            '╭──────╯  │  ╭─╮  ╭───────╮    ╭──────╯  │  │ ╰───────╮',
            '│ ╭───────╯  │ │  │ ╭─────╯    │ ╭────╮  ⎨  ╰──────╮  │',
            '│ │          │ │  │ ╰───────╮  │ │    │  │  ╭──────╯  │',
            '╰─╯          ╰─╯  ╰─────────╯  ╰─╯    ╰──╯  ╰─────────╯'
        ]
        style = f'color({color})'
        if color == 0:
            lines[line] = '                                                       '
        row = line + 8
        column = 14
        cursor_move(row, column)
        console.print(lines[line], style=style)
        cursor_home()

    frame_delay = .06

    logo_print_line(0, 235)
    time.sleep(frame_delay)

    logo_print_line(1, 235)
    logo_print_line(0, 231)
    time.sleep(frame_delay)

    logo_print_line(2, 235)
    logo_print_line(1, 231)
    logo_print_line(0, 249)
    time.sleep(frame_delay)

    logo_print_line(3, 235)
    logo_print_line(2, 231)
    logo_print_line(1, 249)
    logo_print_line(0, 244)
    time.sleep(frame_delay)

    logo_print_line(4, 235)
    logo_print_line(3, 231)
    logo_print_line(2, 249)
    logo_print_line(1, 244)
    logo_print_line(0, 239)
    time.sleep(frame_delay)

    logo_print_line(5, 235)
    logo_print_line(4, 231)
    logo_print_line(3, 249)
    logo_print_line(2, 244)
    logo_print_line(1, 239)
    logo_print_line(0, 235)
    time.sleep(frame_delay)

    logo_print_line(5, 231)
    logo_print_line(4, 249)
    logo_print_line(3, 244)
    logo_print_line(2, 239)
    logo_print_line(1, 235)
    logo_print_line(0, 0)
    time.sleep(frame_delay)

    logo_print_line(5, 249)
    logo_print_line(4, 244)
    logo_print_line(3, 239)
    logo_print_line(2, 235)
    logo_print_line(1, 0)
    time.sleep(frame_delay)

    logo_print_line(5, 244)
    logo_print_line(4, 239)
    logo_print_line(3, 235)
    logo_print_line(2, 0)
    time.sleep(frame_delay)

    logo_print_line(5, 239)
    logo_print_line(4, 235)
    logo_print_line(3, 0)
    time.sleep(frame_delay)

    logo_print_line(5, 235)
    logo_print_line(4, 0)
    time.sleep(frame_delay)

    logo_print_line(5, 0)

    time.sleep(.25)

    frame_delay = .12

    logo_print_line(0, 235)
    logo_print_line(1, 235)
    logo_print_line(2, 235)
    logo_print_line(3, 235)
    logo_print_line(4, 235)
    logo_print_line(5, 235)
    time.sleep(frame_delay)

    logo_print_line(0, 231)
    logo_print_line(1, 231)
    logo_print_line(2, 231)
    logo_print_line(3, 231)
    logo_print_line(4, 231)
    logo_print_line(5, 231)
    time.sleep(frame_delay)

    logo_print_line(0, 253)
    logo_print_line(1, 253)
    logo_print_line(2, 253)
    logo_print_line(3, 253)
    logo_print_line(4, 253)
    logo_print_line(5, 253)
    time.sleep(frame_delay)

    logo_print_line(0, 249)
    logo_print_line(1, 249)
    logo_print_line(2, 249)
    logo_print_line(3, 249)
    logo_print_line(4, 249)
    logo_print_line(5, 249)

    time.sleep(.25)

    def title_print_line(color):
        style = f'color({color})'
        row = 15
        column = 22
        cursor_move(row, column)
        console.print('The Raspberry Pi Event Reporting System', style=style)
        cursor_home()

    title_print_line(235)
    time.sleep(frame_delay)

    title_print_line(231)
    time.sleep(frame_delay)

    title_print_line(253)
    time.sleep(frame_delay)

    title_print_line(249)

    time.sleep(3)

    console.clear()

def header(title):
    cursor_home()
    console.print(f' ≣ {title} ❱❱❱ ')

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

def mock_ui():
    console.print(f' ≣ PiERS ❱ Main Menu  ')
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
    console.print('[bright_cyan]─[/][bright_blue]─[/][blue]─[[/][white] 105[/][bright_blue] of [/][white]200 [/][blue]]────────────────────────────────────────────────────[[/][white]  53[/][bright_blue]% [/][blue]]─[/][bright_blue]─[/][bright_cyan]─[/]')
    console.print('Start Line: ', end='')
    input()
