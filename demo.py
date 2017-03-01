# !/usr/bin/python
"""Example using a character LCD connected to an ESP8266."""

from time import sleep
from LCD import CharLCD


def run():
    """Run demo."""
    # Initialize the LCD
    lcd = CharLCD(rs=1, en=3, d4=15, d5=13, d6=12, d7=14,
                  cols=16, rows=2)

    # Print a 2 line centered message
    lcd.message('Hello', 2)
    lcd.set_line(1)
    lcd.message('World!', 2)
    sleep(3.0)

    # Show the underline cursor.
    lcd.clear()
    lcd.show_underline()
    lcd.message('Underline')
    lcd.set_line(1)
    lcd.message('Cursor: ')
    sleep(3.0)

    # Also show the blinking cursor.
    lcd.clear()
    lcd.show_blink()
    lcd.message('Blinking')
    lcd.set_line(1)
    lcd.message('Cursor: ')
    sleep(3.0)

    # Disable blink and underline cursor.
    lcd.show_underline(False)
    lcd.show_blink(False)

    # Scroll message right & left.
    lcd.clear()
    lcd.message('Scrolling Demo')
    sleep(1.0)
    for i in range(16):
        sleep(0.25)
        lcd.move_right()
    for i in range(16):
        sleep(0.25)
        lcd.move_left()
    sleep(2.0)

    # The End
    lcd.clear()
    lcd.message('The', 3)
    lcd.set_line(1)
    lcd.message('End', 3)
