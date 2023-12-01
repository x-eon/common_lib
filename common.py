import matplotlib.pyplot as plt
from datetime import datetime

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