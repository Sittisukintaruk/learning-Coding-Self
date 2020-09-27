from datetime import date,datetime

#Set date
def Set_datetime():
    d = datetime.date(2016,11,24)
    print(d)
#Set date to day
def Set_dateToday():
    td = datetime.date.today()
    dt_today = datetime.datetime.today()
    dt_now = datetime.datetime.now()
    dt_utcnow = datetime.datetime.utcnow()
    print(dt_today)
    print(dt_now)
    print(dt_utcnow)
    print(td.weekday())
    print(td.isoweekday())

# SET Time 
def Set_time()  :
    t = datetime.time(9, 30 ,45,10000)
    tdd = datetime.datetime(2020,12,7,12,30,45,100000)
    tddd = datetime.timedelta(hours=12)
    print(tdd + tddd)
    print(t.hour)
    #date2 = date1 + timedelta
    #timedelta = date1 + date2
    #bday = datetime.date(2016,9,24)
    #till_bday = bday - td
    #print(till_bday.total_seconds())
# SET Time zone
def Parse_date_str():
    date_Parse = datetime.strptime("20160413","%Y%m%d")
    date_Parse2 = datetime.strptime("20160413","%Y%m%d").date()
    date_Parse3 = datetime.strptime("05/11/2020","%d/%m/%Y").date()
    date_Parse4 = datetime.strptime("05/11/2020T06:45","%d/%m/%YT%H:%M")

    print(date_Parse)
    print(date_Parse2)
    print(date_Parse3)
    print(date_Parse4)


def Today():
    date = datetime.today()
    print("วันที่ ", date.day," เดือน ",date.month , "ปี" , date.year)


Today()
