import os
import numpy as np
import matplotlib.pyplot as plt

print("=== クリフォードのアトラクターの設定 ===")
default_size = 0.3
default_points = 500000
try:
    s_input = input(f"点の太さを入力してください [デフォルト: {default_size}]: ")
    POINT_SIZE = float(s_input) if s_input.strip() != "" else default_size
except ValueError:
    POINT_SIZE = default_size
    print(f"無効な値のため、デフォルト値 ({default_size}) を適用します。")

try:
    p_input = input(f"計算する点の総数を入力してください [デフォルト: {default_points}]: ")
    N_POINTS = int(p_input) if p_input.strip() != "" else default_points
except ValueError:
    N_POINTS = default_points
    print(f"無効な値のため、デフォルト値 ({default_points}) を適用します。")

folder_name = "outputs/clifford-attractor"
os.makedirs(folder_name, exist_ok=True)

x, y = np.zeros(N_POINTS), np.zeros(N_POINTS)
a, b, c, d = -1.4, 1.6, 1.0, 0.7

print("アトラクターの軌道を計算中...")
for i in range(N_POINTS - 1):
    x[i+1] = np.sin(a * y[i]) + c * np.cos(a * x[i])
    y[i+1] = np.sin(b * x[i]) + d * np.cos(b * y[i])

dist = np.sqrt(x**2 + y**2)
steps = np.linspace(0, 1, N_POINTS)
counts, xedges, yedges = np.histogram2d(x, y, bins=600)
densities = counts[np.clip(np.digitize(x, xedges) - 1, 0, counts.shape[0] - 1), 
                  np.clip(np.digitize(y, yedges) - 1, 0, counts.shape[1] - 1)]

fig_size, dpi_val = (8, 8), 600
rules = [("rule1", dist, 'plasma'), ("rule2", steps, 'inferno'), ("rule3", densities, 'magma')]

print(f"'{folder_name}' フォルダに計6枚の画像を生成中（点数: {N_POINTS}, 太さ: {POINT_SIZE}）...\n")

for name, col_data, cmap_name in rules:
    fig, ax = plt.subplots(figsize=fig_size, facecolor='black')
    ax.set_facecolor('black')
    ax.scatter(x, y, c=col_data, cmap=cmap_name, s=POINT_SIZE, alpha=0.4, edgecolors='none')
    ax.axis('off')
    ax.set_aspect('equal', adjustable='box')
    plt.subplots_adjust(left=0, right=1, bottom=0, top=1)
    plt.savefig(os.path.join(folder_name, f'clifford_{name}_dark.png'), dpi=dpi_val, facecolor='black', edgecolor='none')
    plt.close()

    fig, ax = plt.subplots(figsize=fig_size, facecolor='white')
    ax.set_facecolor('white')
    ax.scatter(x, y, c=col_data, cmap=cmap_name, s=POINT_SIZE, alpha=0.6, edgecolors='none')
    ax.axis('off')
    ax.set_aspect('equal', adjustable='box')
    plt.subplots_adjust(left=0, right=1, bottom=0, top=1)
    plt.savefig(os.path.join(folder_name, f'clifford_{name}_light.png'), dpi=dpi_val, facecolor='white', edgecolor='none')
    plt.close()

print("Clifford Attractor 完了")