class Solution(object):
    def reformatDate(self, date):
        """
        :type date: str
        :rtype: str
        """
        day_string, month_string, year = date.split(" ")
        months = {"Jan":"01", "Feb":"02", "Mar":"03", "Apr":"04",
                  "May":"05", "Jun":"06", "Jul":"07", "Aug":"08",
                  "Sep":"09", "Oct":"10", "Nov":"11", "Dec":"12"}
        day = day_string[:-2]
        if len(day) == 1:
            day = "0" + day
        result = year + "-" + months[month_string] + "-" + day
        return result
