import imutils
import cv2

def out(image):
    cv2.imshow("Out" , image)
    cv2.waitKey(0)

if __name__ == "__main__":
    image = cv2.imread("6.png")
    image = cv2.resize(image , (0,0) , fx = 0.5 , fy = 0.5)

    # # Getting Dimensions. All pixels are of the form image[y,x]. 
    # # Depth refers to channels which in case of RGB images are 3.
    (h,w,d) = image.shape
    print("\nH: {}\tW: {}\tD: {}\n".format(h,w,d))
    out(image)

    # # Getting RGB values from a pixel
    (B,G,R) = image[100,50] # Pixel at x=50 and y=100
    print("R: {}\tG: {}\tB:{}".format(R,G,B))

    # # Extracting random ROIs. Play around with the no.s
    randomroi = image[100:200 , 400:500] 
    out(randomroi)

    # # Resizing to a specific width/height keeping the aspect ratio
    REQUIRED_WIDTH = 300
    ratio = REQUIRED_WIDTH/w
    resized = cv2.resize(image , (REQUIRED_WIDTH , int(h*ratio)))
    out(resized)

    # # Using imutils for resizing
    resized = imutils.resize(image , width=200)
    out(resized)

    # # Rotating an image
    center = (w//2 , h//2)
    M = cv2.getRotationMatrix2D(center , -45 , 1.0)
    rotated = cv2.warpAffine(image , M , (w,h))
    out(rotated)

    # # Rotating using imutils
    rotated = imutils.rotate(image , 45)
    out(rotated)

    # # Rotating using imutils
    boundrot = imutils.rotate_bound(image , -45)
    out(boundrot)

    # Smoothing Image
    blurred = cv2.GaussianBlur(image , (11 , 11) , 100)
    out(blurred)

    # Drawing operations are performed in place. So make sure to CREATE SEPERATE COPY OF IMAGE
    
    # Rectaingle 
    output = image.copy()
    cv2.rectangle(output , (100,200) , (200,300) , (0,0,255) , 2)
    out(output)

    # Circle
    output = image.copy()
    cv2.circle(output , (480,280) , 50 , (255 , 0 , 0) , 3) # A thickness of -1 means filled.
    out(output)

    # A random line (mathematical one. Not talking about the nature of the comment moron :D)
    output = image.copy()
    cv2.line(output , (340,300) , (200,200) , (0,0,255) , 3)
    out(output)

    # Adding text
    output = image.copy()
    cv2.putText(output , "Terrible!" , (450,240) , cv2.FONT_HERSHEY_SCRIPT_SIMPLEX , 1 , (0,0,255) , 2)
    out(output)

