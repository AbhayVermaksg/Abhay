#Importing Required Libraries
import tkinter
import pandas as pd
import warnings
warnings.filterwarnings('ignore')
import os
print('Location is:',os.getcwd(),'\n\n\n\n')

#App Creation
app= tkinter.Tk()
app.title('Recommendation System')
app.geometry('400x400')

#Read The Files
cols=['user_id','movie_id','rating','ts']
item_cols=['movie_id','title']+ list(range(22))
df= pd.read_csv('u.data',sep='\t', names=cols ).drop('ts',axis=1)
df1=pd.read_csv('u.item', sep='|', encoding='ISO-8859-1', names=item_cols)[['movie_id','title']]

#Merge The Dataframes
movie= pd.merge(df,df1, on='movie_id')

#Creating Result Variable
result = tkinter.Variable(app)

#Creating A frame/Sub-Window
frame = tkinter.Frame(app)
frame.place(x=10,y=10)

#Creating a List Box and Attach it to Frame
box = tkinter.Listbox(frame, height=10, width=50)
for title in movie['title'].unique():
    box.insert(tkinter.END, title)
box.pack(side='left', fill='y')

#Creating A Scrollbar and Attach it to frame
scroll = tkinter.Scrollbar(frame, orient=tkinter.VERTICAL)
scroll.config(command= box.yview)
box.config(yscrollcommand= scroll.set)
scroll.pack(side='right', fill='y')

#MOVIE RECOMMENDER
def get_movie():
    #Movie Selection
    movie_selected = box.get(box.curselection())

    #Create The Pivot Table
    movie_pivot = movie.pivot_table(index='user_id',columns = 'title',values='rating')
    
    #Find Similarities for Selected Movie
    corrs = movie_pivot.corrwith(movie_pivot[movie_selected])
    corrs_df=pd.DataFrame(corrs,columns=['correlation'])
    corrs_df['rating']=movie.groupby('title')['rating'].mean()
    corrs_df['count']=movie['title'].value_counts()
    
    #Find Top 2-3 Recommendations
    top_recom = list(corrs_df[corrs_df['count']>50].sort_values(by='correlation',ascending=False).head(3).index)
    top_recom.remove(movie_selected)

    # Important
    if movie_selected in top_recom:
        top_recom.remove(movie_selected)
    print('Recommedations:',top_recom)

    if top_recom:
        result.set(top_recom[0])
    else:
        result.set('Sorry NO Recommendations Found!!')
    
tkinter.Button(app, text='Find Recommendations', font=('Arial',22),command= get_movie).place(x=10,y=250)

tkinter.Label(app, textvariable=result, font=('Arial',22)).place(x=10,y=300)

app.mainloop()