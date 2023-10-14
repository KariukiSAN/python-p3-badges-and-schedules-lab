def badge_maker(name):
    message = f'Hello, my name is {name}.'
    return message

def batch_badge_creator(names):
    messages = [f'Hello, my name is {name}.' for name in names]
    return messages




def assign_rooms(names):
      rooms = [
        f'Hello, {name[1]}! You\'ll be assigned to room {name[0]}!' for name in enumerate(names,1)]
      return rooms
assign_rooms(['Guido','Edsger','Ada','Charles','Alan', 'Grace', 'Linus'])

def printer(names):
    return None
