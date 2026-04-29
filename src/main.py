from machine import Pin
import utime

LEDS = 12
ROWS = 4
COLS = 4

keys = [
    ['1', '2', '3', 'A'],
    ['4', '5', '6', 'B'],
    ['7', '8', '9', 'C'],
    ['*', '0', '#', 'D']
]

led_pins_nums = [11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 28, 27]
row_pins_nums = [26, 22, 21, 20]
col_pins_nums = [19, 18, 17, 16]

led_pins = [Pin(pin, Pin.OUT) for pin in led_pins_nums]
for led in led_pins:
    led.value(0)

row_pins = [Pin(pin, Pin.OUT) for pin in row_pins_nums]
for row in row_pins:
    row.value(1)

col_pins = [Pin(pin, Pin.IN, Pin.PULL_UP) for pin in col_pins_nums]

_last_key_active = False


def scan_keypad():
    """Devuelve una tecla o None si no hay pulsación."""
    for r in range(ROWS):
        for rr in range(ROWS):
            row_pins[rr].value(1)
        row_pins[r].value(0)
        utime.sleep_us(50)

        for c in range(COLS):
            if col_pins[c].value() == 0:
                return keys[r][c]
    return None


def get_key_event():
    """Entrega una tecla una sola vez por pulsación (debounce básico)."""
    global _last_key_active

    key = scan_keypad()
    if key is not None and not _last_key_active:
        _last_key_active = True
        return key

    if key is None:
        _last_key_active = False

    return None


def handle_key(key):
    if key == '1':
        led_pins[0].value(1)
    elif key == '2':
        led_pins[1].value(1)
    elif key == '3':
        led_pins[2].value(1)
    elif key == '4':
        led_pins[3].value(1)
    elif key == '5':
        led_pins[4].value(1)
    elif key == '6':
        led_pins[5].value(1)
    elif key == '7':
        led_pins[6].value(1)
    elif key == '8':
        led_pins[7].value(1)
    elif key == '9':
        for i in range(0, 8):
            led_pins[i].value(1)
    elif key == '0':
        for i in range(0, 8):
            led_pins[i].value(0)
    elif key == 'A':
        led_pins[8].value(1)
    elif key == 'B':
        led_pins[9].value(1)
    elif key == 'C':
        led_pins[10].value(1)
    elif key == 'D':
        led_pins[11].value(1)
    elif key == '*':
        for i in range(8, 12):
            led_pins[i].value(1)
    elif key == '#':
        for i in range(8, 12):
            led_pins[i].value(0)


while True:
    key = get_key_event()
    if key is not None:
        handle_key(key)
    utime.sleep_ms(10)
