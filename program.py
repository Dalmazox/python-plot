import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

plt.rcdefaults()

dataset = pd.read_csv('./dataset.csv', parse_dates=True)

# Evolução dos casos de COVID-19 no Brasil desde o primeiro caso - LINE
date_cases = dataset[['date', 'cases']].groupby('date')['cases'].sum()

date_cases.plot.line()

plt.title('Número de casos de COVID-19 por data no Brasil')
plt.ylabel('Quantidade')
plt.xlabel('Data')
mng = plt.get_current_fig_manager()
mng.window.state('zoomed')
plt.show()

# Percentual de casos de COVID-19 por região - PIECHART
plt.close()
regions_cases = dataset[['region', 'cases']].groupby('region')['cases'].sum()

regions_cases.plot.pie(y='cases', figsize=(
    5, 5), autopct='%1.1f%%', legend=True, startangle=90, shadow=False)

plt.title('Distribuição de casos por região')
plt.ylabel('')
plt.xlabel('Distribuição')
mng = plt.get_current_fig_manager()
mng.window.state('zoomed')
plt.show()

# Novos casos x mortos por dia - BAR
plt.close()
date_cases_deaths = dataset[['date', 'cases', 'deaths']].groupby(
    'date').agg({'cases': 'sum', 'deaths': 'sum'})

date_cases_deaths[::7].plot.barh()

plt.ylabel('Data')
plt.xlabel('Quantidade')
plt.legend(['Casos', 'Mortes'])
mng = plt.get_current_fig_manager()
mng.window.state('zoomed')
plt.show()
