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

print("=== 相沢のアトラクターの設定 ===")
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

folder_name = "outputs/aizawa-attractor"
if os.path.exists(folder_name):
    shutil.rmtree(folder_name)
os.makedirs(folder_name, exist_ok=True)

modes = []
if BG_MODE in [1, 4]: modes.append('dark')
if BG_MODE in [2, 4]: modes.append('light')
if BG_MODE in [3, 4]: modes.append('transparent')

dt = 0.01
xs, ys, zs = np.empty(N_STEPS), np.empty(N_STEPS), np.empty(N_STEPS)
xs[0], ys[0], zs[0] = 0.1, 0.0, 0.1
a, b, c, d, e, f = 0.95, 0.7, 0.6, 3.5, 0.25, 0.1

print("微分方程式を数値積分中...")
for i in range(N_STEPS - 1):
    x, y, z = xs[i], ys[i], zs[i]
    dx = (z - b) * x - d * y
    dy = d * x + (z - b) * y
    dz = c + a * z - (z**3) / 3.0 - (x**2 + y**2) * (1.0 + e * z) + f * z * (x**3)
    
    xs[i+1] = x + dx * dt
    ys[i+1] = y + dy * dt
    zs[i+1] = z + dz * dt

steps = np.linspace(0, 1, N_STEPS)
depths = zs
radial = np.sqrt(xs**2 + ys**2)

fig_size, dpi_val = (8, 8), 600
rules = [("rule1", depths, 'viridis'), ("rule2", steps, 'plasma'), ("rule3", radial, 'inferno')]

total_steps = len(rules) * len(modes)
current_step = 0

print(f"\n'{folder_name}' フォルダをクリアし、画像を生成中（ステップ数: {N_STEPS}, 太さ: {POINT_SIZE}）")
print_bar(current_step, total_steps, prefix="画像生成")

for name, col_data, cmap_name in rules:
    for mode in modes:
        if mode == 'dark':
            fig, ax = plt.subplots(figsize=fig_size, facecolor='black')
            ax.set_facecolor('black')
            ax.scatter(xs, ys, c=col_data, cmap=cmap_name, s=POINT_SIZE, alpha=0.5, edgecolors='none')
            ax.axis('off')
            ax.set_aspect('equal', adjustable='box')
            plt.subplots_adjust(left=0, right=1, bottom=0, top=1)
            plt.savefig(os.path.join(folder_name, f'aizawa_{name}_dark.png'), dpi=dpi_val, facecolor='black', edgecolor='none')
        elif mode == 'light':
            fig, ax = plt.subplots(figsize=fig_size, facecolor='white')
            ax.set_facecolor('white')
            ax.scatter(xs, ys, c=col_data, cmap=cmap_name, s=POINT_SIZE, alpha=0.7, edgecolors='none')
            ax.axis('off')
            ax.set_aspect('equal', adjustable='box')
            plt.subplots_adjust(left=0, right=1, bottom=0, top=1)
            plt.savefig(os.path.join(folder_name, f'aizawa_{name}_light.png'), dpi=dpi_val, facecolor='white', edgecolor='none')
        elif mode == 'transparent':
            fig, ax = plt.subplots(figsize=fig_size, facecolor='none')
            ax.set_facecolor('none')
            ax.scatter(xs, ys, c=col_data, cmap=cmap_name, s=POINT_SIZE, alpha=0.6, edgecolors='none')
            ax.axis('off')
            ax.set_aspect('equal', adjustable='box')
            plt.subplots_adjust(left=0, right=1, bottom=0, top=1)
            plt.savefig(os.path.join(folder_name, f'aizawa_{name}_transparent.png'), dpi=dpi_val, transparent=True, edgecolor='none')

        plt.close()
        current_step += 1
        print_bar(current_step, total_steps, prefix="画像生成処理")

print("Aizawa Attractor 完了")