import xlrd


path2 = r'RNA_Opentron_control.xlsx'


def getExcelSheet(path,sheet_name):
    wb = xlrd.open_workbook(path)
    layout_sheet = wb.sheet_by_name(sheet_name)
    return layout_sheet

def getValue(layout_sheet,str_to_find,offset_row=0,offset_col=1):

    indexes=f_index(layout_sheet,str_to_find)
    return layout_sheet.cell_value(indexes[0] + offset_row,indexes[1] + offset_col)

def get96plate(layout_sheet,str_to_find,offset_row=0,offset_col=1):

    indexes=f_index(layout_sheet,str_to_find)
    WellValue=[]
    well=1
    for col in range(12):
        for row in range(8):
            value=layout_sheet.cell_value(row + indexes[0] + offset_row, col + indexes[1] + offset_col)
            if value!='':
                WellValue.append([well,value])
            well+=1

    return WellValue

def f_index(layout_sheet,str_to_find):
    for row in range(layout_sheet.nrows):
        for col in range(layout_sheet.ncols):
            if str(layout_sheet.cell_value(row,col)).replace("\n"," ").replace("  "," ").split(" ") == str_to_find.replace("\n"," ").replace("  "," ").split(" "):
                return [row,col]
    print("Couldnt find " + str_to_find)
    return None

def getSequences(layout_sheet):

    sequences=[]
    well=1
    for col in range(12):
        for row in range(8):
            value=layout_sheet.cell_value(3+row,1+col)
            if value!='':
                sequences.append((well,value))
            well+=1

    return sequences

def getVolumes(layout_sheet):

    volumes=[]
    well=1
    for col in range(12):
        for row in range(8):
            value=layout_sheet.cell_value(23+row,1+col)
            if value!='':
                volumes.append((well,round(value)))
            well+=1

    return volumes

def getConcentrations(layout_sheet):

    concentrations=[]
    well=1
    for col in range(12):
        for row in range(8):
            value=layout_sheet.cell_value(1+row,1+col)
            if value!='':
                concentrations.append((well,value))
            well+=1

    return concentrations

def getConcentrations2(layout_sheet):

    concentrations=[]
    well=1
    for col in range(12):
        for row in range(8):
            value=layout_sheet.cell_value(1+row,16+col)
            if value!='':
                concentrations.append((well,value))
            well+=1

    return concentrations

#---------NT 21/09/23

def getTargetConcentrations(layout_sheet):

    TargetConcentrations=[]
    well=1
    for col in range(12):
        for row in range(8):
            value=layout_sheet.cell_value(1+row,1+col)
            if value!='':
                TargetConcentrations.append((well,value))
            well+=1

    return TargetConcentrations

def getTargetConcentrations2(layout_sheet):

    TargetConcentrations=[]
    well=1
    for col in range(12):
        for row in range(8):
            value=layout_sheet.cell_value(1+row,16+col)
            if value!='':
                TargetConcentrations.append((well,value))
            well+=1

    return TargetConcentrations

#--------- end NT 21/09/23

def getUsedWells(sequences):
    #returns all the wells in the synthesis
    usedWells=[]
    for sample in sequences:
        usedWells.append(sample[0])
    return usedWells

def splitSequences(sequences,cycle):

    ended_wells = []
    A_wells=[]
    C_wells=[]
    G_wells=[]
    U_wells=[]
    M_wells=[]
    N_wells=[]

    nucleos=['A','C','G','U','M','N']
    nucleo_arrays=[ended_wells,A_wells,C_wells,G_wells,U_wells,M_wells,N_wells]

    for nucleo in range(1,6+1):
        for sample in range(len(sequences)):
            if (cycle<=len(sequences[sample][1]) and sequences[sample][1][cycle-1]==nucleos[nucleo-1]):
                nucleo_arrays[nucleo].append(sequences[sample][0])

    for sample in range(len(sequences)):
        if cycle > len(sequences[sample][1]):
            ended_wells.append(sequences[sample][0])

    return nucleo_arrays

def getActiveWells(sequences: object, cycle: object) -> object:
    #Return all the wells in the synthesis minus the finished ones
    usedWells=getUsedWells(sequences)
    ended_wells=splitSequences(sequences,cycle)[0]
    activeWells=[]

    for well in usedWells:
        if well not in ended_wells:
            activeWells.append(well)

    return activeWells

def fromWellsToColumns(wells):
    columns=[]
    for well in wells:
        wellColumn=((well-1)//8) +1
        if wellColumn not in columns:
            columns.append(wellColumn)

    return columns

if __name__ == "__main__":
    layout_sheet=getExcelSheet(r'Normalization.xlsx',"Quantif")
    print(get96plate(layout_sheet,"Plate1 : Sample initial concentration (µM)",3,1))
    print(getValue(layout_sheet,"Normalization "))