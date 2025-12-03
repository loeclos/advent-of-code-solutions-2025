
current_position = 50
zero_counts = 0

# NOTE: PART ONE

# with open('puzzle_input.txt') as f:
#     for rotation in f.readlines():
#         if current_position == 0:
#             zero_counts += 1

#         if rotation.startswith('R'):
#             rotation_value_r = int(rotation[1:])

#             for r in range(rotation_value_r):
#                 if current_position == 99:
#                     current_position = 0
#                 else:
#                     current_position += 1
            
#         if rotation.startswith('L'):
#             rotation_value_l = int(rotation[1:])
            
#             for r in range(rotation_value_l):
#                 if current_position == 0:
#                     current_position = 99
#                 else:
#                     current_position -= 1
            
# NOTE: PART TWO

with open('puzzle_input.txt') as f:
    for rotation in f.readlines():
        # if current_position == 0:
        #     zero_counts += 1

        if rotation.startswith('R'):
            rotation_value_r = int(rotation[1:])

            for r in range(rotation_value_r):
                if current_position == 0:
                    zero_counts += 1

                if current_position == 99:
                    current_position = 0
                else:
                    current_position += 1
            
        if rotation.startswith('L'):
            rotation_value_l = int(rotation[1:])
            
            for r in range(rotation_value_l):
                if current_position == 0:
                    zero_counts += 1

                if current_position == 0:
                    current_position = 99
                else:
                    current_position -= 1


print(zero_counts)