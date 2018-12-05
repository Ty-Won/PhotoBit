from PIL import Image
import numpy as np
import os
import cv2 as cv

class TileProcessor:

    def __init__(self,img_collection_path):
        self.img_collection_path=img_collection_path


    def retrieve_tiles(self, tile_collection, compress_size_x, compress_size_y):
        collection_path=self.img_collection_path
        collection={}
        for root, folders, files in os.walk(collection_path):
            for img in files:
                print(img)
                file_path = os.path.join(root,img)
                img_array = cv.imread(file_path)
                avg_rgb = int(self.process(img_array,compress_size_x,compress_size_y))
                if avg_rgb in collection:
                    collection[avg_rgb].append(img)
                else:
                    collection[avg_rgb]=[]
                
                
                # Displays the current image
                # cv.namedWindow(img, cv.WINDOW_NORMAL)
                # cv.imshow(img,self.process(img_array,compress_size_x,compress_size_y))
                # cv.waitKey(0)
                # cv.destroyAllWindows()

        
            #file_path = os.path.join(root,files)
            # rgb_img_arr = cv.imread(files, mode='RGB')
            # print (rgb_img_arr)
        print(collection)
                


    
    def process(self,img_rgb_array, compressed_width,compressed_height):
        reduced_dim_img = cv.resize(img_rgb_array, dsize=(compressed_width,compressed_height),interpolation=cv.INTER_AREA)
        rgb_avg = np.array(reduced_dim_img).mean(axis=(0,1,2))
        return rgb_avg
                


if __name__=="__main__":
    # img = Image.open("./mosaic.jpeg")
    # img.convert('RGB')
    directory = TileProcessor("./tiles")
    directory.retrieve_tiles("./tiles",100,100)
    
        
    
