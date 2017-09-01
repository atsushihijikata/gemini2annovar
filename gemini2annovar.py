import os, sys

VERSION='0.1'

def to_annovar(data):
    chrom, start, end, ref, alt = data
    if len(ref) == len(alt): # SNV or MNV:
        return chrom, start, end, ref, alt
    elif len(ref) > len(alt): # Deletion
        ref = ref[1:]
        alt = "-"
    elif len(ref) < len(alt): # Insertion
        ref = "-"
        alt = alt[1:]
        start = str(int(start)+1)
    return chrom, start, end, ref, alt

def main():
    if len(sys.argv) != 2:
        print("Usage:\n")
        print("  %s    Gemini_file\n\n" % sys.argv[0])
        exit()

    with open(sys.argv[1], 'r') as f:
        lines = [line.rstrip() for line in f.readlines()]

    for line in lines:
        if line.startswith('#') or line.startswith('chr'):
            continue
        cols = line.split('\t')
        chrom, start, end, ref, alt = to_annovar(cols[0:5])
        print("\t".join([chrom, start, end, ref, alt, "\t".join(cols[5:])]))


if __name__ == '__main__':
    main()
