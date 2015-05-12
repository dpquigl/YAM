import re
import sys

def ExtractMessages(infile):
     with open(infile) as fp:
         for result in re.findall('----(.*?)----', fp.read(), re.S):
             print result

def main(argv=None):
    if argv is None:
        print "Usage: python extract_protobuf.py "
        sys.exit()

    ExtractMessages(argv[1])
    
    
if __name__ == '__main__':
    main(sys.argv)
