from die import Die
import plotly.express as px
from pathlib import Path

die_1=Die()
die_2=Die()
results=[]
for roll_num in range(1000):
    result=die_1.roll()*die_2.roll()
    results.append(result)

frequencies=[]
poss_results=[]
for x1 in range(1,die_1.sides+1):
    for x2 in range(1,die_2.sides+1):
        x=x1*x2
        poss_results.append(x)
for value in poss_results:
    frequence=results.count(value)
    frequencies.append(frequence)

fig=px.bar(x=poss_results,y=frequencies)
#fig.update_layout(xaxis_dtick=1)
output_path = Path (__file__).with_name('15-8.html')
fig.write_html(output_path)
print(f"The file is saved in {output_path}")