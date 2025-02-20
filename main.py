from idlelib.pyparse import trans

import numpy as np
from array import array
from classes import *
from PIL import Image
import matplotlib.pyplot as plt

transformation_grid = [["blue_filter,upside_down,resize(2,2)", "red_filter,resize(3,2)", "resize(1,2)"],[
                        "blue_filter,resize(1,2)","diagonal,blue_filter,resize(2,2)", "upside_down,red_filter,resize(1,2)"],[
                        "blue_filter,resize(3,2)", "upside_down,resize(2,1)", "red_filter,left_to_right,resize(3,2)"]]

test_grid = [["resize(1,1)","resize(2,1)"]]

image_handler = ImageHandler("images/image_raw.png")
image_handler = ImageHandler("images/cute-meerkat-baby-standing-upright-observing-sky.jpg")
#image_handler.apply_transformation_sequence("resize(1,1),blue_filter,resize(1,1),upside_down,resize(1,1)")

transformation_grid1 = [["resize(1,1)"]*8 for _ in range(3)]
transformation_grid2 = [["resize(1,1)"]*8,["left_to_right"]*8,["upside_down"]*8,["diagonal"]*8]
transformation_grid3 = [["resize(1,1),blue_filter"]*4,["resize(1,1),red_filter","resize(2,2)","filled","resize(1,1),red_filter"],["resize(1,1),red_filter","filled","filled","resize(1,1),red_filter"],["resize(1,1),green_filter"]*4]
#transformation_grid3 = [["resize(2,2),blue_filter"]*4,["resize(2,2),red_filter","resize(4,4)","filled","resize(2,2),red_filter"],["resize(2,2),red_filter","filled","filled","resize(2,2),red_filter"],["resize(2,2),green_filter"]*4]
transformation_grid4 = [["resize(1,1),convolve(gauss,1,5),convolve(gauss,2,3),convolve(gauss,3,3),convolve(gauss,5,5)"]]
transformation_grid5 = [["green_filter,resize(1,1)","green_filter,convolve(boxblur,3)","green_filter,convolve(sharpen)","green_filter,convolve(ridge)"],
                        ["blue_filter,resize(1,1)","blue_filter,convolve(boxblur,3)","blue_filter,convolve(sharpen)","blue_filter,convolve(ridge)"],
                        ["red_filter,resize(1,1)","red_filter,convolve(boxblur,3)","red_filter,convolve(sharpen)","red_filter,convolve(ridge)"],
                        ["resize(1,1)","convolve(boxblur,3)","convolve(sharpen)","convolve(ridge)"]]
#image_handler.plot_grid(transformation_grid1)
#image_handler.plot_grid(transformation_grid2)
#image_handler.plot_grid(transformation_grid3)
image_handler.plot_grid(transformation_grid5)
#image_handler.filling_engine_hardcoded(transformation_grid4)
#image_handler.plot_grid(transformation_grid2)


