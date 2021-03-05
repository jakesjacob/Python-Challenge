"""
Please write your name here: Jacob Horgan
"""

import csv




def process_shifts(path_to_csv):
    #print('hello')

    """

    :param path_to_csv: The path to the work_shift.csv
    :type string:
    :return: A dictionary with time as key (string) with format %H:%M
        (e.g. "18:00") and cost as value (Number)
    For example, it should be something like :
    {
        "17:00": 50,
        "22:00: 40,
    }
    In other words, for the hour beginning at 17:00, labour cost was
    50 pounds
    :rtype dict:
    """

    shifts = dict()
    rates = [0] * 25


    with open (path_to_csv, mode='r') as infile:
        reader = csv.reader(infile)
        reader.__next__()  #skips the header part

        

        for row in reader:
            start_shift = row[3]
            start_hour = int(start_shift[:2])
            start_minute = int(start_shift[3:])
            end_shift = row[1]
            end_hour = int(end_shift[:2])
            end_minute = int(end_shift[3:])

            #start_int = start_hour + start_minute
            #end_int = end_hour + end_minute

            time_worked_hour = end_hour - start_hour
            time_worked_minutes = end_minute - start_minute

            pay_rate = float(row[2])
            
            #print('start {}      end {}     time worked {}:{}'.format(start_hour, end_hour, time_worked_hour, time_worked_minutes))
            

            for hour in range(0, 25):

                string_hour = str(hour) + ":00" if hour > 9 else '0' + str(hour) + ':00'

                if hour >= start_hour and hour < end_hour:
                   rates[hour]  = rates[hour] + pay_rate
                

                shifts.update({string_hour : rates[hour]})
        print("LABOUR COST PER HOUR")
        print(shifts)
        print("")


    return shifts


def process_sales(path_to_csv):
    """

    :param path_to_csv: The path to the transactions.csv
    :type string:
    :return: A dictionary with time (string) with format %H:%M as key and
    sales as value (string),
    and corresponding value with format %H:%M (e.g. "18:00"),
    and type float)
    For example, it should be something like :
    {
        "17:00": 250,
        "22:00": 0,
    },
    This means, for the hour beginning at 17:00, the sales were 250 dollars
    and for the hour beginning at 22:00, the sales were 0.

    :rtype dict:
    """

    sales = dict()
    values = [0] * 25


    with open (path_to_csv, mode='r') as infile:
        reader = csv.reader(infile)
        reader.__next__()  #skips the header part

        for row in reader:
            time = row[1]
            hour_int = int(time[:2])
            value = float(row[0])
 
            #print('hour {}      value {}'.format(hour_int, value))

            for hour in range(0, 25):

                string_hour2 = str(hour) + ":00" if hour > 9 else '0' + str(hour) + ':00'

                if hour == hour_int:
                   values[hour]  = values[hour] + value
                

                sales.update({string_hour2 : values[hour]})
        print("SALES FOR EVERY HOUR")
        print(sales)
        print("")


    return sales


def compute_percentage(shifts, sales):
    """

    :param shifts:
    :type shifts: dict
    :param sales:
    :type sales: dict
    :return: A dictionary with time as key (string) with format %H:%M and
    percentage of labour cost per sales as value (float),
    If the sales are null, then return -cost instead of percentage
    For example, it should be something like :
    {
        "17:00": 20,
        "22:00": -40,
    }
    :rtype: dict
    """

    #percentages = dict((k, float((shifts[k]) / sales[k])*100) for k in sales if sales[k] > 0

    percentages = dict()

    for k in sales:
        if sales[k] > 0:
            percent = float((shifts[k] / sales[k])*100)
            percentages.update({k : percent})
        elif sales[k] == 0:
            percent2 = float(sales[k] - shifts[k])
            percentages.update({k : percent2})


    print("PERCENTAGE OF LABOUR COST PER HOUR")
    print(percentages)
    print("")

    return percentages


def best_and_worst_hour(percentages):
    """

    Args:
    percentages: output of compute_percentage
    Return: list of strings, the first element should be the best hour,
    the second (and last) element should be the worst hour. Hour are
    represented by string with format %H:%M
    e.g. ["18:00", "20:00"]

    """


    ordered = dict(sorted(percentages.items(), key=lambda item: item[1]))
    print("ORDERED HOURS FROM WORST TO BEST")
    print(ordered)
    print("")

    best_and_worst = ["",""]


    key_list=list(ordered.keys())
    val_list=list(ordered.values())

    
    m = min(i for i in val_list if i > 0)
    index = val_list.index(m)

    
    best_and_worst[0] = key_list[index]
    best_and_worst[1] = key_list[0]
    

    print("BEST HOUR AND WORST HOUR")
    print(best_and_worst)
    print("")

    return best_and_worst


def main(path_to_shifts, path_to_sales):
    """
    Do not touch this function, but you can look at it, to have an idea of
    how your data should interact with each other
    """

    shifts_processed = process_shifts(path_to_shifts)
    sales_processed = process_sales(path_to_sales)
    percentages = compute_percentage(shifts_processed, sales_processed)
    best_hour, worst_hour = best_and_worst_hour(percentages)
    return best_hour, worst_hour

if __name__ == '__main__':
    # You can change this to test your code, it will not be used
    path_to_sales = "transactions.csv"
    path_to_shifts = "work_shifts.csv"
    best_hour, worst_hour = main(path_to_shifts, path_to_sales)


# Please write you name here: Jacob Horgan
