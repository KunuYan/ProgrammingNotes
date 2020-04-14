import subprocess as sp
import shutil, os, src, sys

# define all file extentions
commonTypes = {
    'audioFormats' : ['.aif', '.cda', '.mid', '.midi', '.mp3', '.mpa', '.ogg', '.wav', '.wma', '.wpl'],
    'cFileFormats' : ['.7z', '.arj', '.deb', '.pkg', '.rar', '.rpm', '.tar.gz', '.z', '.zip'],
    'diskNmediaFormats' : ['.bin', '.dmg', '.iso', '.toast', '.vcd'],
    'dbFormats' : ['.csv', '.dat', '.db', '.dbf', '.log', '.mdb', '.sav', '.sql', '.tar', '.xml'],
    'execFormats' : ['.apk', '.bat', '.bin', '.cgi', '.pl', '.com', '.exe', '.gadget', '.jar', '.py', '.wsf'],
    'fontFormats' : ['.fnt', '.fon', '.otf', '.ttf'],
    'imageFormats' : ['.ai', '.bmp', '.gif', '.ico', '.jpeg', '.jpg', '.png', '.ps', '.psd', '.svg', '.tif', '.tiff'],
    'webFormats' : ['.asp', '.aspx', '.cer', '.cfm', '.cgi', '.pl', '.css', '.htm', '.html', '.js', '.jsp', '.part', '.php', '.py', '.rss', '.xhtml'],
    'presFormats' : ['.key', '.odp', '.pps', '.ppt', '.pptx'],
    'programlangFormats' : ['.c', '.class', '.cpp', '.cs', '.h', '.java', '.sh', '.swift', '.vb'],
    'spreadsheetFormats' : ['.ods', '.xlr', '.xls', '.xlsx'],
    'sysFormats' : ['.bak', '.cab', '.cfg', '.cpl', '.cur', '.dll', '.dmp', '.drv', '.icns', '.ico', '.ini', '.lnk', '.msi', '.sys', '.tmp'],
    'videoFormats' : ['.3g2', '.3gp', '.avi', '.flv', '.h264', '.m4v', '.mkv', '.mov', '.mp4', '.mpg', '.rm', '.swf', '.vob', '.wmv'],
    'fileFormats' : ['.doc', '.odt', '.pdf', '.rtf', '.tex', '.txt', '.wks', '.wps', '.wpd']
}

assocFolders = {
        'audioFormats' : [src.organisedFolder['audioFormats']],
        'cFileFormats' : [src.organisedFolder['cFileFormats']],
        'diskNmediaFormats' : [src.organisedFolder['diskNmediaFormats']],
        'dbFormats' : [src.organisedFolder['dbFormats']],
        'execFormats' : [src.organisedFolder['execFormats']],
        'fontFormats' : [src.organisedFolder['fontFormats']],
        'imageFormats' : [src.organisedFolder['imageFormats']],
        'webFormats' : [src.organisedFolder['webFormats']],
        'presFormats' : [src.organisedFolder['presFormats']],
        'programlangFormats' : [src.organisedFolder['programlangFormats']],
        'spreadsheetFormats' : [src.organisedFolder['spreadsheetFormats']],
        'sysFormats' : [src.organisedFolder['sysFormats']],
        'videoFormats' : [src.organisedFolder['videoFormats']],
        'fileFormats' : [src.organisedFolder['fileFormats']],
        'other': [src.organisedFolder['other']]
    }

def identifieFormat(commonTypes, extension, fileInfo):
    try:
        # loop through commoTypes keys
        for key in commonTypes:
            # check if extension in commoTypes[key]
            if extension in commonTypes[key]:
                # if yes append tuple of file full path and name to associate folder list
                assocFolders[key].append(fileInfo)   
        assocFolders['other'].append(fileInfo)
    except:
        sys.exit(1)

# parse through downloads, if file with extension found: save it's full path
def folderParser():
    try:
        src.identifieOS()
        # loop trough directory
        os.chdir(src.donwloadPath)
        for filename in os.listdir():
            fullPath = str(os.path.abspath(filename))
            # put fullpath into a tuple with name of file
            fileInfo = (fullPath, filename)
            # get the extension
            extension = os.path.splitext(fullPath)[1]
            if extension == '.gz':
                extension = '.tar.gz'
            # identifie extention type
            identifieFormat(commonTypes, extension, fileInfo)
    except:
        sys.exit(2)

# move file with specific type of extentions to their corrresponding folder
def fileMover(assocFolders, donwloadPath):
    try:
        for key in assocFolders:
            for filelement in assocFolders[key]:
                if filelement != assocFolders[key][0]:
                    fileFullPath = assocFolders[key][assocFolders[key].index(filelement)][0]
                    shutil.move(fileFullPath, assocFolders[key][0])
    except:
        sys.exit(3)

def main():
    try:
        folderParser()
        fileMover(assocFolders, src.donwloadPath)
    except:
        print("An error has occured, check exit code to see where")
        print("exit codes: 1=identifieFormat, 2=folderParser, 3=filemover")

if __name__ == "__main__":
    main()   