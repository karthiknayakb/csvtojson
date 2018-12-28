# csvtojson

This simple commandline tool will convert any csv file to a json file (dictionary).
The parseCSV function takes filename(path to csv -> string), pkey(key -> string), fields(fieldnames of csv -> tuple).

## Getting Started

For quick check, clone the repository and execute below command. You should get f1.json file in same directory.

```
csvtojson.py -s f1.csv -k k --header true
```
* f1.csv is sample csv file.
* primary key (-k) is "k".
* header true indicates, header fields are present in csv.

## Usage

```
csvtojson.py [-h] -s SRC [-d DES] -k PKEY [-f FIELDS] [--header HEADER]
```

## Options

```
-h, --help            show this help message and exit
-s SRC, --source SRC  csv source file path.
-d DES, --destination DES
                      json destination file path.
-k PKEY, --key PKEY   the primary key. This has to be present in the
                      heading/fields.
-f FIELDS, --fields FIELDS
                      csv fields, comma seperated. This has to be used in
                      case field is not in the CSV file.
--header HEADER       True if header/fields are present in CSV file. Default
                      is False.
```
