import os
import numpy as np
import matplotlib.pyplot as plt

print("=== バラ曲線の設定 ===")
default_size = 0.8
default_pts = 10000
try:
    s_input = input(f"点の太さを入力してください [デフォルト: {default_size}]: ")
    POINT_SIZE = float(s_input) if s_input.strip() != "" else default_size
except ValueError:
    POINT_SIZE = default_size
    print(f"無効な値のため、デフォルト値 ({default_size}) を適用します。")

try:
    p_input = input(f"描画の解像度（点の分割数）を入力してください [デフォルト: {default_pts}]: ")
    N_PTS = int(p_input) if p_input.strip() != "" else default_pts
except ValueError:
    N_PTS = default_pts
    print(f"無効な値のため、デフォルト値 ({default_pts}) を適用します。")

folder_name = "outputs/rose-curve"
os.makedirs(folder_name, exist_ok=True)

theta = np.linspace(0, 20 * np.pi, N_PTS)
r = np.cos((5 / 7) * theta)
x, y = r * np.cos(theta), r * np.sin(theta)
dist = np.sqrt(x**2 + y**2)

r2 = np.sin((3 / 4) * theta)
x2, y2 = r2 * np.cos(theta), r2 * np.sin(theta)

fig_size, dpi_val = (8, 8), 600

print(f"'{folder_name}' フォルダに計6枚の画像を生成中（解像度: {N_PTS}, 太さ: {POINT_SIZE}）...\n")

single_rules = [("rule1", theta, 'hsv'), ("rule2", dist, 'plasma')]
for name, col_data, cmap_name in single_rules:
    fig, ax = plt.subplots(figsize=fig_size, facecolor='black')
    ax.set_facecolor('black')
    ax.scatter(x, y, c=col_data, cmap=cmap_name, s=POINT_SIZE, edgecolors='none')
    ax.axis('off')
    ax.set_aspect('equal', adjustable='box')
    plt.subplots_adjust(left=0, right=1, bottom=0, top=1)
    plt.savefig(os.path.join(folder_name, f'rose_{name}_dark.png'), dpi=dpi_val, facecolor='black', edgecolor='none')
    plt.close()

    fig, ax = plt.subplots(figsize=fig_size, facecolor='white')
    ax.set_facecolor('white')
    ax.scatter(x, y, c=col_data, cmap=cmap_name, s=POINT_SIZE, edgecolors='none')
    ax.axis('off')
    ax.set_aspect('equal', adjustable='box')
    plt.subplots_adjust(left=0, right=1, bottom=0, top=1)
    plt.savefig(os.path.join(folder_name, f'rose_{name}_light.png'), dpi=dpi_val, facecolor='white', edgecolor='none')
    plt.close()

for bg_col in ['black', 'white']:
    suffix = 'dark' if bg_col == 'black' else 'light'
    fig, ax = plt.subplots(figsize=fig_size, facecolor=bg_col)
    ax.set_facecolor(bg_col)
    ax.scatter(x, y, c='cyan', s=POINT_SIZE, alpha=0.7, edgecolors='none')
    ax.scatter(x2, y2, c='magenta', s=POINT_SIZE, alpha=0.7, edgecolors='none')
    ax.axis('off')
    ax.set_aspect('equal', adjustable='box')
    plt.subplots_adjust(left=0, right=1, bottom=0, top=1)
    plt.savefig(os.path.join(folder_name, f'rose_rule3_{suffix}.png'), dpi=dpi_val, facecolor=bg_col, edgecolor='none')
    plt.close()

print("Rose Curve 完了")