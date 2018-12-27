import csv
import json
def parseCSV(filen,pkey=None,fields=None):
    f=open(filen,"r");
    #title = f.readlines();
    reader = csv.DictReader(f,fieldnames=fields);
    #f.close();
    di = {}
    if pkey not in fields:
        return None;

    for row in reader:
        temp = {}
        for i in fields:
            if i == pkey:
                continue
            else:
                temp[i]=row[i]
        di.update({row[pkey]:temp})
        #di[row[pkey]]=temp
        #print temp

    return di

def main():
    r = parseCSV("./f1.csv",pkey='k',fields=('k','a','b','c'))
    r = json.dumps([r])
    with open("./parsedCSV.json","w") as f:
        f.write(r)
    print r

if __name__=="__main__":
    main()
