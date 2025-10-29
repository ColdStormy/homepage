import os
from pathlib import Path
import json
import glob
from typing import Set
from PIL import Image, ExifTags

####################################################
######## DEFINITIONS ###############################
####################################################

IN_PATH_ORIGINALS = "assets/original/"
OUT_PATH_THUMBNAILS = "static/images/thumbnails"
OUT_PATH_SHOWCASE = "static/images/showcase"
PATH_DATABASE = "static/images/database.json"
MAX_SIZE = (1920, 1920) # width, height
THUMB_SIZE = (500, 500) # width, height
class ImageData:
    width: int = -1
    height: int = -1

    def __init__(self, originalFilePath: str):
        self.originalFilePath = originalFilePath
        self.name = Path(originalFilePath).stem
        
        self.imageID = self.name.split(".")[0]
        self.thumbnailFilePath = f"{OUT_PATH_THUMBNAILS}/{self.name}.jpg"
        self.showcaseFilePath = f"{OUT_PATH_SHOWCASE}/{self.name}.jpg"

    def __eq__(self, other):
        return self.imageID == other.imageID

    def __hash__(self):
        return hash(self.imageID)
    
    def aspectRatio(self):
        return self.width / self.height
    
    def toJSON(self):
        return {
            self.imageID: {
                "name": self.name,
                "imageID": self.imageID,
                "originalFilePath": self.originalFilePath,
                "thumbnailFilePath": self.thumbnailFilePath.replace("static/", ""),
                "showcaseFilePath": self.showcaseFilePath.replace("static/", ""),
                "width": self.width,
                "height": self.height,
                "aspectRatio": self.aspectRatio()
            }
        }

listOfImages: Set[ImageData] = set()


def addImage(img: ImageData):
    if img in listOfImages:
        raise ValueError(f"Duplicate imageID found: {img.imageID}")
    listOfImages.add(img)

def jsonify():
    db = {}
    for img in listOfImages:
        db.update(img.toJSON())
    return db

def serializeDatabase():
    if os.path.exists(PATH_DATABASE):
        os.remove(PATH_DATABASE)
    database_json = jsonify()
    with open(PATH_DATABASE, "w") as f:
        json.dump(database_json, f, indent=4)

####################################################
######## SCRIPT LOGIC ##############################
####################################################

for filename in os.listdir(IN_PATH_ORIGINALS):
    if any(filename.endswith(ext) for ext in [".jpg", ".png", ".jpeg", ".tif"]):
        addImage(ImageData(os.path.join(IN_PATH_ORIGINALS, filename)))

print(f"Found {len(listOfImages)} images.")

for folder in [OUT_PATH_SHOWCASE, OUT_PATH_THUMBNAILS]:
    for file in glob.glob(os.path.join(folder, "*")):
        if os.path.isfile(file):
            os.remove(file)

thumbnail_path = os.path.join(OUT_PATH_THUMBNAILS)
os.makedirs(os.path.dirname(thumbnail_path), exist_ok=True)
showcase_path = os.path.join(OUT_PATH_SHOWCASE)
os.makedirs(os.path.dirname(showcase_path), exist_ok=True)

count = 0
for imageData in listOfImages:
    with Image.open(imageData.originalFilePath) as img:
        aspRatio = min(MAX_SIZE[0] / img.width, MAX_SIZE[1] / img.height)
        new_size = (int(img.width * aspRatio), int(img.height * aspRatio))
        img.resize(new_size, Image.Resampling.LANCZOS)
        img.save(imageData.showcaseFilePath)

        img.thumbnail(THUMB_SIZE)
        img.save(imageData.thumbnailFilePath)

        imageData.width, imageData.height = img.size

        exif = {
            ExifTags.TAGS.get(k, k): v
            for k, v in img._getexif().items()
        } if hasattr(img, "_getexif") and img._getexif() else {}

    count += 1
    print(f"Processed {count}/{len(listOfImages)}: {imageData.name}")

serializeDatabase()