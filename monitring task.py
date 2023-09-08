import datetime
import time

import psutil

sec = 5
threshold = 80

while True:
    cpu_usage = psutil.cpu_percent(1)
    num_of_cpu = psutil.cpu_count(True)
    used_memory = psutil.virtual_memory()[2]
    used_disk = psutil.disk_usage('/')[3]
    dict = psutil.net_if_addrs().values()
    for i in dict:
        host_ip = i[0].address
    current_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    file_name= datetime.datetime.now().strftime("%Y-%m-%d")+'-pip.log'
    file = open(file_name, 'a')
    file.write(f"{current_time}, {cpu_usage}, {num_of_cpu}, {used_memory}, {used_disk}, {host_ip}\n")
    file.close()
    if used_memory > threshold:
        file_name = datetime.datetime.now().strftime("%Y-%m-%d")+'-notification.log'
        notfication = open(file_name, 'a')
        notfication.write("The system is running out of memory.\n")
        notfication.close()
    time.sleep(sec)
