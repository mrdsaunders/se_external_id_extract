import csv


# Written by    David Saunders 
# Created       19-05-2021

with open('output/extids.csv', newline='', mode='w') as f:
    log_writer = csv.writer(f, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
    log_writer.writerow(['ID','Type','DOI','Reporting date','Publication date','Title','Journal','External identifiers','pubmed', 'pmc','isidoc'])
    

with open('input/pubs.csv', encoding='Latin-1') as csvfile:
            readCSV = csv.reader(csvfile, delimiter=',')
            next (readCSV)
            for row in readCSV:
                extids = id = title = doi = pubmed = pmc = isidoc = None
                id = row[0]
                title = row[69]
                journal = row[36]
                type = row[1]
                doi = row[18]
                extids = row[23]
                repdate = row[2]
                pubdate = row[56]

                idsplit = extids.split(", ")
                for extid in idsplit:
                    if extid[:7]== 'pubmed:':
                        pubmed = extid[7:]
                    if extid[:4]== 'pmc:':
                        pmc = extid[4:]
                    if extid[:7]== 'isidoc:':
                        isidoc = extid[7:]



                print(id,type,doi,repdate,pubdate,title,journal,extids,pubmed,pmc,isidoc)
                with open('output/extids.csv', newline='',mode='a') as f:
                    log_writer = csv.writer(f, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
                    try:
                        log_writer.writerow([id,type,doi,repdate,pubdate,title,journal,extids,pubmed,pmc,isidoc])  
                    except:
                        log_writer.writerow(['Writing error'])
