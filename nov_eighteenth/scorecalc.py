def main():

    data = []
    fh = open("scores.csv", "r")
    weightedTotal = 0.0
    weighingTotal = 0.0

    for line in fh:

        line = line.rstrip("\n")
        parts = line.split(",")
        data.append(parts)

    header = data[0]
    del data[0]
      
    for item in data:
        percent = float(item[1]) / float(item[2]) * 100

        weightedScore = percent * float(item[3])
        
        weightedTotal += weightedScore
        weighingTotal += float(item[3])
        
        print(item[0], end="")
        print("\t\t" + str(int(percent)) + "%")

    finalScore = weightedTotal / weighingTotal
    print("Final Score: \t" + str(int(finalScore)) + "%")

main()
