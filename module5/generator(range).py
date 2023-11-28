def my_range(start, stop, step =1):
    if stop<=start:
        raise RuntimeError("Start must be smaller then stop")
    i = start
    while i<stop:
        yield i
        i+=step

try:
    for k in my_range(11,20,2):
        print(k)
except RuntimeError as ex:
    print(ex)
except:
    print("Unknown error occured")