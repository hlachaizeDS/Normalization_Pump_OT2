import datetime
import shutil
import os

def saveExcelFile():

    now=datetime.datetime.now()

    #original Excel
    original_path=r'Normalization.xlsx'

    #new folder path
    general_path = "C:\\Users\\SynthesisDNASCRIPT\\DNA Script\\SO - Synthesis Operations - Bibliothèque\\S.3 - Proto\\P7\\Quartets"
    general_path = "Excel_logs"
    folder_path=str(now.year)[2:]+ force2digits(now.month)

    # new file path
    file_path = str(now.year)[2:] + force2digits(now.month) + force2digits(now.day) + '_' + force2digits(now.hour) + "h" + force2digits(now.minute) +"_OP2Prep"

    #the file will be copied in folder path
    os.makedirs(general_path + '\\' + folder_path, exist_ok=True)

    #Copy the Excel file
    final_path=general_path + '\\' + folder_path + '\\' + file_path + '.xlsx'
    shutil.copy(original_path, final_path)

def force2digits(number):
    if number<10:
        return '0'+str(number)
    else:
        return str(number)

if __name__ == "__main__":
    # On crée la racine de notre interface
    saveExcelFile()
    #readExpID()