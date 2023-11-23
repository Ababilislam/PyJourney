import zipfile

with zipfile.ZipFile("data.zip",'r') as zipobj:
    print(zipobj.namelist())
    # zip_info = zipobj.getinfo(zipobj+'/new_file.txt')
    # print(zip_info.date_time)

###########writing zip

file_list = ['file_create_append_delete.py', 'file_open.py', 'new_file.txt', 'temporary_file.py', 'tex.txt']

with zipfile.ZipFile('new_zip.zip','w') as newzip:
    for name in file_list:
        newzip.write(name)