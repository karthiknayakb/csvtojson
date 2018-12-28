#!/usr/local/bin/python
import csv
import json
import sys
from argparse import ArgumentParser

def parseCSV(filen,pkey=None,fields=None,header=False):
    with open(filen,"r") as f:
        if header:
            fields = tuple(f.readline().strip().split(","))
        reader = csv.DictReader(f,fieldnames=fields);
        di = {}
        if pkey not in fields:
            print("Key has to be in the header/fields.")
            return None;

        for row in reader:
            temp = {}
            for i in fields:
                if i == pkey:
                    continue
                else:
                    temp[i]=row[i]
            di.update({row[pkey]:temp})
    return di

def write_csv_json(src=None,des=None,pkey=None,fields=None,header=None):
    if src and pkey:
        r = parseCSV(src,pkey=pkey,fields=fields,header=header)
        if r:
            r = json.dumps([r])
            if not des:
                des = src.split(".")[0]+".json"
            with open(des,"w") as f:
                f.write(r)
    else:
        print "The src file and primary key is required!"
        return None

def main():
    aparser = ArgumentParser()
    aparser.add_argument('-s','--source',help="csv source file path.",dest="src",required=True)
    aparser.add_argument('-d','--destination',help="json destination file path.",dest="des")
    aparser.add_argument('-k','--key',help="the primary key. This has to be present in the heading/fields.",dest="pkey",required=True)
    aparser.add_argument('-f','--fields',help="csv fields, comma seperated. This has to be used in case field is not in the CSV file.",dest="fields")
    aparser.add_argument('--header',help="True if header/fields are present in CSV file. Default is False.",dest="header")

    args = aparser.parse_args()

    src = args.src
    des = args.des
    pkey = args.pkey
    fields = args.fields
    if fields:
        fields = tuple(fields.split(","))
    header = args.header
    if header:
        header = header.lower()
        if 't' in header:
            header = True
        else:
            header = False

    write_csv_json(src=src,des=des,pkey=pkey,fields=fields,header=header)

if __name__=="__main__":
    main()
