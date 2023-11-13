The **Graphics Template Wisk I Library** is a Python module designed for graphical rendering using Tkinter. This library provides functions for drawing various shapes and elements on a canvas within a specified window and viewport configuration.

## Module Initialization

### `init_graphics(w, h, w_xMin, w_yMin, w_xMax)`

- **Parameters:**
  - `w`: Width of the viewport.
  - `h`: Height of the viewport.
  - `w_xMin`: X-coordinate of the lower-left corner of the window.
  - `w_yMin`: Y-coordinate of the lower-left corner of the window.
  - `w_xMax`: X-coordinate of the upper-right corner of the window.
- **Post-Condition:** Initializes the graphics module with the specified parameters.

## Color Functions

### `rgb_col(r, g, b)`

- **Parameters:**
  - `r`: Red component (0-255).
  - `g`: Green component (0-255).
  - `b`: Blue component (0-255).
- **Returns:** Hex-coded color string (`#rrggbb`).

## Coordinate Transformation

### `window_to_viewport(p_w)`

- **Parameters:**
  - `p_w`: Point in window coordinates.
- **Returns:** Point in viewport coordinates.

## Drawing Functions

### `draw_pixel(canvas, xp, yp, fill_col)`

- **Parameters:**
  - `canvas`: Tkinter canvas.
  - `xp`, `yp`: Point in window coordinates.
  - `fill_col`: Color of the pixel.
- **Post-Condition:** Draws a pixel at the specified location in the specified color.

### `draw_dot(canvas, xd, yd, fill_col)`

- **Parameters:**
  - `canvas`: Tkinter canvas.
  - `xd`, `yd`: Point in window coordinates.
  - `fill_col`: Color of the dot.
- **Post-Condition:** Draws a dot at the specified location in the specified color.

### `draw_line(canvas, x0, y0, x1, y1, fill_col)`

- **Parameters:**
  - `canvas`: Tkinter canvas.
  - `x0`, `y0`, `x1`, `y1`: Points in window coordinates.
  - `fill_col`: Color of the line.
- **Post-Condition:** Draws a line from `(x0, y0)` to `(x1, y1)` in the specified color.

### `draw_rect(canvas, x0, y0, x1, y1, fill_col, to_be_filled)`

- **Parameters:**
  - `canvas`: Tkinter canvas.
  - `x0`, `y0`, `x1`, `y1`: Points in window coordinates.
  - `fill_col`: Color of the rectangle.
  - `to_be_filled`: Boolean to determine whether to fill the rectangle.
- **Post-Condition:** Draws a rectangle from `(x0, y0)` to `(x1, y1)` in the specified color.

### `draw_circle(canvas, xc, yc, r, fill_col, to_be_filled)`

- **Parameters:**
  - `canvas`: Tkinter canvas.
  - `xc`, `yc`: Center point in window coordinates.
  - `r`: Radius of the circle in window coordinates.
  - `fill_col`: Color of the circle.
  - `to_be_filled`: Boolean to determine whether to fill the circle.
- **Post-Condition:** Draws a circle with center `(xc, yc)` and radius `r` in the specified color.

### `draw_axis(canvas)`

- **Parameters:**
  - `canvas`: Tkinter canvas.
- **Post-Condition:** Draws the x and y axes on the canvas.

### `draw_grid(canvas)`

- **Parameters:**
  - `canvas`: Tkinter canvas.
- **Post-Condition:** Draws a grid on the canvas.

### `draw_vector(canvas, x0, y0, x1, y1, color)`

- **Parameters:**
  - `canvas`: Tkinter canvas.
  - `x0`, `y0`, `x1`, `y1`: Points in window coordinates.
  - `color`: Color of the vector.
- **Post-Condition:** Draws a vector from `(x0, y0)` to `(x1, y1)` in the specified color.

### `draw_arc(canvas, x0, y0, r, start_angle, end_angle, color)`

- **Parameters:**
  - `canvas`: Tkinter canvas.
  - `x0`, `y0`: Center point in window coordinates.
  - `r`: Radius of the arc in window coordinates.
  - `start_angle`: Start angle of the arc in radians.
  - `end_angle`: End angle of the arc in radians.
  - `color`: Color of the arc.
- **Post-Condition:** Draws an arc with center `(x0, y0)`, radius `r`, start angle `start_angle`, and end angle `end_angle` in the specified color.

### `draw_text(canvas, x, y, text, color)`

- **Parameters:**
  - `canvas`: Tkinter canvas.
  - `x`, `y`: Point in window coordinates.
  - `text`: Text to be drawn.
  - `color`: Color of the text.
- **Post-Condition:** Draws text at `(x, y)` in the specified color.

