myDic_1 = {
    "name": 'mohamed',
    "seond_name":'mohamed',
    "third_name": "Ashraf",

}

myDic_2 = []
result = dict()

for key, val in myDic_1.items():
    
    if val not in myDic_2:
        myDic_2.append(val)
        result[key] = val

print(result)