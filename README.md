# Numpy taak - Stijn Van Vlaenderen

## Content Table
1. [Intro](#intro)
2. [Setup](#setup)  
&emsp;2.1 [Docker image](#docker-image)  
&emsp;2.2 [Maintaining Docker image](#maintaining-docker-image)  
&emsp;2.3 [Maintaining Github project](#maintaining-github-project)
3. [Classes](#classes)  
&emsp;3.1 [Importasnparray](#importasnparray)  
&emsp;&emsp;3.1.1 [Constructor](#constructor)  
&emsp;3.2 [Transformations](#transformations)  
&emsp;&emsp;3.2.1 [Methods](#methods)  
&emsp;3.3 [Kernel](#kernel)  
&emsp;&emsp;3.3.1 [Identity Kernel](#identity-kernel)  
&emsp;&emsp;3.3.2 [Gaussian Kernel](#gaussian-kernel)  
&emsp;&emsp;3.3.3 [Ridge Kernel](#ridge-kernel)  
&emsp;&emsp;3.3.4 [Sharpen Kernel](#sharpen-kernel)  
&emsp;&emsp;3.3.5 [BoxBlur Kernel](#boxblur-kernel)  
&emsp;3.4 [ImageHandler](#imagehandler)  
&emsp;&emsp;3.4.1 [Methods](#methods)

<a name="intro"></a>
## Intro

This project involves using NumPy for image manipulation tasks. The focus is on converting images into NumPy arrays, applying various transformations, and using convolutional operations to manipulate image data. The goal is to provide an easy-to-use interface for applying common image operations and visualizing the results.

---

<a name="setup"></a>
## 2. Setup

<a name="docker-image"></a>
### 2.1 Docker image
Docker image gebruikt om deze code te runnen is te vinden op:  
```console
docker pull stijnvanvl/taaknumpy:latest
```
Indien u pycharm pro edition gebruikt kan u dit doen via:  
- > Ctrl+Alt+s 
- > Add:interpreter (dropdown) 
- > Select: On Docker...  
- > Select: Pull or use existing  
- > use image tag: "stijnvanvl/taaknumpy:latest"

Indien niet gebruik volgend command in de shell:

```console
docker run -it -v .:/taak_numpy stijnvanvl/taaknumpy:latest python /taak_numpy/main.py
``` 

<a name="maintaining-docker-image"></a>
### 2.2 Maintaining Docker image

- > nieuwe dependency in requirement.txt  
terminal:  
- > docker build -t taaknumpy .  
- > docker login   
- > docker tag taaknumpy stijnvanvl/taaknumpy:latest  
- > docker push stijnvanvl/taaknumpy:latest  

<a name="maintaining-github-project"></a>
### 2.3 Maintaining Github project

- >git add <file> # files die je wilt toevoegen waar je veranderingen hebt gedaan  
- >git commit -m "Message." #berichtje erbij vb datum/important changes  
- >git push (-u) origin main pushed naar de github link 
- >git remote add origin https://github.com/your-username/NumpyTaak.git
- >git init

---

<a name="classes"></a>
## 3. Classes
  
<a name="importasnparray"></a>
### 3.1. Importasnparray

The `Importasnparray` class is responsible for loading an image from a given path and converting it into a NumPy array for manipulation. This class allows further transformations and operations to be applied to the image.
  
<a name="constructor"></a>
#### 3.1.1 Constructor

The constructor initializes the image data from a file path, converts it to the RGB format, and stores it as a NumPy array.

- `np_array`: Stores the image as a NumPy array.
- `transformations_used`: Tracks the transformations applied to the image.
- `path_to_image`: Path to the image file (optional).

---
  
<a name="transformations"></a>
### 3.2. Transformations

The `Transformations` class provides a variety of image manipulation methods. These methods apply basic transformations like flipping, filtering, resizing, and convolution to the image.
  
<a name="methods"></a>
#### 3.2.1 Methods

- **upside_down**: Flips the image vertically.
- **left_to_right**: Flips the image horizontally.
- **diagonal**: Combines both upside down and left to right flips.
- **red_filter**: Removes the green and blue channels, leaving only the red channel visible.
- **green_filter**: Removes the red and blue channels, leaving only the green channel visible.
- **blue_filter**: Removes the red and green channels, leaving only the blue channel visible.
- **empty**: Replaces all pixels with zeros (black image).
- **resize_horizontally**: Resizes the image horizontally by a factor.
- **resize_vertically**: Resizes the image vertically by a factor.
- **resize**: Resizes the image both horizontally and vertically using a tuple of factors.
- **convolve**: Applies a kernel (such as a Gaussian or sharpen filter) to the image via convolution.

---
  
<a name="kernel"></a>
### 3.3. Kernel

The `Kernel` class and its subclasses define various convolution kernels used for filtering operations.
  
<a name="identity-kernel"></a>
#### 3.3.1 Identity Kernel

The `Identity` kernel class defines an identity filter. It is used to return the image unchanged when applied.

- `np_kernel`: A 2D array with a single 1 in the center (identity).
  
<a name="gaussian-kernel"></a>
#### 3.3.2 Gaussian Kernel

The `GaussianKernel` class defines a Gaussian filter for blurring. The kernel is based on a specified size and sigma value.

- `np_kernel`: A 2D Gaussian kernel created from a function of the size and sigma.
  
<a name="ridge-kernel"></a>
#### 3.3.3 Ridge Kernel

The `RidgeKernel` class defines a kernel for edge detection, often referred to as the Laplacian filter.

- `np_kernel`: A 3x3 kernel used to detect edges.
  
<a name="sharpen-kernel"></a>
#### 3.3.4 Sharpen Kernel

The `Sharpen` class defines a sharpening kernel that enhances the edges and details in an image.

- `np_kernel`: A 5x5 kernel that highlights edges for sharpening.
  
<a name="boxblur-kernel"></a>
#### 3.3.5 BoxBlur Kernel

The `BoxBlur` class defines a simple blur kernel by averaging pixel values in a square window.

- `np_kernel`: A 2D array of ones that is normalized for averaging.

---
  
<a name="imagehandler"></a>
### 3.4. ImageHandler

The `ImageHandler` class manages the image and applies sequences of transformations. It also provides a method to fill and transform a grid of images, generating a final image.
  
<a name="methods"></a>
#### 3.4.1 Methods

- **apply_transformation_sequence**: Applies a sequence of transformations from a CSV string, interpreting operations such as resizing and convolution with specific kernels.
- **create_transformed_grid_elements**: Creates a list of transformed grid elements based on a provided grid configuration.
- **filling_engine_hardcoded**: Combines the transformed grid elements into a final output image.
- **complete_input_grid**: Automatically fills in missing grid elements marked as "filled" or "empty."
- **plot_grid**: Displays the final image by plotting the grid of transformed images.

---
