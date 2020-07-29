import win32api,win32con
import time
import os
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide"
import pygame

pygame.init()

pygame.joystick.init()




hiz = 1700
scroll_hiz = 3

yukari = 1
asagi = 2

print("Başlatıldı!")
while 1:
    for event in pygame.event.get():
        if event.type == 12:
            exit()

    for i in range(pygame.joystick.get_count()):

        joystick = pygame.joystick.Joystick(i)
        joystick.init()

        axis_Lx = joystick.get_axis(0)
        if axis_Lx >.5 or axis_Lx <-.5:
            curPos = win32api.GetCursorPos()
            win32api.SetCursorPos((int(curPos[0]+ (1 if axis_Lx>0 else -1)),curPos[1]))
            time.sleep(1/hiz)

        axis_Ly = joystick.get_axis(1)*100
        if axis_Ly >50 or axis_Ly <-50:
            curPos = win32api.GetCursorPos()
            win32api.SetCursorPos((curPos[0],int(curPos[1]+ (1 if axis_Ly>0 else -1))))
            time.sleep(1/hiz)

        if joystick.get_button(yukari):
            win32api.mouse_event(win32con.MOUSEEVENTF_WHEEL, win32api.GetCursorPos()[0], win32api.GetCursorPos()[1],scroll_hiz , 0)

        if joystick.get_button(asagi):
            win32api.mouse_event(win32con.MOUSEEVENTF_WHEEL, win32api.GetCursorPos()[0], win32api.GetCursorPos()[1],-scroll_hiz , 0)
