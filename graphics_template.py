# graphics template Wisk I
import math

WIDTH, HEIGHT = 1024, 768

window_xMin = -1.0
window_yMin = -3.0
window_xMax = 7.0
window_yMax = window_yMin + (window_xMax - window_xMin) / WIDTH * HEIGHT
# above calculation to give window the same aspect ratio as viewport

"""
    @:param: w: width of the viewport
    @:param: h: height of the viewport
    @:param: w_xMin: x-coordinate of the lower left corner of the window
    @:param: w_yMin: y-coordinate of the lower left corner of the window
    @:param: w_xMax: x-coordinate of the upper right corner of the window
    @:post: initializes the graphics module
"""


def init_graphics(w, h, w_xMin, w_yMin, w_xMax):
    global WIDTH, HEIGHT, window_xMin, window_yMin, window_xMax, window_yMax
    WIDTH = w
    HEIGHT = h
    window_xMin = w_xMin
    window_yMin = w_yMin
    window_xMax = w_xMax
    window_yMax = window_yMin + (window_xMax - window_xMin) / WIDTH * HEIGHT
    # above calculation to give window the same aspect ratio as viewport


def rgb_col(r, g, b):
    """
    Assumes r,g and b integer values 0..255
    Returns hex_coded color string '#rrggbb'
    """
    c = '0123456789abcdef'
    return '#' + c[int(r / 16)] + c[r % 16] + c[int(g / 16)] + c[g % 16] + c[int(b / 16)] + c[b % 16]


"""
   :param: p_w: point in window coordinates
    :return: point in viewport coordinates
"""


def window_to_viewport(p_w):
    # translate point over (-window_xMin, -window_yMin)
    x_vp = p_w[0] - window_xMin
    y_vp = p_w[1] - window_yMin

    # scale point with
    # (viewport width / window width , viewport height / window height)
    x_vp = x_vp / (window_xMax - window_xMin) * WIDTH
    y_vp = y_vp / (window_yMax - window_yMin) * HEIGHT

    # flip vertical axis and translate to put (0,0) at lower left corner
    y_vp = HEIGHT - y_vp

    return [x_vp, y_vp]


"""
    @:param: canvas tkinter canvas
    @:param: xp, yp: point in window coordinates
    @:param: fill_col: color of the pixel
    @:post: draws a pixel at (xp, yp) in color fill_col
"""


def draw_pixel(canvas, xp, yp, fill_col):
    vp_point = window_to_viewport([xp, yp])
    canvas.create_line(vp_point[0], vp_point[1], vp_point[0] + 1, vp_point[1] + 1,
                       fill=fill_col)


"""
    @:param: canvas tkinter canvas
    @:param: xd, yd: point in window coordinates
    @:param: fill_col: color of the pixel
    @:post: draws a dot at (xd, yd) in color fill_col
"""


def draw_dot(canvas, xd, yd, fill_col):
    vp_dot = window_to_viewport([xd, yd])
    r = 5  # radius of the dot in pixels
    canvas.create_oval(vp_dot[0] - r, vp_dot[1] - r, vp_dot[0] + r, vp_dot[1] + r,
                       fill=fill_col)


"""
    @:param: canvas tkinter canvas
    @:param: x0, y0, x1, y1: points in window coordinates
    @:param: fill_col: color of the line
    @:post: draws a line from (x0, y0) to (x1, y1) in color fill_col
"""


def draw_line(canvas, x0, y0, x1, y1, fill_col):
    vp_p0 = window_to_viewport([x0, y0])
    vp_p1 = window_to_viewport([x1, y1])
    canvas.create_line(vp_p0[0], vp_p0[1], vp_p1[0], vp_p1[1],
                       fill=fill_col)


"""
    @:param: canvas tkinter canvas
    @:param: x0, y0, x1, y1: points in window coordinates
    @:param: fill_col: color of the rectangle
    @:param: to_be_filled: boolean to fill the rectangle or not
    @:post: draws a rectangle from (x0, y0) to (x1, y1) in color fill_col
"""


def draw_rect(canvas, x0, y0, x1, y1, fill_col, to_be_filled):
    vp_p0 = window_to_viewport([x0, y0])
    vp_p1 = window_to_viewport([x1, y1])
    if to_be_filled:
        canvas.create_rectangle(vp_p0[0], vp_p0[1], vp_p1[0], vp_p1[1],
                                fill=fill_col, outline=fill_col)
    else:
        canvas.create_rectangle(vp_p0[0], vp_p0[1], vp_p1[0], vp_p1[1],
                                outline=fill_col)


"""
    @:param: canvas tkinter canvas
    @:param: xc, yc: center point in window coordinates
    @:param: r: radius of the circle in window coordinates
    @:param: fill_col: color of the circle
    @:param: to_be_filled: boolean to fill the circle or not
    @:post: draws a circle with center (xc, yc) and radius r in color fill_col
"""


