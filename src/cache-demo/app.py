import pandas as pd
df = pd.DataFrame({"course": ["Korean", "Chinese", "German"], "students": [120, 95, 60]})
print(df)
print("รวมนักเรียน:", df["students"].sum())
print("แก้โค้ดนิดเดียว")
print("แก้อีกรอบ")
