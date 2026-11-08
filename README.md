# Turtle Color Dot Project (`turtle_makedot.py`)

## Objective

The main objective of this program is to use Python's Turtle Graphics module to create a grid of randomly coloured dots.

The turtle navigates across the screen, drawing 20 dots per row and filling 15 rows, resulting in a total of **300 coloured dots**.

## Modules Required

- `turtle`
  - `Turtle` object – controls movement, colour and dot drawing.
  - `Screen` object – manages the graphics window and RGB colour mode.
- `random`
  - Generates random RGB values for each dot.

## Program Execution and Logic

### 1. Initialise the Turtle and Screen

I create a Turtle object named `Green` and a Screen object named `screen`.

The turtle is initially lifted using `Green.penup()` and positioned at `(-500, 450)`. Its drawing speed is then set to `fastest` to improve execution speed.

I also configure the screen using:

```python
screen.colormode(255)
```

This allows the program to interpret RGB colour values within the range of 0–255 for each colour channel.

### 2. Generate Random RGB Colours

I define a function called `random_color()` to generate three random integer values representing red, green and blue.

```python
def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    var_color = (r, g, b)
    return var_color
```

The three values are stored in a tuple and returned by the function.

This allows me to call `random_color()` inside the nested loops and assign a different randomly generated colour to each dot.

### 3. Define the Dot Parameters

I create several variables to control the grid layout:

- `dot_num = 20` – number of dots per row.
- `dot_size = 30` – diameter of each dot.
- `dot_spacing = 50` – distance between consecutive dot coordinates.
- `dot_x = -500` – initial horizontal coordinate.
- `dot_y = 350` – initial vertical coordinate.

These variables make it easier to adjust the grid dimensions, dot size and spacing without modifying the entire program.

### 4. Create the Grid Using Nested Loops

I use nested `for` loops to generate the grid:

- The outer loop (`range(15)`) controls the 15 rows.
- The inner loop (`range(20)`) controls the 20 columns within each row.

For every iteration of the inner loop, the turtle:

1. Moves to the current `(dot_x, dot_y)` coordinates.
2. Calls `random_color()` to generate a random RGB tuple.
3. Uses `Green.pencolor(get_color)` to assign the generated colour.
4. Uses `Green.dot(dot_size)` to draw the coloured dot.
5. Increases `dot_x` by 50 to position the next dot horizontally.

The turtle remains lifted between movements, preventing unwanted connecting lines.

### 5. Reset Coordinates for the Next Row

Once the inner loop finishes drawing 20 dots, the program resets `dot_x` to `-500`.

It then decreases `dot_y` by 50 to move the next row downward.

This process repeats until the outer loop completes all 15 rows.

As a result, the program generates:

- 15 rows
- 20 columns
- 300 randomly coloured dots

### 6. Exit the Graphics Window

Finally, I use:

```python
screen.exitonclick()
```

This allows the graphics window to remain open until the user clicks on it, providing a convenient way to inspect the completed output.

## Key Concepts Practised

- Turtle movement and coordinate positioning.
- RGB colour representation.
- Functions and return values.
- Random number generation.
- Nested loops.
- Variable assignment and coordinate updates.
- Using `penup()` to prevent unwanted drawing during movement.
- Using `dot()` to draw circular shapes.
