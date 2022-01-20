from mmap import mmap
import re
import datetime

f=open("abc.txt", "r")
content = f.read()
dates = []

matches = re.findall(r'(\d{2,4}/\d{2}/\d{2,4})', content)
tuple = re.findall(r'(\d{2,2}[\\/\s](Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dec)[\\/\s]\d{4,4})', content);

for x in matches:
    date = None;
    for fmt in ('%Y/%m/%d', '%m/%d/%Y', '%d/%m/%Y'):
        try:
            date = datetime.datetime.strptime(x, fmt)
        except ValueError:
            pass
    if date is not None:
        dates.append(date)

for y in tuple:
    try:
        date = datetime.datetime.strptime(y[0], '%d %b %Y')
        dates.append(date)
    except ValueError:
        pass
    
print(len(dates))
