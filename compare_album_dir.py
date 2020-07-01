import logging
import re
import fnmatch
import os
import os.path
import re
import argparse
import bisect


def parse_args(arg_input=None):
    parser = argparse.ArgumentParser(description='Get OS Albums.')
    parser.add_argument('--infile', metavar='infile', dest='infile',
                    help='in file'),
    parser.add_argument('--log', metavar='log_file', dest='log_file',
                    help='name of output file for log messages'),
    parser.add_argument('--outfile', metavar='outfile', dest='outfile',
                    help='out file'),
    parser.add_argument('--comparefile', metavar='comparefile', dest='comparefile',
                    help='compare out file'),
    return parser.parse_args(arg_input)

def file_to_sorted_list():
    return

def main():
    args = parse_args()
    logging.basicConfig(format='%(asctime)s %(module)s.%(funcName)s:%(levelname)s:%(message)s',
                    datefmt='%m/%d/%Y %I_%M_%S %p',
                    filename=args.log_file,
                    level=logging.INFO)

    if not args.infile:
        args.infile = 'os_albums.txt'

    def readlines_strip(filename):
        with open(filename, 'r') as file_handle:
            lines=[]
            for line in file_handle:
                line=line.rstrip()
                lines.append(line)
            return lines
    jpg_dirs = readlines_strip(args.infile)
    
    if not args.outfile:
        args.outfile = 'g_albums.txt'
    google_albums = readlines_strip(args.outfile)

    if not args.comparefile:
        args.comparefile = 'upload.txt'
    with open(args.comparefile, 'w') as file_handle:
        for jpg_dir in jpg_dirs:
            if os.path.basename(jpg_dir) not in google_albums:
                print(jpg_dir, file=file_handle)
        
if __name__ == '__main__':
  main()



