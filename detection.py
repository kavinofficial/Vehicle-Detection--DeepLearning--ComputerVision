from ultralytics import YOLO

model = YOLO("D://Python//ML//Vehicle Detection//best.pt")

results = model.predict(source="D://Python//ML//Vehicle Detection//test1.mp4", show=True, save=True)