import face_recognition
from PIL import Image

image_path = "./images/yj.jpg"
image = face_recognition.load_image_file(
    image_path)
face_locations = face_recognition.face_locations(image)

PIL_image = Image.open(image_path)

# 얼굴인식 확인
face_index = 0
# print(face_locations)

for face in face_locations:
    top, right, bottom, left = face[0], face[1], face[2], face[3]
    cropFace = PIL_image.crop((left, top, right, bottom))
    cropFaceName = "Cropped_" + image_path[9:]
    face_index += 1
    # 얼굴 잘라서 저장
    cropFace.save(cropFaceName)