import time

#print(time.ctime(0))    # convert a time expressed in seconds since epoch to a readable string
#                          epoch = when your computer
#print(time.time())
#print(time.ctime(time.time()))

#time_object = time.localtime()
#time_object = time.gmtime()
#local_time = time.strftime("%b %d %Y %H:%M:%S", time_object)
#print(local_time)

#time_string = "16 August, 2022"
#time_object = time.strptime(time_string, "%d %B, %Y")
#print(time_object)

# time.asctime(time_tuple) = accepts a time_object or a tuple up to 9 elements and return seconds since epoch
# (year, month, day, hours, minutes, secs, day of the week, day of the year, dst)
time_tuple = (2022, 8, 16, 16, 30, 0, 0, 0, 0)
time_string = time.asctime(time_tuple)
print(time_string)

# (year, month, day, hours, minutes, secs, day of the week, day of the year, dst)
time_tuple = (2022, 8, 16, 16, 30, 0, 0, 0, 0)
time_string = time.mktime(time_tuple)
print(time_string)

