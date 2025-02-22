# Numpy taak - Stijn Van Vlaenderen

## Content Table
1. [Intro](#1-intro)
2. [Setup](#2-setup)  
2.1 [Docker image](#21-docker-image)  
2.2 [Maintaining Docker image](#22-maintaining-docker-image)  
2.3 [Maintaining Github project](#23-maintaining-github-project)  
3. [Classes](#3-classes)  
3.1 [ImportAsNpArray](#31-importasnparray)  
&emsp;3.1.1 [Constructor](#311-constructor)  
3.2 [Transformations](#32-transformations)  
&emsp;3.2.1 [Methods](#321-methods)  
3.3 [Kernel](#33-kernel)  
&emsp;3.3.1 [Identity Kernel](#331-identity-kernel)  
&emsp;3.3.2 [Gaussian Kernel](#332-gaussian-kernel)  
&emsp;3.3.3 [Ridge Kernel](#333-ridge-kernel)  
&emsp;3.3.4 [Sharpen Kernel](#334-sharpen-kernel)  
&emsp;3.3.5 [BoxBlur Kernel](#335-boxblur-kernel)  
3.4 [ImageHandler](#34-imagehandler)  
&emsp;3.4.1 [Methods](#341-methods)
4. [Usage](#4-usage)   
4.1 [Grid construction](#41-grid-construction)  
4.2 [Example composed picture](#42-example-composed-picture)  
4.3 [All options overview](#43-all-options-overview)  

## 1. Intro

This project involves using NumPy for image manipulation tasks. The focus is on converting images into NumPy arrays, applying various transformations, and using convolutional operations to manipulate image data. The goal is to provide an easy-to-use interface for applying common image operations and visualizing the results.

---


## 2. Setup


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


### 2.2 Maintaining Docker image

- > nieuwe dependency in requirement.txt  
terminal:  
- > docker build -t taaknumpy .  
- > docker login   
- > docker tag taaknumpy stijnvanvl/taaknumpy:latest  
- > docker push stijnvanvl/taaknumpy:latest  


### 2.3 Maintaining Github project

- >git add <file> # files die je wilt toevoegen waar je veranderingen hebt gedaan  
- >git commit -m "Message." #berichtje erbij vb datum/important changes  
- >git push (-u) origin main pushed naar de github link 
- >git remote add origin https://github.com/your-username/NumpyTaak.git
- >git init

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
  
#### 3.3.1 Identity Kernel

The `Identity` kernel class defines an identity filter. It is used to return the image unchanged when applied.

- `np_kernel`: A 2D array with a single 1 in the center (identity).
  
#### 3.3.2 Gaussian Kernel

The `GaussianKernel` class defines a Gaussian filter for blurring. The kernel is based on a specified size and sigma value.

- `np_kernel`: A 2D Gaussian kernel created from a function of the size and sigma.
  
#### 3.3.3 Ridge Kernel

The `RidgeKernel` class defines a kernel for edge detection, often referred to as the Laplacian filter.

- `np_kernel`: A 3x3 kernel used to detect edges.
  
#### 3.3.4 Sharpen Kernel

The `Sharpen` class defines a sharpening kernel that enhances the edges and details in an image.

- `np_kernel`: A 5x5 kernel that highlights edges for sharpening.
  
#### 3.3.5 BoxBlur Kernel

The `BoxBlur` class defines a simple blur kernel by averaging pixel values in a square window.

- `np_kernel`: A 2D array of ones that is normalized for averaging.

---
  
### 3.4. ImageHandler

The `ImageHandler` class manages the image and applies sequences of transformations. It also provides a method to fill and transform a grid of images, generating a final image.
  
#### 3.4.1 Methods

- `apply_transformation_sequence`: Applies a sequence of transformations from a CSV string, interpreting operations such as resizing and convolution with specific kernels.
- `create_transformed_grid_elements`: Creates a list of transformed grid elements based on a provided grid configuration.
- `filling_engine_hardcoded`: Combines the transformed grid elements into a final output image.
- `complete_input_grid`: Automatically fills in missing grid elements marked as "filled" or "empty."
- `plot_grid`: Displays the final image by plotting the grid of transformed images.

---

## 4. Usage
### 4.1 Grid construction
### 4.2 Example composed picture
### 4.3 All options overview

---
