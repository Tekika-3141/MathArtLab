import os
import sys
import numpy as np
import matplotlib.pyplot as plt

def print_bar(iteration, total, prefix='進捗', length=25):
    filled = int(length * iteration // total)
    bar = '#' * filled + '-' * (length - filled)
    percent = int(100 * iteration / total)
    sys.stdout.write(f'\r{prefix} |{bar}| {percent}% ({iteration}/{total})')
    sys.stdout.flush()
    if iteration == total:
        print()

print("=== リサージュ図形の設定 ===")
default_size = 0.8
default_pts = 10000
try:
    s_input = input(f"点の太さを入力してください [デフォルト: {default_size}]: ")
    POINT_SIZE = float(s_input) if s_input.strip() != "" else default_size
except ValueError:
    POINT_SIZE = default_size

try:
    p_input = input(f"描画の解像度（点の分割数）を入力してください [デフォルト: {default_pts}]: ")
    N_PTS = int(p_input) if p_input.strip() != "" else default_pts
except ValueError:
    N_PTS = default_pts

folder_name = "outputs/lissajous-curve"
os.makedirs(folder_name, exist_ok=True)

t = np.linspace(0, 2 * np.pi, N_PTS)

x1 = np.sin(3 * t + np.pi / 2)
y1 = np.sin(4 * t)

x2 = np.sin(5 * t)
y2 = np.sin(6 * t + np.pi / 4)

dist = np.sqrt(x1**2 + y1**2)

fig_size, dpi_val = (8, 8), 600

total_steps = 6  # 単体2種(ダーク/ライトで4枚) + 重ね合わせ2種(ダーク/ライトで2枚) = 6枚
current_step = 0

print(f"'{folder_name}' フォルダに画像を生成中（解像度: {N_PTS}, 太さ: {POINT_SIZE}）")
print_bar(current_step, total_steps, prefix="画像生成")

single_rules = [
    ("rule1", x1, y1, t, 'hsv'),
    ("rule2", x1, y1, dist, 'plasma')
]

for name, x_data, y_data, col_data, cmap_name in single_rules:
    fig, ax = plt.subplots(figsize=fig_size, facecolor='black')
    ax.set_facecolor('black')
    ax.scatter(x_data, y_data, c=col_data, cmap=cmap_name, s=POINT_SIZE, edgecolors='none')
    ax.axis('off')
    ax.set_aspect('equal', adjustable='box')
    plt.subplots_adjust(left=0, right=1, bottom=0, top=1)
    plt.savefig(os.path.join(folder_name, f'lissajous_{name}_dark.png'), dpi=dpi_val, facecolor='black', edgecolor='none')
    plt.close()
    current_step += 1
    print_bar(current_step, total_steps, prefix="画像生成")

    fig, ax = plt.subplots(figsize=fig_size, facecolor='white')
    ax.set_facecolor('white')
    ax.scatter(x_data, y_data, c=col_data, cmap=cmap_name, s=POINT_SIZE, edgecolors='none')
    ax.axis('off')
    ax.set_aspect('equal', adjustable='box')
    plt.subplots_adjust(left=0, right=1, bottom=0, top=1)
    plt.savefig(os.path.join(folder_name, f'lissajous_{name}_light.png'), dpi=dpi_val, facecolor='white', edgecolor='none')
    plt.close()
    current_step += 1
    print_bar(current_step, total_steps, prefix="画像生成")

for bg_col in ['black', 'white']:
    suffix = 'dark' if bg_col == 'black' else 'light'
    fig, ax = plt.subplots(figsize=fig_size, facecolor=bg_col)
    ax.set_facecolor(bg_col)
    ax.scatter(x1, y1, c='cyan', s=POINT_SIZE, alpha=0.7, edgecolors='none')
    ax.scatter(x2, y2, c='orange', s=POINT_SIZE, alpha=0.7, edgecolors='none')
    ax.axis('off')
    ax.set_aspect('equal', adjustable='box')
    plt.subplots_adjust(left=0, right=1, bottom=0, top=1)
    plt.savefig(os.path.join(folder_name, f'lissajous_rule3_{suffix}.png'), dpi=dpi_val, facecolor=bg_col, edgecolor='none')
    plt.close()
    current_step += 1
    print_bar(current_step, total_steps, prefix="画像生成")

print("Lissajous Curve 完了")