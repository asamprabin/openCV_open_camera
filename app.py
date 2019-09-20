import cv2

# Connecting to default camera
capture = cv2.VideoCapture(0)
open_camera = True

while open_camera:

    # .read() return a tuple.
    # ret is a boolean indicating if the frame was read correctly
    # frame represents the captured frame
    ret, frame = capture.read()

    if ret:
        # imshow() receives the image to display.
        # In our case the image captured by frame
        cv2.imshow('video', frame)
    else:
        open_camera = False

        # waitkey() function receives as input a delay to wait until the key is pressed, in milliseconds.
        # waitKey function returns the pressed key as a number, 27 represents ESC key
        if cv2.waitKey(1) == 27:
            break

# Releasing Camera
capture.release()
# destroying the window we have created to show the frames of the camera
cv2.destroyAllWindows()
