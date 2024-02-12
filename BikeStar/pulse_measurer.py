from matplotlib import pyplot as plt
import cv2
import io
import time
import numpy as np
import sqlite3

# Setting a connection to db
connection = sqlite3.connect('db.sqlite3')
cursor = connection.cursor()

delay=0

# Camera stream
cap = cv2.VideoCapture(0)
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 1080)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 720)
cap.set(cv2.CAP_PROP_FPS, 30)

# Image crop
x, y, w, h = 800, 500, 100, 100
heartbeat_count = 5
heartbeat_values = [0]*heartbeat_count
heartbeat_times = [time.time()]*heartbeat_count

# Matplotlib graph surface
fig = plt.figure()
ax = fig.add_subplot(111)

while(True):
    # Capture frame-by-frame
    ret, frame = cap.read()

    # Our operations on the frame come here
    img = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    crop_img = img[y:y + h, x:x + w]

    # Update the data
    heartbeat_values = heartbeat_values[1:] + [np.average(crop_img)]
    heartbeat_times = heartbeat_times[1:] + [time.time()]

    # finale
    if delay==5:
        break
    print(round(heartbeat_values[-1]))
    delay+=1
    time.sleep(1)

#print('Итог:', sum(heartbeat_values)//5)
cursor.execute('UPDATE routes SET pulsemin = ? WHERE id = ?', (round(min(heartbeat_values)), 1))
cursor.execute('UPDATE routes SET pulsemax = ? WHERE id = ?', (round(max(heartbeat_values)), 1))
cursor.execute('UPDATE routes SET pulsemid = ? WHERE id = ?', (int(sum(heartbeat_values)//5), 1))
connection.commit()
connection.close()