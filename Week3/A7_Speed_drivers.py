def check_speed(speed=0):
    if speed > 70:
        delta = speed - 70
        points = int(delta / 5)
        if points > 11:
            print("Police: License suspended boy!")
        else:
            print("Police: You went so fast! You have to pay a tax of {} points".format(points))
    else:
        print("Police: Okey, continue")
        
check_speed(600)
    
