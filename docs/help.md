# 病害是识别

# 病害类型及对应id

{0: 'Spodoptera_Frugiperda_Egg', 1: 'Healthy', 2: 'Spodoptera_Frugiperda_aftermath', 3: 'Blight', 4: 'Common_Rust', 5: 'Gray_Leaf_Spot'}

翻译后：
{
    0: "草地贪夜蛾卵",
    1: "健康",
    2: "草地贪夜蛾危害后",
    3: "叶枯病",
    4: "普通锈病",
    5: "灰斑病"
}

# 结果数据提取

```python
for result in results:
    x1 =result.names
    print("类型名",result.names)
    for box in result.boxes:
        print("边界框坐标：",box.xyxy)
        print("置信度：",box.conf)
        print("类别id: ",box.cls)
```