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

print("=== ゴールドバッハ彗星の設定 ===")
default_size = 1.2
default_max = 10000
try:
    s_input = input(f"点の太さを入力してください [デフォルト: {default_size}]: ")
    POINT_SIZE = float(s_input) if s_input.strip() != "" else default_size
except ValueError:
    POINT_SIZE = default_size

try:
    m_input = input(f"検証する偶数の最大値を入力してください [デフォルト: {default_max}]: ")
    MAX_VAL = int(m_input) if m_input.strip() != "" else default_max
except ValueError:
    MAX_VAL = default_max

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

folder_name = "outputs/goldbach-comet"
if os.path.exists(folder_name):
    shutil.rmtree(folder_name)
os.makedirs(folder_name, exist_ok=True)

modes = []
if BG_MODE in [1, 4]: modes.append('dark')
if BG_MODE in [2, 4]: modes.append('light')
if BG_MODE in [3, 4]: modes.append('transparent')

def sieve_of_eratosthenes(max_n):
    sieve = np.ones(max_n + 1, dtype=bool)
    sieve[0] = sieve[1] = False
    for i in range(2, int(np.sqrt(max_n)) + 1):
        if sieve[i]:
            sieve[i*i::i] = False
    return np.nonzero(sieve)[0]

print("素数を生成中...")
primes = sieve_of_eratosthenes(MAX_VAL)
prime_set = set(primes)

print("ゴールドバッハのペアを計算中...")
even_nums, counts, mod4_list, max_diffs, prime_factors_count = [], [], [], [], []

for ev in range(4, MAX_VAL + 1, 2):
    cnt, max_d = 0, 0
    for p in primes:
        if p > ev // 2: break
        q = ev - p
        if q in prime_set:
            cnt += 1
            max_d = max(max_d, q - p)
    if cnt > 0:
        even_nums.append(ev)
        counts.append(cnt)
        mod4_list.append((ev // 2) % 4)
        max_diffs.append(max_d)
        
        temp_n, f_cnt, d = ev // 2, 0, 2
        while d * d <= temp_n:
            while temp_n % d == 0:
                f_cnt += 1
                temp_n //= d
            d += 1
        if temp_n > 1: f_cnt += 1
        prime_factors_count.append(f_cnt)

x = np.array(even_nums)
y = np.array(counts)
fig_size = (10, 6)
dpi_val = 600

rules = [
    ("rule1", y, 'inferno'),
    ("rule2", np.array(mod4_list), 'tab10'),
    ("rule3", np.array(max_diffs), 'plasma'),
    ("rule4", x, 'viridis'),
    ("rule5", np.array(prime_factors_count), 'twilight')
]

total_steps = len(rules) * len(modes)
current_step = 0

print(f"\n'{folder_name}' フォルダをクリアし、画像を生成中（最大値: {MAX_VAL}, 太さ: {POINT_SIZE}）")
print_bar(current_step, total_steps, prefix="画像生成")

for name, col_data, cmap_name in rules:
    for mode in modes:
        if mode == 'dark':
            fig, ax = plt.subplots(figsize=fig_size, facecolor='black')
            ax.set_facecolor('black')
            ax.scatter(x, y, c=col_data, cmap=cmap_name, s=POINT_SIZE, edgecolors='none')
            ax.axis('off')
            plt.subplots_adjust(left=0, right=1, bottom=0, top=1)
            plt.savefig(os.path.join(folder_name, f'goldbach_{name}_dark.png'), dpi=dpi_val, facecolor='black', edgecolor='none')
        elif mode == 'light':
            fig, ax = plt.subplots(figsize=fig_size, facecolor='white')
            ax.set_facecolor('white')
            ax.scatter(x, y, c=col_data, cmap=cmap_name, s=POINT_SIZE, edgecolors='none')
            ax.axis('off')
            plt.subplots_adjust(left=0, right=1, bottom=0, top=1)
            plt.savefig(os.path.join(folder_name, f'goldbach_{name}_light.png'), dpi=dpi_val, facecolor='white', edgecolor='none')
        elif mode == 'transparent':
            fig, ax = plt.subplots(figsize=fig_size, facecolor='none')
            ax.set_facecolor('none')
            ax.scatter(x, y, c=col_data, cmap=cmap_name, s=POINT_SIZE, edgecolors='none')
            ax.axis('off')
            plt.subplots_adjust(left=0, right=1, bottom=0, top=1)
            plt.savefig(os.path.join(folder_name, f'goldbach_{name}_transparent.png'), dpi=dpi_val, transparent=True, edgecolor='none')

        plt.close()
        current_step += 1
        print_bar(current_step, total_steps, prefix="画像生成")

print("Goldbach Comet 完了")