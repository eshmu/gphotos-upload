import logging
import re
import fnmatch
import os
import os.path
import re
import argparse


def parse_args(arg_input=None):
    parser = argparse.ArgumentParser(description='Get OS Albums.')
    parser.add_argument('--top_dir', metavar='top_dir', dest='top_dir',
                    help='root photo directory.',
                    type=str)
    parser.add_argument('--log', metavar='log_file', dest='log_file',
                    help='name of output file for log messages')
    parser.add_argument('--output', metavar='output_file', dest='output_file',
                    help='name of output file for OS albums'),
    return parser.parse_args(arg_input)


def main():
    args = parse_args()
    logging.basicConfig(format='%(asctime)s %(module)s.%(funcName)s:%(levelname)s:%(message)s',
                    datefmt='%m/%d/%Y %I_%M_%S %p',
                    filename=args.log_file,
                    level=logging.INFO)

    if not args.top_dir:
        args.top_dir = 'd:\\Users\\kumars\\Pictures'

    if not args.output_file:
        args.output_file = 'os_albums.txt'

    
    dirs_with_jpg = []
    for (root,dirs,files) in os.walk(args.top_dir, topdown=True):
        if root == args.top_dir:
            #print('realpath='+os.path.realpath(root))
            if ((os.path.realpath(root)).lower() == "d:\\Users\\kumars\\Pictures".lower()):
                dirs[:] = fnmatch.filter(dirs, '[12]*Pictures')
        #print(root)
        my_dirname = ''
        if (len(fnmatch.filter(files, '*.[Jj][Pp][Gg]')) > 0):
            basename = os.path.basename(root)
            if ( basename == 'jpg'):
                my_dirname = os.path.dirname(root)
                dirs_with_jpg.append(my_dirname)
            elif ( basename == 'camerajpg' or basename == 'camera jpg' or basename == 'Camera jpg'):
                my_dirname = os.path.dirname(root)
                dirs_with_jpg.append(my_dirname)
            elif ( basename == '.picasaoriginals' or basename == 'Originals'or basename == 'cr2'):
                my_dirname = os.path.dirname(root)
                #skip all .picasaoriginals and Originals dirs_with_jpg.append(my_dirname)
            else:
                my_dirname = root
                dirs_with_jpg.append(my_dirname)
    
    sorted_uniq_dirs_with_jpg = sorted(set(dirs_with_jpg))
    with open(args.output_file, 'w') as output_f:
        for d in sorted_uniq_dirs_with_jpg:
            print(d, file=output_f)
        
if __name__ == '__main__':
  main()



