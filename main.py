import serial
import os

moniter = serial.Serial('/dev/ttyACM0', 9600)

def split(word):
    return list(word)

while True:
    try:
        raw_data = moniter.readline().decode('UTF-8')
    except:
        continue

    if raw_data == '':

        continue

    else:

        raw_data = split(raw_data)

        x_commands = [raw_data[0], raw_data[1]]
        y_commands = [raw_data[2].strip(), raw_data[3].strip()]
        left_click = raw_data[4]
        right_click = raw_data[5]
        
        if y_commands == ['0', '0']:
            os.system('xdotool click 5')
            pass

        # print(x_commands[0])
        if x_commands == ['1', '1']:
            pass

        elif x_commands == ['0', '0']:
            os.system('xdotool click 4 ')
            pass
        else:
            # print('lol')
            if int(x_commands[0]) == 0:
                # print('here')
                
                os.system('xdotool mousemove_relative -- -5 0');

                pass
                
            
            elif int(x_commands[1]) == 0:
                os.system('xdotool mousemove_relative 5 0');
                # print('here too')
                pass
        

        if y_commands == ['1', '1']:
            pass
        
        elif y_commands == ['0', '0']:
            pass

        else:

            if int(y_commands[0]) == 0:
                # print('here')
                
                os.system('xdotool mousemove_relative -- 0 -4');
                pass
                
            
            elif int(y_commands[1]) == 0:

                os.system('xdotool mousemove_relative 0 4');

                # print('here too')
                pass
        
        if left_click == '0' or 0:
            os.system('xdotool click 1')
        
        if right_click == '0' or 0:
            os.system('xdotool click 3')
    





