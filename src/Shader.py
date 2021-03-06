import cv2


# DefaultShader: After identifying edges of an input image, draw the edges and iterate their color over time.
class DefaultShader:

    def __init__(self, source_path):

        # Get source image, as well as its height and width
        self.source = cv2.imread(source_path, 0)
        self.source_height, self.source_width = self.source.shape[:2]

        # Define shader image components:
        # shader_image refers to the entire image created by the shader, while shader_pixels refers to only the pixels
        # that belong to an edge of the Canny filter
        self.shader_image = []
        self.shader_pixels = []

    # Creates a new shader with specified threshold, brightness and contrast values
    # TODO: ADD FUNCTIONALITY FOR BRIGHTNESS AND CONTRAST
    def create_shader(self, threshold, brightness, contrast):

        # Re-initialize the list of shader pixels
        self.shader_pixels = []

        # Create list of pixels (using HSV color space) for the shader
        canny_filter = cv2.Canny(self.source, 100, threshold)
        x = cv2.cvtColor(canny_filter, cv2.COLOR_GRAY2RGB)
        self.shader_image = cv2.cvtColor(x, cv2.COLOR_RGB2HSV)

        # Create list that holds locations of pixels that belong to an edge
        for i in range(self.source_height):
            for j in range(self.source_width):
                if self.shader_image[i,j][2] != 0:
                    self.shader_pixels.append((i, j))

    # Generates a single frame of the shader
    def generate_frame(self, iterator, mod):

        # Copy the shaded image
        frame = self.shader_image

        # For each pixel actually belonging to an edge (each visible pixel only) apply the shader's effect over time
        # (this is controlled by the 'iterator' argument).
        for i in range(self.shader_pixels.__len__()):
            current_pixel_location = self.shader_pixels[i]
            frame[current_pixel_location][0] = iterator

        return frame

    # Shows the shader window
    # TODO: IMPLEMENT MODIFIER FUNCTIONALITY
    def show_shader(self):

        # Define the iterator and modifier values
        i = 0
        m = 0

        # Define flag for changing the iterator value (when hue channel reaches the max value of 179, decrement the
        # value rather then increment it to go back down through each hue value until 0.
        increment = True

        # Display frame after frame of the shader onto output window
        while True:

            # Create the current frame by calling the frame generator function with the iterator and modifier arguments
            current_frame = self.generate_frame(i, m)

            # Show the current frame, use waitKey to show it only for a small amount of time
            cv2.imshow('Shader', current_frame)
            cv2.waitKey(1)

            # Update iterator flag
            if increment and i == 179:
                increment = False
            if not increment and i == 0:
                increment = True

            # Update iterator value
            if increment:
                i += 1
            else:
                i -= 1


# DepthShader: Ranges color hue from a user's upper bound to lower bound depending on the depth of the pixel.
class DepthShader:

    def  __init__ (self, source_path):

        # Get source image, as well as its height and width
        self.source = cv2.imread(source_path, 0)
        self.source_height, self.source_width =self.source.shape[:2]

        # shader_image refers to the entire image created by the shader, which is what will be used to update the image
        x = cv2.cvtColor(self.source, cv2.COLOR_GRAY2RGB)
        self.shader_image = cv2.cvtColor(x, cv2.COLOR_RGB2HSV)

    # Creates a new shader with specified bounds, brightness and contrast values
    # TODO: ADD FUNCTIONALITY FOR BRIGHTNESS AND CONTRAST
    def create_shader(self, hue_upperbound, hue_lowerbound, brightness, contrast):

        # Get length of user's specified hue bound (amount of possible hue values to map to)
        range_user = hue_upperbound - hue_lowerbound

        # Maps values from the 8-bit greyscale depth map color space to the HSV color space used by the shader
        def mapping(value):
            return (float(value / 255) * range_user) + hue_lowerbound

        # Map each pixel's greyscale depth value to its corresponding HSV value according to the user's bounds, do this
        # by using the above mapping function for each pixel in the source image
        for i in range(self.source_height):
            for j in range(self.source_width):
                self.shader_image[i,j] = (int(mapping(self.source[i,j])), 100, 100)

    # Generates a single frame of the shader
    def generate_frame(self):
        return self.shader_image

    # Shows the shader window
    def show_shader(self):

        # Display frame after frame of the shader onto output window
        while True:

            # Create the current frame by calling the frame generator function with the iterator and modifier arguments
            current_frame = self.generate_frame()

            # Show the current frame, use waitKey to show it only for a small amount of time
            cv2.imshow('Depth_Shader', current_frame)
            cv2.waitKey(1)
