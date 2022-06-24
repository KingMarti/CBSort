import os
from datetime import date
from pathlib import Path
import shutil
dir='Enter File Path To Videos'
year=2016
current_year= date.today().year
def sort():
    print('getting data for ', year)
    for v in os.listdir(dir):
        if os.path.isfile(dir+'\\'+v) == True:
            Path(dir+'\\'+str(year)).mkdir(parents=True, exist_ok=True)
            if str(year) in v:
                print('Moving file: ',v)
                shutil.move(dir+'\\'+v, dir+'\\'+str(year)+'\\'+v)
            
if __name__ == '__main__':
    while year <= current_year:
        sort()
        year+=1

