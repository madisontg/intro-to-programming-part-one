# Madison Thorburn-Gundlach
# Due September 3, 2015
# Using the internet as a source, find a module that will generate today's date

# import module
# I don't know what the "from" does but it doesn't work without it
from datetime import datetime

# assign variables
x = datetime.now()
date = x.strftime("%Y-%m-%d")
date_america = x.strftime("%m-%d-%Y")

# call/print
print("Today's date is:", date)
print("Or, if you're like most Americans, it's:", date_america)




# source:http://www.cyberciti.biz/faq/howto-get-current-date-time-in-python/
