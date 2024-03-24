from PIL import Image
from fall_prediction import Fall_prediction

img1 = Image.open("frame_00336.jpg")
img2 = Image.open("frame_00348.jpg")
img3 = Image.open("frame_00360.jpg")

response = Fall_prediction(img1, img2, img3)

if response:
    print("There is", response['category'])
    print("Confidence :", response['confidence'])
    print("Angle : ", response['angle'])
    print("Keypoint_corr :", response['keypoint_corr'])
else:
     print("There is no fall detetcion...")

# from PIL import Image
# from fall_prediction import Fall_prediction
# import cv2

# def detect_fall_in_video(video_path, frame_interval=500):
#   """
#   Analyzes a video file for potential falls using the Fall_prediction model.

#   Args:
#       video_path (str): Path to the video file.
#       frame_interval (int, optional): Interval in milliseconds between frame snapshots. Defaults to 500.

#   Returns:
#       bool: True if a fall is detected, False otherwise.
#   """

#   # Open the video capture object
#   cap = cv2.VideoCapture(video_path)

#   # Check if video opened successfully
#   if not cap.isOpened():
#       print("Error opening video file:", video_path)
#       return False

#   # Flag to indicate fall detection
#   fall_detected = False

#   # Process video frames
#   while True:
#       # Capture frame-by-frame
#       ret, frame = cap.read()

#       # Check for successful frame capture
#       if not ret:
#           print("Reached end of video or error reading frame.")
#           break

#       # Convert frame to RGB format (assuming fall_prediction expects RGB)
#       frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

#       # Convert frame to PIL Image for compatibility with fall_prediction
#       frame_image = Image.fromarray(frame)

#       # Process frame with fall detection model (assuming Fall_prediction takes a single frame)
#       response = Fall_prediction(frame_image)

#       if response:
#           # Fall detected
#           fall_detected = True
#           print(f"Fall detected at frame {cap.get(cv2.CAP_PROP_POS_FRAMES)} with:")
#           print(" - Category:", response['category'])
#           print(" - Confidence:", response['confidence'])
#           print(" - Angle:", response['angle'])
#           print(" - Keypoint_corr:", response['keypoint_corr'])

#       # Wait for frame_interval milliseconds before capturing the next frame
#       cv2.waitKey(frame_interval)

#   # Release the video capture object
#   cap.release()
#   cv2.destroyAllWindows()

#   return fall_detected

# # Example usage:
# video_file = "videos/video_2.mp4"
# fall_detected = detect_fall_in_video(video_file)

# if fall_detected:
#   print("Fall detected in the video.")
# else:
#   print("No fall detected in the video.")


# from PIL import Image
# from fall_prediction import Fall_prediction
# import cv2

# def detect_fall_in_video(video_path, frame_interval=500):
#   """
#   Analyzes a video file for potential falls using the Fall_prediction model and reports frame numbers.

#   Args:
#       video_path (str): Path to the video file.
#       frame_interval (int, optional): Interval in milliseconds between frame snapshots. Defaults to 500.

#   Returns:
#       bool: True if a fall is detected, False otherwise.
#   """

#   # Open the video capture object
#   cap = cv2.VideoCapture(video_path)

#   # Check if video opened successfully
#   if not cap.isOpened():
#       print("Error opening video file:", video_path)
#       return False

#   # Flag to indicate fall detection
#   fall_detected = False

#   # Process video frames
#   while True:
#       # Capture frame-by-frame
#       ret, frame = cap.read()

#       # Check for successful frame capture
#       if not ret:
#           print("Reached end of video or error reading frame.")
#           break

#       # Get current frame number
#       current_frame_number = int(cap.get(cv2.CAP_PROP_POS_FRAMES))

#       # Convert frame to RGB format (assuming fall_prediction expects RGB)
#       frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

#       # Convert frame to PIL Image for compatibility with fall_prediction
#       frame_image = Image.fromarray(frame)

#       # Process frame with fall detection model (assuming Fall_prediction takes a single frame)
#       response = Fall_prediction(frame_image)

#       if response:
#           # Fall detected
#           fall_detected = True
#           print(f"Fall detected at frame {current_frame_number} with:")
#           print(" - Category:", response['category'])
#           print(" - Confidence:", response['confidence'])
#           print(" - Angle:", response['angle'])
#           print(" - Keypoint_corr:", response['keypoint_corr'])

#       # Wait for frame_interval milliseconds before capturing the next frame
#       cv2.waitKey(frame_interval)

#   # Release the video capture object
#   cap.release()
#   cv2.destroyAllWindows()

#   return fall_detected

# # Example usage:
# video_file = "videos/video_3.mp4"
# fall_detected = detect_fall_in_video(video_file)

# if fall_detected:
#   print("Fall detected in the video.")
# else:
#   print("No fall detected in the video.")


# import cv2

# def video_to_image_list(video_path, frame_interval=500):
#   """
#   Converts a video file to a list of PIL Images, capturing frames at a specified interval.

#   Args:
#       video_path (str): Path to the video file.
#       frame_interval (int, optional): Interval in milliseconds between captured frames. Defaults to 500.

#   Returns:
#       list: A list of PIL Images extracted from the video.
#   """

#   # Open the video capture object
#   cap = cv2.VideoCapture(video_path)

#   # Check if video opened successfully
#   if not cap.isOpened():
#       print("Error opening video file:", video_path)
#       return []

#   # List to store extracted images
#   images = []

#   while True:
#       # Capture frame-by-frame
#       ret, frame = cap.read()

#       # Check for successful frame capture
#       if not ret:
#           print("Reached end of video or error reading frame.")
#           break

#       # Convert frame to RGB format (assuming compatibility with PIL)
#       frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

#       # Create a PIL Image from the frame
#       image = Image.fromarray(frame)

#       # Append the image to the list
#       images.append(image)

#       # Wait for frame_interval milliseconds before capturing the next frame
#       cv2.waitKey(frame_interval)

#   # Release the video capture object
#   cap.release()
#   cv2.destroyAllWindows()

#   return images

# # Example usage:
# video_file = "videos/video_1.mp4"
# image_lis = video_to_image_list(video_file)
# # from PIL import Image
# from fall_prediction import Fall_prediction

# def detect_fall_in_images(image_list):
#   """
#   Analyzes a list of images for potential falls using the Fall_prediction model,
#   processing images in windows of 3.

#   Args:
#       image_list (list): A list of PIL Images.

#   Returns:
#       str: Fall detection result ("Fall detected", "No fall detected", or "Video is too short").
#   """

#   # Check if list has at least 3 images
#   if len(image_list) < 3:
#       return "Video is too short"

#   # Loop through the image list in windows of 3
#   for i in range(len(image_list) - 2):
#       window = image_list[i:i+3]  # Extract a window of 3 consecutive images

#       # Process the window with fall detection model
#       response = Fall_prediction(window[0], window[1], window[2])

#       if response:
#           # Fall detected in the window
#           return "Fall detected"

#   # No fall detected in any window
#   return "No fall detected"



# fall_detection_result = detect_fall_in_images(image_lis)
# print(fall_detection_result)


# print("Extracted", len(image_list), "images from the video.")
