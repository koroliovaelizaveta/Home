def staff_min_efficiency (staff):
    minimum = 150
    for worker in staff:
        if staff[worker]['ефективність'] < minimum:
            minimum = staff[worker]['ефективність']
    return minimum

def staff_max_efficiency (staff):
    maximum = 0
    for worker in staff:
        if staff[worker]['ефективність'] > maximum:
            maximum = staff[worker]['ефективність']
    return maximum


staff = {
     'Петрик': {
         'посаду': 'менеджер з продажу',
         'ефективність': 86
     },
     'Ткач': {
         'посаду': 'менеджер з продажу',
         'ефективність': 69
     },
     'Костін': {
         'посаду': 'менеджер з продажу',
         'ефективність': 78
     },
     'Костилєв': {
         'посаду': 'менеджер з продажу',
         'ефективність': 91
     },
     'Борисенко': {
         'посаду': 'менеджер з продажу',
         'ефективність': 99
     }
}
print ('Кращий результат:', staff_max_efficiency(staff))
print ('Найгірший результат:', staff_min_efficiency(staff))