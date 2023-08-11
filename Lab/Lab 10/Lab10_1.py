from random import *


def main():
    length = 12
    sales = [0] * length
    min_sales_quarter_no = min_average_sales_quarter_no = 10000 #some very big value than sales and sum of sales
    max_sales_quarter_no = max_average_sales_quarter_no = -1
    min_sales_quarter = min_average_sales_quarter = 10000
    max_sales_quarter = max_average_sales_quarter = -1
    print(end='Monthly Sales: ')
    for i in range(length):
        sales[i] = randint(10, 99)
        print(sales[i], end=' ')
    print()
    sum = 0
    for i in range(0, 12):
        if i % 3 == 0:
            print(f'Quarter {i // 3 + 1}: ',end='')
            max = min = sales[i]
        print(sales[i], end=' ')
        sum += sales[i]
        if max < sales[i]:  max = sales[i];
        if min > sales[i]:  min = sales[i];
        if (i + 1) % 3 == 0:        #to check end of quarter after every 3 months
            average = sum / 3
            print (f'\tMin: {min}\tMax: {max}\tAverage: {average:.2f}')
            if min_sales_quarter > min:     min_sales_quarter = min;    min_sales_quarter_no = i // 3 + 1;
            if max_sales_quarter < max:     max_sales_quarter = max;    max_sales_quarter_no = i // 3 + 1;
            if min_average_sales_quarter > average:     min_average_sales_quarter = average;    min_average_sales_quarter_no = i // 3 + 1;
            if max_average_sales_quarter < average:     max_average_sales_quarter = average;    max_average_sales_quarter_no = i // 3 + 1;
            sum = 0
    print (f'Quarter {min_sales_quarter_no} has minimum sale {min_sales_quarter}')
    print (f'Quarter {max_sales_quarter_no} has maximum sale {max_sales_quarter}')
    print (f'Quarter {min_average_sales_quarter_no} has minimum average sale {min_average_sales_quarter:.2f}')
    print (f'Quarter {max_average_sales_quarter_no} has maximum average sale {max_average_sales_quarter:.2f}')

main()