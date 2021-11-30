from djitellopy import Tello 


tello = Tello()

tello.connect()



# move
# tello.takeoff()
# tello.move_up(110)
# tello.flip_forward(30)
# tello.move_forward(100)
# tello.rotate_clockwise(90)
# tello.move_forward(120)
# tello.rotate_clockwise(90)




# tello.land()

import cv2
panel = cv2.imread('./tello.jpg')
cv2.imshow('tello panel', panel)
while True:
    key = cv2.waitKey(1)
    if key == ord('q'):
        break
    elif key == ord('t'):
        tello.takeoff()
    elif key == ord('l'):
        tello.land()
    elif key == ord('b'):
        tello.move('back', 60)
    elif key == ord('f'):
        tello.move('forward', 60)
    elif key == ord('u'):
        tello.move('up', 110)
    elif key == ord('d'):
        tello.move('down', 30)
    elif key == ord('w'):
        tello.rotate_clockwise(90)
    elif key == ord('r'):
        tello.move('right', 20)
    elif key == ord('l'):
        tello.move('left', 20)
    elif key == ord('pf'):
        tello.flip_forward(20)

pass