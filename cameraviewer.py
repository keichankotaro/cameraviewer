# -*- coding:utf-8 -*-
# Copyright (c) 2021-2022 木須啓介. All Rights Reserved.
# The details of the license can be found in "license.txt".

import cv2
import numpy as np
import win32gui
import win32con
import tkinter.ttk as ttk
import tkinter as tk
from tkinter import messagebox
import sys

print("""
        ######         #        ##       ##   ######   #####         #
       #              # #       # #     # #   #        #    #       # #
       #             #   #      #  #   #  #   #        #####       #   #
       #            #     #     #  #   #  #   #####    ##         #     #
       #           #########    #   # #   #   #        # #       #########
       #           #       #    #   # #   #   #        #  #      #       #
        ######     #       #    #    #    #   ######   #   ##    #       #


        #     #     ######     ######   #     #     #    ######   #####
        #     #       ##       #        #     #     #    #        #    #
         #   #        ##       #         #   # #   #     #        #####
         #   #        ##       #####     #   # #   #     #####    ##
          # #         ##       #          # #   # #      #        # #
          # #         ##       #          # #   # #      #        #  #
           #        ######     ######      #     #       ######   #   ##


                    by keichan kotaro
""")

with open("./main.cfg", "r") as f:
    cfg = f.readline()
    f.close()

cfg = cfg.split("|")

def run():
    print("please wait...")
    cv2.namedWindow("camera")
    v = cv2.VideoCapture(int(cfg[5]))
    v.set(cv2.CAP_PROP_FRAME_WIDTH, int(cfg[0]))
    v.set(cv2.CAP_PROP_FRAME_HEIGHT, int(cfg[1]))
    v.set(cv2.CAP_PROP_FPS, int(cfg[4]))
    a = win32gui.FindWindow(None,"camera")
    win32gui.SetWindowLong(a, win32con.GWL_STYLE, win32con.WS_POPUP)
    print(a)
    while(v.isOpened()):
        r, f = v.read()
        if ( r == False ):
            break
        cv2.imshow("camera", f)
        win32gui.SetWindowPos(a, win32con.HWND_NOTOPMOST, int(cfg[2]), int(cfg[3]), int(cfg[0]), int(cfg[1]), win32con.SWP_SHOWWINDOW)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    v.release()
    cv2.destroyAllWindows()

run()
