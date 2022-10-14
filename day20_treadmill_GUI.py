from ssl import get_default_verify_paths
import tkinter as ttk
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns 
import warnings
warnings.filterwarnings('ignore')

data = pd.read_csv('treadmil-users.csv')

app = ttk.Tk()
app.title('Treadmill User Analysis')
app.geometry('600x300')

graphs = ttk.Variable(app)
values = {
    'Pair Plot': 'sns.pairplot(data= data)',
    'Jointplot': "sns.jointplot(data= data, x='{col1}', y='{col2}')",
    'Bar Plot': "sns.barplot(data= data, x='{col1}', y='{col2}')"
}
graphs.set(values['Pair Plot'])
y=10
for key, value in values.items():
    ttk.Radiobutton(app, text=key, variable=graphs, value= value).place(x=10,y=y)
    y+=20

## Option Menu 1
col1 = ttk.Variable(app)
values = ['Select'] + list(data.columns)
col1.set(values[0])
ttk.Label(app, text= 'Column 1').place(x=100,y=10)
ttk.OptionMenu(app, col1, *values).place(x= 100, y=40)

## Option Menu 2
col2 = ttk.Variable(app)
col2.set(values[0])
ttk.Label(app, text= 'Column 2').place(x=100,y=80)
ttk.OptionMenu(app, col1, *values).place(x= 100, y=110)

## Option Menu 3
col3 = ttk.Variable(app)
col3.set(values[0])
ttk.Label(app, text= 'Column 3').place(x=100,y=150)
ttk.OptionMenu(app, col1, *values).place(x= 100, y=180)


def show():
    print(graphs.get())
    print(col1.get())

ttk.Button(app, text='Show', command= show).place(x=400,y=10)

app.mainloop()