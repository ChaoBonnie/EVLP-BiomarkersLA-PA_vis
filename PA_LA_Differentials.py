import pandas as pd
import seaborn as sns; sns.set(style='darkgrid', context='talk')
import matplotlib.pyplot as plt
from matplotlib.gridspec import GridSpec


location_map = {'30': 'LA-PA at 30min', '90': 'LA-PA at 90min', '150': 'LA-PA at 150min'}

# Graph by cytokines #

y_cytokine = ['IL-6 (pg/mL)', 'IL-8 (pg/mL)', 'sTNF-R1 (pg/mL)', 'sTREM-1 (pg/mL)',
      'ET-1 (pg/mL)', 'GM-CSF (pg/mL)', 'IL-10 (pg/mL)', 'IL-1β (pg/mL)']

def make_graph_by_cytokine(data_path, sheet_name, style, figsize=(20, 12)):
    df_cytokine = pd.read_excel(data_path, sheet_name=sheet_name)

    fig = plt.figure(figsize=figsize)
    gs = GridSpec(3, 3)
    axs = []
    for i in range(len(y_cytokine)):
        row = i // gs.ncols
        col = i % gs.ncols
        axs.append(fig.add_subplot(gs[row, col]))

    if style == 'bar':
        for ax, y in zip(axs, y_cytokine):
            sns.barplot(x='EVLP ID', y=y, hue='Time (min)', data=df_cytokine, ax=ax)
            print(y, df_cytokine[y].mean())
            ax.legend().remove()

        handles, labels = axs[0].get_legend_handles_labels()
        labels = [location_map[l] for l in labels]
        fig.legend(handles, labels, loc=(0.78, 0.15))
        fig.tight_layout()
        fig.savefig('LA-PA Difference Bar Plot by Cytokines.png', dpi=200)

    else:
        for ax, y in zip(axs, y_cytokine):
            sns.stripplot(x='Time (min)', y=y, data=df_cytokine, ax=ax)
            sns.boxplot(x='Time (min)', y=y, data=df_cytokine, ax=ax, saturation=0.5, palette='pastel')
        fig.tight_layout()
        fig.savefig('LA-PA Difference Scatter Plot by Cytokines.png', dpi=200)

make_graph_by_cytokine(r'C:\Users\chaob\Documents\LA-PA Data Sheets.xlsx', 'Differences by Cytokines', 'bar')
make_graph_by_cytokine(r'C:\Users\chaob\Documents\LA-PA Data Sheets.xlsx', 'Differences by Cytokines', 'scatter', figsize=(18, 12))

# Graph by donors #

y_donor = ['#480', '#489', '#492', '#493', '#497', '#500',
           '#510', '#512', '#513', '#518', '#519', '#522']

def make_graph_by_donor(data_path, sheet_name, style, figsize=(36, 18)):

    df_donor = pd.read_excel(data_path, sheet_name=sheet_name)

    fig = plt.figure(figsize=figsize)
    gs = GridSpec(3, 4)
    axs = []
    for i in range(len(y_donor)):
        row = i // gs.ncols
        col = i % gs.ncols
        axs.append(fig.add_subplot(gs[row, col]))

    for ax, y in zip(axs, y_donor):
        if style == 'bar':
            sns.barplot(x='Cytokines', y=y, hue='Time (min)', data=df_donor, ax=ax)
            print(y, df_donor[y].mean())
            ax.legend().remove()
            fig.tight_layout()
            fig.savefig('LA-PA Difference Bar Plot by Donors.png', dpi=200)
        else:
            sns.stripplot(x='Time (min)', y=y, data=df_donor, ax=ax)
            sns.boxplot(x='Time (min)', y=y, data=df_donor, ax=ax, saturation=0.5, palette='pastel')
            fig.tight_layout()
            fig.savefig('LA-PA Difference Scatter Plot by Donors.png', dpi=200)

make_graph_by_donor(r'C:\Users\chaob\Documents\LA-PA Data Sheets.xlsx', 'Differences by Donors', 'bar')
make_graph_by_donor(r'C:\Users\chaob\Documents\LA-PA Data Sheets.xlsx', 'Differences by Donors', 'scatter', figsize=(24, 18))