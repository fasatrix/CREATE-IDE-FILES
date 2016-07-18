import re

NSN =[]

#The content of this file should contain the pact exception (missing students from ENROL) raised in PaCT under manage/Updates after importing the old IDE files. Cut and paste the content of the page(list of student-NSN) into this file
fname = '/home/ubuntu/workspace/ex50/data/LEFT_SCHOOL_NSN'

#The below file should contain the  students list was eated with the create_ide_for_missing_students.py script
school_1279 = '/home/ubuntu/workspace/ex50/data/3276.csv'

#OUTPUT
output = '/home/ubuntu/workspace/ex50/data/newIDE_3276.csv'

f = open(fname)

for line in f.readlines():
    lines = line.split(') ')
for line in lines:
    m = re.search('NSN:(.+)[0-9]+', line)
    if m:
        NSN.append(m.group(1))
        
with open(school_1279) as school, open(output, 'w') as newfile:
    for line in school:
        if not any(nsn in line for nsn in NSN):
            newfile.write(line)
        
