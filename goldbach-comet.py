import os
import numpy as np
import matplotlib.pyplot as plt

print("=== ゴールドバッハ彗星の設定 ===")
default_size = 1.2
default_max = 10000
try:
    s_input = input(f"点の太さを入力してください [デフォルト: {default_size}]: ")
    POINT_SIZE = float(s_input) if s_input.strip() != "" else default_size
except ValueError:
    POINT_SIZE = default_size
    print(f"無効な値のため、デフォルト値 ({default_size}) を適用します。")

try:
    m_input = input(f"検証する偶数の最大値を入力してください [デフォルト: {default_max}]: ")
    MAX_VAL = int(m_input) if m_input.strip() != "" else default_max
except ValueError:
    MAX_VAL = default_max
    print(f"無効な値のため、デフォルト値 ({default_max}) を適用します。")

folder_name = "outputs/goldbach-comet"
os.makedirs(folder_name, exist_ok=True)

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

print(f"'{folder_name}' フォルダに計10枚の画像を生成中（最大値: {MAX_VAL}, 太さ: {POINT_SIZE}）...\n")

for name, col_data, cmap_name in rules:
    fig, ax = plt.subplots(figsize=fig_size, facecolor='black')
    ax.set_facecolor('black')
    ax.scatter(x, y, c=col_data, cmap=cmap_name, s=POINT_SIZE, edgecolors='none')
    ax.axis('off')
    plt.subplots_adjust(left=0, right=1, bottom=0, top=1)
    plt.savefig(os.path.join(folder_name, f'goldbach_{name}_dark.png'), dpi=dpi_val, facecolor='black', edgecolor='none')
    plt.close()

    fig, ax = plt.subplots(figsize=fig_size, facecolor='white')
    ax.set_facecolor('white')
    ax.scatter(x, y, c=col_data, cmap=cmap_name, s=POINT_SIZE, edgecolors='none')
    ax.axis('off')
    plt.subplots_adjust(left=0, right=1, bottom=0, top=1)
    plt.savefig(os.path.join(folder_name, f'goldbach_{name}_light.png'), dpi=dpi_val, facecolor='white', edgecolor='none')
    plt.close()

print("Goldbach Comet 完了")