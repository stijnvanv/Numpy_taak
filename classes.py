from abc import abstractclassmethod, abstractmethod, ABC
import numpy as np
from PIL import Image
import matplotlib.pyplot as plt
import re


class ImageAsNpArray:
    def __init__(self, path_to_image=None):
        self.np_array = None
        self.transformations_used = []
        if path_to_image:
            self.np_array = np.array(Image.open(path_to_image).convert("RGB"))

    @classmethod
    def from_transformation(cls, np_array, str_transformation, previous_instance=None):
        obj = cls.__new__(cls)
        obj.__init__()
        obj.np_array = np_array
        if previous_instance:
            obj.transformations_used = previous_instance.transformations_used.copy()
            obj.transformations_used.append(str_transformation)
        return obj

    def apply_transformation(self, transformation_function, *args):
        np_array = transformation_function(self.np_array, *args)
        str_transformation = transformation_function.__name__ + " from " + type(
            transformation_function.__self__).__name__
        self.transformations_used.append(str_transformation)
        print(self.make_plot_title() + " executed!")
        self.transformations_used.pop()
        return ImageAsNpArray.from_transformation(np_array, str_transformation, self)

    def make_plot_title(self):
        title_str = ""
        for transformation in self.transformations_used:
            if title_str:
                title_str = transformation + " after " + title_str
            else:
                title_str = transformation
        return title_str.capitalize()

    def plot(self):
        if self.transformations_used:
            plt.title(self.make_plot_title())
        else:
            plt.title("Original picture")
        plt.imshow(self.np_array)
        plt.show()


class Transformations:
    def __init__(self):
        pass

    def upside_down(self, np_array):
        return np_array[::-1,:,:]

    def left_to_right(self, np_array):
        return np_array[:, ::-1,:]

    def diagonal(self, np_array):
        return self.upside_down(self.left_to_right(np_array))

    def red_filter(self, np_array):
        np_array = np_array.copy()
        np_array[:,:,1] = 0
        np_array[:,:,2] = 0
        return np_array

    def green_filter(self, np_array):
        np_array = np_array.copy()
        np_array[:,:,0] = 0
        np_array[:,:,2] = 0
        return np_array

    def blue_filter(self, np_array):
        np_array = np_array.copy()
        np_array[:,:,0] = 0
        np_array[:,:,1] = 0
        return np_array

    def empty(self, np_array):
        np_array = np.zeros_like(np_array)
        return np_array

    def resize_horizontally(self, np_array, factor):
        return np.repeat(np_array, factor, axis=1)

    def resize_vertically(self, np_array, factor):
        return np.repeat(np_array, factor, axis=0)

    def resize(self, np_array, factors):
        return self.resize_vertically(self.resize_horizontally(np_array, factors[0]), factors[1])

    def convolve(self, np_array, np_kernel):
        pad_height = np_kernel.shape[0] // 2
        pad_width = np_kernel.shape[1] // 2
        padded_image = np.pad(np_array, ((pad_height, pad_height), (pad_width, pad_width), (0, 0)), mode='constant',
                              constant_values=0)
        np_array_out = np.zeros_like(np_array)

        #convololutie loop alle rgb-waarden apart??
        for channel in range(np_array.shape[2]):
            for i in range(np_array.shape[0]):
                for j in range(np_array.shape[1]):
                    region = padded_image[i:i + np_kernel.shape[0], j:j + np_kernel.shape[1], channel]
                    np_array_out[i, j, channel] = np.sum(region * np_kernel)

        np_array_out = np.clip(np_array_out, 0, 255).astype(np.uint8)
        print("i convolved")
        return np_array_out


class Kernel:
    def __init__(self):
        self.name = None
        self.np_kernel = None
        self.create_np_kernel()

    def normalise(self):
        self.np_kernel = self.np_kernel/np.sum(self.np_kernel)

    def __str__(self):
        return f"{self.np_kernel}"

    @abstractmethod
    def create_np_kernel(self):
        pass

class Identity(Kernel, ABC):
    def __init__(self, size = 3):
        super().__init__()
        self.name = "identity"
        self.size = size
        self.create_np_kernel()

    def create_np_array(self):
        np_array = np.zeros((self.size, self.size))
        loc = self.size // 2
        np_array[loc,loc] = 1

class GaussianKernel(Kernel, ABC):
    def __init__(self, sigma = 1, size = 5):
        super().__init__()
        self.name = "gauss"
        self.sigma = sigma
        self.size = size
        self.create_np_array()
        self.normalise()

    def create_np_array(self):
        self.np_kernel = np.fromfunction(
            lambda x, y: (1 / (2 * np.pi * self.sigma ** 2)) * np.exp(
                - ((x - (self.size - 1) / 2) ** 2 + (y - (self.size - 1) / 2) ** 2) / (2 * self.sigma ** 2)),
            (self.size, self.size)
        )

