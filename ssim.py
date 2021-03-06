# Strctural Similarity Index between two images

# USAGE
# python compare.py

# import the necessary packages
from skimage.measure import structural_similarity as ssim
import matplotlib.pyplot as plt
import numpy as np
import cv2

def mse(imageA, imageB):
	# the 'Mean Squared Error' between the two images is the
	# sum of the squared difference between the two images;
	# NOTE: the two images must have the same dimension
	err = np.sum((imageA.astype("float") - imageB.astype("float")) ** 2)
	err /= float(imageA.shape[0] * imageA.shape[1])
	
	# return the MSE, the lower the error, the more "similar"
	# the two images are
	return err

total_m = 0
total_s = 0


def compare_images(imageA, imageB, title, f):
	# compute the mean squared error and structural similarity
	# index for the images
	global total_m, total_s

	m = mse(imageA, imageB)
	s = ssim(imageA, imageB)



	total_m += m
	total_s += s

	# write this in file
	f.write(str(m)+","+str(s)+"\n")
	# print(s)


	# setup the figure
	# fig = plt.figure(title)
	# plt.suptitle("MSE: %.2f, SSIM: %.2f" % (m, s))

	# # show first image
	# ax = fig.add_subplot(1, 2, 1)
	# plt.imshow(imageA, cmap = plt.cm.gray)
	# plt.axis("off")

	# # show the second image
	# ax = fig.add_subplot(1, 2, 2)
	# plt.imshow(imageB, cmap = plt.cm.gray)
	# plt.axis("off")

	# # show the images
	# plt.show()      

f = open("mse_ssim.txt","w")

for i in range(1,221):
    original = cv2.imread("results/test5/images_to_compare/"+str(i)+"/outputs.png")
    contrast = cv2.imread("results/test5/images_to_compare/"+str(i)+"/targets.png")
    # shopped = cv2.imread("images/jp_gates_photoshopped.png")

    # convert the images to grayscale
    original = cv2.cvtColor(original, cv2.COLOR_BGR2GRAY)
    contrast = cv2.cvtColor(contrast, cv2.COLOR_BGR2GRAY)
    # shopped = cv2.cvtColor(shopped, cv2.COLOR_BGR2GRAY)

    # initialize the figure
    fig = plt.figure("Images")
    images = ("Original", original), ("Contrast", contrast)

    # loop over the images
	
    # for (i, (name, image)) in enumerate(images):
    #     # show the image
    #     ax = fig.add_subplot(1, 3, i + 1)
    #     ax.set_title(name)
    #     plt.imshow(image, cmap = plt.cm.gray)
    #     plt.axis("off")

    # # show the figure
    # plt.show()
	

    # compare the images
    # compare_images(original, original, "Output Depth Map vs. Output Depth Map")

    compare_images(original, contrast, "Output Depth Map vs. Depth Map from Dataset", f)
    # compare_images(original, shopped, "Original vs. Photoshopped")
f.write("\n\n")
f.write("AVERAGE VALUES - \n\n")
f.write(f"SSIM INDEX - {total_s/220}\n")
f.write(f"Mean Square Error - {total_m/220}\n")

f.close()

print (total_m/221, total_s/221)






