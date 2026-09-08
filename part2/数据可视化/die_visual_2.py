from die import Die
import plotly.express as px 
from pathlib import Path

die_1=Die()
die_2=Die(10)
results=[]
for roll_number in range(1000):
    result1=die_1.roll()
    result2=die_2.roll()
    results.append(result2+result1)

    frequencies=[]
    poss_result=range(2,die_1.sides+die_2.sides+1)
    for value in poss_result:
        frequence=results.count(value)
        frequencies.append(frequence)

#定制1
title="results of rolling two D6 "
labels={'x':'result','y':'frequence'}
fig = px.bar(x=poss_result,y=frequencies,title=title,labels=labels) 
#定制2
fig.update_layout(xaxis_dtick=1)

#fig.show()
output_path = Path(__file__).with_name('roll_die_2.html')       
fig.write_html(output_path)
print(f"The file is saved in {output_path}")