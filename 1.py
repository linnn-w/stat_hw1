import numpy as np
import matplotlib.pyplot as plt
from scipy import stats
from matplotlib.lines import Line2D

lambd = [0.5, 1, 1.5, 2, 3]
x = np.linspace(0, 10, 1000)

fig, ax = plt.subplots(figsize=(7, 4.5))
colors = plt.cm.Dark2(np.linspace(0, 1, len(lambd)))

line_handles, mean_handles = [], []

for c, lam in zip(colors, lambd):
    mu = 1 / lam
    y = stats.expon.pdf(x, scale=mu)

    # 主曲線 (λ)
    line, = ax.plot(x, y, color=c, linewidth=2.2, label=rf"$\lambda={lam}$")
    line_handles.append(line)

    # 均值點 + 輔助虛線
    ax.axvline(mu, color=c, linestyle='--', linewidth=1.2, alpha=0.25)
    ax.scatter(mu, stats.expon.pdf(mu, scale=mu), color=c, s=28, zorder=5)

    # μ 的 legend 只用點表示
    mean_handles.append(Line2D([0], [0], marker='o', color='none',
                               markerfacecolor=c, markersize=6,
                               label=rf"$\mu={mu:.2f}$"))

# 第一個 legend (λ)
leg1 = ax.legend(handles=line_handles, title="Rate (λ)",
                 loc="upper right", bbox_to_anchor=(1, 1), frameon=True)

# 第二個 legend (μ)，放在第一個 legend 下方
leg2 = ax.legend(handles=mean_handles, title="Expected Value (μ)",
                 loc="upper right", bbox_to_anchor=(1, 0.6), frameon=True)

# 把第一個 legend 放回畫布
ax.add_artist(leg1)

ax.set_title("Exponential Distribution with Expected Values")
ax.set_xlabel("x")
ax.set_ylabel("Density")
ax.grid(alpha=0.25)
fig.tight_layout()
plt.show()
