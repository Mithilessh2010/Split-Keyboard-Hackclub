import board
from kmk.kmk_keyboard import KMKKeyboard
from kmk.keys import KC
from kmk.scanners import DiodeMatrix

keyboard = KMKKeyboard()

row_pins = [board.D0, board.D1, board.D2, board.D3, board.D4, board.D5]
col_pins = [board.D6, board.D7, board.D8, board.D9, board.D10, board.D11, board.D12]

keyboard.matrix = DiodeMatrix(row_pins=row_pins, column_pins=col_pins, diode_orientation=DiodeMatrix.ROW2COL)

keyboard.keymap = [[
    KC.ESC, KC.F1, KC.F2, KC.F3, KC.F4, KC.F5, KC.F6,
    KC.TAB, KC.Q, KC.W, KC.E, KC.R, KC.T, KC.Y,
    KC.LCTRL, KC.A, KC.S, KC.D, KC.F, KC.G, KC.H,
    KC.LSHIFT, KC.Z, KC.X, KC.C, KC.V, KC.B, KC.N,
    KC.SPC, KC.M, KC.COMMA, KC.DOT, KC.SLASH, KC.RALT, KC.RCTRL,
    KC.LEFT, KC.DOWN, KC.UP, KC.RIGHT, KC.HOME, KC.END, KC.ENTER
]]

if __name__ == '__main__':
    keyboard.go()
