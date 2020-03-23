import numpy as np
import time
import random

time_array=[]
for j in range(100):
    test =np.array([0, 0, 0, 4, 4, 4, 4, 4, 2, 2, 2, 2, 2,2, \
                2, 2, 2, 2, 4, 4, 4, 1,1, 1, 1, 1, 1,1, 1, 4, \
                 0, 0,0, 2, 2, 0, 4, 1, 1, 1, 2, 2, 0, 0])

    # method 1
    find_index = np.where(test==4)
    # print(test)
    start_time = time.time()
    for i in find_index[0]:
        # print(i,test[i-1],test[i],test[i+1])
        if test[i+1]==0 and test[i-1]==1:
            test[i]=2
    delta = time.time()-start_time
    time_array.append(delta)  #100次 平均时间： 6.63304328918457e-05 最长用时: 0.006543159484863281 最短用时： 0.0

    # # mehod 2
    # target = np.array([1,4,0])
    # # print(test)
    # find_index = np.where(test==4)[0]
    # start_time=time.time()
    # for i in find_index:
    #     random_array = test[i-1:i+2]
    #     # print(i,target,random_array)
    #     if (random_array==target).all():
    #         test[i]=2        
    #         break
    # delta = time.time()-start_time
    time_array.append(delta)  #100次 平均时间： 9.998559951782227e-05 最长用时: 0.009903669357299805 最短用时： 0.0

print("平均时间：",np.average(time_array),'最长用时:',np.max(time_array),"最短用时：",np.min(time_array))
    




