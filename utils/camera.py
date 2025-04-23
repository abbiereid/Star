import cv2

class Camera:
    def __init__(self):
        Camera.cap = cv2.VideoCapture(0)

        self.frame = None
        self.success = False

    def capture(self):
        try:
            self.success, self.frame = Camera.cap.read()
            if not self.success:
                print("Ignoring empty camera frame.")
                self.release()
        except Exception as e:
            print(f"Error in camera: {e}")

    def release(self):
        Camera.cap.release()
        cv2.destroyAllWindows()

    def release_window(self, title):
        cv2.destroyWindow(title)

    def get_frame(self):
        if self.frame is not None:
            return cv2.flip(self.frame, 1)
        else:
            return None
        
    def get_success(self):
        return self.success
    
    def show(self, frame, text="No gesture detected", title="Camera"):
        self.frame = frame

        if text is not None:
            cv2.putText(frame, text, (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2, cv2.LINE_AA)

        if self.frame is not None:
            cv2.imshow(title, frame)
        else:
            cv2.destroyWindow(title)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            self.release()
            cv2.destroyAllWindows()

    def resize(self, image, width, height):
        return cv2.resize(image, (width, height))
    
    def recolour(self, image):
        return cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
