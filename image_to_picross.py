from PIL import Image
import math
import sys
import base64
import numpy
from functools import reduce
import json

def board_to_hints():
	pass

def row_to_hint(out, x, i, r):
	if (x == False and out[-1] == 0) or (r[i-1] == False and x == False):
		out[-1] += 1
	elif (r[i-1] == True and x == False):
		out.append(1)
	return out

def rw(row):
	out = [0]
	i = 0
	for x in row:
		out = row_to_hint(out, x, i, row)
		i += 1
	return out

def y_hints(b):
	return list(map(rw, b))


def x_hints(b):
	return list(map(rw, [*zip(*b)]))
	


filename = sys.argv[1]
img = Image.open(filename)
# img.pixels
thresh = math.floor((128+64)/2)
def fn(x): return 255 if x > thresh else 0


r = img.convert('L').point(fn, mode='1')
board = numpy.array(r).tolist()
data = {
	"x": r.size[0],
	"y": r.size[1],
	"hints": {
		"x": x_hints(board),
		"y": y_hints(board)
	}
}
print(base64.urlsafe_b64encode(json.dumps(data).encode("utf-8")))
r.save('myuu.png')
