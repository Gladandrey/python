#1 min = 60
#1 hour = 60 * 60 = 3600
#1 day = 60 * 60 * 24 = 86400

x=input('Введите интервал времени в секундах: ')

t=int(x)

day= t//86400
hour= (t-(day*86400))//3600
minutes= (t - ((day*86400) + (hour*3600)))//60
seconds= t - ((day*86400) + (hour*3600) + (minutes*60))
print( day, 'дней' , hour,'часов', minutes, 'минут',seconds,'секунд')

