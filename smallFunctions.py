
def fromWellsToColumns(wells):
    columns=[]
    for well in wells:
        wellColumn=((well-1)//8) +1
        if wellColumn not in columns:
            columns.append(wellColumn)

    return columns

def getColumn(wells):
    wellColumn = ((wells-1)//8) +1
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
    print(wellnb2str(96))
    #print(is_list_empty(list))
    #print(list.index([5,8]))
