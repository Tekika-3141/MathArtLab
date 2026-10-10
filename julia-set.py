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

print("=== ジュリア集合の設定 ===")
default_iter = 250
try:
    user_input = input(f"計算回数（最大イテレーション数）を入力してください [デフォルト: {default_iter}]: ")
    MAX_ITER = int(user_input) if user_input.strip() != "" else default_iter
except ValueError:
    MAX_ITER = default_iter

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

folder_name = "outputs/julia-set"
if os.path.exists(folder_name):
    shutil.rmtree(folder_name)
os.makedirs(folder_name, exist_ok=True)

modes = []
if BG_MODE in [1, 4]: modes.append('dark')
if BG_MODE in [2, 4]: modes.append('light')
if BG_MODE in [3, 4]: modes.append('transparent')

width, height = 1000, 1000
xmin, xmax, ymin, ymax = -1.5, 1.5, -1.5, 1.5
x = np.linspace(xmin, xmax, width)
y = np.linspace(ymin, ymax, height)
Z_orig = x[np.newaxis, :] + 1j * y[:, np.newaxis]

def get_julia_img(c, max_iter):
    Z = Z_orig.copy()
    img = np.zeros(Z.shape, dtype=float)
    for i in range(max_iter):
        mask = np.abs(Z) < 10
        Z[mask] = Z[mask]**2 + c
        img[mask] = i
    return img

img1 = get_julia_img(-0.7 + 0.27015j, MAX_ITER)
img2 = get_julia_img(-0.4 + 0.6j, MAX_ITER)

configs = [
    ("rule1", img1, 'inferno'),
    ("rule2", img1, 'twilight'),
    ("rule3", img2, 'plasma')
]

total_steps = len(configs) * len(modes)
current_step = 0

print(f"\n'{folder_name}' フォルダをクリアし、画像を生成中（計算回数: {MAX_ITER}）")
print_bar(current_step, total_steps, prefix="画像生成")

for name, img_data, cmap_name in configs:
    for mode in modes:
        is_transparent = (mode == 'transparent')
        bg_col = 'black' if mode == 'dark' else ('white' if mode == 'light' else 'none')
        c_map = cmap_name if mode != 'light' else cmap_name + '_r'
        
        fig, ax = plt.subplots(figsize=(8, 8), facecolor=bg_col if not is_transparent else 'none')
        if not is_transparent:
            ax.set_facecolor(bg_col)
        else:
            ax.set_facecolor('none')
            
        ax.imshow(img_data, extent=[xmin, xmax, ymin, ymax], cmap=c_map, origin='lower')
        ax.axis('off')
        plt.subplots_adjust(left=0, right=1, bottom=0, top=1)
        
        filename = f'julia_{name}_{mode}.png'
        plt.savefig(os.path.join(folder_name, filename), dpi=600, facecolor=bg_col if not is_transparent else 'none', transparent=is_transparent, edgecolor='none')
        plt.close()
        
        current_step += 1
        print_bar(current_step, total_steps, prefix="画像生成")

print("Julia Set 完了")