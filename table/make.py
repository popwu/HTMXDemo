import json
import random

# 生成100条随机数据
data = [
    {"id": i, "name": f"User{i}", "age": random.randint(20, 40)} for i in range(100)
]

with open("data.json", "w") as f:
    json.dump(data, f)
