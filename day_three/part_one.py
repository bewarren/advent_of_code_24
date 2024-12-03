
with open('input.txt', 'r') as file:
    ans = 0
    for line in file:
        first_val = ""
        second_val = ""
        start_count = 0
        for v in line:
            
            if v == "m" and start_count == 0:
                
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
            
            else:
                start_count = 0
                first_val = ""
                second_val = ""

    print(ans)
