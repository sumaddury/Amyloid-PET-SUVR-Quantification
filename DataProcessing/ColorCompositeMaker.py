import os
import pydicom
import png
import shutil
import glob
import numpy as np
from PIL import Image

DCMROOT = "C:\\Users\\sumad\\OneDrive - San José Unified School District\\Documents\\AMYLOID DATASET COMPLETE ALL\\AllAmyloidProcessedSeperated"
dcmPathName = os.path.join(DCMROOT, "*")
dcmDirList = glob.glob(dcmPathName)


dcmList = {}
for d in dcmDirList:
    currDir = os.path.join(d, "*")
    ID = currDir[127:(len(currDir)-2)]
    currFileList = glob.glob(currDir)
    if len(currFileList) != 3:
        errString = "Directory: " + d + " does not have 3 files"
        raise ValueError(errString)
    dcmList[ID] = [currFileList[0], currFileList[1], currFileList[2]]
print(len(dcmList))


IMGROOT = "C:\\Users\\sumad\\OneDrive - San José Unified School District\\Documents\\AMYLOID DATASET COMPLETE ALL\\AllAmyloidProcessedSeperatedPNG"
if os.path.exists(IMGROOT):
    shutil.rmtree(IMGROOT) 
os.makedirs(IMGROOT)

for f in dcmList:
    os.makedirs(IMGROOT+"\\"+f)
    for img in dcmList[f]:
        imageFile = os.path.basename(img)
        imageFile = imageFile.replace(".dcm", ".png")
        print(imageFile)
    #ds = pydicom.dcmread(f)
    #imageData = ds.pixel_array
    #cv2.imwrite(os.path.join(JPGROOT, imageFile), imageData)
    
        ds = pydicom.dcmread(img)
        shape = ds.pixel_array.shape

    # Convert to float to avoid overflow or underflow losses.  
        image_2d = ds.pixel_array.astype(float)

    # Rescaling grey scale between 0-255
        image_2d_scaled = (np.maximum(image_2d,0) / image_2d.max()) * 255.0
    
    # Convert to uint
        image_2d_scaled = np.uint8(image_2d_scaled)
    #IMGROOT+"\\"+f+"Slice"+str(count)
        with open(os.path.join("C:\\Users\\sumad\\OneDrive - San José Unified School District\\Documents\\AMYLOID DATASET COMPLETE ALL\\AllAmyloidProcessedSeperatedPNG",f,"Slice"+imageFile[97:99]+'.png'), 'wb') as png_file:
            w = png.Writer(shape[1], shape[0], greyscale=True)
            w.write(png_file, image_2d_scaled)

def load_images_to_single(path_a, path_b, path_c, size=(160, 160)):

    # load images as grayscale
    img_a = np.array(Image.open(path_a).convert('L').resize(size))
    img_b = np.array(Image.open(path_b).convert('L').resize(size))
    img_c = np.array(Image.open(path_c).convert('L').resize(size))

    # map images to channels as:
    #     img_a -> R channel
    #     img_b -> G channel
    #     img_c -> B channel
    img_rgb = np.dstack([img_a, img_b, img_c])

    return img_rgb

masterPath = "C:\\Users\\sumad\OneDrive - San José Unified School District\\Documents\\AMYLOID DATASET COMPLETE ALL\\AllAmyloidProcessedSeperatedPNG"
outPath = "C:\\Users\\sumad\OneDrive - San José Unified School District\\Documents\\AMYLOID DATASET COMPLETE ALL\\Full Set\\AllAmyloidProcessedRGBV2"

for root, dirs, files in os.walk(masterPath):
    imgroot, imgdirs = root, dirs
    break

y = []
for patient in dirs:
    y.append(imgroot + "\\" + patient)

os.chdir(outPath)
for path in y:
    for root, dirs, files in os.walk(path):
        x = {}
        for img in files:
            x[img] = root + "\\" + img
        rgbimage = load_images_to_single(x['Slice36.png'], x['Slice48.png'], x['Slice60.png'])
        im = Image.fromarray(rgbimage)
        im.save(os.path.basename(path)+'.png')
        break