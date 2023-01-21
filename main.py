from PIL import Image
import numpy as np

im = Image.open('lenna.png')
im = im.convert('L')
im.show()

pixsize = 8

def weight (num):
    char = ''
    if num < 255:
        char = '^'
    if num < 200:
        char = '!'
    if num < 175:
        char = '('
    if num < 150:
        char = ']'
    if num < 125:
        char = '&'
    if num < 100:
        char = '#'
    if num < 75:
        char = '$'
    if num < 50:
        char = '%'
    if num < 25:
        char = '@'
    return char

data1 = np.asarray(im)
l = [[data1[y:y+pixsize,x:x+pixsize] for x in range(0, len(data1[0]), pixsize)] for y in range(0, len(data1), pixsize)]
el = [[round(np.sum(np.array(l[y][x]))/np.size(np.array(l[y][x]))) for x in range(0, len(l[0]))] for y in range(0, len(l))]

elpixel = np.zeros((len(el) * pixsize, len(el[0]) * pixsize))
z, w = 0, 0
for q in range(0, len(el)):
    for p in range(0, len(el[0])):
        elpixel[w:w+pixsize, z:z+pixsize] = el[q][p]
        z += pixsize
    w += pixsize
    z = 0

im = Image.fromarray(np.array(elpixel))
im.show()

ascii_art = ''
for i in el:
    for j in i:
        ascii_art += weight(j) + ' '
    ascii_art += '\n'

with open('ascii_art.txt', 'w') as f:
    f.write(ascii_art)