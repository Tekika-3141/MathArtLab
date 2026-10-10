import os
import sys
import shutil
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

print("=== ド・ジョン・アトラクターの設定 ===")
default_size = 0.3
default_points = 500000
try:
    s_input = input(f"点の太さを入力してください [デフォルト: {default_size}]: ")
    POINT_SIZE = float(s_input) if s_input.strip() != "" else default_size
except ValueError:
    POINT_SIZE = default_size

try:
    p_input = input(f"計算する点の総数を入力してください [デフォルト: {default_points}]: ")
    N_POINTS = int(p_input) if p_input.strip() != "" else default_points
except ValueError:
    N_POINTS = default_points

print("\n=== 背景モードの選択 ===")
print("1. ダーク (Dark)")
print("2. ライト (Light)")
print("3. 透過 (Transparent)")
print("4. すべて生成 (Dark, Light, Transparent)")
try:
    bg_input = input("番号を入力してください [デフォルト: 4]: ")
    BG_MODE = int(bg_input) if bg_input.strip() != "" else 4
except ValueError:
    BG_MODE = 4

folder_name = "outputs/dejong-attractor"
if os.path.exists(folder_name):
    shutil.rmtree(folder_name)
os.makedirs(folder_name, exist_ok=True)

modes = []
if BG_MODE in [1, 4]: modes.append('dark')
if BG_MODE in [2, 4]: modes.append('light')
if BG_MODE in [3, 4]: modes.append('transparent')

x, y = np.zeros(N_POINTS), np.zeros(N_POINTS)
x[0], y[0] = 0.1, 0.1
a, b, c, d = 1.4, -2.3, 2.4, -2.1

print("アトラクターの軌道を計算中...")
for i in range(N_POINTS - 1):
    x[i+1] = np.sin(a * y[i]) - np.cos(b * x[i])
    y[i+1] = np.sin(c * x[i]) - np.cos(d * y[i])

dist = np.sqrt(x**2 + y**2)
steps = np.linspace(0, 1, N_POINTS)
counts, xedges, yedges = np.histogram2d(x, y, bins=600)
densities = counts[np.clip(np.digitize(x, xedges) - 1, 0, counts.shape[0] - 1), 
                  np.clip(np.digitize(y, yedges) - 1, 0, counts.shape[1] - 1)]

fig_size, dpi_val = (8, 8), 600
rules = [("rule1", dist, 'plasma'), ("rule2", steps, 'inferno'), ("rule3", densities, 'magma')]

total_steps = len(rules) * len(modes)
current_step = 0

print(f"\n'{folder_name}' フォルダをクリアし、画像を生成中（点数: {N_POINTS}, 太さ: {POINT_SIZE}）")
print_bar(current_step, total_steps, prefix="画像生成")

for name, col_data, cmap_name in rules:
    for mode in modes:
        if mode == 'dark':
            fig, ax = plt.subplots(figsize=fig_size, facecolor='black')
            ax.set_facecolor('black')
            ax.scatter(x, y, c=col_data, cmap=cmap_name, s=POINT_SIZE, alpha=0.4, edgecolors='none')
            ax.axis('off')
            ax.set_aspect('equal', adjustable='box')
            plt.subplots_adjust(left=0, right=1, bottom=0, top=1)
            plt.savefig(os.path.join(folder_name, f'dejong_{name}_dark.png'), dpi=dpi_val, facecolor='black', edgecolor='none')
        elif mode == 'light':
            fig, ax = plt.subplots(figsize=fig_size, facecolor='white')
            ax.set_facecolor('white')
            ax.scatter(x, y, c=col_data, cmap=cmap_name, s=POINT_SIZE, alpha=0.6, edgecolors='none')
            ax.axis('off')
            ax.set_aspect('equal', adjustable='box')
            plt.subplots_adjust(left=0, right=1, bottom=0, top=1)
            plt.savefig(os.path.join(folder_name, f'dejong_{name}_light.png'), dpi=dpi_val, facecolor='white', edgecolor='none')
        elif mode == 'transparent':
            fig, ax = plt.subplots(figsize=fig_size, facecolor='none')
            ax.set_facecolor('none')
            ax.scatter(x, y, c=col_data, cmap=cmap_name, s=POINT_SIZE, alpha=0.5, edgecolors='none')
            ax.axis('off')
            ax.set_aspect('equal', adjustable='box')
            plt.subplots_adjust(left=0, right=1, bottom=0, top=1)
            plt.savefig(os.path.join(folder_name, f'dejong_{name}_transparent.png'), dpi=dpi_val, transparent=True, edgecolor='none')

        plt.close()
        current_step += 1
        print_bar(current_step, total_steps, prefix="画像生成")

print("De Jong Attractor 完了")