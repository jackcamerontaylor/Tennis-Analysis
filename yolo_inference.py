from ultralytics import YOLO

model = YOLO("yolov9e")

result = model.predict("input_videos/input_video.mp4", save=True)

print(result)
print("boxes: ")
for box in result[0].boxes:
    print(box)
