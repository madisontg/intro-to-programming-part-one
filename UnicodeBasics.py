# Madison Thorburn-Gundlach
# September 28 LAB
# Prints out Unicode values 1 to 127 with the corresponding index next to it

index_count = 1

while index_count < 128:
    print(chr(index_count), index_count)
    index_count += 1
    
### weird spacing:
##    0 --> null
##    9 --> tab
##    10 --> line feed
##    13 --> carriage return
##    28 --> curser right
##    29 --> curser left
##    30 --> curser up
##    31 --> curser down
##    
### weird character:
##    127 --> supposed to be some sort of weird thing and came out a different weird thing