class RidgeKernel(Kernel, ABC):
    def __init__(self):
        super().__init__()
        self.name = "ridge"
        self.create_np_array() #geen normalisatie hier!!

    def create_np_array(self):
        self.np_kernel = np.array([[0, -1, 0],
                  [-1, 4, -1],
                  [0, -1, 0]])

class Sharpen(Kernel, ABC):
    def __init__(self):
        super().__init__()
        self.name = "sharpen"
        self.create_np_array()

    def create_np_array(self):
        #idialiter id-laplaciaan
        self.np_kernel = np.array([[0,0,-1,0,0],
                                   [0,-1, -2, -1, 0],
                                   [-1,-2, 17,-2, -1],
                                   [0, -1,-2,-1, 0],
                                   [0,0,-1,0,0]])

class BoxBlur(Kernel, ABC):
    def __init__(self, size):
        super().__init__()
        self.name = "boxblur"
        self.size = size
        self.create_np_array()
        self.normalise()

    def create_np_array(self):
        self.np_kernel = np.ones((self.size, self.size))


class ImageHandler:
    def __init__(self, image_path):
        self.image = ImageAsNpArray(image_path)
        self.transformations = Transformations()

    def apply_transformation_sequence(self, transformations_as_csv_string):
        pattern = re.compile(r'([a-zA-Z_]+(?:\([^\)]*\))?)')
        transformations = pattern.findall(transformations_as_csv_string)
        print(transformations)
        x = self.image
        for transformation in transformations:
            match_resize = re.search(r'resize\((\d+),(\d+)\)', transformation)
            match_convolve = re.search(r"convolve\((\w+)(?:,\s*(\d+))?(?:,\s*(\d+))?\)", transformation)
            if match_resize:
                params = [int(match_resize.group(1)), int(match_resize.group(2))]
                transformation = "resize"
                x = x.apply_transformation(getattr(self.transformations, transformation), params)
            elif match_convolve:
                kernel_type = match_convolve.group(1)
                transformation = "convolve"
                print(kernel_type)
                if kernel_type == "identity":
                    size = int(match_convolve.group(2))
                    kernel = Identity(size)
                elif kernel_type == "gauss":
                    sigma, size = int(match_convolve.group(2)), int(match_convolve.group(3))
                    kernel = GaussianKernel(sigma, size)
                elif kernel_type == "ridge":
                    kernel = RidgeKernel()
                elif kernel_type == "sharpen":
                    kernel = Sharpen()
                elif kernel_type == "boxblur":
                    size = int(match_convolve.group(2))
                    kernel = BoxBlur(size)
                else:
                    raise ValueError(f"Unsupported kernel type: {kernel_type}")
                x = x.apply_transformation(getattr(self.transformations, transformation), kernel.np_kernel)
            else:
                x = x.apply_transformation(getattr(self.transformations, transformation))
        return x

    def create_transformed_grid_elements(self, grid):
        transformed_elements = []
        for i, row in enumerate(grid):
            for j, item in enumerate(row):
                if item != "filled":
                    transformed_element = self.apply_transformation_sequence(item).np_array
                    transformed_elements.append((transformed_element,i,j))
        return transformed_elements

    def filling_engine_hardcoded(self, grid):
        base_x, base_y, base_z = self.image.np_array.shape[0], self.image.np_array.shape[1], self.image.np_array.shape[2]
        x,y,z = (len(grid)*base_x,
                 len(grid[0])*base_y,
                 base_z)
        np_array_grid = np.zeros((x, y, z), dtype=np.uint8)
        grid_elements = self.create_transformed_grid_elements(grid)
        for item in grid_elements:
            np_array_grid[base_x*item[1]:base_x*item[1] + item[0].shape[0], base_y*item[2]:base_y*item[2] + item[0].shape[1]] = item[0]
        return np_array_grid

    def complete_input_grid(self,grid):
        """
        Attempt to fill in "filled" and "empty" automatically.
        """
        def extract_resize_values(command):
            pass
        pass

    def plot_grid(self, transformation_grid):
        """
        Apply transformations based on the grid and then display the resulting image.
        """
        final_image = self.filling_engine_hardcoded(transformation_grid)
        print(final_image.shape)
        plt.imshow(final_image)
        plt.title("Transformed Image Grid")
        plt.show()

