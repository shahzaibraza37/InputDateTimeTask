from datetime import datetime


date = dict()
time = dict()


def run():
    try:
        nOfDataEntry = int(input('How much data do you want to enter?'))

        for dateTimeIdx in range(nOfDataEntry):
            # input Date
            inputDate = input('Please enter a date:')
            try: 
                datetime.strptime(inputDate, '%d.%m.%Y')
                date[dateTimeIdx] = inputDate
            except ValueError as e:
                print('ERROR' + str(e))
                # restart the function
                return run()
            
            # input Time
            inputTime = input('Please enter a time:')
            try: 
                datetime.strptime(inputTime, '%H:%M')
                time[dateTimeIdx] = inputTime
            except ValueError as e:
                print('ERROR' + str(e))
                # restart the function
                return run()


        checkIdx = 0
        while 1:
            dateTimeObj = datetime.now()
            dateStamp = dateTimeObj.strftime('%d.%m.%Y')
            timeStamp = dateTimeObj.strftime('%H:%M')
            idx = 1
            if dateStamp == date[checkIdx] and timeStamp == time[checkIdx]:
                print('The time has been reached to perform the task', str(idx), '(' + date[checkIdx] +' - '+ time[checkIdx] +')')
                idx += 1
                checkIdx += 1
            if checkIdx == len(time):
                result = 'Thank you very much. I will notify them!'
                print(result)
                return result
    except:
        print('Oops! Write an integer here. Try again......!')
        # restart the function
        return run()

run()
