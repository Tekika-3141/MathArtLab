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

print("=== ローレンツのアトラクターの設定 ===")
default_size = 0.3
default_steps = 100000
try:
    s_input = input(f"点の太さを入力してください [デフォルト: {default_size}]: ")
    POINT_SIZE = float(s_input) if s_input.strip() != "" else default_size
except ValueError:
    POINT_SIZE = default_size

try:
    st_input = input(f"シミュレーションのステップ数を入力してください [デフォルト: {default_steps}]: ")
    N_STEPS = int(st_input) if st_input.strip() != "" else default_steps
except ValueError:
    N_STEPS = default_steps

folder_name = "outputs/lorenz-attractor"
os.makedirs(folder_name, exist_ok=True)

dt = 0.01
xs, ys, zs = np.empty(N_STEPS), np.empty(N_STEPS), np.empty(N_STEPS)
xs[0], ys[0], zs[0] = 0.1, 0.0, 0.0
s, r, b = 10.0, 28.0, 8.0/3.0

print("微分方程式を数値積分中...")
for i in range(N_STEPS - 1):
    x, y, z = xs[i], ys[i], zs[i]
    xs[i+1] = x + s * (y - x) * dt
    ys[i+1] = y + (x * (r - z) - y) * dt
    zs[i+1] = z + (x * y - b * z) * dt

steps = np.linspace(0, 1, N_STEPS)
speeds = np.sqrt(np.gradient(xs)**2 + np.gradient(zs)**2)

fig_size, dpi_val = (8, 8), 600
rules = [("rule1", ys, 'viridis'), ("rule2", steps, 'plasma'), ("rule3", speeds, 'inferno')]

total_steps = len(rules) * 2
current_step = 0

print(f"'{folder_name}' フォルダに画像を生成中（ステップ数: {N_STEPS}, 太さ: {POINT_SIZE}）")
print_bar(current_step, total_steps, prefix="画像生成")

for name, col_data, cmap_name in rules:
    fig, ax = plt.subplots(figsize=fig_size, facecolor='black')
    ax.set_facecolor('black')
    ax.scatter(xs, zs, c=col_data, cmap=cmap_name, s=POINT_SIZE, alpha=0.5, edgecolors='none')
    ax.axis('off')
    ax.set_aspect('equal', adjustable='box')
    plt.subplots_adjust(left=0, right=1, bottom=0, top=1)
    plt.savefig(os.path.join(folder_name, f'lorenz_{name}_dark.png'), dpi=dpi_val, facecolor='black', edgecolor='none')
    plt.close()
    current_step += 1
    print_bar(current_step, total_steps, prefix="画像生成")

    fig, ax = plt.subplots(figsize=fig_size, facecolor='white')
    ax.set_facecolor('white')
    ax.scatter(xs, zs, c=col_data, cmap=cmap_name, s=POINT_SIZE, alpha=0.7, edgecolors='none')
    ax.axis('off')
    ax.set_aspect('equal', adjustable='box')
    plt.subplots_adjust(left=0, right=1, bottom=0, top=1)
    plt.savefig(os.path.join(folder_name, f'lorenz_{name}_light.png'), dpi=dpi_val, facecolor='white', edgecolor='none')
    plt.close()
    current_step += 1
    print_bar(current_step, total_steps, prefix="画像生成")

print("Lorenz Attractor 完了")