nums=[11,2,3,44,200]

max = nums[0]

for nu in nums:
    if nu < max:
        max = nu
print(max)

mi=[2,3,4,5,5,6]
uniques=[]

for m in mi:
    if m not in uniques:
        uniques.append(m)
print(uniques)


phone=input('Phone:')
ut=""
dic={
    '1':'one',
    '2':'two',
    '3':'three',
    '4':'four'
}

for u in phone:
 ut=ut+dic.get(u,'?')
print(ut)





