invalid_id_sum = 0

# NOTE: PART ONE

# with open('puzzle_input.txt') as f:
#     for range_value in f.read().split(','):
#         starting_value = range_value.split('-')[0]
#         ending_value = range_value.split('-')[1]


#         for num in range(int(starting_value), int(ending_value)+1):
#             str_num = str(num)

#             if len(str_num) % 2 != 0:
#                 continue

#             else:
#                 first_half = str_num[:int(len(str_num)/2)]
#                 second_half = str_num[int(len(str_num)/2):]

#                 if first_half == second_half:
#                     invalid_id_sum += num

# NOTE: PART TWO
with open('puzzle_input.txt') as f:
    for range_value in f.read().split(','):
        starting_value = range_value.split('-')[0]
        ending_value = range_value.split('-')[1]


        for num in range(int(starting_value), int(ending_value)+1):
            str_num = str(num)
            # kinda bruteforce but must work ¯\_(ツ)_/¯
            for split in range(1, 11):
                if len(str_num) % split == 0:
                    # first_split = str_num[:split]
                    # second_split = str_num[split:split*2]
                    parts = [str_num[i:i+split] for i in range(0, len(str_num), split)]
                    

                    if all(x == parts[0] for x in parts) and len(parts) != 1:
                        invalid_id_sum += num
                        break
                else:
                    continue


print(invalid_id_sum)