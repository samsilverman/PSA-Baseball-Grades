import os
from PIL import Image
import cv2

curr_dir = os.getcwd()

dirs = [
    f'{curr_dir}/PSA-Grades-Baseball/psa1',
    f'{curr_dir}/PSA-Grades-Baseball/psa2',
    f'{curr_dir}/PSA-Grades-Baseball/psa3',
    f'{curr_dir}/PSA-Grades-Baseball/psa4',
    f'{curr_dir}/PSA-Grades-Baseball/psa5',
    f'{curr_dir}/PSA-Grades-Baseball/psa6',
    f'{curr_dir}/PSA-Grades-Baseball/psa7',
    f'{curr_dir}/PSA-Grades-Baseball/psa8',
    f'{curr_dir}/PSA-Grades-Baseball/psa9',
    f'{curr_dir}/PSA-Grades-Baseball/psa10',
]

image_size = (150, 200)

for dir in dirs:
    for file in os.listdir(dir):
        # skip non-jpeg files/dirs
        if not file.endswith('.jpg'):
            continue

        filepath = dir + '/' + file
        image = Image.open(filepath)

        # rotate image if width > height
        if image.size[0] > image.size[1]:
            image = image.rotate(90, expand=True)

        # try to resize images to as close to 150x200 as possible
        image.thumbnail(image_size)

        # load the image with OpenCV
        image.save(filepath)
        image = cv2.imread(filepath)

        # find errors in image width and height from desired values of 150x200
        width_error = image_size[0] - image.size[0]
        height_error = mage_size[1] - image.size[1]

        # pad (using replication) based off the errors (evenly split for both sides of the image)
        image_replicate = cv2.copyMakeBorder(image, height_error//2, height_error-(height_error//2), width_error//2, width_error-(width_error//2), cv2.BORDER_REPLICATE)
        cv2.imwrite(filepath, image_replicate)