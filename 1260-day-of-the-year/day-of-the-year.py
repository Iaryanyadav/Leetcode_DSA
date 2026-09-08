import datetime

class Solution:
    def dayOfYear(self, date: str) -> int:
        if len(date) != 10:
            return -1
        return int(datetime.datetime.strptime(date, "%Y-%m-%d").strftime("%j"))