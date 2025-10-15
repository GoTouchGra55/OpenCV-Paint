import cv2
from utils import DrawingBoard

board = DrawingBoard()

actions = {
  "r": lambda: board.set_color("r"),
  "g": lambda: board.set_color("g"),
  "b": lambda: board.set_color("b"),
  "d": lambda: board.set_color("d"),
  "s": lambda: board.set_color("s"),
  "x": lambda: board.canvas.fill(255)
}

cv2.namedWindow("Drawing Board")
cv2.setMouseCallback("Drawing Board", board.draw)

while True:
  cv2.imshow("Drawing Board", board.canvas)
  key = cv2.waitKey(1) & 0xFF

  if key == ord('q'):
    break
  char = chr(key)
  if char in actions:
    actions[char]()

cv2.destroyAllWindows()