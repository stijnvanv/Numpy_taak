# Numpy taak - Stijn Van Vlaenderen

## Content Table
1. [Intro](#1-intro)
2. [Setup](#2-setup)  
2.1 [Docker image](#21-docker-image)  
2.2 [Maintaining Docker image](#22-maintaining-docker-image)  
2.3 [Maintaining GitHub project](#23-maintaining-github-project)  
3. [Classes](#3-classes)  
3.1 [ImportAsNpArray](#31-importasnparray)  
&emsp;3.1.1 [Constructor](#311-constructor)    
&emsp;3.1.2 [Methods](#312-methods)    
3.2 [Transformations](#32-transformations)    
&emsp;3.2.1 [Methods](#321-methods)  
3.3 [Kernel](#33-kernel)  
&emsp;3.3.1 [Constructor](#331-constructor)  
&emsp;3.3.2 [Methods](#332-methods)  
&emsp;3.3.3 [Identity Kernel](#333-identity-kernel)    
&emsp;3.3.4 [Gaussian Kernel](#334-gaussian-kernel)    
&emsp;3.3.5 [Horizontal Edge Kernel](#335-horizontal-edge-kernel)  
&emsp;3.3.5 [Vertical Edge Kernel](#336-vertical-edge-kernel)  
&emsp;3.3.6 [Sharpen Kernel](#337-sharpen-kernel)  
&emsp;3.3.7 [BoxBlur Kernel](#338-boxblur-kernel)  
3.4 [ImageHandler](#34-imagehandler)  
&emsp;3.4.1 [Constructor](#341-constructor)  
&emsp;3.4.2 [Methods](#342-methods)
4. [Usage](#4-usage)   
4.1 [Grid construction](#41-grid-construction)  
4.2 [Example composed picture](#42-example-composed-picture)  
4.3 [All options overview](#43-all-options-overview)  

## 1. Intro

This project involves using NumPy for image manipulation tasks. The focus is on converting images into NumPy arrays, applying various transformations, and using convolutional operations to manipulate image data. The goal is to provide an easy-to-use interface for applying common image operations and visualizing the results.

---


## 2. Setup


### 2.1 Docker image
You can use the docker image used to run this codebase with:  

```console
docker pull stijnvanvl/taaknumpy:latest
```
Or when using pycharm pro:  
- > Ctrl+Alt+s 
- > Add:interpreter (dropdown) 
- > Select: On Docker...  
- > Select: Pull or use existing  
- > use image tag: "stijnvanvl/taaknumpy:latest"

If you want to run the code in the terminal:

```console
docker run -it -v .:/taak_numpy stijnvanvl/taaknumpy:latest python /taak_numpy/main.py
```

### 2.2 Maintaining Docker image

Add new dependencies in requirement.txt.  
terminal:  
```console
docker build -t taaknumpy . 
``` 
```console
docker login
```
```console
docker tag taaknumpy stijnvanvl/taaknumpy:latest
```
```console 
docker push stijnvanvl/taaknumpy:latest
```  

### 2.3 Maintaining GitHub project

Useful GitHUb commands:  
- Adding changes
```console
git add <file> 
```
```console
git commit -m "Message." #message e.g. date/important changes
```
```console
git push (-u) #origin main pushed to github link
``` 
- To get the project from GitHub:
```console
git remote add origin https://github.com/stijnvanv/NumpyTaak.git
```
```console
git init
```

---

## 3. Classes
  
### 3.1. ImportAsNpArray

The `Importasnparray` class is responsible for loading an image from a given path and converting it into a NumPy array for manipulation. This class allows further transformations and operations to be applied to the image.
  
#### 3.1.1 Constructor

The constructor initializes the image data from a file path, converts it to the RGB format, and stores it as a NumPy array.

- `np_array`: Stores the image as a NumPy array.
- `transformations_used`: Tracks the transformations applied to the image.
- `path_to_image`: Path to the image file (optional).

#### 3.1.2 Methods

Methods include applying transformations and tracking and/or visualizing changes.  

- `from_transformation`: Ensures a new object is created after a transformation is applied, also updates `transformations_used`. 
- `apply_transformation`: Applies a single transformation from [Transformations](#32-transformations).
- `make_plot_title`: Makes a tittle for plot containing transformations used, mainly used in development. 
- `plot`: Plots the `np_array`, mainly used in development.  

---
  
### 3.2. Transformations

The `Transformations` class provides a variety of image manipulation methods. These methods apply basic transformations like flipping, filtering, resizing, and convoluting the image.
  
#### 3.2.1 Methods

- `upside_down`: Flips the image vertically.
- `left_to_right`: Flips the image horizontally.
- `diagonal`: Combines both upside down and left to right flips.
- `red_filter`: Removes the green and blue channels, leaving only the red channel visible.
- `green_filter`: Removes the red and blue channels, leaving only the green channel visible.
- `blue_filter`: Removes the red and green channels, leaving only the blue channel visible.
- `empty`: Replaces all pixels with zeros (black image).
- `resize_horizontally`: Resizes the image horizontally by a factor.
- `resize_vertically`: Resizes the image vertically by a factor.
- `resize`: Resizes the image both horizontally and vertically using a tuple of factors.
- `convolve`: Applies a kernel (e.g. Gaussian or sharpen) to the image via convolution.

---
  
### 3.3. Kernel

The `Kernel` class and its subclasses define various convolution kernels used for filtering operations.

#### 3.3.1 Constructor

the constructor uses `create_np_kernel` and `normalise` respectively. Children call it by using the `__super__` method but are expected to keep their own hyperparameters in their derived constructors. 

#### 3.3.2 Methods
Methods of `Kernel` are intended for it's children as they handle the creation, normalisation (if needed) and visualisation for `np_kernel`.

- `create_np_kernel`: blueprint method for the creation of `np_kernel`
- `__str__`: represents the Kernel by showing `np_kernel`
- `normalise`: ensures that the sum of all kernel elements equals to one. This avoids changing the brightness of the pictures when a low/high passing filter is applied. 
#### 3.3.3 Identity Kernel

The `Identity` kernel class defines an identity filter. It is used to return the image unchanged when applied.

- `np_kernel`: A 2D array with a single 1 in the center (identity).
  
#### 3.3.4 Gaussian Kernel

The `GaussianKernel` class defines a Gaussian filter. The kernel is based on a specified size and sigma value.

- `np_kernel`: A 2D Gaussian kernel created from a function of the size and sigma.
  
#### 3.3.5 Horizontal Edge Kernel

The `HorizontalEdgeKernel` class defines a kernel for horizontal edge detection, referred to as the Sobel Kernel.

- `np_kernel`: A 3x3 kernel used to detect edges.

#### 3.3.6 Vertical Edge Kernel

The `VerticalEdgeKernel` class defines a kernel for vertical edge detection, referred to as the Sobel Kernel.

- `np_kernel`: A 3x3 kernel used to detect edges.
  
#### 3.3.7 Sharpen Kernel

The `Sharpen` class defines a sharpening kernel that enhances the details in an image by removing noice. Created by `2*Identity-Gaussian`, with size 3 and sigma 0.2.

- `np_kernel`: A 3x3 kernel that highlights edges for sharpening.
  
#### 3.3.8 BoxBlur Kernel

The `BoxBlur` class defines a simple blur kernel by averaging pixel values in a square window.

- `np_kernel`: A 2D array of ones that is normalized for averaging.

#### 3.3.9 From Np Array Kernel

the `KernelFromNpArray` class allows more complex or custom-made kernels to be implemented.

- `np_kernel`: A 2D array passed to the constructor.  

---
  
### 3.4. ImageHandler

The `ImageHandler` class manages the image and applies sequences of transformations in a grid which is a `list` of `lists`. 
Gives the user an option to plot a custom-made grid and safe it if needed. 

#### 3.4.1 Constructor

Main goal of the constructor is to load the original picture and keep it as a starting point for various transformation sequences. 
Also Initialises all possible transformation functions defined in the `Transformation` class.

- `image`: uses `ImageAsNpArray` with `image_path`  
- `transformations` : initialises  `Transformations()`
-  `final_image`: starts of the grid as `None` in order to keep track of grids being computed.
  
#### 3.4.2 Methods

- `apply_transformation_sequence`: Applies a sequence of transformations from a CSV string, interpreting operations such as resizing and convolution with specific kernels.
- `create_transformed_grid_elements`: Creates a list of transformed grid elements based on a provided grid configuration.
- `filling_engine_hardcoded`: Combines the transformed grid elements into a final output image.
- `complete_input_grid`: Automatically fills in missing grid elements marked as "filled" or "empty." ~Will be added next patch. :^)
- `plot_grid`: Displays the final image by plotting the grid of transformed images.
- `reset_handler`: reset `final_image`to `None`
- `make_grid`: calls `filling_engine_hardcoded` with an option to plot the result.
- `save_grid_as:`: after calling `make_grid` this method allows the user to safe their image 
with the desired named and file extension.
---

## 4. Usage

In order to make a composition of a picture the user needs to give the path of a 
picture to the `ImageHandler` constructor. Then compute the grid with `make_grid`,
where he can inspect the result by using `plot_grid=True`as argument.
Saving the picture is possible by calling `save_grid_as` with png as standard format. 

   
### 4.1 Grid construction
An `element` inside the grid is made by using to transformation's name as a `string`.
Applying `multiple transformations` to a grid element is done by `joining` single operations by `,`.
Then these elements need to be put inside a `list` of `lists` where `row` and `colum` represent the `position`.
When using `resize(x_axis,y_axis)` the picture is enlarged by an integer factor in a direction but need to have `filled` inside the rows and columns it would take up.
This is important so that `list` always has the same length and to ensure there's no ambiguity.  


### 4.2 Example composed picture

```python
from classes import *

image_handler = ImageHandler("images/cute-meerkat-baby-standing-upright-observing-sky.jpg")
transformation_grid = [["resize(1,1),blue_filter"]*4,
                       ["resize(1,1),red_filter","resize(2,2)","filled","resize(1,1),red_filter"],
                       ["resize(1,1),red_filter","filled","filled","resize(1,1),red_filter"],
                       ["resize(1,1),green_filter"]*4
                       ]
image_handler.make_grid(transformation_grid)
image_handler.save_grid_as("example_composed_picture")
```
The above code will produce the following picture:
<div style="text-align:center">
  <img src="images/manip3_meerkat.png" alt="Manip1">
</div>

### 4.3 All options overview
| *Transformation*          | *String repr.*             |
|---------------------------|----------------------------|
| blue filter               | blue_filter                |
| red filter                | red_filter                 |
| green filter              | green_filter               |
| resize                    | resize                     |
| mirror upside down        | upside_down                |
| mirror left to right      | left_to_right              |
| mirror pointwise          | diagonal                   |
| empty                     | empty                      |
| convolve identity kernel  | convolve(identity)         |
| convolve gaussian kernel  | convolve(gauss,sigma,size) |
| horizontal edge detection | convolve(horizontaledge)   |
| vertical edge detection   | convolve(verticaledge)     |
| sharpen                   | convolve(sharpen)          |
| box blur                  | convolve(boxblur,size)     |

---
