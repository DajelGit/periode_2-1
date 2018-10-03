import time


class StopWatch():
    def __init__(_):
        _.__start_time = 0
        _.__stop_time = 0
        _.start()

    def start(_):
        _.__start_time = time.time()

    def stop(_):
        _.__stop_time = time.time()

    def get_elapsed_time(_):
        return _.__stop_time - _.__start_time

    def getStartTime(_):
        return _.__start_time

    def getStopTime(_):
        return _.__stop_time


size = 1000000
stopWatch = StopWatch()
sum = 0
for i in range(1, size + 1):
    sum += i

stopWatch.stop()
print("The loop time is", stopWatch.get_elapsed_time(), "milliseconds")
