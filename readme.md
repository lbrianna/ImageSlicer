# Auto-Slicing Code for AMBA Registration

This code was created with the purpose of auto-cropping images of brain sections to register with the Allen Mouse Brain Atlas. It takes an image, asks for user input about the number of rows and columns and slices into even parts. Everything can be customized directly in the code. The alignment code is private.

Before running the code, you should make sure that CV2 is installed on the computer. You can do this by opening the terminal and runnning "pip install opencv-python"

## Documentation
You can also view this information at: https://lbrianna.github.io/ImageSlicerDocumentation/
## Instructions
1. Create a folder with TIF images of the brain sections. Use different folders for different brains. Rename the files to the following format: {YYYY.MM.DD}_{Identification}_{Slide #}.tif (Example: 2022.07.22_S8192-488_Slide1.tif)
2. Copy folder path
3. Run the code and answer the prompts
4. You can customize input type (line 16), image width (line 43), image overlap (line 59), and output type (line 78)

## Test Images
You can use the test images in the test_images folder to try the code.
