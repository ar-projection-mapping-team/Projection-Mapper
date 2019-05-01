import cv2
import numpy as np


class OutlineCalibration:

    def __init__(self, input_image, w, h):

        # INIT IMAGES #
        #   Save original image, edge-detected greyscale image, and edge-detected color image:
        self.image = input_image
        #   Save width and height of image:
        self.width = w
        self.height = h
        #   Call function to create the edge detected images, with the default thresholds.
        self.create_edge_image(240)

    # Updates the threshold for the Canny edge detector and re-defines the image variables
    def create_edge_image(self, thresh):

        # UPDATE IMAGES #
        self.edge_image = cv2.Canny(self.image, 100, thresh)
        self.edge_color = cv2.cvtColor(self.edge_image, cv2.COLOR_GRAY2RGB)

        # CREATE EDGE PIXEL LOCATION LIST #
        #   Create list that holds locations of pixels that belong to an edge:
        self.edges = []
        for i in range(self.height):
            for j in range(self.width):
                if self.edge_image[i, j] == 255:
                    self.edges.append((i, j))
        #   Create list that holds locations of pixels bordering edges:
        self.border_edges = []
        for x in range(len(self.edges)):
            (i, j) = self.edges[x]
            if j != 0:
                n = (i, j - 1)
                self.border_edges.append(n)
            if i != self.height - 1:
                e = (i + 1, j)
                self.border_edges.append(e)
            if j != self.width - 1:
                s = (i, j + 1)
                self.border_edges.append(s)
            if i != 0:
                w = (i - 1, j)
                self.border_edges.append(w)

    # Applies shader to a single frame of the object edge calibration output
    def shade_frame(self, itr):

        # GENERATE A SHADED FRAME #
        #   Copy the RGB edge-detected image:
        shaded_image = self.edge_color
        #   Iterate through each pixel belonging to a edge, and color it:
        for i in range(len(self.border_edges)):
            shaded_image[self.border_edges[i]] = (0 + itr, 255 - itr, 0+itr)
        for i in range(len(self.edges)):
            shaded_image[self.edges[i]] = (50 + itr, 255 - itr, 50+itr)
        #   Return the shaded frame:
        return shaded_image

    # Shows the object edge calibration video
    def show_outlines(self):

        # DISPLAY THE SHADED CALIBRATION OUTPUT #
        #   Initialize a iterator that will be responsible for changing colors over time:
        itr = 0
        #   Initialize a switch that will force iterator to count down/up from a value that is invalid:
        up = True
        #   Loop to display video:
        while(True):
            #   Resets the iterator when it reaches a value that will generate a out-of-bounds color value:
            if itr == 0:
                up = True
            elif itr == 128:
                up = False
            #   Displays a single shaded image frame:
            cv2.imshow('Object Edge Calibration', self.shade_frame(itr))
            cv2.waitKey(1)
            #   Iterates the color-changer:
            if up:
                itr += 4
            else:
                itr -= 4
