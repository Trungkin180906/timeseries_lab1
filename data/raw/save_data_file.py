import os
import pandas as pd

url = "https://raw.githubusercontent.com/selva86/datasets/master/a10.csv"
df = pd.read_csv(url)

# Lưu thẳng file a10.csv vào cùng thư mục với file code này
current_dir = os.path.dirname(os.path.abspath(__file__))
output_file = os.path.join(current_dir, "a10.csv")

df.to_csv(output_file, index=False)
print("Đã tải và lưu thành công tại:", output_file)