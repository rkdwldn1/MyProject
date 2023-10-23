import cv2
import numpy as np
from flask import Flask, render_template, Response, request

app = Flask(__name__)

face_cascade = cv2.CascadeClassifier(
    "C:/OpenCV/opencv/opencv-4.x/data/haarcascades/haarcascade_frontalface_alt.xml"
)

# 초기 입술 이미지 설정 (lip1.png 사용)
selected_mask = "lip1.png"

if face_cascade.empty():
    raise IOError("Unable to load the face cascade classifier xml file")

cap = cv2.VideoCapture(0)
scaling_factor = 0.5


def generate_frames():
    while True:
        ret, frame = cap.read()
        if not ret:
            break
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        face_rects = face_cascade.detectMultiScale(gray, 1.3, 5)
        for x, y, w, h in face_rects:
            if h > 0 and w > 0:
                x = int(x + 0.2 * w)
                y = int(y + 0.6 * h)
                w = int(0.6 * w)
                h = int(0.4 * h)

                frame_roi = frame[y : y + h, x : x + w]
                # 선택된 입술 이미지를 로드하고 알파 채널을 포함하여 읽음
                face_mask_small = cv2.imread(selected_mask, cv2.IMREAD_UNCHANGED)
                face_mask_small = cv2.resize(
                    face_mask_small, (w, h), interpolation=cv2.INTER_AREA
                )

                # 입술 이미지의 알파 채널을 사용하여 배경을 제거하고 합성
                alpha_channel = face_mask_small[:, :, 3] / 255.0
                for c in range(0, 3):
                    frame_roi[0:h, 0:w, c] = (
                        frame_roi[0:h, 0:w, c] * (1 - alpha_channel)
                        + face_mask_small[:, :, c] * alpha_channel
                    )

        ret, buffer = cv2.imencode(".jpg", frame)
        frame = buffer.tobytes()
        yield (b"--frame\r\n" b"Content-Type: image/jpeg\r\n\r\n" + frame + b"\r\n")


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/video_feed")
def video_feed():
    return Response(
        generate_frames(), mimetype="multipart/x-mixed-replace; boundary=frame"
    )


# 선택한 입술 이미지를 변경하는 엔드포인트
@app.route("/change_mask")
def change_mask():
    global selected_mask
    mask_name = request.args.get("mask")
    selected_mask = mask_name
    return ""


if __name__ == "__main__":
    app.run(debug=True)
