from console import console
from rich.style import Style
import ui
import time

console.clear()

def move(r, c):
    print(f'\033[{r};{c}H', end='')

console.clear()
move(1,1)
console.print('Wait for it...', end='')
time.sleep(2)



move(8,14)
console.print('[white]╭─────────╮  ╭─╮  ╭─────────╮  ╭─────────╮  ╭─────────╮[/]', end='')
time.sleep(.10)



move(9,14)
console.print('[white]╰──────╮  │  ╰─╯  ╰─────────╯  ╰──────╮  │  │ ╭───────╯[/]', end='')
move(8,14)
console.print('[bright_black]╭─────────╮  ╭─╮  ╭─────────╮  ╭─────────╮  ╭─────────╮[/]', end='')
time.sleep(.10)



move(10,14)
console.print('[white]╭──────╯  │  ╭─╮  ╭───────╮    ╭──────╯  │  │ ╰───────╮[/]', end='')
move(9,14)
console.print('[bright_black]╰──────╮  │  ╰─╯  ╰─────────╯  ╰──────╮  │  │ ╭───────╯[/]', end='')
move(8,14)
console.print('                                                       ', end='')
time.sleep(.10)



move(11,14)
console.print('[white]│ ╭───────╯  │ │  │ ╭─────╯    │ ╭────╮  ⎨  ╰──────╮  │[/]', end='')
move(10,14)
console.print('[bright_black]╭──────╯  │  ╭─╮  ╭───────╮    ╭──────╯  │  │ ╰───────╮[/]', end='')
move(9,14)
console.print('                                                       ', end='')
time.sleep(.10)



move(12,14)
console.print('[white]│ │          │ │  │ ╰───────╮  │ │    │  │  ╭──────╯  │[/]', end='')
move(11,14)
console.print('[beight_black]│ ╭───────╯  │ │  │ ╭─────╯    │ ╭────╮  ⎨  ╰──────╮  │[/]', end='')
move(10,14)
console.print('                                                       ', end='')
time.sleep(.10)



move(13,14)
console.print('[white]╰─╯          ╰─╯  ╰─────────╯  ╰─╯    ╰──╯  ╰─────────╯[/]', end='')
move(12,14)
console.print('[bright_black]│ │          │ │  │ ╰───────╮  │ │    │  │  ╭──────╯  │[/]', end='')
move(11,14)
console.print('                                                       ', end='')
time.sleep(.10)



move(13,14)
console.print('[bright_black]╰─╯          ╰─╯  ╰─────────╯  ╰─╯    ╰──╯  ╰─────────╯[/]', end='')
move(12,14)
console.print('                                                       ', end='')
time.sleep(.10)



move(13,14)
console.print('                                                       ', end='')
time.sleep(.10)



time.sleep(.50)

move(8,14)
console.print('[bright_black]╭─────────╮  ╭─╮  ╭─────────╮  ╭─────────╮  ╭─────────╮[/]', end='')
move(9,14)
console.print('[bright_black]╰──────╮  │  ╰─╯  ╰─────────╯  ╰──────╮  │  │ ╭───────╯[/]', end='')
move(10,14)
console.print('[bright_black]╭──────╯  │  ╭─╮  ╭───────╮    ╭──────╯  │  │ ╰───────╮[/]', end='')
move(11,14)
console.print('[bright_black]│ ╭───────╯  │ │  │ ╭─────╯    │ ╭────╮  ⎨  ╰──────╮  │[/]', end='')
move(12,14)
console.print('[bright_black]│ │          │ │  │ ╰───────╮  │ │    │  │  ╭──────╯  │[/]', end='')
move(13,14)
console.print('[bright_black]╰─╯          ╰─╯  ╰─────────╯  ╰─╯    ╰──╯  ╰─────────╯[/]', end='')

time.sleep(.10)

move(8,14)
console.print('[bright_white]╭─────────╮  ╭─╮  ╭─────────╮  ╭─────────╮  ╭─────────╮[/]', end='')
move(9,14)
console.print('[bright_white]╰──────╮  │  ╰─╯  ╰─────────╯  ╰──────╮  │  │ ╭───────╯[/]', end='')
move(10,14)
console.print('[bright_white]╭──────╯  │  ╭─╮  ╭───────╮    ╭──────╯  │  │ ╰───────╮[/]', end='')
move(11,14)
console.print('[bright_white]│ ╭───────╯  │ │  │ ╭─────╯    │ ╭────╮  ⎨  ╰──────╮  │[/]', end='')
move(12,14)
console.print('[bright_white]│ │          │ │  │ ╰───────╮  │ │    │  │  ╭──────╯  │[/]', end='')
move(13,14)
console.print('[bright_white]╰─╯          ╰─╯  ╰─────────╯  ╰─╯    ╰──╯  ╰─────────╯[/]', end='')

time.sleep(.20)


move(8,14)
console.print('[white]╭─────────╮  ╭─╮  ╭─────────╮  ╭─────────╮  ╭─────────╮[/]', end='')
move(9,14)
console.print('[white]╰──────╮  │  ╰─╯  ╰─────────╯  ╰──────╮  │  │ ╭───────╯[/]', end='')
move(10,14)
console.print('[white]╭──────╯  │  ╭─╮  ╭───────╮    ╭──────╯  │  │ ╰───────╮[/]', end='')
move(11,14)
console.print('[white]│ ╭───────╯  │ │  │ ╭─────╯    │ ╭────╮  ⎨  ╰──────╮  │[/]', end='')
move(12,14)
console.print('[white]│ │          │ │  │ ╰───────╮  │ │    │  │  ╭──────╯  │[/]', end='')
move(13,14)
console.print('[white]╰─╯          ╰─╯  ╰─────────╯  ╰─╯    ╰──╯  ╰─────────╯[/]', end='')



move(1,1)
time.sleep(5)