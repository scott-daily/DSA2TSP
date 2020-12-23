import math

def timeToMinutes(time):
    hours = int(time.split(':')[0])
    minutes = int(time.split(':')[1].split()[0])
    meridiem = time.split(':')[1].split()[1]

    if meridiem == 'PM':
        hours += 12

    return (hours*60) + minutes

def minutesToTime(minutes):
    if minutes > 60:
        hours = math.floor(minutes / 60)
        minutes = minutes % 60
        merediem = " AM"

        if hours < 10:
            if minutes < 10:
                return "0" + str(hours) + ":0" + str(minutes) + merediem
            else:
                return "0" + str(hours) + ":" + str(minutes) + merediem
        elif hours >= 10 and hours < 12:
            if minutes < 10:
                return str(hours) + ":0" + str(minutes) + merediem
            else:
                return str(hours) + ":" + str(minutes) + merediem
        elif hours >= 12:
            merediem = " PM"
            if hours == 12:
                if minutes < 10:
                    return str(hours) + ":0" + str(minutes) + merediem
                else:
                    return str(hours) + ":" + str(minutes) + merediem
            elif hours > 12:
                hours -= 12
                if hours < 10:
                    if minutes < 10:
                        return "0" + str(hours) + ":0" + str(minutes) + merediem
                    else:
                        return "0" + str(hours) + ":" + str(minutes) + merediem
                else:
                    if minutes < 10:
                        return str(hours) + ":0" + str(minutes) + merediem
                    else:
                        return str(hours) + ":" + str(minutes) + merediem
    else:
        if minutes < 10:
            return "00:0" + str(minutes) + " AM"
        else:
            return "00:" + str(minutes) + " AM"