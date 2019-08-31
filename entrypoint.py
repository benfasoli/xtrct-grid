#!/usr/bin/env python
# Ben Fasoli

import argparse
import os
import subprocess


def latitude(x):
    x = float(x)
    if x < -90 or x > 90:
        raise argparse.ArgumentError('latitude must be in range [-90, 90]')
    return x


def longitude(x):
    x = float(x)
    if x < -180 or x > 180:
        raise argparse.ArgumentError('longitude must be in range [-180, 180]')
    return x


def quoted(x):
    return '\"' + x + '\"'


def xtrct_grid(input: str,
               input_dir: str,
               output: str,
               output_dir: str,
               levels: int,
               xmin: float,
               xmax: float,
               ymin: float,
               ymax: float):
    """Extract spatial subdomain from ARL packed file

    Parameters
    ----------
    input : str
        input data file name without path
    input_dir : str
        mount location for input data volume
    output : str
        output data file name
    output_dir : str
        mount locatino for output data volume
    levels : int
        vertical levels to extract
    xmin : float
        minimum x coordinate of subdomain
    xmax : float
        maximum x coordinate of subdomain
    ymin : float
        minimum y coordinate of subdomain
    ymax : float
        maximum y coordinate of subdomain
    """
    input_dir = os.path.join(input_dir, '')
    header = ','.join([
        'Met_Directory',
        'File_Name',
        'Lower_Left_Lat',
        'Lower_Left_Lon',
        'Upper_Right_Lat',
        'Upper_Right_Lon',
        'Levels',
        'Output_file'
    ])
    body = ','.join(str(x) for x in [
        quoted(input_dir),
        quoted(input),
        ymin,
        xmin,
        ymax,
        xmax,
        levels,
        quoted(output)
    ])
    config = '\n'.join([header, body])
    with open('INPUT_EXTRACT.TXT', 'w') as f:
        f.write(config)
    wd = os.path.dirname(os.path.realpath(__file__))
    proc = subprocess.run(os.path.join(wd, 'xtrct_grid'), check=True)
    os.rename(output, os.path.join(output_dir, output))


if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        description='Extract spatial subdomain from ARL packed file.')

    parser.add_argument('-l', '--xmin', type=longitude, required=True,
                        help='minimum x coordinate of subdomain')
    parser.add_argument('-r', '--xmax', type=longitude, required=True,
                        help='maximum x coordinate of subdomain')
    parser.add_argument('-b', '--ymin', type=latitude, required=True,
                        help='minimum y coordinate of subdomain')
    parser.add_argument('-t', '--ymax', type=latitude, required=True,
                        help='maximum y coordinate of subdomain')

    parser.add_argument('-i', '--input', type=str, required=True,
                        help='input data file name without path')
    parser.add_argument('-o', '--output', type=str, required=True,
                        help='output data file name')
    parser.add_argument('--input_dir', type=str, default='/input',
                        help='mount location for input data volume')
    parser.add_argument('--output_dir', type=str, default='/output',
                        help='mount location for output data volume')
    parser.add_argument('--levels', type=int, default=36,
                        help='vertical levels to extract')
                        
    args = parser.parse_args()
    xtrct_grid(**vars(args))
