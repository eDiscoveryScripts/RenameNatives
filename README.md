# RenameNatives
This python script adds the confidentiality branding to your natives files that are linked in your concordance load file and updates the reference in the load file.  

Create a copy of the NATIVE folder of your production prior running the script. Curently only works for utf-8 encoded loadfiles. The script might not work, if your native file contains multiple dots (".").  
  
### #input and output  
input_loadfile = "Salt-v-Pepper (UK date format).dat" #specify the input filename of your loadfile   
output_loadfile = 'loadfile_modified.dat' #name of the copy of the loadfile that is created  
  
### #parameters  
delimiter = "¶"  
quotechar = "þ"  
separator = "-" #specifies the separator for the branding tag   
native_filepath_field = 'NativeLink' #field that points to the natives in your loadfile  
confidentiality_field = 'CONFIDENTIALITY' #field that contains tthe confidentiality branding in your loadfile  
rename_files = True #if False only the loadfile will be updated and files will not be renamed  
