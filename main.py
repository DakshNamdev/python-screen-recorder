import cv2
import numpy as np
import mss
import time
import threading

WIDTH, HEIGHT = 1920, 1080
fps = 60.0
frame_duration = 1.0 / fps

codec = cv2.VideoWriter_fourcc(*"XVID")
out = cv2.VideoWriter("Recording.avi", codec, fps, (WIDTH, HEIGHT))

cv2.namedWindow("Live", cv2.WINDOW_NORMAL)
cv2.resizeWindow("Live", 480, 270)

monitor = {"top": 0, "left": 0, "width": WIDTH, "height": HEIGHT}

latest_frame = None
running = True
lock = threading.Lock()

# 🔹 Capture thread (mss MUST be created here)
def capture():
    global latest_frame
    sct = mss.mss()  # ✅ create inside thread

    while running:
        img = sct.grab(monitor)
        frame = np.array(img)[:, :, :3]
        frame = cv2.cvtColor(frame, cv2.COLOR_BGRA2BGR)

        with lock:
            latest_frame = frame

# Start capture thread
threading.Thread(target=capture, daemon=True).start()

next_frame_time = time.perf_counter()

while True:
    now = time.perf_counter()

    if now >= next_frame_time:
        next_frame_time += frame_duration

        with lock:
            frame = latest_frame

        if frame is not None:
            out.write(frame)
            cv2.imshow("Live", frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

running = False
out.release()
cv2.destroyAllWindows()
