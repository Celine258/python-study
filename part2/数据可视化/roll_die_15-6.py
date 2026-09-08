from die import Die

die_1=Die(8)
die_2=Die(8)
results=[]
for roll_num in range(1000):
    result=die_1.roll()+die_2.roll()
    results.append(result)

frequencies=[]
poss_result=range(1,die_1.sides+die_2.sides+1)
for value in poss_result:
    frequence=results.count(value)
    frequencies.append(frequence)

print(frequencies)