
current_position = 50
zero_counts = 0

with open('puzzle_input.txt') as f:
    for rotation in f.readlines():
        if rotation.startswith('R'):
            current_sum = current_position + int(rotation[1:])
            if current_sum > 99:
                between_sum = current_sum
                while between_sum > 99:
                    between_sum -= 99
                # current_position = (current_sum - 99)
            else:
                current_position = current_sum
        elif rotation.startswith('L'):
            current_diff = current_position - int(rotation[1:]) 
            if current_diff < 0:
                between_sum = current_diff
                while between_sum < 0:
                    between_sum += 99
            else:
                current_position = current_diff
        if current_position == 0:
            zero_counts += 1
        # print(current_position)
        print(zero_counts)