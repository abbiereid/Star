import cv2
import time
import requests

#Captures and returns a series of images from the webcam
def capture():
    images = []

    cap = cv2.VideoCapture(0)
    while True:
        ret, frame = cap.read()
        cv2.imshow("testing", frame)
        if cv2.waitKey(1) & 0xFF == ord('c'):
            for i in range(40):
                ret, frame = cap.read()
                if ret:
                    images.append(('file', (f'image_{i}.png', cv2.imencode('.png', frame)[1].tobytes(), 'image/png')))
                    time.sleep(0.01)
            break
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()

    return images

#Takes in captured images and sends them to the translation model
def send_to_model(images):
    return requests.post('http://localhost/Star-Server/BSL_Translator/bsl_translator.php', files=images)

print(send_to_model(capture()))

