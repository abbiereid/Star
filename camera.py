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

    def show(self, frame, text="No gesture detected"):
        self.frame = frame
        cv2.putText(frame, text, (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2, cv2.LINE_AA)
        cv2.imshow('Camera', frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            self.release()
            cv2.destroyAllWindows()

        # TEMP RECORDING FUNCTIONALITY, WILL BE CONNECTED TO MAIN AND WAKE WORD.

        if cv2.waitKey(1) & 0xFF == ord('r'):
            self.record()

        if cv2.waitKey(1) & 0xFF == ord('s'):
            self.stop_recording()

    def get_frame(self):
        return self.frame
        
    def get_success(self):
        if self.cap.isOpened():
            self.success = True
            return self.success

    def release(self):
        self.cap.release()
        self.running = False

    def record(self):
        self.out = cv2.VideoWriter('requests/request.mp4', cv2.VideoWriter_fourcc(*'mp4v'), 20.0, self.cap.get(cv2.CAP_PROP_FRAME_WIDTH), self.cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

    def stop_recording(self):
        self.out.release()