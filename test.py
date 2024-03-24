from PIL import Image
from fall_prediction import Fall_prediction
from Vid_to_img import video_to_image_list

video_file = "videos/video_6.mp4"
image_list = video_to_image_list(video_file)

# img1 = Image.open("Images/fall_img_7.png")
# img2 = Image.open("Images/fall_img_8.png")
# img3 = Image.open("Images/fall_img_9.png")

flag=0

if(len(image_list)<3):
    print("Video too short or error loading video")
else: 
    for i in range(len(image_list)-2):
        if flag:
            break
        img1 = Image.open(image_list[i])
        img2 = Image.open(image_list[i+1])
        img3 = Image.open(image_list[i+2])
        response = Fall_prediction(img1, img2, img3)
        if response:
            print("There is", response['category'])
            print("Confidence :", response['confidence'])
            print("Angle : ", response['angle'])
            print("Keypoint_corr :", response['keypoint_corr'])
            flag=1

if not flag:
    print("There is no fall detected...")

# response = Fall_prediction(img1, img2, img3)

# if response:
#     print("There is", response['category'])
#     print("Confidence :", response['confidence'])
#     print("Angle : ", response['angle'])
#     print("Keypoint_corr :", response['keypoint_corr'])
# else:
#      print("There is no fall detetcion...")
