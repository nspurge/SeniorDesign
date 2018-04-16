import time
import datetime
import base64
import picamera

#base64 image function
def base64Image():
        filename = '/home/pi/Desktop/SeniorDesign/ProjectCode/Images/' + datetime.datetime.now().strftime("%Y-%m-%d-%H.%M.%S.jpg")
        
        cam = picamera.PiCamera()
        cam.resolution = (640, 480)
        cam.capture(filename)
        time.sleep(.5)

        image = open(filename, 'rb')
        image_read = image.read()
        image_64_encode = base64.encodestring(image_read)

        return image_64_encode
