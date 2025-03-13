import cv2

class Camera:
    def __init__(self):
        Camera.cap = cv2.VideoCapture(0)
        self.frame = None
        self.success = False
        self.writer = None

    def capture(self):
        try:
            self.success, self.frame = Camera.cap.read()
            if not self.success:
                print("Ignoring empty camera frame.")
                self.release()
        except Exception as e:
            print(f"Error in camera: {e}")

    def show(self, frame, text="No gesture detected", title="Camera"):
        self.frame = frame

        if text is not None:
            cv2.putText(frame, text, (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2, cv2.LINE_AA)

        if self.frame is not None:
            cv2.imshow(title, frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            self.release()
            cv2.destroyAllWindows()

        # TEMP RECORDING FUNCTIONALITY, WILL BE CONNECTED TO MAIN AND WAKE WORD.

        if cv2.waitKey(1) & 0xFF == ord('r'):
            self.record()

        if cv2.waitKey(1) & 0xFF == ord('s'):
            self.stop_recording()

    def get_frame(self):
        if self.frame is not None:
            return cv2.flip(self.frame, 1)
        
    def get_success(self):
        if Camera.cap.isOpened():
            self.success = True
            return self.success

    def release(self):
        Camera.cap.release()
        self.running = False
        if self.writer is not None:
            self.writer.release()

    def resize(self, image, width, height):
        return cv2.resize(image, (width, height))
    
    def recolour(self, image):
        return cv2.cvtColor(image, cv2.COLOR_BGR2RGB) 
    

    # def record(self):
    #     self.recording = True
    #     self.writer = cv2.VideoWriter('models/request.mp4',
    #                                 cv2.VideoWriter_fourcc(*'mp4v'),
    #                                 20.0,
    #                                 (int(Camera.cap.get(cv2.CAP_PROP_FRAME_WIDTH)), int(Camera.cap.get(cv2.CAP_PROP_FRAME_HEIGHT))))
    #     self.text = "Recording started"

    # def stop_recording(self):
    #     self.recording = False
    #     self.writer.release()
    #     self.text = "Recording stopped"
    #     self.release()