import pandas as pd
import statistics as st
import plotly_express as pe
import plotly.figure_factory as pf
import random as rand
import plotly.graph_objects as pg

data = pd.read_csv("medium_data.csv")
read= data["reading_time"].tolist()
regmean = st.mean(read)
regsd = st.stdev(read)

meanlist =[]

def sampling():
    list=[]
    for i in range(0,30):
        r=rand.randint(0,len(read)-1)
        list.append(read[r])
    return(st.mean(list))

def samplingsetup():
    for i in range(0,100):
        meanlist.append(sampling())
samplingsetup()

newmean = st.mean(meanlist)
newsd = st.stdev(meanlist)

print("The new mean of the data after sampling is", newmean)
print('The new standard deviation of the data after sampling is', newsd)

def plot_graph():
    #First intervention
    firstsdstart, firstsdend = newmean - newsd, newmean+newsd
    secondsdstart, secondsdend = newmean-2*newsd, newmean+2*newsd
    thirdsdstart, thirdsdend= newmean-3*newsd, newmean+3*newsd
    newgraph = pf.create_distplot([meanlist], ["News Data"], show_hist=False)
    newgraph.add_trace(pg.Scatter(x=[firstsdstart, firstsdstart], y=[0,0.5], mode="lines", name="First Region Start"))
    newgraph.add_trace(pg.Scatter(x=[firstsdend, firstsdend], y=[0, 0.5], mode="lines", name="First Region End"))
    newgraph.add_trace(pg.Scatter(x=[secondsdstart, secondsdstart], y=[0, 0.5], mode="lines", name="Second Region Start"))
    newgraph.add_trace(pg.Scatter(x=[secondsdend, secondsdend], y=[0, 0.5], mode="lines", name="Second Region End"))
    newgraph.add_trace(pg.Scatter(x=[thirdsdstart, thirdsdstart], y=[0, 0.5], mode="lines", name="Third Region Start"))
    newgraph.add_trace(pg.Scatter(x=[thirdsdend, thirdsdend], y=[0, 0.5], mode="lines", name="Third Region End"))
    newgraph.show()

plot_graph()