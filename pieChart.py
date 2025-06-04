import pandas as pd
import matplotlib.pyplot as plt

# Đọc dữ liệu
df = pd.read_csv("cntt_chuyennganh.csv")
df.set_index("Khóa", inplace=True)

# Dữ liệu năm 2022
data_2022 = df.loc[2022]

# Danh sách chuyên ngành sắp xếp giảm dần theo số lượng
sorted_data = data_2022.sort_values(ascending=False)

# Tính phần trăm
percent_2022 = sorted_data / sorted_data.sum() * 100

# Lấy bảng màu (có thể thay đổi cmap nếu muốn)
colors = plt.cm.tab20.colors[:len(sorted_data)]  # đảm bảo số lượng màu đúng
# Bạn có thể thay tab20 bằng:
# plt.cm.Paired.colors
# plt.cm.Set3.colors
# plt.cm.Accent.colors

# Tạo figure
fig, axes = plt.subplots(1, 2, figsize=(14, 7), gridspec_kw={'width_ratios': [1, 0.8]}, constrained_layout=False) # Tỉ lệ 2 phần: 1, 0.8

fig.suptitle(
    "Tỉ lệ sinh viên Nhóm ngành CNTT được xét vào chuyên ngành khóa 2022",
    fontsize=16,
    fontweight='bold',
    color='darkblue',
    y=0.98
)

# === Biểu đồ tròn (trái) ===
axes[0].pie(
    percent_2022,
    labels= [name if count > 9 else '' for name, count 
             in zip (sorted_data.index, sorted_data.values)], #sorted_data.index tránh chồng, chỉ count > 9
    autopct=lambda pct: f'{pct:.1f}%' if pct > 3 else '', # tránh chồng nhau, chỉ tỉ lệ > 3%
    startangle=90,
    colors=colors,
    wedgeprops={'linewidth': 1, 'edgecolor': 'white'}
)
axes[0].set_title("Tỷ lệ sinh viên theo chuyên ngành", fontsize=10, fontweight='bold')

# === Biểu đồ cột ngang (phải) ===
bars = axes[1].barh(
    sorted_data.index,
    sorted_data.values,
    color=colors
)
for i, (value, label) in enumerate(zip(sorted_data.values, sorted_data.index)):
    axes[1].text(value + 2, i, str(value), va='center', fontsize=9)

axes[1].invert_yaxis()
axes[1].set_xlabel("Số lượng")
axes[1].set_title("Số lượng sinh viên theo chuyên ngành", fontsize=10, fontweight='bold')

total_students = data_2022.sum()
axes[0].text(
    0.5, -0.1,  # x, y theo tọa độ tương đối của axes[0]
    f"Tổng số sinh viên: {total_students}",
    fontsize=12,
    fontweight='bold',
    color='darkblue',
    ha='center',
    transform=axes[0].transAxes  # dùng hệ tọa độ tương đối theo axes
)

# Layout & lưu
# plt.show()
fig.tight_layout(rect=[0, 0, 1, 0.95]) #[left, bottom, right, top] Giữ lại 5% trên cùng
plt.savefig("bieu_do_chuyen_nganh_2022.png", dpi=300)
# plt.show()
