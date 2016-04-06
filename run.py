#!usr/bin/python3
#Hello! This is my text-based assistant.
print('Type help() for help.')
freeInput = input('>>> ')
approvedCommands = ['help()', 'rangeFind()']
def help():
    print('Here is a list of commands you can use:', '\n', '    - help(): You already know this :D' '\n', '    - CTRL^C: Exits, providing you are in linux.', '\n', '    - rangeFind(): Gives the range of an object, provided the length of scope, the size in inches of the lens, the zoom factor of the lens, the percentage of lens the object takes up (long way), and the estimated length of the object.')
def rangeFind():
    scopeLength = float(input('Length in inches of your telescope: '))
    lensSize = float(input('Size in inches of (objective) lens: '))
    lensZoom = float(input('Zoom factor (place one if none): '))
    blockPercentage = float(input('Percentage of length the object takes up of the view, long ways: '))
    objectLength = float(input('Estimated length of the object, inches: '))
    rangeFound = (scopeLength*(objectLength/lensSize))*lensZoom/(blockPercentage/100.0)
    rangeFoundFeet = rangeFound / 12.0
    print('\n', 'The estimated distance between you and the object is {0} inches, or {1} feet.'.format(rangeFound, rangeFoundFeet))
while True:
    if str(freeInput) in approvedCommands:
        exec(freeInput)
        freeInput = input('>>> ')
