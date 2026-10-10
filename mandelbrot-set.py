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

print("=== マンデルブロ集合の設定 ===")
default_iter = 250
try:
    user_input = input(f"計算回数（最大イテレーション数）を入力してください [デフォルト: {default_iter}]: ")
    MAX_ITER = int(user_input) if user_input.strip() != "" else default_iter
except ValueError:
    MAX_ITER = default_iter

folder_name = "outputs/mandelbrot-set"
os.makedirs(folder_name, exist_ok=True)

width, height = 1000, 1000
xmin, xmax, ymin, ymax = -2.0, 0.5, -1.25, 1.25
x = np.linspace(xmin, xmax, width)
y = np.linspace(ymin, ymax, height)
c = x[np.newaxis, :] + 1j * y[:, np.newaxis]

def get_mandelbrot(max_iter):
    Z = np.zeros_like(c)
    img = np.zeros(Z.shape, dtype=float)
    for i in range(max_iter):
        mask = np.abs(Z) < 10
        Z[mask] = Z[mask]**2 + c[mask]
        img[mask] = i
    return img

img_mandel = get_mandelbrot(MAX_ITER)

configs = [
    ("rule1", img_mandel, 'inferno'),
    ("rule2", img_mandel, 'magma'),
    ("rule3", img_mandel, 'twilight')
]

total_steps = len(configs) * 2
current_step = 0

print(f"'{folder_name}' フォルダに画像を生成中（計算回数: {MAX_ITER}）")
print_bar(current_step, total_steps, prefix="画像生成")

for name, img_data, cmap_name in configs:
    fig, ax = plt.subplots(figsize=(8, 8), facecolor='black')
    ax.set_facecolor('black')
    ax.imshow(img_data, extent=[xmin, xmax, ymin, ymax], cmap=cmap_name, origin='lower')
    ax.axis('off')
    plt.subplots_adjust(left=0, right=1, bottom=0, top=1)
    plt.savefig(os.path.join(folder_name, f'mandelbrot_{name}_dark.png'), dpi=600, facecolor='black', edgecolor='none')
    plt.close()
    current_step += 1
    print_bar(current_step, total_steps, prefix="画像生成")

    fig, ax = plt.subplots(figsize=(8, 8), facecolor='white')
    ax.set_facecolor('white')
    ax.imshow(img_data, extent=[xmin, xmax, ymin, ymax], cmap=cmap_name + '_r', origin='lower')
    ax.axis('off')
    plt.subplots_adjust(left=0, right=1, bottom=0, top=1)
    plt.savefig(os.path.join(folder_name, f'mandelbrot_{name}_light.png'), dpi=600, facecolor='white', edgecolor='none')
    plt.close()
    current_step += 1
    print_bar(current_step, total_steps, prefix="画像生成")

print("Mandelbrot Set 完了")