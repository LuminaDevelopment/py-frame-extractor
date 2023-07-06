import cv2
import os

folder = os.getcwd()
video = os.path.join(folder, "RENAME-TO-YOUR-MP4-file.mp4")
if not os.path.isfile(video):
    print(f"The file {video} does not exist. Please double-check the filename and path.")
else:
    print(f"Processing the file: {video}")
    vidcap = cv2.VideoCapture(video)
    if not vidcap.isOpened():
        print(f"Error: Unable to open video file {video}")
    else:
        frame_count = 0
        while vidcap.isOpened():
            ret, frame = vidcap.read()
            if not ret:
                print("End of video file reached.")
                break

            frame_name = os.path.join(folder, f"frame{frame_count}.jpg")
            cv2.imwrite(frame_name, frame)
            print(f"Saved frame {frame_count} to {frame_name}")

            frame_count += 1

        vidcap.release()

        print("Frame extraction completed!")
