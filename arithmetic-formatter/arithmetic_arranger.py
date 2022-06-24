def arithmetic_arranger(problems, calculate=None):
  arranged_problems = ''
  if (len(problems) <= 5):
    problems = [i.split(" ") for i in problems]

    operation = [i[1] for i in problems]
    num_row_1 = [i[0] for i in problems]
    num_row_2 = [i[2] for i in problems]

    valid_num_row_1 = [len(i) <= 4 for i in num_row_1]
    valid_num_row_2 = [len(i) <= 4 for i in num_row_2]

    isdigit_num_row_1 = [i.isdigit() for i in num_row_1]
    isdigit_num_row_2 = [i.isdigit() for i in num_row_2]
    max_len = [max([len(num_row_1[i]),len(num_row_2[i])]) for i in range(len(problems))]

    if ('/' in operation or '*' in operation):
      arranged_problems = "Error: Operator must be '+' or '-'."
    elif(False in valid_num_row_1 or False in valid_num_row_2):
      arranged_problems = "Error: Numbers cannot be more than four digits."
    elif(False in isdigit_num_row_1 or False in isdigit_num_row_2):
      arranged_problems = "Error: Numbers must only contain digits."
    else:
      empty_space = 4 * ' '
      for i in range(len(problems)):
        if (i == len(problems) -1):
          arranged_problems += "{}{}{}".format(" "*2,(max_len[i]-len(num_row_1[i]))*" ",num_row_1[i])
        else:
          arranged_problems += "{}{}{}{}".format(" "*2,(max_len[i]-len(num_row_1[i]))*" ",num_row_1[i],empty_space)

      arranged_problems += "\n"
      for i in range(len(problems)):
        if (i == len(problems) -1):
          arranged_problems += "{}{}{}".format(operation[i]+" ",(max_len[i]-len(num_row_2[i]))*" ",num_row_2[i])
        else:
          arranged_problems += "{}{}{}{}".format(operation[i]+" ",(max_len[i]-len(num_row_2[i]))*" ",num_row_2[i],empty_space)
      arranged_problems += "\n"
      
      for i in range(len(problems)):
        if(i == len(problems)-1):
          arranged_problems += '{}'.format((max_len[i]+2)*"-")
        else:
          arranged_problems += '{}{}'.format((max_len[i]+2)*"-",empty_space)
      
      if (calculate):
        arranged_problems += "\n"
        for i in range(len(problems)):
          if (i == len(problems)-1):
            if (operation[i] == '+'):
              arranged_problems += "{}{}".format(((max_len[i]+2)-len(str(int(num_row_1[i])+int(num_row_2[i]))))*" ",int(num_row_1[i])+int(num_row_2[i]))
            elif(operation[i] == '-'):
              arranged_problems += "{}{}".format(((max_len[i]+2)-len(str(int(num_row_1[i])-int(num_row_2[i]))))*" ",int(num_row_1[i])-int(num_row_2[i]))
          else:
            if (operation[i] == '+'):
              arranged_problems += "{}{}{}".format(((max_len[i]+2)-len(str(int(num_row_1[i])+int(num_row_2[i]))))*" ",int(num_row_1[i])+int(num_row_2[i]),empty_space)
            elif(operation[i] == '-'):
              arranged_problems += "{}{}{}".format(((max_len[i]+2)-len(str(int(num_row_1[i])-int(num_row_2[i]))))*" ",int(num_row_1[i])-int(num_row_2[i]),empty_space)
  else :
    arranged_problems = "Error: Too many problems."


  return arranged_problems

print(arithmetic_arranger(["32 + 8", "1 - 3801", "9999 + 9999", "523 - 49"]))


