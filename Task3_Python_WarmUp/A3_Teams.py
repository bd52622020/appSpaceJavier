import random

def check_parameters_team(total_games, wins, loses, team_name="uknown", draws=0):
    # Check if the user introduced draws
    calculated_draws = total_games - (wins + loses)
    if draws == 0 and calculated_draws - draws != 0:
        draws = calculated_draws
    
    total_points = wins * 3 + draws * 1
    taunts = {1: "LETS PLAY SHITTY TEAM! EOEOEO"}
    good_comments = {1: "This team should be playing in the galaxy",
                     2: "This team should be upon the table",
                     3: "This team should be playing all day!"}
    
    bad_comments = {1: "My brother can play better than this team",
                     2: "My mum can play better than this team",
                     3: "My grandma can play betther than this shitty players"}
    
    print("Welcome to our team checker!")
    print("Analyzing {}...".format(team_name))
    print("This team has a total of points of ", total_points)
    print("The supporters usually sings the following: ", taunts.get(1))
    print("Our comments are:")
    if wins > loses:
        print(good_comments.get(random.randrange(1, 3)))
    else:
        print(bad_comments.get(random.randrange(1, 3)))
        
        
check_parameters_team(20, 5, 10, "Chelsea FC")