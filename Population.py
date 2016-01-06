#Madison Thorburn-Gundlach
#August 31, 2015

#Take input "years" and spit out estimated population

#Establish known variables
current_population_int = 307357870
births_per_second_float = 1/7
deaths_per_second_float = 1/13
immigrants_per_second_float = 1/35
seconds_to_year = 31536000

#Prompt for input
the_future_str = input("I can tell the future.  How many years ahead? ")

#Convert from string type to integer type
the_future_int = int(the_future_str)

#Calculate: add births and immigrations, and sutract deaths
future_population_float = current_population_int \
                          + births_per_second_float * seconds_to_year * the_future_int \
                          - deaths_per_second_float * seconds_to_year * the_future_int\
                          + immigrants_per_second_float * seconds_to_year * the_future_int

#Tell the future (aka print results)
print ("The population in ", the_future_int, " years will be about",\
       future_population_float, "people.")
