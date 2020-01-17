import pandas as pd 
import csv

with open('meteorite-landings.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
    # for row in csv_reader:
    #     if line_count == 0:
    #         print(f'Las columnas son: {" - ".join(row)}')
    #         line_count +=1
    #     else:
    #         print(f'\t El meteoro {row[0]} de ID: {row[1]} y de tipo: {row[2]}. Recclass: {row[3]}. Masa: {row[4]}')
    #         line_count += 1
    # print(f'Procesed {line_count} lines.')



def filterFile(inputFileName,outputFileName,filterCriteriaFileName,columnToFilter):

	infile = open(inputFileName, "r")
	read = csv.reader(infile)
	headers = next(read)

	outfile = open(outputFileName, "w")
	write = csv.writer(outfile)

	write.writerow([headers[4]])

	inFilterfile = open(filterCriteriaFileName, "r")
	filterCriteriaList = list(csv.reader(inFilterfile))


	for row in read:
            #print (row[4])
            try:
                write.writerow([row[4]])
            except Exception as e: 
                print(e)

filterFile('meteorite-landings.csv','OutputFile.csv','filterCriteria.csv',4)