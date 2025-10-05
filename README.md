# Image to Colored ASCII Art Converter

This is a Python script that converts an image to a colored ASCII art in an HTML document.

## Usage

Clone the repository and access it:
```bash
git clone https://github.com/mrnng/ascii.git
cd ascii
```

Install the required ```pillow``` library:
```bash
pip install -r requirements.txt
```

Run the script with the path to an image as a command-line argument:
```bash
python3 ascii.py path/to/image
```

The HTML file with the ASCII art is created in the same directory with the name ```ascii.html```, which you can change in the source code.

You will often need to zoom in or out to see the art properly.
You can also change the constants WIDTH_FACTOR and HEIGHT_FACTOR as specified in the source code to change the resolution of the output ASCII art.

## Example

Suppose this image is saved in the same directory with the name ```winnie.png```:
![An image of Winnie the Pooh](./images/winnie.png)

Then you run:
```bash
python3 ascii.py ./winnie.png
```

This produces the following page:
![An image of the converted ASCII art of Winnie the Pooh](./images/ascii-winnie.png)

## Support

This script was tested on the three most common image formats on the internet: JPG, PNG, and WebP.

Running the script produces a SyntaxWarning because of the use of "\|" in the grey-to-ascii map, which Python sees as an invalid escape character.
You may choose to suppress this warning.

## Inspiration

I was interested in what I can do by manipulating images pixel-by-pixel and thought of ASCII art, which I always liked.
I wanted to make something which creates simple but nostalgic art in the era of over-processed, generative AI "art".