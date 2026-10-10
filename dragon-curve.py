import os
import numpy as np
import matplotlib.pyplot as plt

print("=== ドラゴン曲線の設定 ===")
default_size = 0.5
default_n = 16
try:
    s_input = input(f"点の太さを入力してください [デフォルト: {default_size}]: ")
    POINT_SIZE = float(s_input) if s_input.strip() != "" else default_size
except ValueError:
    POINT_SIZE = default_size
    print(f"無効な値のため、デフォルト値 ({default_size}) を適用します。")

try:
    n_input = input(f"世代数（折れ曲がり回数）を入力してください [デフォルト: {default_n}]: ")
    N_GEN = int(n_input) if n_input.strip() != "" else default_n
except ValueError:
    N_GEN = default_n
    print(f"無効な値のため、デフォルト値 ({default_n}) を適用します。")

folder_name = "outputs/dragon-curve"
os.makedirs(folder_name, exist_ok=True)

def get_dragon(n):
    coords = [0+0j, 1+0j]
    for _ in range(n):
        rev = coords[::-1]
        center = coords[-1]
        coords += [center + (c - center) * 1j for c in rev[1:]]
    return np.array([p.real for p in coords]), np.array([p.imag for p in coords])

x, y = get_dragon(N_GEN)
fig_size = (8, 8)
dpi_val = 600

dx = np.diff(x)
dy = np.diff(y)
cross = dx[:-1] * dy[1:] - dy[:-1] * dx[1:]
turns = np.zeros(len(x))
turns[1:-1] = np.sign(cross)

angles = np.zeros(len(x))
angles[:-1] = np.arctan2(dy, dx)
angles[-1] = angles[-2]

counts, xedges, yedges = np.histogram2d(x, y, bins=600)
x_idx = np.clip(np.digitize(x, xedges) - 1, 0, counts.shape[0] - 1)
y_idx = np.clip(np.digitize(y, yedges) - 1, 0, counts.shape[1] - 1)
densities = counts[x_idx, y_idx]

cx, cy = np.mean(x), np.mean(y)
distances = np.sqrt((x - cx)**2 + (y - cy)**2)

rules = [
    ("rule1", np.linspace(0, 1, len(x)), 'plasma'),
    ("rule2", turns, 'cool'),
    ("rule3", angles, 'hsv'),
    ("rule4", densities, 'inferno'),
    ("rule5", distances, 'viridis')
]

print(f"'{folder_name}' フォルダに計10枚の画像を生成中（世代数: {N_GEN}, 太さ: {POINT_SIZE}）...\n")

for name, col_data, cmap_name in rules:
    fig, ax = plt.subplots(figsize=fig_size, facecolor='black')
    ax.set_facecolor('black')
    ax.scatter(x, y, c=col_data, cmap=cmap_name, s=POINT_SIZE, edgecolors='none')
    ax.axis('off')
    ax.set_aspect('equal', adjustable='box')
    plt.subplots_adjust(left=0, right=1, bottom=0, top=1)
    plt.savefig(os.path.join(folder_name, f'dragon_{name}_dark.png'), dpi=dpi_val, facecolor='black', edgecolor='none')
    plt.close()

    fig, ax = plt.subplots(figsize=fig_size, facecolor='white')
    ax.set_facecolor('white')
    ax.scatter(x, y, c=col_data, cmap=cmap_name, s=POINT_SIZE, edgecolors='none')
    ax.axis('off')
    ax.set_aspect('equal', adjustable='box')
    plt.subplots_adjust(left=0, right=1, bottom=0, top=1)
    plt.savefig(os.path.join(folder_name, f'dragon_{name}_light.png'), dpi=dpi_val, facecolor='white', edgecolor='none')
    plt.close()

print("Dragon Curve 完了")