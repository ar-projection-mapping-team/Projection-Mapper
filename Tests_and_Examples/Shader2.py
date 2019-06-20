import cv2


class Shader:

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

        # Create list of pixels (using HSV color space) for the shader
        canny_filter = cv2.Canny(self.source, 100, threshold)
        #canny_filter = cv2.Sobel(self.source, cv2.CV_8U, 1, 0, ksize=3)
        x = cv2.cvtColor(canny_filter, cv2.COLOR_GRAY2RGB)
        self.shader_image = cv2.cvtColor(x, cv2.COLOR_RGB2HSV)

        # Create list that holds locations of pixels that belong to an edge
        for i in range(self.source_height):
            for j in range(self.source_width):
                if self.shader_image[i, j][2] != 0:
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

        # Define flag for changing the iterator value
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
