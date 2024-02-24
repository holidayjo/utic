import cv2
import yaml

with open("data\cfg.yaml", encoding='UTF8') as f:
    data_dict = yaml.load(f, Loader=yaml.SafeLoader)  # data dict
# print(data_dict)

cctv_url = data_dict["CCTV"]+data_dict["key"]
print(cctv_url)

