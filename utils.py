import cv2
import numpy as np
import tkinter as tk

root = tk.Tk()
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
root.destroy()

prev = None
colors = {
  "d": (0, 0, 0),
  "r": (0, 0, 200), 
  "g": (0, 200, 0), 
  "b": (200, 0, 0), 
  "s": (255, 255, 255)
}

class DrawingBoard():
  def __init__(self):
    self.prev = None
    self.color = colors["d"]
    self.canvas = np.ones((screen_height, screen_width, 3), dtype=np.uint8) * 255

  def set_color(self, btn="d"):
    self.color = colors.get(btn, self.color)

  def draw(self, event, x, y, *args):
    if event == cv2.EVENT_LBUTTONDOWN:
      self.prev = (x, y)
    elif event == cv2.EVENT_MOUSEMOVE and self.prev is not None:
      cv2.line(self.canvas, self.prev, (x, y), color=self.color, thickness=3)
      self.prev = (x, y)
    elif event == cv2.EVENT_LBUTTONUP:
      self.prev = None