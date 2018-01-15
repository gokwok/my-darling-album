from PIL import Image
import process
import shutil
import os


photo = process.Graphics('photo_base','photo_base')
photo.cut_by_ratio()