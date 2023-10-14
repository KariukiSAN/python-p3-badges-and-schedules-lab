def badge_maker(name):
    message = f'Hello, my name is {name}.'
    return message

def batch_badge_creator(names):
    messages = [f'Hello, my name is {name}.' for name in names]
    return messages




def assign_rooms(names):
    room_assignments = []
    for i, name in enumerate(names, 1):
        room_assignments.append("Hello, {}! You'll be in room {}.".format(name, i))
    return room_assignments

def printer(names):
    return None