### `draw_angle_arc(canvas, x0, y0, x1, y1, color)`

- **Parameters:**
  - `canvas`: Tkinter canvas.
  - `x0`, `y0`: Center point in window coordinates.
  - `x1`, `y1`: Point to draw the angle arc to.
  - `color`: Color of the angle arc.
- **Post-Condition:** Draws an angle arc from `(x0, y0)` to `(x1, y1)` in the specified color.

---
## Code Snippet and Usage - Parametric Curve Animation

### Code Snippet:

```python
from tkinter import Tk, Canvas
from graphics_template import *
from time import sleep
import time
import math

# Define viewport dimensions and window coordinates
vp_width, vp_height = 1024, 768
w_xMin, w_yMin, w_xMax = -15, -10, 15
w_yMax = w_yMin + (w_xMax - w_xMin) / vp_width * vp_height

# Create Tkinter window and canvas
window = Tk()
canvas = Canvas(window, width=vp_width, height=vp_height, bg=rgb_col(0, 0, 0))
canvas.pack()

# Initialize graphics module with viewport settings
init_graphics(vp_width, vp_height, w_xMin, w_yMin, w_xMax)

# Initialize animation variables
points = []
animation_done = False
DELTA_TDRAW = 0.02  # 50 fps

# Function to draw a parametric curve at a given parameter t
def draw_parametric_curve(t, color):
    param1 = t * math.cos(t)
    param2 = t * math.sin(t)
    draw_vector(canvas, 0, 0, param1, param2, color)
    draw_angle_arc(canvas, 0, 0, param1, param2, rgb_col(255, 0, 0))
    points.append([param1, param2])
    for (i, point) in enumerate(points):
        if i > 0:
            draw_line(canvas, points[i - 1][0], points[i - 1][1], point[0], point[1], color)
    curve_length = 0
    for (i, point) in enumerate(points):
        if i > 0:
            curve_length += math.sqrt((points[i - 1][0] - point[0]) ** 2 + (points[i - 1][1] - point[1]) ** 2)
    draw_text(canvas, 3, 3, "Curve length: " + str(round(curve_length, 2)), rgb_col(255, 255, 255))

# Function to handle animation logic
def do_animation(t):
    global animation_done
    if t > 2 * math.pi:
        sleep(3)
        animation_done = True

# Function to draw the entire scene at a given parameter t
def draw_scene(t):
    draw_grid(canvas)
    draw_axis(canvas)
    draw_parametric_curve(t, rgb_col(0, 255, 0))

# Function to initialize the scene
def init_scene():
    do_animation(0.0)
    draw_scene(0.0)

# Initial setup
init_graphics(vp_width, vp_height, w_xMin, w_yMin, w_xMax)
init_time = time.perf_counter()
prev_draw_time = 0
init_scene()

# Animation loop
while not animation_done:
    draw_dt = time.perf_counter() - init_time - prev_draw_time
    if draw_dt > DELTA_TDRAW:  # 50 fps
        prev_draw_time += DELTA_TDRAW
        do_animation(prev_draw_time)
        canvas.delete("all")
        draw_scene(prev_draw_time)
        canvas.update()
```

### Usage:

1. **Import Required Libraries:**
   ```python
   from tkinter import Tk, Canvas
   from graphics_template import *
   from time import sleep
   import time
   import math
   ```

2. **Set Viewport and Window Coordinates:**
   ```python
   vp_width, vp_height = 1024, 768
   w_xMin, w_yMin, w_xMax = -15, -10, 15
   w_yMax = w_yMin + (w_xMax - w_xMin) / vp_width * vp_height
   ```

3. **Create Tkinter Window and Canvas:**
   ```python
   window = Tk()
   canvas = Canvas(window, width=vp_width, height=vp_height, bg=rgb_col(0, 0, 0))
   canvas.pack()
   ```

4. **Initialize Graphics Module:**
   ```python
   init_graphics(vp_width, vp_height, w_xMin, w_yMin, w_xMax)
   ```

5. **Define Animation Variables:**
   ```python
   points = []
   animation_done = False
   DELTA_TDRAW = 0.02  # 50 fps
   ```

6. **Define Drawing Functions:**
   - `draw_parametric_curve(t, color)`
   - `do_animation(t)`
   - `draw_scene(t)`

7. **Initialize the Scene:**
   ```python
   init_scene()
   ```

8. **Animation Loop:**
```python
   while not animation_done:
       draw_dt = time.perf_counter() - init_time - prev_draw_time
       if draw_dt > DELTA_TDRAW:  # 50 fps
           prev_draw_time += DELTA_TDRAW
           do_animation(prev_draw_time)
           canvas.delete("all")
           draw_scene(prev_draw_time)
           canvas.update()
```