import argparse

ap = argparse.ArgumentParser()
ap.add_argument("-i", "--input", help = "text you want to write to the my_diary.txt file")
args = vars(ap.parse_args())

print('Thanks for using the python diary app!')

#This file is made to test that replace("_", " ") works, entries should have _ as spaces, no whitespace!
if args["input"] != None:  #Only runs if input is given (ie Not equal != to None)
    string1 = str(args["input"]).replace("_", " ")
    print( string1 )
    print("Success")

else:
    print("No input given, try again!")


