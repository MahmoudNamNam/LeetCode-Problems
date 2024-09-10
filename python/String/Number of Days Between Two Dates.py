import datetime 
class Solution:
    def daysBetweenDates(self, date1: str, date2: str) -> int:
        date1 = date1.split("-")
        date2 = date2.split("-")

        date1 = datetime.date(int(date1[0]),int(date1[1]),int(date1[2]))
        date2 = datetime.date(int(date2[0]), int(date2[1]), int(date2[2]))


        return abs((date1 - date2).days)



from datetime import datetime

class Solution:
    def daysBetweenDates(self, date1: str, date2: str) -> int:
        date_format = "%Y-%m-%d"  
        d1 = datetime.strptime(date1, date_format)  
        d2 = datetime.strptime(date2, date_format)  
        delta = abs((d2 - d1).days)  
        return delta