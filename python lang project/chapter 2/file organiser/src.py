import os


winDPath = r"C:\Users\male-\Downloads"
linuxDPath = '/home/joelly/Downloads/'
organisedFolderW = {
    'audioFormats' : r'C:\Users\male-\Organised Downloads\audio',
    'cFileFormats' : r'C:\Users\male-\Organised Downloads\compressed',
    'diskNmediaFormats' : r'C:\Users\male-\Organised Downloads\disk and media',
    'dbFormats' : r'C:\Users\male-\Organised Downloads\data and database',
    'execFormats' : r'C:\Users\male-\Organised Downloads\executables',
    'fontFormats' : r'C:\Users\male-\Organised Downloads\fonts',
    'imageFormats' : r'C:\Users\male-\Organised Downloads\images',
    'webFormats' : r'C:\Users\male-\Organised Downloads\internet related',
    'presFormats' : r'C:\Users\male-\Organised Downloads\presentations',
    'programlangFormats' : r'C:\Users\male-\Organised Downloads\programming',
    'spreadsheetFormats' : r'C:\Users\male-\Organised Downloads\spreadsheet',
    'sysFormats' : r'C:\Users\male-\Organised Downloads\sys',
    'videoFormats' : r'C:\Users\male-\Organised Downloads\video',
    'fileFormats' : r'C:\Users\male-\Organised Downloads\text files',
    'other': r'C:\Users\male-\Organised Downloads\others'
}

organisedFolderL = {
    'audioFormats' : [r'C:\Users\male-\Organised Downloads\audio'],
    'cFileFormats' : [r'C:\Users\male-\Organised Downloads\compressed'],
    'diskNmediaFormats' : [r'C:\Users\male-\Organised Downloads\disk and media'],
    'dbFormats' : [r'C:\Users\male-\Organised Downloads\data and database'],
    'execFormats' : [r'C:\Users\male-\Organised Downloads\executables'],
    'fontFormats' : [r'C:\Users\male-\Organised Downloads\fonts'],
    'imageFormats' : [r'C:\Users\male-\Organised Downloads\images'],
    'webFormats' : [r'C:\Users\male-\Organised Downloads\internet related'],
    'presFormats' : [r'C:\Users\male-\Organised Downloads\presentations'],
    'programlangFormats' : [r'C:\Users\male-\Organised Downloads\programming'],
    'spreadsheetFormats' : [r'C:\Users\male-\Organised Downloads\spreadsheet'],
    'sysFormats' : [r'C:\Users\male-\Organised Downloads\sys'],
    'videoFormats' : [r'C:\Users\male-\Organised Downloads\video'],
    'fileFormats' : [r'C:\Users\male-\Organised Downloads\text files'],
    'other': [r'C:\Users\male-\Organised Downloads\others']
}
# check what system user is on
def identifieOS():
    currentOs = os.name
    if currentOs == 'nt':
        donwloadPath = winDPath
        organisedFolder = organisedFolderW
    elif currentOs == 'posix':
        donwloadPath = linuxDPath
        organisedFolder = organisedFolderL
    return donwloadPath, organisedFolder

donwloadPath, organisedFolder = identifieOS()