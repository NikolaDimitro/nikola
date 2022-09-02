def on_button_pressed_a():
    basic.show_arrow(ArrowNames.NORTH)
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_gesture_shake():
    basic.show_arrow(ArrowNames.EAST)
input.on_gesture(Gesture.SHAKE, on_gesture_shake)

def on_button_pressed_b():
    basic.show_arrow(ArrowNames.NORTH_EAST)
input.on_button_pressed(Button.B, on_button_pressed_b)

basic.show_leds("""
    . . . . .
        . # . # .
        . . . . .
        # . . . #
        . # # # .
""")
basic.show_icon(IconNames.GHOST)
basic.show_string("Hallo!")
basic.show_leds("""
    # . . . .
        # # . . .
        # . # . .
        # . . # .
        # # # # #
""")
basic.show_string("Hallo Nikola Spasov Dimitrov!")

def on_forever():
    pass
basic.forever(on_forever)