def draw_circle(canvas, xc, yc, r, fill_col, to_be_filled):
    vp_c = window_to_viewport([xc, yc])
    vp_r = window_to_viewport([0, r])
    vp_0 = window_to_viewport([0, 0])
    r = vp_r[1] - vp_0[1]
    if to_be_filled:
        canvas.create_oval(vp_c[0] - r, vp_c[1] - r, vp_c[0] + r, vp_c[1] + r,
                           fill=fill_col)
    else:
        canvas.create_oval(vp_c[0] - r, vp_c[1] - r, vp_c[0] + r, vp_c[1] + r,
                           outline=fill_col)


"""
    @:param: canvas tkinter canvas
    @:post: draws the x and y axis
"""


def draw_axis(canvas):
    draw_line(canvas, 0, window_yMin, 0, window_yMax, rgb_col(255, 255, 255))
    draw_line(canvas, window_xMin, 0, window_xMax, 0, rgb_col(255, 255, 255))


"""
    @:param: canvas tkinter canvas
    @:post: draws the grid
"""


def draw_grid(canvas):
    for i in range(math.trunc(window_xMin), math.ceil(window_xMax)):
        draw_line(canvas, i, window_yMin, i, window_yMax, rgb_col(0, 0, 255))
    for j in range(math.trunc(window_yMin), math.ceil(window_yMax)):
        draw_line(canvas, window_xMin, j, window_xMax, j, rgb_col(0, 0, 255))


"""
    @:param: canvas tkinter canvas
    @:param: x0, y0, x1, y1: points in window coordinates
    @:param: color: color of the vector
    @:post: draws a vector from (x0, y0) to (x1, y1) in color fill_col
"""


def draw_vector(canvas, x0, y0, x1, y1, color):
    draw_line(canvas, x0, y0, x1, y1, color)
    dx = x1 - x0
    dy = y1 - y0
    angel = math.atan2(dy, dx)
    arrow_len = 0.2
    arrow_angle = 0.2
    draw_line(canvas, x1, y1, x1 - arrow_len * math.cos(angel + arrow_angle),
              y1 - arrow_len * math.sin(angel + arrow_angle), color)
    draw_line(canvas, x1, y1, x1 - arrow_len * math.cos(angel - arrow_angle),
              y1 - arrow_len * math.sin(angel - arrow_angle), color)


"""
    @:param: canvas tkinter canvas
    @:param: x0, y0: center point in window coordinates
    @:param: r: radius of the arc in window coordinates
    @:param: start_angle: start angle of the arc in radians
    @:param: end_angle: end angle of the arc in radians
    @:param: color: color of the arc
    @:post: draws an arc with center (x0, y0), radius r, start angle start_angle 
                                        and end angle end_angle in color fill_col
"""


def draw_arc(canvas, x0, y0, r, start_angle, end_angle, color):
    # angle in [0, 2pi]
    start_angle = start_angle % (2 * math.pi)
    end_angle = end_angle % (2 * math.pi)
    if start_angle > end_angle:
        end_angle += 2 * math.pi
    # draw arc
    vp_c = window_to_viewport([x0, y0])
    vp_r = window_to_viewport([0, r])
    vp_0 = window_to_viewport([0, 0])
    r = vp_r[1] - vp_0[1]
    canvas.create_arc(vp_c[0] - r, vp_c[1] - r, vp_c[0] + r, vp_c[1] + r,
                      start=start_angle * 180 / math.pi,
                      extent=(end_angle - start_angle) * 180 / math.pi,
                      outline=color)


"""
    @:param: canvas tkinter canvas
    @:param: x, y: point in window coordinates
    @:param: text: text to be drawn
    @:param: color: color of the text
    @:post: draws text at (x, y) in color fill_col
"""


def draw_text(canvas, x, y, text, color):
    vp_point = window_to_viewport([x, y])
    canvas.create_text(vp_point[0], vp_point[1], text=text, fill=color)


"""
    @:param: canvas tkinter canvas
    @:param: x0, y0, x1, y1: points in window coordinates
    @:param: color: color of the angle arc
    @:post: draws an angle arc from (x0, y0) to (x1, y1) in color fill_col
"""


def draw_angle_arc(canvas, x0, y0, x1, y1, color):
    dx = x1 - x0
    dy = y1 - y0
    angle = math.atan2(dy, dx)
    r = math.sqrt(dx ** 2 + dy ** 2)
    draw_arc(canvas, x0, y0, r * 0.5, 0, angle, color)
    # angle in [0, 2pi]
    angle = angle % (2 * math.pi)
    # draw text middle of angle arc
    x0 = x0 + r * 0.5 * math.cos(angle / 2)
    y0 = y0 + r * 0.5 * math.sin(angle / 2)
    # add offset scale of angle arc
    x0 += 0.5 * math.cos(angle / 2)
    y0 += 0.5 * math.sin(angle / 2)
    draw_text(canvas, x0, y0, "θ = " + str(round(angle * 180 / math.pi, 2)) + "°", color)
