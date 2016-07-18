import re

def remove_long_names(line,pos):
        name = line.split(',')
        fname = name[pos]
        ffname = fname.split()
        name[pos] = ffname[0]
        name = ','.join (name)
        return(name)

def create_IDE_file(line, personID, IDE,i):
        number_s = (personID.split(','))
        s_id = number_s[1]
        prefix = number_s[0]
        line = line.split(',')
        a = prefix + str((int(s_id)+i)) +','+line[0]+','+','+line[19].strip()+','+','+line[1]+','+line[2]+','+line[1]+','+line[3]+','+line[4]+','+'Student'+','+','+','+','+','+'Y'+line[15]
        return IDE.append(a)
        
def create_IDE_FINAL(lines,output, IDE):
        NSN=[]
        for line in lines:          
                m = re.search('NSN:(.+)[0-9]+', line)
                if m:
                   NSN.append(m.group(1))
        with open(output, 'w') as newfile:
                newfile.write(IDE[0]+'\n')
                for linea in IDE:
                   if any(nsn in linea for nsn in NSN):
                        newfile.write(remove_long_names(linea,7)+'\n')
                return newfile