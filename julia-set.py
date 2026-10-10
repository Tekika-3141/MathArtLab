import os
import numpy as np
import matplotlib.pyplot as plt

print("=== ジュリア集合の設定 ===")
default_iter = 250
try:
    user_input = input(f"計算回数（最大イテレーション数）を入力してください [デフォルト: {default_iter}]: ")
    MAX_ITER = int(user_input) if user_input.strip() != "" else default_iter
except ValueError:
    MAX_ITER = default_iter
    print(f"無効な値のため、デフォルト値 ({default_iter}) を適用します。")

folder_name = "outputs/julia-set"
os.makedirs(folder_name, exist_ok=True)

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

print(f"'{folder_name}' フォルダに計6枚の画像を生成中（計算回数: {MAX_ITER}）...\n")

for name, img_data, cmap_name in configs:
    fig, ax = plt.subplots(figsize=(8, 8), facecolor='black')
    ax.set_facecolor('black')
    ax.imshow(img_data, extent=[xmin, xmax, ymin, ymax], cmap=cmap_name, origin='lower')
    ax.axis('off')
    plt.subplots_adjust(left=0, right=1, bottom=0, top=1)
    plt.savefig(os.path.join(folder_name, f'julia_{name}_dark.png'), dpi=600, facecolor='black', edgecolor='none')
    plt.close()

    fig, ax = plt.subplots(figsize=(8, 8), facecolor='white')
    ax.set_facecolor('white')
    ax.imshow(img_data, extent=[xmin, xmax, ymin, ymax], cmap=cmap_name + '_r', origin='lower')
    ax.axis('off')
    plt.subplots_adjust(left=0, right=1, bottom=0, top=1)
    plt.savefig(os.path.join(folder_name, f'julia_{name}_light.png'), dpi=600, facecolor='white', edgecolor='none')
    plt.close()

print("Julia Set 完了")