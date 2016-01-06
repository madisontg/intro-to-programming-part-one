# Madison Thorburn-Gundlach
# Due September 6, 2015

# For every magnitude between 8.5 and 10.0 (inclusive)
# return every earthquake with that magnitude

import math

# variable assignment
magnitude = 85

# earthquakes
eight_point_five = ["Lima, Peru", "Sanriku, Japan","Chile-Argentina Border","Kamchatka\nBanda Sea, Indonesia","Kuril Islands","Southern Sumatra, Indonesia"]

eight_point_six = ["Assam, Tibet","Andreanof Islands, Alaska","Northern Sumatra, Indonesia","Off the West Coast of Northern Sumatra"]
                   
eight_point_seven = ["Valparaiso, Chile","Lisbon, Portugal","Rat Islands, Alaska"]

eight_point_eight = ["Off the Coast of Esmereldas, Ecuador","Offshore Bio-Bio, Chile"]
                     
nine = ["Cascadia Subduction Zone","Arica, Peru (now Chile)","Kamchatka","Near the East Coast of Honshu, Japan"]

nine_point_one = ["Sumatra-Andaman Islands"]

nine_point_two = ["Prince William Sound, Alaska"]


# while loop
while magnitude <= 100:
    if magnitude == 85:
        print(magnitude/10,":",sep = "")
        for place in eight_point_five:
            print(place)
        print("\n")
    elif magnitude == 86:
        print(magnitude/10,":",sep = "")
        for place in eight_point_six:
            print(place)
        print("\n")
    elif magnitude == 87:
        print(magnitude/10,":",sep = "")
        for place in eight_point_seven:
            print(place)
        print("\n")
    elif magnitude == 88:
        print(magnitude/10,":",sep = "")
        for place in eight_point_eight:
            print(place)
        print("\n")
    elif magnitude == 90:
        print(magnitude/10,":",sep = "")
        for place in nine:
            print(place)
        print("\n")
    elif magnitude == 91:
        print(magnitude/10,":",sep = "")
        for place in nine_point_one:
            print(place)
        print("\n")
    elif magnitude == 92:
        print(magnitude/10,":",sep = "")
        for place in nine_point_two:
            print(place)
        print("\n")
    else:
        pass
    magnitude += 1
