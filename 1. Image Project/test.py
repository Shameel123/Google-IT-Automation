from PIL import Image
import glob, os

size = 128, 128
path = "*.TIFF"
for infile in glob.glob(path):
    file, ext = os.path.splitext(infile)
    im = Image.open(infile)
    im.rotate(270)
    im.save(file,"JPEG")
