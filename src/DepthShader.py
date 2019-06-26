import cv2

class Depth_Shader:

        def __init__(self, source_path):

            # GET SOURCE IMAGE #
            self.source = cv2.imread(source_path, 0)
            self.source_height, self.source_width = self.source.shape[:2]
        def show_depth_shader(self):

            cv2.imshow('Depth_Shader', self.source)
            cv2.waitKey(0)
