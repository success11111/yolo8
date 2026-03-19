from roboflow import Roboflow
rf = Roboflow(api_key="aj1rAvxz1nkGWRN9YphU")
project = rf.workspace("imperial-college-tcys7").project("neu-det-hsegd")
version = project.version(2)
dataset = version.download("yolov8")