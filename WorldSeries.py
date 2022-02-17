infile = open('WorldSeriesWinners.txt','r')
infile2 = open('WorldSeriesWinners.txt','r')


output = int(input("Type in a year: "))


if output == 1904:
    print("No World Series played this year.")
elif output == 1994:
    print("No World Series played this year.")
else:
    winners = {}


    for line in infile:
        line = line.rstrip("\n")
        if line in winners:
            winners[line] = winners[line] + 1
        else:
            winners[line] = 1
    winners[line]

##############################################################
    year = {}


    counter = 1902
    for line in infile2:
        line = line.rstrip("\n")
        if counter == 1903:
            counter += 2 
            year[counter] = line
        elif counter == 1993:
            counter += 2 
            year[counter] = line
        else:
            counter += 1
            year[counter] = line
    year[counter] = line

    counter = output
    result = year[counter]
    wins = winners[result]
    print("World Series Champion:",result)
    print("Number of Championships won:", wins)
