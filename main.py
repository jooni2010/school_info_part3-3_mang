def on_logo_pressed():
    global total
    total = 0
input.on_logo_event(TouchButtonEvent.PRESSED, on_logo_pressed)

def on_button_pressed_a():
    global num
    num += 1
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_button_pressed_ab():
    global dan
    dan += 1
input.on_button_pressed(Button.AB, on_button_pressed_ab)

def on_button_pressed_b():
    global dan
    dan = dan * num
    basic.show_number(total)
input.on_button_pressed(Button.B, on_button_pressed_b)

total = 0
num = 0
dan = 0
dan = 2
num = 0
basic.show_number(dan)

def on_forever():
    pass
basic.forever(on_forever)
