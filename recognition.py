from ultralytics import YOLO
model = YOLO(r"model/best.pt")

# 返回识别结果字典的函数
# key:类别id value:置信度
def return_diagnosis_dic(filename:str):
    results = model(filename)
    d_result = {}
    for result in results:
        # print("类型名",result.names)
        for box in result.boxes:
            # print("边界框坐标：",box.xyxy)
            # print("置信度：",box.conf)
            # print("类别id: ",box.cls)
            classfyid = int(box.cls.item())
            confidence = round(float(box.conf.item()), 2)
            if classfyid not in d_result:
                d_result[classfyid] = []
            d_result[classfyid].append(confidence)
    for key in d_result:
        d_result[key] = max(d_result[key])
    return d_result

if __name__ == "__main__":
    filename = "image/test.jpg"
    d_result = return_diagnosis_dic(filename)
    print(d_result)