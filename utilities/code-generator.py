__author__ = 'ershadmoi'

import re
import sys

# Small utility method to copy between two streams
def copyfilestreams(inputfile, outputfile):
    for line in inputfile:
        print(line, file=outputfile)

# Main method that will do code generation magic
def main(argv):
    # lets read the file first
    f = open(argv[1], "r+")
    newf = open("generated" + argv[1], "w+")

    # For each line, check if its an annotation
    for line in f:
        # Strip new lines
        line = line.rstrip('\n')

        # Check if it is a comment line
        if line.startswith("//"):
            # Search for Overrides pattern
            searchobj = re.search( r'@Overrides\((.*)\)', line, re.M)

            # If search returns true then we have our override files to use
            # and inline a generated file
            if searchobj:
                # Get the override files by parsing csv
                overridefiles = searchobj.group(1).split(",")

                # For each override file copy the filestreams
                for overrideFile in overridefiles:
                    tempf = open(overrideFile, "r+")
                    copyfilestreams(tempf, newf)
                    tempf.close()

        # Otherwise just proxy print the lines from f to newf
        else:
            print(line, file=newf)

    # Close the file streams
    f.close()
    newf.close()

# Call main only if explicity invoked
if __name__ == "__main__":
    main(sys.argv)


