import os
import argparse
  
parser = argparse.ArgumentParser(description='This script finds and prints the total energy from amber mdout files.')
parser.add_argument('path', help='The file path for the file being analyzed')
args = parser.parse_args()
    
infile = args.path
file = open(infile, 'r')
data = file.readlines()
file.close()

basefile = infile.split('.')[0]
newfilename = f'{basefile}_Etot.txt'
newfile = open(newfilename, 'w')

etot = []
for line in data:
    splitline = line.split()
    if 'Etot' in line:
        etot.append(splitline[2])
etot = etot[:-2]    
for energy in etot:
    newfile.write(f'{energy} \n')
newfile.close()