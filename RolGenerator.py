from datetime import date
import datetime
from dateutil.relativedelta import relativedelta
import pandas as pd


def checkIsDigit(input_str):
    if input_str.strip().isdigit():
        return True
    else:
        return False
    
def getWeekDay(dayNumber):
    daysDict = {
        0 : "Lunes ",
        1 : "Martes ",
        2 : "Miercoles ",
        3 : "Jueves ",
        4 : "Viernes ",
        5 : "Sábado ",
        6 : "Domingo ",
    }
    return daysDict[dayNumber]
    
def getEmoji(week):
    emojiDict = {   
        1 : "🐠",
        2 : "🐡",
        3 : "🦈",
        4 : "🎣",
        5 : "🦦",
        6 : "🍥",
    }
    return emojiDict[week]

def getMonth(monthNumber):
    monthDict = {
        1 : ' Enero ',
        2 : ' Febero ',
        3 : ' Marzo ',
        4 : ' Abril ',
        5 : ' Mayo ',
        6 : ' Junio ',
        7 : ' Julio ',
        8 : ' Agosto ',
        9 : ' Septiembre ',
        10 : ' Octubre ',
        11 : ' Noviembre ',
        12 : ' Diciembre ',
    }
    return monthDict[monthNumber]

print(' ')
print('\t██████╗░░█████╗░██╗░░░░░  ░██████╗░█████╗░███╗░░██╗██╗██████╗░░█████╗░')
print('\t██╔══██╗██╔══██╗██║░░░░░  ██╔════╝██╔══██╗████╗░██║██║██╔══██╗██╔══██╗')
print('\t██████╔╝██║░░██║██║░░░░░  ╚█████╗░██║░░██║██╔██╗██║██║██║░░██║██║░░██║')
print('\t██╔══██╗██║░░██║██║░░░░░  ░╚═══██╗██║░░██║██║╚████║██║██║░░██║██║░░██║')
print('\t██║░░██║╚█████╔╝███████╗  ██████╔╝╚█████╔╝██║░╚███║██║██████╔╝╚█████╔╝')
print('\t╚═╝░░╚═╝░╚════╝░╚══════╝  ╚═════╝░░╚════╝░╚═╝░░╚══╝╚═╝╚═════╝░░╚════╝░\n\n')



while(True):
    print('¿Quíeres generar la tabla del mes siguiente o el actual?')
    print('-->      1-Mes Actual       2-Mes Siguiente   <--')

    menuoption = str(input('\nSelect one option: '))
    
    if(checkIsDigit(menuoption)):
        menuoption = int(menuoption)
        if(menuoption == 1 or menuoption == 2):
            break
        else:
            print('> INPUT ERROR: Select a valid number (1,2) <')
            print('\n----------------------------------------- ')
    else:
        print('> INPUT ERROR: Select a valid number (1,2) <')
        print('\n----------------------------------------- ')

todayDate = date.today()
if menuoption == 2:
    todayDate += relativedelta(months=+1)
    
currentMonth = todayDate.month
currentYear = todayDate.year

startDate = datetime.date(int(currentYear),int(currentMonth),1)
week = 1
primerSabado = True
primerViernes = True
print('\n\n\t----- Semana ', week,getEmoji(week),'-----\n')

while (currentMonth == startDate.month):
    temp = pd.Timestamp(startDate)
    
    dia = temp.dayofweek

    if temp.dayofweek == 1:
        print('ENSAYO ' + getWeekDay(temp.dayofweek) + str(startDate.day) + ' de' + getMonth(startDate.month) + '6:00pm | Sonido: \n')
        
    if temp.dayofweek == 2:
        print('NOCHE ADORACION ' +getWeekDay(temp.dayofweek) + str(startDate.day) + ' de' + getMonth(startDate.month) + '6:00pm | Sonido:   Multimedia: \n')
    
    if temp.dayofweek == 4 and primerViernes:
        print('Parejas ' + getWeekDay(temp.dayofweek) + str(startDate.day) + ' de' + getMonth(startDate.month) + '6:30pm | Sonido:  \n')
        primerViernes = False
    
    if temp.dayofweek == 5 and primerSabado:
        print('DESAYUNO MUJERES ' + getWeekDay(temp.dayofweek) + str(startDate.day) + ' de' + getMonth(startDate.month) + '9:30am | Sonido:  \n')
        print('RED JOVENES ' + getWeekDay(temp.dayofweek) + str(startDate.day) + ' de' + getMonth(startDate.month) + '6:00pm | Sonido:  \n')
        primerSabado = False
        
    elif temp.dayofweek == 5 and week == 3:
        print('AYUNO ' + getWeekDay(temp.dayofweek) + str(startDate.day) + ' de' + getMonth(startDate.month) + '8:00am  | Sonido:  \n')
        print('RED JOVENES ' + getWeekDay(temp.dayofweek) + str(startDate.day) + ' de' + getMonth(startDate.month) + '6:00pm | Sonido:  \n')
        
    elif temp.dayofweek == 5:
        print('RED JOVENES ' + getWeekDay(temp.dayofweek) + str(startDate.day) + ' de' + getMonth(startDate.month) + '6:00pm | Sonido:  \n')
        
    if temp.dayofweek == 6:
        print('CULTO FAMILIAR ' + getWeekDay(temp.dayofweek) + str(startDate.day) + ' de' + getMonth(startDate.month))
        print('8:00 am | Sonido:   Multimedia:  ')
        print('10:30 am | Sonido:   Multimedia:  \n')

    if temp.dayofweek == 0:
        week += 1
        print('\t----- Semana ', week ,getEmoji(week),'-----\n')
    
    startDate += relativedelta(days=+1)
    

    




