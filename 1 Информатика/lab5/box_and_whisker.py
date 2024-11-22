import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from matplotlib.ticker import MultipleLocator
def create_box_and_whisker(csv_file):
    try:
        data = pd.read_csv(csv_file, sep=';', encoding='utf-8')
        columns = ['Дата', 'Открытие', 'Макс', 'Мин', 'Закрытие']
        if not all(i in data.columns for i in columns):
            missing_col = [i for i in columns if i not in data.columns()]
            raise ValueError(f"Нет столбца/столбцов: {', '.join(missing_col)}")
        data['Дата'] = pd.to_datetime(data['Дата'], format='%d.%m.%Y')
        new_data = data.melt(id_vars='Дата', value_vars=[i for i in data.columns if i != 'Дата'])
        x_column = 'Дата'
        y_column = new_data.columns[-1]
        categories = new_data.columns[-2]
        plt.figure(figsize=(25, 8))
        sns.boxplot(data=new_data, x=new_data[x_column].dt.strftime('%d.%m.%Y'),
                    y=new_data[y_column], hue=new_data[categories], palette='husl')
        plt.title('Ящик с усами', fontsize=15, x=0.5, y=1.1)
        plt.xlabel('')
        plt.ylabel('')
        plt.legend(loc='upper center', bbox_to_anchor=(0.5, 1.09), ncol=4, title=None)
        plt.ylim(100000, 120000)
        plt.gca().yaxis.set_major_locator(MultipleLocator(2000))
        plt.grid(axis='y', linestyle='-', alpha=0.4)
        plt.show()
    except ValueError as error:
        print(f"Ошибка: {error}")
    except Exception as error:
        print(f"Ошибка: {error}")
create_box_and_whisker('/Users/sofiaabdullaeva/Downloads/additional_task2.csv')
