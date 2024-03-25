# from PIL import Image
# from fall_prediction import Fall_prediction
# from Vid_to_img import video_to_image_list

# video_file = "test_videos/test_4.mp4"
# image_list = video_to_image_list(video_file)

# # img1 = Image.open("Images/fall_img_7.png")
# # img2 = Image.open("Images/fall_img_8.png")
# # img3 = Image.open("Images/fall_img_9.png")

# flag=0

# if(len(image_list)<3):
#     print("Video too short or error loading video")
# else: 
#     for i in range(len(image_list)-2):
#         if flag:
#             break
#         img1 = Image.open(image_list[i])
#         img2 = Image.open(image_list[i+1])
#         img3 = Image.open(image_list[i+2])
#         response = Fall_prediction(img1, img2, img3)
#         if response:
#             print("There is", response['category'])
#             print("Confidence :", response['confidence'])
#             print("Angle : ", response['angle'])
#             print("Keypoint_corr :", response['keypoint_corr'])
#             flag=1

# if not flag:
#     print("There is no fall detected...")

# # response = Fall_prediction(img1, img2, img3)

# # if response:
# #     print("There is", response['category'])
# #     print("Confidence :", response['confidence'])
# #     print("Angle : ", response['angle'])
# #     print("Keypoint_corr :", response['keypoint_corr'])
# # else:
# #      print("There is no fall detetcion...")


from PIL import Image
from fall_prediction import Fall_prediction
from Vid_to_img import video_to_image_list

video_file = "test_videos/test_1.mp4"
image_list = video_to_image_list(video_file)

# Open the output file in write mode
with open("test_1.txt", "w") as output_file:

  flag = 0

  if (len(image_list) < 3):
    output_file.write("Video too short or error loading video\n")
  else:
    for i in range(len(image_list) - 2):
      if flag:
        break
      img1 = Image.open(image_list[i])
      img2 = Image.open(image_list[i + 1])
      img3 = Image.open(image_list[i + 2])
      response = Fall_prediction(img1, img2, img3)

      if response:
        output_file.write(f"There is {response['category']}\n")
        output_file.write(f"Confidence : {response['confidence']}\n")
        output_file.write(f"Angle : {response['angle']}\n")
        output_file.write(f"Keypoint_corr : {response['keypoint_corr']}\n\n")
        flag = 1

  if not flag:
    output_file.write("There is no fall detected...\n")
