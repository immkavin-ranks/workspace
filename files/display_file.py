def main():
    filename = input('Enter a filename: ')
    infile = open(filename)
    contents = infile.read()
    infile.close()
    print(contents)

main()
   