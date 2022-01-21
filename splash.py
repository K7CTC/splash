import time
import ui
from rich.console import Console

def cursor_move(row, column):
    print(f'\033[{row};{column}H', end='')

def cursor_home():
    print(f'\033[1;1H', end='\r')

def logo(shade,line):
    line0 = f'[grey{shade}]                                                       [/]'
    line1 = f'[grey{shade}]╭─────────╮  ╭─╮  ╭─────────╮  ╭─────────╮  ╭─────────╮[/]'
    line2 = f'[grey{shade}]╰──────╮  │  ╰─╯  ╰─────────╯  ╰──────╮  │  │ ╭───────╯[/]'
    line3 = f'[grey{shade}]╭──────╯  │  ╭─╮  ╭───────╮    ╭──────╯  │  │ ╰───────╮[/]'
    line4 = f'[grey{shade}]│ ╭───────╯  │ │  │ ╭─────╯    │ ╭────╮  ⎨  ╰──────╮  │[/]'
    line5 = f'[grey{shade}]│ │          │ │  │ ╰───────╮  │ │    │  │  ╭──────╯  │[/]'
    line6 = f'[grey{shade}]╰─╯          ╰─╯  ╰─────────╯  ╰─╯    ╰──╯  ╰─────────╯[/]'
    logo = [line0, line1, line2, line3, line4, line5, line6]
    return logo[line]

console = Console()

console.clear()

cursor_move(9,16)
console.print('▰▰   ▰▰   ▰▰▰▰▰▰▰    ▰▰▰▰▰▰   ▰▰▰▰▰▰▰▰    ▰▰▰▰▰▰', style='color(26)')
cursor_move(10,16)
console.print('▰▰  ▰▰    ▰    ▰▰   ▰▰           ▰▰      ▰▰     ', style='color(32)')
cursor_move(11,16)
console.print('▰▰▰▰▰         ▰▰    ▰▰           ▰▰      ▰▰     ', style='color(38)')
cursor_move(12,16)
console.print('▰▰  ▰▰       ▰▰     ▰▰           ▰▰      ▰▰     ', style='color(32)')
cursor_move(13,16)
console.print('▰▰   ▰▰      ▰▰      ▰▰▰▰▰▰      ▰▰       ▰▰▰▰▰▰', style='color(26)')
cursor_move(15,27)
console.print('[grey70][grey89]C[/] h r i s    [grey89]C[/] l e m e n t[/]')
cursor_home()

time.sleep(1.5)

cursor_move(19,30)
console.print('[grey70]Proudly presents...[/]')
cursor_home()

time.sleep(1.5)

console.clear()

time.sleep(.75)

speed = .06

cursor_move(8,14)
console.print(logo(15,1))
cursor_home()
time.sleep(speed)

cursor_move(9,14)
console.print(logo(15,2))
cursor_move(8,14)
console.print(logo(100,1))
cursor_home()
time.sleep(speed)

cursor_move(10,14)
console.print(logo(15,3))
cursor_move(9,14)
console.print(logo(100,2))
cursor_move(8,14)
console.print(logo(70,1))
cursor_home()
time.sleep(speed)

cursor_move(11,14)
console.print(logo(15,4))
cursor_move(10,14)
console.print(logo(100,3))
cursor_move(9,14)
console.print(logo(70,2))
cursor_move(8,14)
console.print(logo(50,1))
cursor_home()
time.sleep(speed)

cursor_move(12,14)
console.print(logo(15,5))
cursor_move(11,14)
console.print(logo(100,4))
cursor_move(10,14)
console.print(logo(70,3))
cursor_move(9,14)
console.print(logo(50,2))
cursor_move(8,14)
console.print(logo(30,1))
cursor_home()
time.sleep(speed)

cursor_move(13,14)
console.print(logo(15,6))
cursor_move(12,14)
console.print(logo(100,5))
cursor_move(11,14)
console.print(logo(70,4))
cursor_move(10,14)
console.print(logo(50,3))
cursor_move(9,14)
console.print(logo(30,2))
cursor_move(8,14)
console.print(logo(0,0))
cursor_home()
time.sleep(speed)

cursor_move(13,14)
console.print(logo(100,6))
cursor_move(12,14)
console.print(logo(70,5))
cursor_move(11,14)
console.print(logo(50,4))
cursor_move(10,14)
console.print(logo(30,3))
cursor_move(9,14)
console.print(logo(0,0))
cursor_home()
time.sleep(speed)

cursor_move(13,14)
console.print(logo(70,6))
cursor_move(12,14)
console.print(logo(50,5))
cursor_move(11,14)
console.print(logo(30,4))
cursor_move(10,14)
console.print(logo(0,0))
cursor_home()
time.sleep(speed)

cursor_move(13,14)
console.print(logo(50,6))
cursor_move(12,14)
console.print(logo(30,5))
cursor_move(11,14)
console.print(logo(0,0))
cursor_home()
time.sleep(speed)

cursor_move(13,14)
console.print(logo(30,6))
cursor_move(12,14)
console.print(logo(0,0))
cursor_home()
time.sleep(speed)

cursor_move(13,14)
console.print(logo(0,0))
cursor_home()

time.sleep(.5)

speed = .12

cursor_move(8,14)
console.print(logo(15,1))
cursor_move(9,14)
console.print(logo(15,2))
cursor_move(10,14)
console.print(logo(15,3))
cursor_move(11,14)
console.print(logo(15,4))
cursor_move(12,14)
console.print(logo(15,5))
cursor_move(13,14)
console.print(logo(15,6))
cursor_home()
time.sleep(speed)

cursor_move(8,14)
console.print(logo(100,1))
cursor_move(9,14)
console.print(logo(100,2))
cursor_move(10,14)
console.print(logo(100,3))
cursor_move(11,14)
console.print(logo(100,4))
cursor_move(12,14)
console.print(logo(100,5))
cursor_move(13,14)
console.print(logo(100,6))
cursor_home()
time.sleep(speed)

cursor_move(8,14)
console.print(logo(85,1))
cursor_move(9,14)
console.print(logo(85,2))
cursor_move(10,14)
console.print(logo(85,3))
cursor_move(11,14)
console.print(logo(85,4))
cursor_move(12,14)
console.print(logo(85,5))
cursor_move(13,14)
console.print(logo(85,6))
cursor_home()
time.sleep(speed)

cursor_move(8,14)
console.print(logo(70,1))
cursor_move(9,14)
console.print(logo(70,2))
cursor_move(10,14)
console.print(logo(70,3))
cursor_move(11,14)
console.print(logo(70,4))
cursor_move(12,14)
console.print(logo(70,5))
cursor_move(13,14)
console.print(logo(70,6))
cursor_home()

time.sleep(.25)

cursor_move(15,22)
console.print('[grey15]The Raspberry Pi Event Reporting System[/]',end='')
cursor_home()
time.sleep(speed)

cursor_move(15,22)
console.print('[grey100]The Raspberry Pi Event Reporting System[/]',end='')
cursor_home()
time.sleep(speed)

cursor_move(15,22)
console.print('[grey85][grey89]T[/]he [grey89]R[/]aspberry [grey89]P[/]i [grey89]E[/]vent [grey89]R[/]eporting [grey89]S[/]ystem[/]',end='')
cursor_home()
time.sleep(speed)

cursor_move(15,22)
console.print('[grey70][grey89]T[/]he [grey89]R[/]aspberry [grey89]P[/]i [grey89]E[/]vent [grey89]R[/]eporting [grey89]S[/]ystem[/]',end='')
cursor_home()

time.sleep(3)

console.clear()

ui.header('PiERS')
ui.frame()