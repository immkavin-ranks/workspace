def main():
    filename = input('Enter a filename: ')
    try:
        infile = open(filename)
        contents = infile.read()
        infile.close()
        print(contents)
    except IOError:
        print('An error occurred trying to read')
        print('the file', filename)

main()