import matplotlib.pyplot as plt

# 数据
robsizes = [1024, 512, 256, 128, 64, 32, 16, 8, 4, 2]

# Minimal 配置
ipcs_minimal = [1.390743, 1.390743, 1.390743, 1.390743, 1.390743, 1.391384, 1.229334, 0.785566, 0.427468, 0.224478]

# NanhuG 配置
ipcs_nanhug = [1.823996, 1.823996, 1.823996, 1.823996, 1.829128, 1.676457, 1.221408, 0.699886, 0.016988, None]

# Default 配置
ipcs_default = [2.560265, 2.560265, 2.564732, 2.559266, 2.299096, 1.801814, 1.144567, 0.553030, None, None]

# 创建等间距的 x 轴位置
x_positions = range(len(robsizes))

# 绘制图形
plt.figure()

plt.plot(x_positions, ipcs_minimal, marker='o', label='Minimal Config')
plt.plot(x_positions, ipcs_nanhug, marker='s', label='NanhuG Config')
plt.plot(x_positions, ipcs_default, marker='^', label='Default Config')

# 设置 x 轴刻度和标签
plt.xticks(x_positions, robsizes)
plt.gca().invert_xaxis()

plt.xlabel('ROBSIZE')
plt.ylabel('IPC')
plt.title('IPC variation with ROBSIZE(Coremark 10 iterations)')
plt.legend()
plt.grid(True)
plt.show()``