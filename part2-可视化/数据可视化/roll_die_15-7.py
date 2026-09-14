from die import Die
import plotly.express as px
from pathlib import Path

die_1=Die()
die_2=Die()
die_3=Die()
results=[]
for roll_num in range(1000):
    result=die_1.roll()+die_2.roll()+die_3.roll()
    results.append(result)

frequencies=[]
poss_result=range(1,die_1.sides+die_2.sides+die_3.sides+1)
for value in poss_result:
    frequence=results.count(value)
    frequencies.append(frequence)

title="Result of three D6"
labels={'x':'poss_result','y':'frequence'}
fig=px.bar(x=poss_result,y=frequencies,title=title,labels=labels)
fig.update_layout(xaxis_dtick=1)

output_path = Path(__file__).with_name(f"{title}.html")
fig.write_html(output_path)
print(f"The file is saved in {output_path}")
