import os
import json
from typing import Set
from PIL import Image, ExifTags

####################################################
######## DEFINITIONS ###############################
####################################################
imageIDList: Set[str] = set()

class ImageData:
    def __init__(self, originalFilePath: str):
        self.originalFilePath = originalFilePath
        self.name = os.path.basename(originalFilePath)
        
        self.imageID = self.name.split(".")[0]
        if self.imageID in imageIDList:
            raise ValueError(f"Duplicate imageID found: {self.imageID}")
        imageIDList.add(self.imageID)


listOfImages: Set[ImageData] = set()

####################################################
######## SCRIPT LOGIC ##############################
####################################################

# read existing database or create new one
if os.path.exists("assets/database.json"):
    with open("assets/database.json", "r") as f:
        database = json.load(f)
else:
    database = {"images": []}


# fetch images from input (assets/original/*)
input_directory = "assets/original/"
for filename in os.listdir(input_directory):
    if any(filename.endswith(ext) for ext in [".jpg", ".png", ".jpeg", ".tif"]):
        listOfImages.add(ImageData(os.path.join(input_directory, filename)))

print(f"Found {len(listOfImages)} images.")

# create a thumbnail for each image
for imageData in listOfImages:
    thumbnail_path = os.path.join("assets/thumbnails", imageData.name)
    os.makedirs(os.path.dirname(thumbnail_path), exist_ok=True)
    with Image.open(imageData.originalFilePath) as img:
        img.thumbnail((500, 500))
        img.save(thumbnail_path)

        exif = {
            ExifTags.TAGS.get(k, k): v
            for k, v in img._getexif().items()
        } if hasattr(img, "_getexif") and img._getexif() else {}

        print(exif)

        # wait for input to continue
        input("Press Enter to continue...")