# import libraries
from PIL import Image
import matplotlib.pyplot as plt
import numpy as np
import imageio
# input path 
image_path = "E:/Beautiful_Girl_Pictures/"
# open image
img = Image.open(image_path + "rose.jpg")

# matrix transform
T_scale = np.array([
    [0.5, 0, 0],
    [0, 0.5, 0],
    [0, 0, 1]])
T_rotate = np.array([
    [0.98, -(0.17), 0],
    [0.17,    0.98, 0],
    [   0,       0, 1]])
T_shear = np.array([
    [1, 0.2, 0],
    [0.1, 1, 0],
    [0,   0, 1]])
T_translate = np.array([
    [1, 0, 50],
    [0, 1, 50],
    [0, 0,  1]])
T_euclidean = T_translate.dot(T_rotate)
T_similarity = T_euclidean.dot(T_scale)
T_affine = T_similarity.dot(T_shear)

# transform
def transform(matrix, img):
	'''
	Input: matrix transform and input image
	Output: list of Original image and image-transformed
	'''
	images = []
	images.append(img)
	width = np.asarray(img).shape[0]
	height = np.asarray(img).shape[1]
	T_inv = np.linalg.inv(matrix)
	img_transformed = img.transform((height, width), Image.AFFINE, data=T_inv.flatten()[:6], resample=Image.NEAREST)
	images.append(img_transformed)
	
	return images

out_path = "E:/Beautiful_Girl_Pictures/"

def scale(img):
	images = transform(T_scale, img)
	imageio.mimsave(out_path + 'rose_scaled.gif', images, duration=1)

def rotate(img):
	images = transform(T_rotate, img)
	imageio.mimsave(out_path + 'rose_rotated.gif', images, duration=1)

def shear(img):
	images = transform(T_shear, img)
	imageio.mimsave(out_path + 'rose_sheared.gif', images, duration=1)

def translate(img):
	images = transform(T_translate, img)
	imageio.mimsave(out_path + 'rose_translated.gif', images, duration=1)

def euclidean(img):
	images = transform(T_euclidean, img)
	imageio.mimsave(out_path + 'rose_euclidean.gif', images, duration=1)

def similarity(img):
	images = transform(T_similarity, img)
	imageio.mimsave(out_path + 'rose_similarity.gif', images, duration=1)

def affine(img):
	images = transform(T_affine, img)
	imageio.mimsave(out_path + 'rose_affine.gif', images, duration=1)

scale(img)
rotate(img)
shear(img)
translate(img)
euclidean(img)
similarity(img)
affine(img)
