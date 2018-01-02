#==================================================#
# The features are being tested for part of PKL
#==================================================#


class Direction:
    N = 0
    CW = 1
    CCW = 2


def main():
    value = 0

    while (value <= 2):

        if (value == Direction.N):
            print "NEUTRAL"
            print Direction.N
            value = Direction.CCW
            print value
        elif (value == Direction.CW):
            print "CW"
            print Direction.CW
            print value
        elif (value == Direction.CCW):
            print "CCW"
            print Direction.CCW
            print value

        value += 1


main()
