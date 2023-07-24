from Graphics import canvas
import random
CANVAS_WIDTH = 300
CANVAS_HEIGHT = 300 
circle_size = 20 
N_CIRCLE = 20 
canvas=canvas(CANVAS_WIDTH, CANVAS_HEIGHT)
for i in range(N_CIRCLE):
    color = random_color()
    canvas.create_oval