from tkinter import Tk, Canvas
from graphics_template import *
from time import sleep
import time

vp_width, vp_height = 1024, 768
w_xMin, w_yMin, w_xMax = -15, -10, 15
w_yMax = w_yMin + (w_xMax - w_xMin) / vp_width * vp_height

window = Tk()
canvas = Canvas(window, width=vp_width, height=vp_height, bg=rgb_col(0, 0, 0))
canvas.pack()

init_graphics(vp_width, vp_height, w_xMin, w_yMin, w_xMax)

points = []
animation_done = False
DELTA_TDRAW = 0.02  # 50 fps


def draw_parametric_curve(t, color):
    #         (α^2*cos(α),)
    # Φ : α → (           )
    #         (α^2*sin(α) )
    # 0 ≤ α ≤ 2π
    # 0 ≤ t ≤ 1
    param1 = t * math.cos(t)
    param2 = t * math.sin(t)
    draw_vector(canvas, 0, 0, param1, param2, color)
    draw_angle_arc(canvas, 0, 0, param1, param2, rgb_col(255, 0, 0))
    points.append([param1, param2])
    for (i, point) in enumerate(points):
        if i > 0:
            draw_line(canvas, points[i - 1][0], points[i - 1][1], point[0], point[1], color)
    # calculate the curve length
    curve_length = 0
    for (i, point) in enumerate(points):
        if i > 0:
            curve_length += math.sqrt((points[i - 1][0] - point[0]) ** 2 + (points[i - 1][1] - point[1]) ** 2)
    draw_text(canvas, 3, 3, "Curve length: " + str(round(curve_length, 2)), rgb_col(255, 255, 255))


def do_animation(t):
    global animation_done
    if t > 2 * math.pi:
        sleep(3)
        animation_done = True


def draw_scene(t):
    draw_grid(canvas)
    draw_axis(canvas)
    draw_parametric_curve(t, rgb_col(0, 255, 0))


def init_scene():
    # dummy values, set in do_animation (0.0)
    do_animation(0.0)
    draw_scene(0.0)


init_graphics(vp_width, vp_height, w_xMin, w_yMin, w_xMax)

# time.perf_counter() -> float. Return the value (in fractional seconds)
# of a performance counter, i.e. a clock with the highest available resolution
# to measure a short duration. It does include time elapsed during sleep and
# is system-wide. The reference point of the returned value is undefined,
# so that only the difference between the results of consecutive calls is valid.

init_time = time.perf_counter()
prev_draw_time = 0
init_scene()

while not animation_done:
    draw_dt = time.perf_counter() - init_time - prev_draw_time
    if draw_dt > DELTA_TDRAW:  # 50 fps
        prev_draw_time += DELTA_TDRAW
        do_animation(prev_draw_time)
        canvas.delete("all")
        draw_scene(prev_draw_time)
        canvas.update()
