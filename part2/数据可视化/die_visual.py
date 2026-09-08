from die import Die
import plotly.express as px 

die=Die()
results=[]
for roll_number in range(1000):
    result=die.roll()
    results.append(result)

    frequencies=[]
    poss_result=range(1,die.sides+1)
    for value in poss_result:
        frequence=results.count(value)
        frequencies.append(frequence)

title="results of rolling"
labels={'x':'result','y':'frequence'}
fig = px.bar(x=poss_result,y=frequencies,title=title,labels=labels) 
fig.show()       

print(frequencies)