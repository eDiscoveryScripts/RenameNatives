# This is a sample Python script.
import csv
import os
# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.

#input and output
input_loadfile = "Salt-v-Pepper (UK date format).dat"
output_loadfile = 'loadfile_modified.dat'

#parameters
delimiter = "¶"
quotechar = "þ"
separator = "-"
native_filepath_field = 'NativeLink'
confidentiality_field = 'CONFIDENTIALITY'
#if False only the loadfile will be updated
rename_files = True

def modify_loadfile(loadfilepath):

    #set counter
    numberofnativefiles=0
    numberofrenamedfiles=0
    numberoffailedfiles=0
    numberofnorename=0
    numberofalreadyrenamed=0

    #open loadfile if exist
    if os.path.exists(loadfilepath):
        with open(loadfilepath, newline='', encoding='utf-8') as loadfile:
            loadfilereader = csv.DictReader(loadfile, delimiter=delimiter, quotechar=quotechar)
            #open new loadfile
            with open(output_loadfile, 'w', newline='', encoding='utf-8') as new_loadfile:
                loadfilewriter = csv.DictWriter(new_loadfile, fieldnames=loadfilereader.fieldnames, delimiter=delimiter, quotechar=quotechar, quoting=csv.QUOTE_ALL)
                loadfilewriter.writeheader()
                #iterate over loadfile
                for row in loadfilereader:
                    new_row=row.copy()
                    if row[native_filepath_field]!="":
                        numberofnativefiles=numberofnativefiles+1
                        if row[confidentiality_field]!= "":
                            #modify new row
                            new_row[native_filepath_field]=new_row[native_filepath_field].replace(".", separator + new_row[confidentiality_field] + ".")
                            #obtain basepath based on loadfile location
                            basepath=os.path.abspath(os.path.join(loadfilepath, os.pardir))
                            #update file pathing for renaming
                            nativefile_path=os.path.join(basepath, row[native_filepath_field].replace("/", os.sep).replace("\\", os.sep))
                            new_nativefile_path=os.path.join(basepath, new_row[native_filepath_field].replace("/", os.sep).replace("\\", os.sep))

                            #check if native file exists
                            if os.path.exists(nativefile_path):
                                try:
                                    #check if tryout or actual re-name required.
                                    if rename_files:
                                        os.rename(nativefile_path, new_nativefile_path)
                                except (OSError, IOError):
                                    #do not update line, if error
                                    print("Error renaming file: "+nativefile_path)
                                    new_row = row.copy()
                                    numberofrenamedfiles=numberofrenamedfiles+1
                                else:
                                    numberofrenamedfiles=numberofrenamedfiles+1
                                    print("File successfully renamed: "+nativefile_path)
                            else:
                                #check if files have already been renamed
                                if os.path.exists(new_nativefile_path):
                                    print("File already renamed: "+nativefile_path)
                                    numberofalreadyrenamed=numberofalreadyrenamed+1
                                else:
                                    #do not update line, if file does not exist or has not been renamed already
                                    print("File does not exist: "+nativefile_path)
                                    numberoffailedfiles=numberoffailedfiles+1
                                    new_row = row.copy()
                        else:
                            numberofnorename=numberofnorename+1
                    #add line to modified loadfile
                    loadfilewriter.writerow(new_row)

        if rename_files==False:
            print("Only the loadfile has been updates. Numbers are just a forecast")

        print("Total Natives: {}".format(numberofnativefiles))
        print("Successfully rename: {}".format(numberofrenamedfiles))
        print("Failed to rename: {}".format(numberoffailedfiles))
        print("No renaming required for: {}".format(numberofnorename))
        print("Already renamed: {}".format(numberofalreadyrenamed))
    else:
        print("loadfile does not exist")
# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    modify_loadfile(input_loadfile)


