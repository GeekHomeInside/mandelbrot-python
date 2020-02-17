from PIL import Image, ImageDraw

class Param:
    def __init__(self):
        # Max iteration
        self.maxit = 1000
        # Image size (pixels)
        self.width = 800
        self.height = 800
        # Define Real
        self.re_start = -2
        self.re_end = 2
        # Define Image
        self.im_start = -1
        self.im_end = 1
        # Define Output file
        self.output = "foo.bmp"

def mandelbrot(c, maxit):
    z = complex(0.0, 0.0)
    n = 0
    while abs(z) <= 2 and n < maxit:
        z = z*z + c
        n += 1
    return n

def newimage(width, height):
    # Define New Image
    im = Image.new('RGB', (width, height), (0, 0, 0))
    return im

def newdraw(im):
    # Define Draw Image
    draw = ImageDraw.Draw(im)
    return draw

def pixeltopoint(x, y, re_start, re_end, im_start, im_end, height, width):
    c = complex(re_start + (x / width) * (re_end - re_start), im_start + (y / height) * (im_end - im_start))
    return c

if __name__ == '__main__':
    p = Param()
    im = newimage(p.width, p.height)
    d = newdraw(im)

    print("Resolution =", p.width, "x", p.height)
    print("Number of maximun iteration =", p.maxit)
    print("Real =", [p.re_start,p.re_end])
    print("Imaginary =", [p.im_start,p.im_end])

    for x in range(0, p.width):
        for y in range(0, p.height):
            # Convert pixel coordinate to complex number
            c = pixeltopoint(x, y, p.re_start, p.re_end, p.im_start, p.im_end, p.height, p.width)
            # Compute the number of iterations
            m = mandelbrot(c, p.maxit)
            # The color depends on the number of iterations
            color = 255 - int(m * 255 / p.maxit)
            # Plot the point
            d.point([x, y], (color, color, color))

    im.save(p.output, 'BMP')