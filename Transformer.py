import roboflow  # install with 'pip install roboflow'

roboflow.login()

rf = roboflow.Roboflow()

project = rf.workspace(WORKSPACE_ID).project("football-players-detection-3zvbc")
dataset = project.version(VERSION).download("yolov8")

project.version(dataset.version).deploy(model_type="yolov8", model_path=f"{HOME}/runs/detect/train/")