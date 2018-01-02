import u3
import traceback
from datetime import datetime

MAX_REQUESTS = 250  # Loops for 250 times and can be changed for desire inputs
testCount = 0   # Initialize Counts for MAX_REQUESTS
d = u3.U3()

def main():
    global testCount
    print "LabJack Potentiometer v0.1: By Dominic Ricchio"
    while True:
        main_answer = raw_input("Press [Y|N] to continue ")

        if main_answer == "Y" or main_answer == "y":
            print "Connecting to the Labjack U3"
            try:
                d.configU3()
                d.getCalibrationData()
                d.configIO(FIOAnalog=3)
                print "configuring U3 stream"
                d.streamConfig(NumChannels=2, PChannels=[0, 1], NChannels=[31, 31], Resolution=3, ScanFrequency=5000)
                testCount = testCount + 1
                test()
            except:
                if testCount > 0:
                    print "Test is successful, Labjack disconnected"
                else:
                    print "LabJack is not connected"

        elif main_answer == "N" or main_answer == "n":
            print "Aborting the code in 3 sec"
            print "Aborted"
            exit()

        else:
            print "Please Try Again with different input"

def test():
    # Start Test Cycle
    try:
        # Initialize stream connections and counts
        print "Start stream"
        d.streamStart()
        start = datetime.now()
        print start

        missed = 0
        dataCount = 0
        packetCount = 0

        for r in d.streamData():
            if r is not None:
                #Stop Condition
                if dataCount >= MAX_REQUESTS:
                    break
                if r['errors'] != 0:
                    print "Error: %s ; " %r['numPackets'], datetime.now()
                if r['numPackets'] != d.packetsPerRequest:
                    print "----- UNDERFLOW: %s : " %r['numPackets'], datetime.now()
                if r['missed'] != 0:
                    missed += r['missed']
                    print "+++ Missed ", r['missed']
                # Raw Results are obtained below if it missed all if statements
                print "Potentiometer Voltage: ", sum(r['AIN0']) / len(r['AIN0'])

                dataCount += 1
                packetCount += r['numPackets']

            else:
                #No data obtained if stream didn't show or USB read timeout ~ 1 sec
                print "No Data obtained ", datetime.now()
    except:
        print "".join(i for i in traceback.format_exc())

    finally:
        # When MAX_REQUESTS reached numbers then starts to cut stream connection to shut down
        stop = datetime.now()
        d.streamStop()
        print "Stream stopped"
        d.close()
        
        # Starts to gather data together and preparing outputs
        sampleTotal = packetCount * d.streamSamplesPerPacket
        scanTotal = sampleTotal / 2 # sampleTotal / numChannels

        print "$s requests with %s packets per request with %s samples per packet = %s samples total." % (
        dataCount, (float(packetCount) / dataCount), d.streamSamplesPerPacket, sampleTotal)
        print "%s samples were lost due to errors." % missed
        sampleTotal -= missed
        print "Adjusted number of samples = %s" % sampleTotal

        runTime = (stop - start).seconds + float((stop - start).microseconds) / 1000000
        print "The experiment took %s seconds." % runTime
        print "Scan Rate: %s scans / %s seconds = %s Hz" % (scanTotal, runTime, float(scanTotal) / runTime)
        print "Sample Rate: %s samples / %s seconds = %s Hz" % (sampleTotal, runTime, float(sampleTotal) / runTime)


main()
