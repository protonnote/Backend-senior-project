# emp = []
# label_name = ["prayut","note","tonnam","copter","prayat","tat","mook"]
# label_pre = [0.95,0.87,0.81,0.92,0.80,0.88,0.85]

# [ emp.append([label_name[i],label_pre[i]]) for i in range(len(label_name))]

 
# # print(emp)
# emp_sort = sorted(emp,key=lambda l:l[1],reverse=True)

# # for i in emp_sort:
# #     if i[1]*100 >= 80 :

# print(emp_sort)

import write_log as wr

dd = {"Name": ["jobs","note","prayut"],"Percent": [5.84,22.46,71.7],"Time": "25/07/2022 18:40:37"}


# print(wr.save_log(dd))
print(wr.read_log(123456))
