
# def extract_game_data(game_description):
#     parts = game_description.split(": ")
#     game_number = int(parts[0].split(" ")[1]) 

#     subsets = parts[1].split("; ")

#     for subset in subsets:
#         # Initialize counts for each subset
#         blue_count, red_count, green_count = 0, 0, 0

#         cubes = subset.split(", ")
#         for cube in cubes:
#             cube_details = cube.split(" ")
#             if len(cube_details) == 2: 
#                 count, color = int(cube_details[0]), cube_details[1]
#                 if color == "blue":
#                     blue_count += count
#                 elif color == "red":
#                     red_count += count
#                 elif color == "green":
#                     green_count += count

#             # Check counts for each subset
#             if blue_count > 14 or red_count > 12 or green_count > 13:
#                 return game_number, False
        
#     return game_number, True


# import re

# file_path = './day-2/input.txt'  

# results_list = []
# import re

# # import the txt file and reads each line into a list of strings
# file = open('./day-2/input.txt' , 'r')
# lines = file.read().splitlines()

# # my functions
# def get_info(str_arg, req):  # split the color and count given group
#     if req == 'num': return int(re.split(' ', str_arg)[0])
#     elif req == 'color': return re.split(' ', str_arg)[1]

# def find_true(boolean_list): # given list of [True, False, True, True...], return True indexes
#     return [index for index, value in enumerate(boolean_list) if value]

# # game limitations:
# game_limits = [['red', 12], ['green', 13], ['blue', 14]]  # can add or remove limits
# game_possibility = []
# games_power = [] # ADDED FOR PART 2

# for i in range(len(lines)):
#     # parse each string to get data out
#     separated = re.split('; |: ', lines[i])  # split at ":" after game number and ";" between sets
#     current_game = [re.split(', ', separated[j]) for j in range(len(separated))]
#     max_green, max_red, max_blue = 0, 0, 0     # ADDED FOR PART 2:
#     set_possibility = []
#     for set in current_game[1:]:  # for each set of cubes revealed from the bag
#         color_possibility = []
#         for index, string in enumerate(set):
#             color = get_info(string, 'color')
#             quantity = get_info(string, 'num')
#             # is the color acceptable?
#             if any(color in sublist for sublist in game_limits):

#                 # ADDED FOR PART 2: get max quantity that's pulled from the bag for each color
#                 if color == 'green' and quantity > max_green:
#                     max_green = quantity
#                 elif color == 'red' and quantity > max_red:
#                     max_red = quantity
#                 elif color == 'blue' and quantity > max_blue:
#                     max_blue = quantity

#                 # check quantity against the relevant rule in game_limits
#                 rule = next(i for i, j in enumerate(game_limits) if color in j)
#                 if quantity <= (game_limits[rule][1]):
#                     color_possibility.append(True)
#                 else:
#                     color_possibility.append(False)
#             else:
#                 color_possibility.append(False)

#         if all(color_possibility): # if all colors and quantities are ok, set is possible
#             set_possibility.append(True)
#         else:
#             set_possibility.append(False)

#     if all(set_possibility): # if all sets are possible, game is possible
#         game_possibility.append(True)
#     else:
#         game_possibility.append(False)

#     # ADDED FOR PART 2:
#     power = max_green * max_blue * max_red
#     games_power.append(power)

# # get indexes of true games, then add 1 to get game number
# print(find_true(game_possibility))
# indexes = find_true(game_possibility)
# game_numbers = [x + 1 for x in indexes]
# answer = sum(game_numbers)
# print('Part 1 answer = ' + str(answer))

# # PART 2
# sum_of_powers = sum(games_power)
# print('Part 2 answer = ' + str(sum_of_powers))





















def extract_game_data(game_description):
    parts = game_description.split(": ")
    game_number = int(parts[0].split(" ")[1]) 

    subsets = parts[1].split("; ")


    for subset in subsets:
        cubes = subset.split(", ")
        blue_count, red_count, green_count = 0, 0, 0
        for cube in cubes:
            cube_details = cube.split(" ")
            if len(cube_details) == 2: 
                count, color = int(cube_details[0]), cube_details[1]
                print(count,color)
                if color == "blue":
                    blue_count += count
                elif color == "red":
                    red_count += count
                elif color == "green":
                    green_count += count

        if game_number==61 or game_number==45:
            print(cube_details)
            print(blue_count, red_count, green_count,blue_count>14 or red_count >12 or green_count>13)

        if blue_count>14 or red_count >12 or green_count>13:
            
            return game_number, False
    
    return game_number, True


import re

file_path = './day-2/input.txt'  

total=0
# only 12 red cubes, 13 green cubes, and 14 blue cubes?
curr=[]
with open(file_path, 'r') as file:
    for line in file:
        game,result=extract_game_data(line.strip())
        print("^^^^^^ ",game,result)
        if result:
            curr.append(game)
            total+=game
print(total)

print(curr)

[4, 7, 8, 9, 10, 14, 17, 18, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 33, 34, 37, 38, 39, 40, 41, 42, 43, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 58, 61, 62, 64, 66, 67, 68, 70, 71, 75, 76, 77, 78, 80, 82, 84, 88, 90, 93, 96, 99]
[4, 7, 8, 9, 10, 14, 17, 18, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 33, 34, 37, 38, 39, 40, 41, 42, 43, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 58, 61, 62, 64, 66, 67, 68, 70, 71, 75, 76, 77, 78, 80, 82, 84, 88, 90, 93, 96, 99]


44,  60

[4, 7, 8, 9, 10, 14, 17, 18, 22, 23, 24, 26, 27, 30, 31, 34, 37, 38, 40, 41, 42, 45, 46, 49, 50, 52, 54, 55, 58, 60, 62, 64, 66, 67, 68, 70, 71, 75, 76, 77, 78, 80, 82, 84, 88, 90, 93, 96, 99]