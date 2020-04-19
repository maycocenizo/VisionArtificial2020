#! /usr/bin/env python
# -*- coding: utf-8 -*-
import sys
import cv2

cap = cv2.VideoCapture('VIDEO1.mp4')
while cap.isOpened():
    ret, frame = cap.read()
    gray = cv2.cvtColor(frame , cv2.COLOR_BGR2GRAY)
    cv2.imshow('frame', gray)
    if (cv2.waitKey(int(cap.get(cv2.CAP_PROP_FPS))) & 0xFF) == ord('q'):
        break
cap.release()
cv2.destroyAllWindows()

##usamos int(cap.get(cv2.CAP_PROP_FPS)) para pasarle los fps en numeros enteros
