import cv2

class Camera:
    def __init__(self):
        self.cap = cv2.VideoCapture(0)
        self.frame = None
        self.success = False

    def capture(self):
        try:
            self.success, self.frame = self.cap.read()
            if not self.success:
                print("Ignoring empty camera frame.")
                self.release()
        except Exception as e:
            print(f"Error in camera: {e}")

    def show(self, frame):
        self.frame = frame
        cv2.imshow('Camera', frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            self.release()
            cv2.destroyAllWindows()

    def get_frame(self):
        return self.frame
        
    def get_success(self):
        if self.cap.isOpened():
            self.success = True
            return self.success

    def release(self):
        self.cap.release()
        self.running = False