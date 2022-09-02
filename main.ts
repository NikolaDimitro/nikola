input.onButtonPressed(Button.A, function () {
    basic.showArrow(ArrowNames.North)
})
input.onGesture(Gesture.Shake, function () {
    basic.showArrow(ArrowNames.East)
})
input.onButtonPressed(Button.B, function () {
    basic.showArrow(ArrowNames.NorthEast)
})
basic.showLeds(`
    . . . . .
    . # . # .
    . . . . .
    # . . . #
    . # # # .
    `)
basic.showIcon(IconNames.Ghost)
basic.showString("Hallo!")
basic.showLeds(`
    # . . . .
    # # . . .
    # . # . .
    # . . # .
    # # # # #
    `)
basic.showString("Hallo Nikola Spasov Dimitrov!")
basic.forever(function () {
	
})
