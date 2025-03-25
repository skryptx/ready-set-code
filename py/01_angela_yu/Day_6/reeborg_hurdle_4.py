# def turn_right():
#     turn_left()
#     turn_left()
#     turn_left()
#
#
# def move_up():
#     counter = 0
#     while wall_on_right():
#         move()
#         counter += 1
#     return counter
#
#
# def move_down(counter):
#     while counter != 0:
#         move()
#         counter -= 1
#
#
# def cycle():
#     turn_left()
#     steps_up = move_up()
#     turn_right()
#     move()
#     turn_right()
#     move_down(steps_up)
#     turn_left()
#
#
# while not at_goal():
#     while not wall_in_front():
#         if at_goal():
#             break
#         move()
#     if at_goal():
#         break
#     cycle()
