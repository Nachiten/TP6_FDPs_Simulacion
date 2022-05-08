import datetime
from datetime import timedelta


def readFileAndGenerate(filename):
    lines = []

    with open(filename + ".csv") as f:
        # Read all lines on the file
        linesRead = f.readlines()

        # For each linea, remove the newline character and split the line into a list of strings
        for line in linesRead:
            line = line.rstrip()
            line = line.split(';')
            lines.append(line)

    # Print each element of the list in a new line
    # for line in lines:
    #    print(line)

    times = []

    last_time = datetime.datetime.now()

    times.append(last_time.strftime("%d/%m/%Y %H:%M:%S"))

    for line in lines:
        for i in range(0, int(line[1])):
            mins_sum = timedelta(minutes=(int(line[0])))
            new_time = last_time + mins_sum
            last_time += mins_sum
            times.append(new_time.strftime("%d/%m/%Y %H:%M:%S"))

    # for time in times:
    #    print(time)

    # Write all the times to a new file
    with open(filename + ".txt", 'w') as f:
        for time in times:
            f.write(time + '\n')

    print("File '" + filename + ".txt' generated successfully")


readFileAndGenerate("Generacíón de datos - IA - New")
