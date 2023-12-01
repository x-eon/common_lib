import matplotlib.pyplot as plt
from datetime import datetime
import time
from threading import Timer, Thread, Event

class Common:

    def ViewCounter(self, period, idx):
        per = period * 1.0
        if (idx / per) - int(idx / per) == 0:
            return True
        return False

    def cicle_index(self, idx, maxidx):
        res = idx
        if idx >= maxidx:
            mn = int(idx / maxidx)
            res = int(idx - mn * maxidx)
        return res

class Time:
    def timeNew(self):
        return datetime.now().strftime("%d-%m-%Y %H:%M:%S")
    
    def StepHour(self, secs):
        return round(60 / (secs / 60), 2)

    # 1 step seconds.
    def sec_one_step(self, tmin, epochs):
        res = (tmin * 60) / epochs
        return res

    def start_time(self):
        return time.time()

    def timeNew(self):
        return datetime.now().strftime("%d-%m-%Y %H:%M:%S")

    def timeToStr(self, _datetime):
        return _datetime.strftime("%d-%m-%Y %H:%M:%S")

    def timeToStrMQL(self, _datetime):
        return _datetime.strftime('%Y.%m.%d %H:%M:%S')

    def strToTime(self, _strtime):
        return datetime.strptime(_strtime, "%Y.%m.%d %H:%M")

    def spent_time(self, name, start_tm):
        end_time = time.time()
        run_time = (end_time - start_tm) / 60
        spen_tm = round(run_time, 2)
        print(name + ' TM:', spen_tm, 'min.')
        return spen_tm

    def calc_time(self, start_tm, _epochs):
        tmin = self.spent_time('learning', start_tm)
        secstep = round(self.sec_one_step(tmin, _epochs),4)
        h1 = self.StepHour(secstep)
        return secstep, h1

    def difference_time(self, read_time, cur_time):
        r_time = read_time.timestamp()
        c_time = cur_time.timestamp()
        return c_time - r_time


class Convert:

    def freq_to_ms(self, data_freq):
        """ converting frequency to milliseconds """
        frequency = float(data_freq)  
        milliseconds = 1 / frequency * 10**6  
        return milliseconds    
    
    def datetime_to_unix(time_str, time_pattern):
        """Convert time to Unix time.
           template example: '%Y-%m-%dT%H:%M:%S.%fZ'"""
        try:
            time_obj = datetime.strptime(time_str, time_pattern)
            unix_time = int(time_obj.timestamp() * 1000)
        except Exception as ex:
            print('Error convert:',ex)
            unix_time = 0
        return unix_time
    
    
class Chart:
    
    def chart(self, data, params):
        """simple graph display"""
        plt.plot(data) 
        plt.title(params.title)
        plt.xlabel(params.xlabel) 
        plt.ylabel(params.ylabel) 
        plt.show()

    def histogram(self, data, params):
        """simple histogram display"""
        plt.hist(data, bins=10, edgecolor='black')
        plt.title(params.title)
        plt.xlabel(params.xlabel) 
        plt.ylabel(params.ylabel) 
        plt.show()
        
class X_Timer():
    def __init__(self, _interval, _onTimer):
        self.tmr = None
        self.interval = _interval
        self.x_onTimer = _onTimer

    def tm_start(self):
        self.tmr = Timer(self.interval, self.tm_start)
        self.tmr.start()
        self.x_onTimer(self.tmr)

    def tm_stop(self):
        self.tmr.cancel()

    def one_start(self):
        self.tmr = Timer(self.interval, self.x_onTimer)
        self.tmr.start()
        
class XTimer: 
    
    def __init__(self):
        self.evnt = Event()
        self.tm = X_Timer()

    def timer_start(self, interval, timer_Callbak):
        xwait = XTimer(interval, timer_Callbak)
        xwait.tm_start()
        return xwait
    
    def timer_break(self, xwait):
        xwait.tm_stop()
        self.evnt.set()
        
    def timer_stop(self, timer):
        timer.cancel()
        self.evnt.set()
        
    def timer_start_example(self, interval, timer_Callbak):
        xwait = None
        try:
            xwait = self.tm.timer_start(interval, timer_Callbak)
        except Exception as ins:
            print('Error waiting: ', ins)
            self.tm.timer_break(xwait)
        except KeyboardInterrupt:
            print("breack waiting")
            self.tm.timer_break(xwait)        