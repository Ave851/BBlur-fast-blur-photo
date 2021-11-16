from PIL import Image, ImageFilter
import os
import re
        
        
class BBlur():
    
    #Simple blur
    def imgBlur(self, img_dir):
        self.img_dir = img_dir
        
        #open image
        img = Image.open(self.img_dir)
        f, e = os.path.splitext(self.img_dir)
        #add blur
        blur_img = img.filter(ImageFilter.BLUR)
        #rename image
        if re.search(r".jpg", self.img_dir):
            blur_img.save(f + "_blurred.jpg")
            
        elif re.search(r".png", self.img_dir):
            blur_img.save(f + "_blurred.png")

        
    #Box blur
    def imgBoxBlur(self, img_dir, img_num):
        self.img_dir = img_dir
        self.img_num = img_num
        
        #open image
        img = Image.open(self.img_dir)
        f, e = os.path.splitext(self.img_dir)
        #add blur
        box_blur_img = img.filter(ImageFilter.BoxBlur(self.img_num))
        #rename image
        if re.search(r".jpg", self.img_dir):
            box_blur_img.save(f + "_box_blurred.jpg")
        elif re.search(r".png", self.img_dir):
            box_blur_img.save(f + "_box_blurred.png")

        
    #Gaussian blur    
    def imgGausBlur(self, img_dir, img_num):
        self.img_dir = img_dir
        self.img_num = img_num
        
        #open image
        img = Image.open(self.img_dir)
        f, e = os.path.splitext(self.img_dir)
        #add blur
        gaus_blur_img = img.filter(ImageFilter.GaussianBlur(self.img_num))
        #rename image
        if re.search(r".jpg", self.img_dir):
            gaus_blur_img.save(f + "_gaus_blurred.jpg")
        elif re.search(r".png", self.img_dir):
            gaus_blur_img.save(f + "_gaus_blurred.png")


