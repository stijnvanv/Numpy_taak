from classes import *

# Grids of interest
transformation_grid1 = [["resize(1,1)"]*8 for _ in range(3)]
transformation_grid2 = [["resize(1,1)"]*8,["left_to_right"]*8,["upside_down"]*8,["diagonal"]*8]
transformation_grid3 = [["resize(1,1),blue_filter"]*4,["resize(1,1),red_filter","resize(2,2)","filled","resize(1,1),red_filter"],["resize(1,1),red_filter","filled","filled","resize(1,1),red_filter"],["resize(1,1),green_filter"]*4]
transformation_grid4 = [["green_filter,resize(1,1)","green_filter,convolve(boxblur,3)","green_filter,convolve(horizontaledge)","green_filter,convolve(verticaledge)","green_filter,convolve(sharpen)"],
                        ["blue_filter,resize(1,1)","blue_filter,convolve(boxblur,3)","blue_filter,convolve(horizontaledge)","blue_filter,convolve(verticaledge)","blue_filter,convolve(sharpen)"],
                        ["red_filter,resize(1,1)","red_filter,convolve(boxblur,3)","red_filter,convolve(horizontaledge)","red_filter,convolve(verticaledge)","red_filter,convolve(sharpen)"],
                        ["resize(1,1)","convolve(boxblur,3)","convolve(horizontaledge)","convolve(verticaledge)","convolve(sharpen)"]]

grids = [transformation_grid1,transformation_grid2,transformation_grid3,transformation_grid4]

# My code in action :^)
image_handler = ImageHandler("images/image_raw.png")

for number, grid in enumerate(grids):
    image_handler.make_grid(grid)
    image_handler.save_grid_as(f"manip{number+1}_self")

# more ambitious picture, meer meerkatten :O
image_handler_meercat = ImageHandler("images/cute-meerkat-baby-standing-upright-observing-sky.jpg")

for number, grid in enumerate(grids):
    image_handler_meercat.make_grid(grid)
    image_handler_meercat.save_grid_as(f"manip{number+1}_meerkat")
