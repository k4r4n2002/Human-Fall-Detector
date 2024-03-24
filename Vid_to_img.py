import cv2
import time

def video_to_image_list(video_path, frame_interval=0.5):
  """
  Converts an MP4 video to a list of JPEG images, capturing frames at a specified interval.

  Args:
      video_path (str): Path to the MP4 video file.
      frame_interval (float, optional): Interval in seconds between captured frames. Defaults to 0.5.

  Returns:
      list: A list of paths to the captured JPEG images.
  """

  # Open the video capture object
  cap = cv2.VideoCapture(video_path)

  # Check if video opened successfully
  if not cap.isOpened():
      print("Error opening video file:", video_path)
      return []

  # Initialize an empty list to store image paths
  image_list = []
  frame_count = 0

  while True:
      # Capture frame-by-frame
      ret, frame = cap.read()

      # Check for successful frame capture
      if not ret:
          print("Reached end of video or error reading frame.")
          break

      # Capture image at specified interval
      if frame_count % (int(frame_interval * cap.get(cv2.CAP_PROP_FPS))) == 0:
          # Generate unique filename based on frame count
          filename = f"frame_{frame_count:05d}.jpg"
          # Convert frame to RGB format (assuming compatibility with opencv)
          rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
          # Save frame as JPEG image
          cv2.imwrite(filename, rgb_frame)
          # Append the image path to the list
          image_list.append(filename)

      frame_count += 1

      # Wait for a short time to maintain frame rate
      time.sleep(1 / cap.get(cv2.CAP_PROP_FPS))

  # Release the video capture object
  cap.release()
  cv2.destroyAllWindows()

  return image_list

# Example usage:
video_file = "videos/video_3.mp4"
image_list = video_to_image_list(video_file)

if image_list:
  print("Extracted", len(image_list), "JPEG images from the video.")
else:
  print("No images captured from the video.")