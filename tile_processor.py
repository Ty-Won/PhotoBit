from PIL import Image
import numpy as np
import os
import cv2 as cv

class TileProcessor:

    def __init__(self, tile_dimension):
        self.tile_dimension = tile_dimension


    def retrieve_tiles(self, img_collection_path):
        collection_path=img_collection_path
        collection={}
        for root, folders, files in os.walk(collection_path):
            for img in files:
                print(img)
                file_path = os.path.join(root,img)
                img_array = cv.imread(file_path)
                
                # cv.namedWindow(img,cv.WINDOW_NORMAL)
                # cv.imshow(img,img_array)
                # cv.waitKey(0)
                # cv.destroyAllWindows()

                avg_rgb = self.process(img_array, self.tile_dimension)
                if avg_rgb in collection:
                    collection[avg_rgb].append(img)
                else:
                    collection[avg_rgb]=[img]
                
        return collection
    


    


    
    def process(self,img_rgb_array, tile_size):
        reduced_dim_img = downscale(img_rgb_array,tile_size)
        rgb_avg = int(np.array(reduced_dim_img).mean(axis=(0,1,2)))
        return rgb_avg

# #Used to cut down image into a square tile to solve different image dimensions
def downscale(img_array, tile_size):
    return cv.resize(img_array, dsize=(tile_size,tile_size), interpolation=cv.INTER_AREA)



if __name__=="__main__":
    # img = Image.open("./mosaic.jpeg")
    # img.convert('RGB')
    directory = TileProcessor(50)
    directory.retrieve_tiles("./tiles")
    
        
    
