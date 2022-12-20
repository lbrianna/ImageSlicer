import cv2
import os

# return list of points of where dim is divided evenly into num rows/cols
def divide_points(num, dim):
    points = []
    stride = int(dim/num)
    pt = 0
    while pt <= dim:
        points.append(pt)
        pt += stride
    return points

def crop_image(resized_img, x_points, y_points, overlap):
    cropped_imgs = []
    overlap = overlap/2
    for i in range(len(y_points) - 1):
        for j in range(len(x_points) - 1):
            if (i == 0):
                start_row = 0
            if (j == 0):
                start_col = 0
            else:
                start_row = int(y_points[i] * (1 - overlap))
                start_col = int(x_points[j] * (1 - overlap))

            if (i == len(y_points) - 2):
                end_row = y_points[i+1]
            if (j == len(x_points) - 2):
                end_col = x_points[j+1]
            else:
                end_row = int(y_points[i+1] * (1 + overlap))
                end_col = int(x_points[j+1] * (1 + overlap))
            cropped = resized_img[start_row:end_row, start_col:end_col]
            cropped_imgs.append[cropped]
    return cropped_imgs
