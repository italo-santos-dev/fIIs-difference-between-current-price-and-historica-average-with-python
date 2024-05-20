import pandas as pd
import matplotlib.pyplot as plt
import yfinance as yf
import locale

locale.setlocale(locale.LC_ALL, 'pt_BR.UTF-8')

ticker = 'LVBI11.SA'

data = yf.download(ticker, start="2000-01-01", end="2024-01-01")

historical_mean = data['Close'].mean()

current_price = data['Close'].iloc[-1]

comparison = pd.DataFrame({
    'Preço': [historical_mean, current_price],
}, index=['Média Histórica', 'Preço Atual'])

plt.style.use('ggplot')

fig, ax = plt.subplots(figsize=(10, 6))
bars = ax.bar(comparison.index,
              comparison['Preço'],
              color='#2F3336',
              edgecolor='black',
              width=0.2)

for bar in bars:
    yval = bar.get_height()
    ax.text(bar.get_x() + bar.get_width()/2, yval + 0.5,
            locale.currency(yval, grouping=True),
            ha='center', va='bottom', fontsize=12)

ax.set_xlim(-0.5, len(comparison.index) - 0.5)

ax.set_title(f'Comparação da Média Histórica do Preço da Cota com o Preço Atual do {ticker}',
             fontsize=12, weight='bold')
ax.set_ylabel('Preço (R$)', fontsize=12)
ax.set_xlabel('Tipo de Preço', fontsize=12)
ax.set_xticks(range(len(comparison.index)))
ax.set_xticklabels(comparison.index, fontsize=12)
ax.grid(axis='y', linestyle='--', linewidth=0.7)
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)

plt.tight_layout()
plt.show()
