import csv
def read_flie():
    with open(r"rio2016.csv" , newline= "") as f :
        data = f.read()
        print(data)
    

def read_csv():
    with open(r"rio2016.csv" , newline= "") as f :
        data = csv.reader(f)
        print(data)
        for row in data :
            print(f'{row}')


def read_csv_tab():
    with open(r"rio2016tab.txt" , newline= "") as f :
        data = csv.reader(f,delimiter ="\t")
        print(data)
        for row in data :
            print(f'{row[0]:25}  : {row[1]:2} {row[2]:2}  {row[3]:2}')



def read_csv_header():
    with open(r"rio2016_header_column.csv" , newline= "") as f :
        data = csv.DictReader(f)
        print(data)
        print(data.fieldnames)
        for row in data :
            # print(f'{row["country"]} , {row["gold"]}')
            print(f'{row}')


read_csv_header()