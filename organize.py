import os

extensions = {
    'DOCS': ['.txt', '.pdf', '.ppt', '.pptx', '.xls', '.xlsx', '.doc', '.docx'],
    'PGMS': ['.h', '.cpp', '.c', '.java', '.cs', '.py', '.js', '.css'],
    'VIDS': ['.mp4', '.mkv', '.mov', '.avi', '.flv'],
    'AUD' : ['.mp3', '.wav', '.ogg', '.aac'],
    'PICT': ['.png', '.jpg', '.gif'],
    'COMP' : ['.tar', 'zip', 'rar']
}

# create folders for different file extensions
os.popen('mkdir ./DOCUMENTS ./PROGRAMS ./VIDEOS ./AUDIOS ./PICTURES')

# function to organize the files into their respective folders
def organize(item):
    ext = os.path.splitext(item)

    if ext[1] in extensions['DOCS']:
        os.popen('mv ' + item + ' DOCUMENTS/' + item)
    elif ext[1] in extensions['PGMS']:
        os.popen('mv ' + item + ' PROGRAMS/' + item)
    elif ext[1] in extensions['VIDS']:
        os.popen('mv ' + item + ' VIDEOS/' + item)
    elif ext[1] in extensions['AUD']:
        os.popen('mv ' + item + ' AUDIOS/' + item)
    elif ext[1] in extensions['PICT']:
        os.popen('mv ' + item + ' PICTURES/' + item)

items = os.listdir('.')

for item in items:
    if os.path.isfile(item) and item !=  'organize.py':
        organize(item)
