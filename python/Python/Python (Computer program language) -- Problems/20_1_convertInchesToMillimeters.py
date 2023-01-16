foot=inch=0
Centimeter=meter=0
footToMeter=footToCentimeter=inchToMeter=inchToCentimeter=0
def read():
    foot=int(input('Enter Foot : '))
    inch=int(inch('Enter inch : '))
def calculate ():
    footToMeter=0.3048*foot
    footToCentimeter=100*footToMeter
    inchToMeter=(1.0/12)*0.3048*inch
    inchToCentimeter=100*inchToMeter
def write():
    print('The ',foot,' foot is ',footToMeter,' meter')
    print('The ',foot,' foot is ',footToCentimeter,' Centimeter')
    print('The ',inch,' inch is ',inchToMeter,'meter' )
    print('The ',inch,' inch is ',inchToCentimeter,'centimeter')
def main():
    read()
    calculate()
    write()
main()