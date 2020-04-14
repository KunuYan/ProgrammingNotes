import csv, os

def writeInfo():
    OrganisedPath = '/home/joelly/organisedDownloads/'
    infoDict = {}
    os.chdir(OrganisedPath)
    # fieldnames = []

    fieldnames = os.listdir()
    for fieldlabel in fieldnames:
        filenames = []
        cwd = os.getcwd()
        childnode = os.path.join(cwd, fieldlabel)
        try:
            os.chdir(childnode)
        except FileNotFoundError:
            continue
        for filename in os.listdir():
            filenames.append(filename)
        infoDict[fieldlabel] = filenames
        os.chdir('..')


    # write into csv file
    with open('/home/joelly/organisedDownloads/organised data/OrganisedD.csv', 'w') as OF:
        OFwritter = csv.writer(OF)
        OFwritter.writerow(fieldnames)
        for key in infoDict.keys():
            if infoDict[key]:
                OFwritter.writerow(infoDict[key])

writeInfo()