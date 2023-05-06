from data_gen_from_text.QA_from_text import get_response
import os 
import time
main_dir='App/data_gen_from_text/text_files/'
list_text = os.listdir(main_dir)

for file in list_text:
    f = open(main_dir+file)
    text = f.read()
    get_response(text)
    time.sleep(2)
