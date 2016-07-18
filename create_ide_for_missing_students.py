import re
from library import remove_long_names, create_IDE_file, create_IDE_FINAL

# THIS SCRIPT CREATES AN IDE FILE WITH STUDENTS THAT ARE MISSING IN PACT/TWA AFTER A NEW ENROL REFRESH

#INPUT FILES - the below input files should be changed each time you are trying to create an IDE for a NEW school
fi_enrol = '/home/ubuntu/workspace/ex50/data/input_enrol.txt' # the content of this file comes directly from django/notifications/import results/ENROL of target school - cut and paste is content into this file
Missing_NSN = '/home/ubuntu/workspace/ex50/data/Missing_NSN' #the content of this file comes from the pact exception raised in PaCT under manage/Updates after importing the old IDE files. Cut and paste the content of the page(list of student-NSN) into this file

#THE FOLLOWING PARAMETER(s) WILL HAVE TO BE POPULATED WITH LAST VALUE(+1) OF THE "mlepSmsPersonId" FIELD ( (Unique identifier) THAT CAN BE FOUND IN THE YOUR ORIGINAL IDE FILE - DO NOT FORGET TO SEPARATE THE NUMBER(s) FROM THE WORDS WITH A COMMA
personID = 'Otari,12'

#OUTPUT FILES
output = '/home/ubuntu/workspace/ex50/data/FINAL_IDE.txt' # call this file whatever you like - it will contain the final output which is correctly formatted IDE records for each student (NSN) listed in the file above (Missing_NSN 



#INITIALIZATION
heather = 'mlepSmsPersonId,mlepStudentNSN,mlepUsername,mlepFirstAttending,mlepLastAttendance,mlepFirstName,mlepLastName,mlepPreferredName,mlepDOB,mlepGender,mlepRole,mlepAssociatedNSN,mlepEmail,mlepOrganisation,mlepGroupMembership,mlepHomeGroup'
output_enrol_after_clean = []
IDE = []
i = 0

#TIDY UP ENROL RAW FILE
f = open(fi_enrol)
for line in f.readlines():
    output_enrol_after_clean = line.split(', ')

#CREATE A TEMPORARY IDE FILE FROM THE ENROL STUDENT LIST 
IDE.append(heather)
for line in output_enrol_after_clean: 
        if line:
            create_IDE_file(line,personID, IDE, i)
            i+=1

#CREATE FINAL IDE FILE CONTAINING ONLY STUDENTS THAT ARE CURRENTLY MISSING IN PACT 
f_NSN = open(Missing_NSN)
with open(Missing_NSN) as f:
       if len(f.readlines()) == 1:
            for line in f_NSN.readlines():
                lines = line.split(') ')
            create_IDE_FINAL(lines,output,IDE)
       else:
            lines = f_NSN.readlines()
            create_IDE_FINAL(lines,output,IDE)