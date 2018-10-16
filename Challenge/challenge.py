import time
import challenge_slow
import challenge_second
import challenge_thirth
import challenge_4
import challenge_5
import challenge_constraint



def speedtest(function):
    start_time = time.time()
    function()
    print("{:25s}".format(function.__module__), (time.time() - start_time) * 1000, "ms")

speedtest(challenge_slow.test)
speedtest(challenge_second.test)
speedtest(challenge_thirth.test)
speedtest(challenge_4.test)
speedtest(challenge_5.test)
speedtest(challenge_constraint.test)
