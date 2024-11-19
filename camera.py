import cv2

class Camera:
    def __init__(self):
        self.cap = cv2.VideoCapture(0)
        self.frame = None
        self.running = False

    def capture(self):
        try:
            self.running = True
            while self.cap.isOpened():
                success, self.frame = self.cap.read()
                if not success:
                    print("Ignoring empty camera frame.")
                    self.release()
                    break

                cv2.imshow("Camera", self.frame)

                if cv2.waitKey(1) & 0xFF == ord('q'):
                    self.release()
                    break
        except Exception as e:
            print(f"Error in camera: {e}")
        finally:
            self.release()

    def get_frame(self):
        return self.frame
    
    def get_running(self):
        return self.running

    def release(self):
        self.cap.release()
        self.running = False

    # def __del__(self):
    #     self.release()