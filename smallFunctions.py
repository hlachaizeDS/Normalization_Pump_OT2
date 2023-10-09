
def fromWellsToColumns(wells):
    columns=[]
    for well in wells:
        wellColumn=((well-1)//8) +1
        if wellColumn not in columns:
            columns.append(wellColumn)

    return columns

def firstValuesOfColumns(WellValue_list):
    ''' WellValue_list is a list of [well_number,value]
    returns a list of 12, containing the value for the first item in the column (0 if doesn't exist)'''

    first_values=[0]*12
    for WellValue in WellValue_list:
        well=WellValue[0]
        if (well - 1) % 8 == 0:
            first_values[getColumn(well)-1]=WellValue[1]
    return first_values

def getColumn(well):
    wellColumn = ((well-1)//8) +1
    return wellColumn

def is_list_empty(list):
    count = 0
    for i in range(len(list)):
        if list[i] != []:
            return False
    return True

def wellnb2str(well_nb):
    well_col=((well_nb-1)//8) +1
    well_row=((well_nb-1)%8) +1

    return chr(64+well_row) + str(well_col)

def inter_columns(list_of_list_of_columns):
    '''Returns a list containing all the columns appearing at least in one of the column lists, in numeric order'''
    cols=[]
    for col in range(12):
        for column_list in list_of_list_of_columns:
            if col+1 in column_list:
                cols.append(col+1)
                break
    return cols

if __name__ == "__main__":
    # usedWells = [1, 5, 9, 11, 36, 45]
    # usedWellsEven = []
    # usedWellsOdd = []
    # for well in usedWells:
    #     if getColumn(well) % 2 == 0:
    #         usedWellsEven.append(well)
    #     else:
    #         usedWellsOdd.append(well)
    # print(usedWellsEven)
    # print(usedWellsOdd)
    #print(wellnb2str(96))
    #print(is_list_empty(list))
    #print(list.index([5,8]))
    print(inter_columns([[1,2,3,4,5],[2,3,4],[8,9,10,11,12,13]]))
