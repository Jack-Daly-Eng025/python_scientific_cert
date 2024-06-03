#Portfolio project that does put out the correct format but doesn't pass the tests for the Beta Certificate just yet.

def arithmetic_arranger(problems, show_answers=False):
   
    if len(problems) > 5:
        #check if list given is more than 5 in length
        return 'Error: Too many problems.'
    #variables for checks
    first_num = ""
    operator =""
    second_num = ""
    #Variables for output
    top_line =""
    bottom_line =""
    lines = ""
    total = ""
    result =""
    for eq in problems:
        split= eq.split()

        first_num = split[0]
        operator = split[1]
        second_num = split [2]
        sum_num = 0
        #error messages
        if operator!="+" and operator!="-" :
            return "Error: Operator must be '+' or '-'."
        elif len(first_num) > 4 or len(second_num) > 4:
            return "Error: Numbers cannot be more than four digits."
        elif not first_num.isdigit() or not second_num.isdigit():
            return 'Error: Numbers must only contain digits.'
        
        if operator=="+":
            sum_num = int(first_num) + int(second_num)
        if operator =="-":
            sum_num = int(first_num) - int(second_num)
        line =""

        distance = (max(len(first_num), len(second_num)) + 2)
        
        #start formatting
        top_line = top_line+(str(first_num).rjust(distance))+" "*4
        bottom_line = bottom_line + operator+str(second_num).rjust(distance-1)+" "*4
        total = total + str(sum_num).rjust(distance)+" "*4
        for i in range(distance):
            line+="-"
        lines=lines+line+" "*4
    if show_answers == True:
        result = top_line + "\n" + bottom_line + "\n" + lines + "\n" + total
    if show_answers == False:
         result = top_line + "\n" + bottom_line + "\n" + lines 
    return result


rs=arithmetic_arranger(["3 + 855", "3801 - 2", "45 + 43", "123 + 49"],True)

print(rs)