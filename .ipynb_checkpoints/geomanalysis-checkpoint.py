import numpy as np
import os
import argparse

def calc_dist(coords1, coords2):
    distance = np.sqrt((coords1[0]-coords2[0])**2+(coords1[1]-coords2[1])**2+(coords1[2]-coords2[2])**2)
    return distance

def bond_check(distances, min_len=0, max_len=1.5):
    '''
    Check if a distance is a bond based on minimum and maximum lengths
    Inputs: distance, minimum length, maximum length
    Defults: minimum = 0, maximum = 1.5
    Returns: True or False
    '''
    if distances > min_len and distances <= max_len:
        return True
    else:
        return False
    
if __name__ == '__main__':

    parser = argparse.ArgumentParser(description='This script analyzes an xyz file and outputs the bonds and their lengths.')
    parser.add_argument('xyz_file', help='the filepath for the xyz file being analyzed')
    args = parser.parse_args()

    file = args.xyz_file
    water = np.genfromtxt(fname=file, skip_header=2, dtype='unicode')
    num_atoms = len(water)
    atom = water[:,0]
    coords = water[:,1:]
    coords = coords.astype(np.float)
    for i in range(0, num_atoms):
        for j in range(0, num_atoms):
            if i < j:
                distances = calc_dist(coords[i], coords[j])
                if bond_check(distances) is True:
                    print(f'{atom[i]} to {atom[j]} : {distances:.3f}')