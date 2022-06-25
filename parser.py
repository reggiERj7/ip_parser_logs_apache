from file_read_backwards import FileReadBackwards
import re
from collections import Counter
import csv


class Parse:
    buff = []
    counter = 0
    def SelectIP(self):
        with FileReadBackwards('logs\data.txt') as f:
            for i in f:
                if 'GET / HTTP/1.1' in i:
                    try:
                        ip = re.match(r'\d+\.\d+\.\d+\.\d+', i).group(0)
                        self.buff.append(ip)
                        self.counter += 1
                        print(f"Строка №{self.counter}")
                    except:
                        self.counter += 1
                        print(f"Строка №{self.counter}")
                        continue
                else:
                    self.counter += 1
                    print(f"Строка №{self.counter}")
                    continue

    def CreateCSV(self):
        result = Counter(self.buff)
        with open('results\\result.csv', 'a', newline='') as k:
            fields = ['ip', 'repeats']
            writer = csv.DictWriter(k, fields)
            for key, value in result.items():
                writer.writerow({'ip': key, 'repeats': value})
