import os
import glob

# obtener los filepaths
images = sorted(glob.glob('*.jpeg'), key=os.path.getmtime)

for i,image in enumerate(images):
    aux_name = str(i) + '.jpeg'
    os.rename(image, aux_name)


