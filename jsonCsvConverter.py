import csv 
import json
import re

def jsonToCsv(jsonFile, output):
    fileInput = jsonFile
    fileOutput = output
    inputFile = open(fileInput) #open json file
    outputFile = open(fileOutput, 'w') #load csv file
    data = json.load(inputFile) #load json content
    inputFile.close() #close the input file
    output = csv.writer(outputFile) #create a csv.write
    output.writerow(data[0].keys())  # header row
    for row in data:
        output.writerow(row.values()) #values row
        
def csvToJson(csvFile,output):
    fileInput = csvFile
    fileOutput = output
    inputFile = open(fileInput) #open csv file
    outputFile = open(fileOutput, 'w') #open json/output file
    lines= []
    for line in inputFile:
        line = line.replace("\n","") #remove newline chars from the end of each rec
        lines.append(line) # read each line into lines list
    header = lines[0].split(",")
    for i in lines[1:]:
        data_line = i.split(",")
        data_dict = dict(zip(header,data_line))
        json.dump(data_dict, outputFile) 
        
def jsonRegex(infile, output):
    '''
    jsonRegex(infile,output) expects a file from CSVTOJSON function.
    jsonRegex takes in a the formated file from csv2json and adds a [ at the beginning of the file
    and formats between the }{ to add a comma },{. It also adds the closing bracket ] at the end of 
    the file. Current is is added to a new line. currently working on getting it to the end of the last
    entry
    '''
    fileInput = infile
    fileOutput = output
    inputfile = open(fileInput,'r')
    outputfile= open(fileOutput, 'w')
    outputfile.write("[")
    for x in inputfile:
        outputfile.write(x.replace("}{","},{"))
    outputfile.write("]")
    outputfile.close()
