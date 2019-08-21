import argparse

ap = argparse.ArgumentParser()
ap.add_argument("-i", "--input", help = "text you want to write to the my_diary.txt file")
args = vars(ap.parse_args())

print('Thanks for using the python diary app!')

if args["input"] != None:  #Only opens and writes to txt file if input is given (ie Not equal != to None)
    string1 = str(args["input"]).replace("_", " ") + "\n"
    # \n is placed to indicate End of Line

    txtfilename = "my_diary.txt"
    file1 = open( txtfilename, "a" )    #open the text file, append to it 
    file1.write(string1)
    file1.close()
    print("Your entry has been recorded!")

else:
    print("No input given, try again!")

