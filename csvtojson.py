import csv
import json
def parseCSV(filen,pkey=None,fields=None,header=False):
    with open(filen,"r") as f:
        if header:
            fields = tuple(f.readline().strip().split(","))
            print fields
        reader = csv.DictReader(f,fieldnames=fields);
        di = {}
        if pkey not in fields:
            print("Key has to be in the header/fields.")
            return None;

        for row in reader:
            temp = {}
            print row
            for i in fields:
                if i == pkey:
                    continue
                else:
                    temp[i]=row[i]
            di.update({row[pkey]:temp})
    return di

def main():
    r = parseCSV("./f1.csv",pkey='k2',header=True)
    r = json.dumps([r])
    with open("./parsedCSV.json","w") as f:
        f.write(r)

if __name__=="__main__":
    main()
