
def add_time(stime, addtime, *args):

    dayofweek = []
    noon = 'AM'
    if len(args) != 0:
        dayofweek = args[0].lower() #小文字変換
        week = {'monday':0, 'tuesday':1, 'wednesdagy':2, 'thursday':3, 'friday':4, \
            'saturday':5,'sunday':6}
        no_week = ([(n, d) for d,n in week.items()])
        dayofweek_num  = week[dayofweek]
    
    st = stime.split()
    start = st[0].split(':')
    ad = addtime.split(':')

    st_min = conv_min(start[0], start[1])
    if st[1] == 'PM':
        st_min += (12*60)
    
    ad_min = conv_min(ad[0], ad[1])
    total_min = st_min + ad_min
    result_min = total_min % 60
    result_hor = ((total_min - result_min) / 60) % 24
    result_day = int((((total_min - result_min) / 60) - result_hor) /24)

    if result_hor > 13:
        noon = 'PM'
        result_hor -= 12
    elif result_hor == 12:
        noon = 'PM'
    elif result_hor == 0:
        result_hor = 12
        noon = 'AM'

    result= '# Returns: {h:g}:{m:02g} {noon}'.format(h=result_hor, m=result_min, noon=noon)

    if dayofweek != []:
        dayofweek_num = (dayofweek_num + result_day) % 7
        result = result + ', '+ no_week[dayofweek_num][1].capitalize() #　先頭大文字

    if result_day == 1:
        result += ' (next day)'
    elif result_day > 1:
        result += ' ({r_day:g} days later)'.format(r_day=result_day)

    return result

def conv_min(h, m):
    hor = int(h)*60
    min = int(m)
    return hor+min

