import cv2
import imutils
import argparse

def initArgs():
    parser = argparse.ArgumentParser()
    parser.add_argument("-i" , "--image" , required=True , help="Path to Input Image")
    args = vars(parser.parse_args())
    return args

if __name__ == "__main__":
    args = initArgs()
    image = cv2.imread(args["image"])
    image = cv2.resize(image , (0,0) , fx=0.6 , fy=0.6)
    cv2.imshow("Image" , image)
    cv2.waitKey()

    # Converting to grayscale
    gray = cv2.cvtColor(image , cv2.COLOR_BGR2GRAY)
    cv2.imshow("Gray" , gray)
    cv2.waitKey()

    # Edge detection
    edges = cv2.Canny(gray , 0 , 100)
    cv2.imshow("Edges" , edges)
    cv2.waitKey()

    # Inamge thresholding
    thresh = cv2.threshold(gray , 100 , 255 , cv2.THRESH_BINARY_INV)[1]
    cv2.imshow("Thresholding" , thresh)
    cv2.waitKey()

    # Finding Contours
    cunts = cv2.findContours(thresh.copy() , cv2.RETR_EXTERNAL , cv2.CHAIN_APPROX_SIMPLE)
    cunts = imutils.grab_contours(cunts)
    output = image.copy()

    # Interesting. Doesnt work as expected. Read on this
    for c in cunts:
        cv2.drawContours(output , [c] , -1 , (0,0,255) , 3)

    cv2.imshow("Contours", output)
    cv2.waitKey(0)

    # Eroding 
    mask = thresh.copy()
    mask = cv2.erode(mask , None , iterations = 1)
    cv2.imshow("Erode" , mask)
    cv2.waitKey(0)

    # Dilation
    mask = thresh.copy()
    mask = cv2.dilate(mask , None , iterations = 1)
    cv2.imshow("Dilated" , mask)
    cv2.waitKey(0)