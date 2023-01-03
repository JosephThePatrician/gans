import numpy as np
import cv2
from PIL import Image

def show_img(img, resize=(256, 256), grid=5):
    
    if (type(img) is str) or (isinstance(img, Path)):
        img = cv2.imread(str(img))
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    
    elif type(img) is not np.ndarray:
        
        if (type(img[0]) is str) or (isinstance(img[0], Path)):
            imgs = []
            for path in img:
                temp_img = cv2.imread(str(path))
                temp_img = cv2.cvtColor(temp_img, cv2.COLOR_BGR2RGB)
                
                imgs.append(temp_img)
                
            img = imgs
        
        lines_of_imgs = []
        for i in range(ceil(len(img) / grid)):
            
            lines_of_imgs.append(
                np.hstack(img[i * grid : (i + 1) * grid])
            )
            
        lack = lines_of_imgs[0].shape[1] - lines_of_imgs[-1].shape[1]
        if lack > 0:
            temp = lines_of_imgs[0][:, 0 : lack, :].copy()
            temp[:] = 255
            lines_of_imgs[-1] = np.hstack([lines_of_imgs[-1], temp])
            
        img = np.vstack(lines_of_imgs)

    
    img = img.astype("uint8")
    
    if resize:
        img = cv2.resize(img, resize)

    return Image.fromarray(img)