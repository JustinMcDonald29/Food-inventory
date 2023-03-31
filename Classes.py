import datetime as dt

class food:
    def __init__(self,name,count,date_bought,lifespan):
        self.name = name
        self.count = count
        self.date_bought = date_bought
        self.lifespan = lifespan
        self.use_by = date_bought + dt.timedelta(days=lifespan)
        self.days_left = self.use_by - dt.date.today()
        if self.days_left <= 1:
            self.warn_flag = True
        else:
            self.warn_flag = False



