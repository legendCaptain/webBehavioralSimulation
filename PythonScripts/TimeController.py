'''
@Project ：webBehavioralSimulation 
@File    ：TimeController.py
@IDE     ：PyCharm 
@Author  ：kant
@Date    ：2024/1/16 11:58 
@content :时间控制
'''
from datetime import datetime
if __name__ == '__main__':
    #v_month_aft = datetime.strptime('20230101', '%Y%m%d%H:%M:%S')
    count = 1
    print(datetime.strftime(datetime.now(),'%Y%m%d%H%M%S'))
    while(str(datetime.strftime(datetime.now(),'%Y%m%d%H%M%S'))!='20240116144605'):
        count = count +1
    print(count)
    print(datetime.strftime(datetime.now(), '%Y%m%d%H%M%S'))