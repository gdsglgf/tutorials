import numpy as np

def toGray(rgb):
  row, column, pipe = rgb.shape
  for i in range(row):
    for j in range(column):
      pix = rgb[i, j]
      r = pix[0]
      g = pix[1]
      b = pix[2]

      gray = (r * 299 + g * 587 + b * 114) / 1000

      print '%4d' %(gray),
    print


rgb1 = np.array(np.arange(8 * 8 * 3).reshape((8, 8, 3)), dtype='uint8')
toGray(rgb1)

rgb2 = np.array(
[[[  0,   0,   2],
  [  2,   3,   5],
  [  6,   7,   9],
  [  9,  10,  12],
  [ 11,  12,  14],
  [ 14,  15,  17],
  [ 17,  18,  20],
  [ 20,  21,  23]],

 [[ 23,  24,  26],
  [ 26,  27,  29],
  [ 29,  30,  32],
  [ 32,  33,  35],
  [ 34,  35,  37],
  [ 37,  38,  40],
  [ 41,  42,  44],
  [ 44,  45,  47]],

 [[ 49,  50,  52],
  [ 51,  52,  54],
  [ 55,  56,  58],
  [ 58,  59,  61],
  [ 60,  61,  63],
  [ 63,  64,  66],
  [ 67,  68,  70],
  [ 70,  71,  73]],

 [[ 71,  72,  74],
  [ 74,  75,  77],
  [ 78,  79,  81],
  [ 81,  82,  84],
  [ 83,  84,  86],
  [ 86,  87,  89],
  [ 90,  91,  93],
  [ 92,  93,  95]],

 [[ 96,  97,  99],
  [ 98,  99, 101],
  [102, 103, 105],
  [105, 106, 108],
  [107, 108, 110],
  [110, 111, 113],
  [114, 115, 117],
  [117, 118, 120]],

 [[118, 119, 121],
  [121, 122, 124],
  [125, 126, 128],
  [128, 129, 131],
  [130, 131, 133],
  [133, 134, 136],
  [137, 138, 140],
  [139, 140, 142]],

 [[144, 145, 147],
  [147, 148, 150],
  [151, 152, 154],
  [154, 155, 157],
  [156, 157, 159],
  [159, 160, 162],
  [162, 163, 165],
  [165, 166, 168]],

 [[168, 169, 171],
  [171, 172, 174],
  [174, 175, 177],
  [177, 178, 180],
  [179, 180, 182],
  [182, 183, 185],
  [186, 187, 189],
  [189, 190, 192]]])

toGray(rgb2)


# rgb1
#    0    3    6    9   12   15   18   21
#   24   27   30   33   36   39   42   45
#   48   51   54   57   60   63   66   69
#   72   75   78   81   84   87   90   93
#   96   99  102  105  108  111  114  117
#  120  123  126  129  132  135  138  141
#  144  147  150  153  156  159  162  165
#  168  171  174  177  180  183  186  189


# rgb2
#    0    2    6    9   11   14   17   20
#   23   26   29   32   34   37   41   44
#   49   51   55   58   60   63   67   70
#   71   74   78   81   83   86   90   92
#   96   98  102  105  107  110  114  117
#  118  121  125  128  130  133  137  139
#  144  147  151  154  156  159  162  165
#  168  171  174  177  179  182  186  189

