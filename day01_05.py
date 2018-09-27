# 电话号码联想功能
search = '168'

num_a = '1286-168-0006'
num_b = '1681-222-0006'

position_a =  num_a.find(search)
position_b =  num_b.find(search)

print(search + ' is at ' + str(position_a+1) + ' to ' + str(position_a+len(search))+' of num_a')
print(search + ' is at ' + str(position_b+1) + ' to ' + str(position_b+len(search))+' of num_b')
