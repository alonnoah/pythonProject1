import cv2
import numpy as np
import random
import math as mt

def colorShapes(img):

    imgsmooth = cv2.GaussianBlur(img, (5, 5), 0)
    canny_img = cv2.Canny(imgsmooth, 100, 200)

    _, threshold = cv2.threshold(canny_img, 240, 255, cv2.THRESH_BINARY)
    result = img.copy()
    # Find contours
    contours, _ = cv2.findContours(threshold, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
    # Analyze contours
    for cnt in contours:

        epsilon = 0.01 * cv2.arcLength(cnt, True)
        approx = cv2.approxPolyDP(cnt, epsilon, True)

        shape, color = get_shape_name(vertices=len(approx))
        x, y, w, h = cv2.boundingRect(cnt)
        center = (int(x + w / 2), int(y + h / 2))

        if len(approx) == 4:
            aspect_ratio = w / float(h)
            if (aspect_ratio >= 0.99 and aspect_ratio <= 1.02):
                shape = "square"
                color = (238, 130, 238)
                print(aspect_ratio, 'square')
            elif (aspect_ratio >= 0.5 and aspect_ratio < 0.75):
                shape = "rhombus"
                color = (216, 191, 216)
                print(aspect_ratio, 'rhombus')
            elif (2.21 < aspect_ratio < 2.5):
                shape = "parallelogram"
                color = (128, 64, 255)
                print(aspect_ratio, 'parallelogram')
            else:
                shape = "rectangle"
                color = (128, 0, 128)
                print(aspect_ratio, 'rectangle')

        result = cv2.drawContours(result, [cnt], -1, color, -1)
        cv2.drawContours(result, [approx], 0, (0, 0, 0), 3)
        result = cv2.putText(result, shape, (center[0] - 20, center[1]), cv2.FONT_HERSHEY_COMPLEX, 0.6, (0, 0, 0), 1)

    return result

def get_shape_name(vertices):
    shape = None
    color = None

    if vertices == 3:
        shape = "Triangle"
        color = (0, 255, 0)

    elif vertices == 4:
        shape = "Quadrilateral"
        color = (255, 0, 0)

    elif vertices == 5:
        shape = "Pentagon"
        color = (255, 0, 255)

    elif vertices == 6:
        shape = "Hexagon"
        color = (255, 255, 0)

    elif vertices == 8:
        shape = "Octagon"
        color = (200, 120, 0)

    elif vertices == 10:
        shape = "Star"
        color = (0, 255, 255)

    elif 7 < vertices <= 13:
        shape = "Ellipse"
        color = (125, 0, 255)

    else:
        shape = "Circle"
        color = (0, 125, 255)

    return shape, color

def sp_noise(image, prob):
    '''
    Add salt and pepper noise to image
    prob: Probability of the noise
    '''
    output = np.zeros(image.shape, np.uint8)
    thres = 1 - prob
    for i in range(image.shape[0]):
        for j in range(image.shape[1]):
            rdn = random.random()
            if rdn < prob:
                output[i][j] = 0
            elif rdn > thres:
                output[i][j] = 255
            else:
                output[i][j] = image[i][j]
    return output

def reduce_noise(image, prob):

    image = cv2.medianBlur(image, 5)

    return image

