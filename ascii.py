from PIL import Image, ImageEnhance
from math import floor
import sys

if len(sys.argv) < 2:
    raise SystemExit("Usage: ascii.py IMG_PATH")

IMG_PATH = sys.argv[1]

print("Opening image...")
im = Image.open(IMG_PATH)
print("Image opened.")

# some photos convert to ascii better with some contrast
CONTRAST_FACTOR = 2
enhancer = ImageEnhance.Contrast(im)
im = enhancer.enhance(CONTRAST_FACTOR)

width, height = im.size

# "compression" factors for width and height
# (how many pixels convert to a character, e.g. each 3x2 become 1 ascii character)
WIDTH_FACTOR = 10
HEIGHT_FACTOR = 20

# "trimming" extra pixels by not considering them at all
# (height needs to be divisible by HEIGHT_FACTOR, and likewise for width)
width -= (width % WIDTH_FACTOR)
height -= (height % HEIGHT_FACTOR)

# converts from a grey value between 0 and 255 to an ascii character
def grey_to_ascii(grey):
    # conversion is based on this MAP of ascii characters sorted by intensity
    # the commented MAP contains reserved HTML characters <>
    # MAP = """$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/|()1{}[]?-_+~<>i!lI;:,"^`'."""
    MAP = """$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/\|()1{}[]?-_+~i!lI;:,"^`'."""
    idx  = floor(grey / 255 * (len(MAP) - 1))
    return MAP[idx]

# returns a hex color string in the format #rrggbb
def rgb_to_hex(r, g, b):
    return f"#{hex(r)[2:]:0<2}{hex(g)[2:]:0<2}{hex(b)[2:]:0<2}"

ascii_result = [] # keeps track of ascii strings (ascii image rows)

# every possible value to add to an (i, j) pixel to group it with other pixels
pixel_range = [(s, t) for s in range(WIDTH_FACTOR) for t in range(HEIGHT_FACTOR)]

print("Converting to ASCII...")
for j in range(0, height-1, HEIGHT_FACTOR):
    ascii_string = "" # keeps track of ascii characters (making up a row in the final ascii image)
    for i in range(0, width-1, WIDTH_FACTOR):
        rgb = [im.getpixel((i+x, j+y)) for x, y in pixel_range]
        R, G, B = 0, 0, 0
        for color in rgb:
            R += color[0]
            G += color[1]
            B += color[2]
        R //= len(rgb)
        G //= len(rgb)
        B //= len(rgb)
        grey = floor(0.30 * R + 0.59 * G + 0.11 * B) # RGB to greyscale formula
        ascii_string += f"""<span style="color: {rgb_to_hex(R, G, B)}">{grey_to_ascii(grey)}</span>"""
    ascii_result.append(ascii_string)
print("Conversion complete.")

print("Making HTML file...")

# ascii with line breaks for HTML file
html_ascii = "<br>\n".join(ascii_result)

# HTML template
html_string = f"""<!DOCTYPE html>
<html>
<head>
<title>ascii art</title>
</head>
<body style="font-family: monospace">
{html_ascii}
</body>
</html>
"""

# generating HTML file
with open("./ascii.html", "w") as f:
    f.write(html_string)

print("HTML file complete: ascii.html")