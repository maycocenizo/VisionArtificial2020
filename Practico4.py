#! /usr/bin/env python
# -*- coding: utf-8 -*-
import cv2
cap = cv2.VideoCapture(0)
fourcc = cv2.VideoWriter_fourcc('X', 'V', 'I', 'D')
out = cv2.VideoWriter('output.avi', fourcc, int(cap.get(cv2.CAP_PROP_FPS)), (int((cap.get(cv2.CAP_PROP_FRAME_WIDTH))), int(((cap.get(cv2.CAP_PROP_FRAME_HEIGHT))))))
while cap.isOpened():
    ret, frame = cap.read()
    if ret is True:
        out.write(frame)
        cv2.imshow('frame', frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    else:
        break
cap.release()
out.release()
cv2.destroyAllWindows()

##usamos int(cap.get(cv2.CAP_PROP_FRAME)) para pasarle el tamaño con el que captura la camara