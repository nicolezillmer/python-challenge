import os

import csv

csvpath = os.path.join('bankdata.csv')

#lists to store data
months = []
profloss = []
total = []
sum = 0
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')

    print(csvreader) 

    csv_header = next(csvreader)

    print(f"CSV Header: {csv_header}")


    for row in csvreader:
        #Add dates
        months.append(row[0])

        #Add profits/losses
        profloss.append(row[1])

    
#calculate number of months
    print ("Number of months = " + str(len(months)))

    #define profit/loss starting total
    total = 0
greatest_increase = profloss[1]-profloss[0]
    #loop through rows
    for i in range(0,len(profloss)):
        #add profits and losses row by row
        total = int(i) + total 
      
        sum=sum + (profloss[i+1]-profloss[i])
        if (profloss[i+1]-profloss[i])>greatest_increase:
            greatest_increase=(profloss[i+1]-profloss[i])
            date=months[i+1]
       



    print ("Total = " + str(total))

    # get average profit/loss
    print ("average change = " + str(sum / len(months)))

    #find maximum gain
    maxgain = 0
    #loop through profloss
    for i in profloss:
        if int(i) > maxgain:
            maxgain = int(i)
    
    #locate the date
    #print date

maxgain = int(i)
            
#print ("Maximum profit = " + str(i))
print ("Maximum profit = " + str(maxgain))

maxloss = 0

for j in profloss:
    if int(j) < maxloss:
        maxloss = int(j)

maxloss = int(j)

#print ("Maximum loss = " + str(j))
print ("Maximum loss = " + str(maxloss))



    
