import time

# Start the timer
start_time = time.time()

with open('input.txt', 'r') as file:
    ans = 0
    first_val = ""
    second_val = ""
    start_count = 0

    do_count = 0

    do = True

    for line in file:
        

        for v in line:
            
            if v == "m" and start_count == 0 and do:
                
                start_count = 1
            
            elif v == "u" and start_count == 1:
                
                start_count = 2
            
            elif v == "l" and start_count == 2:
                
                start_count = 3

            elif v == "(" and start_count == 3:
                
                start_count = 4
            
            elif start_count == 4 and v.isdigit():
                
                first_val += v
                
            elif start_count == 4 and v == ",":
                start_count = 5

            elif start_count == 5 and v.isdigit():
                second_val += v
            
            elif start_count == 5 and v == ")":
                
                ans += int(first_val)  * int (second_val)

                start_count = 0
                first_val = ""
                second_val = ""

            elif v == "d":
                start_count = 0
                first_val = ""
                second_val = ""

                do_count = 1
            
            elif v == 'o' and do_count == 1:
                do_count = 2
            
            elif v == "(" and do_count == 2:
                do_count = 3
            elif v == ")" and do_count == 3:
                do_count = 0
                do = True

            elif v == "n" and do_count == 2:
                do_count = 3
            elif v == "\'" and do_count == 3:
                
                do_count = 4
            elif v == "t" and do_count == 4:
                do_count = 5
            elif v == "(" and do_count == 5:
                do_count = 6
            elif v == ")" and do_count == 6:
                do_count = 0
                do = False


            
            else:
                do_count = 0
                start_count = 0
                first_val = ""
                second_val = ""

    print(ans)

end_time = time.time()
runtime = (end_time - start_time) * 1_000_000
print(f"Runtime: {runtime:.2f} microseconds")