from random import *

def main():
    i = 1
    fail_count = 0
    sum_mid = sum_final = sum_sessional = sum_total = 0
    print('Roll No	Mid	Final	Sessional	Total	Grade')
    while i <= 30:
        mid = randint(0, 35)
        final = randint(0, 40)
        sessional = randint(0, 25)
        total = mid + final + sessional
        sum_total = sum_total + total
        sum_mid = sum_mid + mid
        sum_final = sum_final + final
        sum_sessional = sum_sessional + sessional
        if i == 1:
            max = min = total
            max_mid = min_mid = mid
            max_final = min_final = final
            max_sessional = min_sessional = sessional
        else:
            if max < total: max = total;
            elif min > total: min = total;
            if max_mid < mid:   max_mid = mid;
            elif min_mid > mid: min_mid = mid;
            if max_final < mid:   max_final = final;
            elif min_final > mid: min_final = final;
            if max_sessional < sessional:   max_sessional = sessional;
            elif min_sessional > sessional: min_sessional = sessional;
        print(f' {i}\t\t{mid}   {final}        {sessional}        {total}       ', end='')
        if total < 50:
            print ('F')
            fail_count = fail_count + 1
        elif total < 55:
            print ('D')
        elif total < 58:
            print ('C-')
        elif total < 61:
            print ('C')
        elif total < 65:
            print ('C+')
        elif total < 70:
            print ('B-')
        elif total < 75:
            print ('B')
        elif total < 80:
            print ('B+')
        elif total < 85:
            print ('A-')
        else:
            print ('A')
        i = i + 1
    print ('Total: ', 30)
    print ('Pass: ', 30 - fail_count)
    print ('Fail: ', fail_count)
    print ('Overall Average Marks: ', sum_total/30)
    print ('Average Midterm Marks: ', sum_mid/30)
    print ('Average Sessional Marks: ', sum_sessional/30)
    print ('Average Final term Marks: ', sum_final/30)
    print ('Maximum Marks: ', max)
    print ('Maximum Midterm Marks: ', max_mid)
    print ('Maximum Sessional Marks: ', max_sessional)
    print ('Maximum Final term Marks: ', max_final)
    print ('Minimum Marks: ', min)
    print ('Minimum Midterm Marks: ', min_mid)
    print ('Minimum Sessional Marks: ', min_sessional)
    print ('Minimum Final term Marks: ', min_final)

main()