import cv2

class Shader:

    def __init__(self, source_path):

        # GET SOURCE IMAGE #
        self.source = cv2.imread(source_path, 0)
        self.source_height, self.source_width = self.source.shape[:2]




    def create_shader(self, shader_threshold):

        # INITIALIZE SHADER EDGE PIXEL LISTS #
        self.edges = []
        self.border_edges = []

        # UPDATE IMAGE #
        self.shader = cv2.Canny(self.source, 100, shader_threshold)
        self.edge_color = cv2.cvtColor(self.shader, cv2.COLOR_GRAY2RGB)

        # CREATE EDGE PIXEL LOCATION LIST #
        # Create list that holds locations of pixels that belong to an edge:
        for i in range(self.source_height):
            for j in range(self.source_width):
                if self.shader[i,j] == 255:
                    self.edges.append((i,j))
        # Create list that holds locations of pixels bordering edges:
        for x in range(len(self.edges)):
            (i, j) = self.edges[x]
            if j != 0:
                n = (i, j - 1)
                self.border_edges.append(n)
            if i != self.source_height - 1:
                e = (i + 1, j)
                self.border_edges.append(e)
            if j != self.source_width - 1:
                s = (i, j + 1)
                self.border_edges.append(s)
            if i != 0:
                w = (i - 1, j)
                self.border_edges.append(w)


    def shade_frame(self, itr):

        # GENERATE A SHADED FRAME #
        #   Copy the RGB edge-detected image:
        shaded_image = self.edge_color
        #   Iterate through each pixel that borders an edge and color it:
        for i in range(len(self.border_edges)):
            shaded_image[self.border_edges[i]] = (0 + itr, 255 - itr, 0 + itr)
        #   Iterate through each pixel belonging to an edge and color it:
        for i in range(len(self.edges)):
            shaded_image[self.edges[i]] = (50 + itr, 255 - itr, 50 + itr)
        #   Return the shaded frame:
        return shaded_image


    def show_shader(self):

        # DISPLAY THE SHADER #
        # Initialize a iterator that will be responsible for changing colors over time:
        itr = 0
        # Initialize a switch that will force iterator to count down/up from a value that is invalid:
        up = True
        # Loop to display video:
        while (True):
            # Resets the iterator when it reaches a value that will generate a out-of-bounds color value:
            if itr == 0:
                up = True
            elif itr == 128:
                up = False
            # Displays a single shaded image frame:
            cv2.imshow('Shader', self.shade_frame(itr))
            cv2.waitKey(1)
            # Iterates the color-changer:
            if up:
                itr += 4
            else:
                itr -= 4
