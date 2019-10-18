

import cv2
import numpy as np
import os

 

vid = cv2.VideoCapture(0)

# Define the codec and create VideoWriter object
fourcc = cv2.VideoWriter_fourcc(*'XVID')
out = cv2.VideoWriter('output.avi',fourcc,10, (500,375))

while(vid.isOpened()):
    ret, frame = vid.read()

    rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    if ret==True:
        frame = cv2.flip(frame,1)

        # write the flipped frame
        out.write(frame)

        cv2.imshow('frame', rgb)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    else:
        break
    
print('todo male sal')

os.path.isfile('output.avi')


# Una vez que se captura la imagen del vídeo, spliteamos

vidcap = cv2.VideoCapture('output.avi')
success,image = vidcap.read()
print(vidcap.read())
print(success)
count = 1
while success:
    cv2.imwrite('/images/batteries/battery%d.jpg' % count, image)          
    cv2.imwrite('/images/electronic_devices/e_d%d.jpg' % count, image)          
    cv2.imwrite('/images/fabrics/cloths%d.jpg' % count, image)          
    cv2.imwrite('/images/organic/org%d.jpg' % count, image)          
    cv2.imwrite('/images/paper/pap%d.jpg' % count, image)          
    cv2.imwrite('/images/plastic/plastic%d.jpg' % count, image)          
    cv2.imwrite('/images/sigre/med%d.jpg' % count, image)          
    cv2.imwrite('/images/trash/leftover%d.jpg' % count, image)          
    # save frame as JPEG file      
    success,image = vidcap.read()
    print('Read a new frame: ', success)
    count += 1


vid.release()
print('vid_release')
out.release()
print('out_release')
a=cv2.destroyAllWindows()
print(a)






