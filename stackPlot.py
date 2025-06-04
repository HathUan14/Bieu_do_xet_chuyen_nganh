import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Đọc dữ liệu
df = pd.read_csv("cntt_chuyennganh.csv")
df.set_index("Khóa", inplace=True)

# Tính phần trăm
df_percent = df.div(df.sum(axis=1), axis=0) * 100

# Tính tổng sinh viên theo năm
totals = df.sum(axis=1)

# Chuẩn bị dữ liệu cho stackplot
years = df_percent.index.values
categories = df_percent.columns
data = df_percent.T.values  # Transpose để stackplot cần mỗi dòng là 1 category

# Vẽ biểu đồ miền
plt.figure(figsize=(12, 6))
colors = plt.get_cmap("tab20").colors
plt.stackplot(years, data, labels=categories, colors=colors[:len(categories)], alpha=0.85)

# Chú thích trực tiếp phần trăm
for i, year in enumerate(years):
    y_bottom = 0
    for j, category in enumerate(categories):
        value = df_percent.iloc[i, j]
        y_center = y_bottom + value / 2
        if value > 3:  # Chỉ hiện nếu chiếm >3% để tránh rối
            plt.text(year, y_center, f"{value:.0f}%", ha='center', va='center', fontsize=8)
        y_bottom += value

# Ghi tổng sinh viên ở trên cùng mỗi cột
for i, year in enumerate(years):
    plt.text(year, 103, f"Tổng: {totals[year]}", ha='center', va='bottom',
              fontsize=9, fontweight='bold', color='black')
    
# Cài đặt biểu đồ
plt.title("Phân bố sinh viên Nhóm ngành Công Nghệ Thông Tin được xét vào chuyên ngành theo từng khóa",
    fontsize=14,
    fontweight='bold',
    color='darkblue',
    loc='left',      # hoặc 'left', 'right'
    pad=20)
plt.xlabel("Khóa")
plt.ylabel("Tỷ lệ (%)")
plt.xticks(years)
plt.yticks(range(0, 111, 10))
plt.legend(loc='center left', bbox_to_anchor=(1.01, 0.5))
plt.grid(True, linestyle='--', alpha=0.5)
plt.tight_layout()


plt.savefig("bieu_do_mien_chuyen_nganh.png", dpi=300)
# plt.show()
