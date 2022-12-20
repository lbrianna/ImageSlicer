import cv2
import os
import sys
from split import divide_points, crop_image

# Enter path to folder with images of the same brain
img_path = str(input('\n\nEnter path to folder: '))
cwd_path = os.getcwd() #current working directory path
img_num = 1 #iterator for image/section number, add to output file name

# Sort files within working folder alphanumerically
files = os.listdir(img_path)
sorted_files = sorted(files)

for image_name in sorted_files:
    if (image_name.endswith('.tif')):
        print('\n\033[1m'+'Processing', image_name+'\033[0m')

        # LOCATE FOLDER
        name = image_name[:-4]
        new_folder = cwd_path + '/' + name
        if not os.path.exists(new_folder):
            os.makedirs(new_folder)
        img = cv2.imread(img_path + '/' + image_name, cv2.IMREAD_UNCHANGED)

        #USER INPUT
        if (img.shape[0] > img.shape[1]):
            while True:
                answer = input('Image appears to be rotated incorrectly. Would you like to proceed? (Y/N)?: ')
                if (answer == ('N' or 'n')):
                    sys.exit("Image is rotated incorrectly.")
                elif (answer == ('Y' or 'y')):
                    break
                else:
                    print('Please enter a Y/N.')
        
        num_cols = int(input('Enter number of columns: '))
        num_rows = int(input('Enter number of rows: '))
        
        # DOWNSIZING IMAGE
        # calculate dimensions for new image shape = [rows/height, col/width]
        # print('\nOriginal Dimensions (h, w):', img.shape)
        scale_percent = (num_cols * 1500)/img.shape[1] #1500 is number of pixels wide
        new_h = int(img.shape[0] * scale_percent)
        new_w = int(img.shape[1] * scale_percent)
        new_dim = (new_w, new_h)

        # print('\nDownsizing', image_name, '\n')
        resized_img = cv2.resize(img, new_dim, interpolation = cv2.INTER_AREA)
        cv2.imwrite(os.path.join(new_folder, '{}_{}.{}'.format(image_name[:-4], 'Resized', 'png')), resized_img)
        # print ('Resized Dimensions (h, w):', resized_img.shape, '\n')
        
        #SPLITTING IMAGE W/OVERLAP
        # print ('Splitting', image_name, '\n')
        Y_points = divide_points(num_rows, new_h)
        X_points = divide_points(num_cols, new_w)
        
        #customize overlap
        overlap = 0.12/2 #when customizing overlap, do not remove the /2
    
        for i in range(len(Y_points) - 1):
            for j in range(len(X_points) - 1):
                start_row = int(Y_points[i] * (1 - overlap))
                start_col = int(X_points[j] * (1 - overlap))
                end_row = int(Y_points[i+1] * (1 + overlap))
                end_col = int(X_points[j+1] * (1 + overlap))
                
                if (i == 0):
                    start_row = 0
                if (i == len(Y_points) - 2):
                    end_row = Y_points[i+1]
                if (j == 0):
                    start_col = 0
                if (j == len(X_points) - 2):
                    end_col = X_points[j+1]
                    
                cropped_img = resized_img[start_row:end_row, start_col:end_col]
                isSaved = cv2.imwrite(os.path.join(new_folder, '{}_{}.{}'.format(name, 's'+str(img_num).zfill(3), 'png')), cropped_img)
                img_num +=1
                # cv2.imshow('image',cropped_img)
                # cv2.waitKey(0)
                
        print("Completed processing", image_name, "\n")