import argparse 
import datetime #want to date the diary entries 

x = datetime.datetime.now()  #set date and time variable
str_time = str(x)[11:-7]   #str(x) = 2019-08-21 02:35:24.144516   Here we cut out the fat
str_day = x.strftime("%A") #day of the week in string format (str f), %A is the weekday option, use %a for month abbreviation, ie tues
str_date = x.strftime("%d") #numerical date in string format, %d is the date option
str_month = x.strftime("%B") #month in string format, %B is the month option, use %b for month abbreviation, ie dec
str_year = str(x.year)

date_formatted = "[" + str_time + "] " + str_day + ", " + str_month + " " + str_date +", " + str_year + ": \n" 

ap = argparse.ArgumentParser()
ap.add_argument("-i", "--input", help = "text you want to write to the my_diary.txt file")
args = vars(ap.parse_args())

print('Thanks for using the python diary app!')

if args["input"] != None:  #Only opens and writes to txt file if input is given (ie Not equal != to None)
    string1 = date_formatted + str(args["input"]).replace("_", " ") + "\n \n"
    # \n is placed to indicate End of Line

    txtfilename = "my_diary.txt"
    file1 = open( txtfilename, "a" )    #open the text file, append to it 
    file1.write(string1)
    file1.close()
    print("Your entry has been recorded!")

else:
    print("No input given, try again!")

