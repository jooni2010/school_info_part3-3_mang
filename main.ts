input.onLogoEvent(TouchButtonEvent.Pressed, function () {
    total = 0
    num = 1
    basic.showNumber(total)
})
input.onButtonPressed(Button.A, function () {
    num += 1
})
input.onButtonPressed(Button.AB, function () {
    dan += 1
    basic.showNumber(dan)
})
input.onButtonPressed(Button.B, function () {
    dan = dan * num
    basic.showNumber(total)
})
let total = 0
let num = 0
let dan = 0
dan = 2
num = 1
total = 0
basic.showNumber(dan)
basic.forever(function () {
	
})
