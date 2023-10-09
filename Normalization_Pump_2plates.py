from excelRead import *
from excel_save import *
from smallFunctions import *
from commands import *
from Buffer import *
import time

PROTOCOL_PATH = 'a_Normalization.py'
EXCEL_PATH = r'Normalization.xlsx'

protocolFile = open(PROTOCOL_PATH, "w")

#DEFINE USED LABWARES
#Pipets
pipet300 = "p300"
pipet20="p20"

#Plates
mother_plate1="mother_plate1"
plate_to_normalize1="plate_to_normalize1"
op2_plate1="op2_plate1"
mother_plate2="mother_plate2"
plate_to_normalize2="plate_to_normalize2"
op2_plate2="op2_plate2"
#Tips
tips_300 = 'tiprack_300'
tiprack_20_plate1 = 'tiprack_20_plate1'
tiprack_20_plate2 = 'tiprack_20_plate2'
#Reservoirs
LadderReservoir = "LadderReservoir"


HEADER_PATH = 'Normalization_header_2plates.py'
header_file = open(HEADER_PATH, "r")
protocolFile.write(header_file.read() + "\n")
header_file.close()

layout_sheet = getExcelSheet(EXCEL_PATH,"Quantif")

plate_type_on_spacer_1 = getValue(layout_sheet,"Plate1 type (for normalized samples)")
plate_type_on_spacer_2 = getValue(layout_sheet,"Plate2  type (for normalized samples)")


if plate_type_on_spacer_1=="Greiner (half/full area)":
    protocolFile.write("    del protocol.deck['4']\n")
    protocolFile.write("    plate_to_normalize1 = protocol.load_labware('greiner_96well_full_area_350ul_onspacer', 4)\n")
    protocolFile.write("\n\n")

if plate_type_on_spacer_2=="Greiner (half/full area)":
    protocolFile.write("    del protocol.deck['5']\n")
    protocolFile.write("    plate_to_normalize2 = protocol.load_labware('greiner_96well_full_area_350ul_onspacer', 5)\n")
    protocolFile.write("\n\n")



op2_plates=[op2_plate1,op2_plate2]
mother_plates=[mother_plate1,mother_plate2]
plates_to_normalize=[plate_to_normalize1,plate_to_normalize2]

tips_20=[tiprack_20_plate1,tiprack_20_plate2]

column_offset_by_plate=[0,16]

nb_of_plates=int(getValue(layout_sheet,"Nb of plates"))

for plate in range(nb_of_plates):

    # transfer from mother plate to norma plate
    ASP_FROM_BOTTOM = 1.3
    ASP_FLOW_RATE = 1
    DISP_FROM_BOTTOM = 0
    DISP_FLOW_RATE = 1
    MIX_FLOW_RATE = 3

    #transfer from Norma plate to OP2 plate
    ASP_FROM_BOTTOM_OP2 = 0
    ASP_FLOW_RATE_OP2 = 1
    DISP_FROM_BOTTOM_OP2 = 0
    DISP_FLOW_RATE_OP2 = 1
    MIX_FLOW_RATE_OP2 = 3

    #Get All parameters from excel file

    NORMALIZATION = getValue(layout_sheet, "Normalization ")
    TRANSFER_OF_SAMPLES_FOR_NORMA = getValue(layout_sheet, "Transfer of samples to be normalized")
    OP2_PLATE = getValue(layout_sheet, "Preparation of OP2 plate")

    concentrations = get96plate(layout_sheet, "Plate1 : Sample initial concentration (µM)", offset_row=3,offset_col=1 + column_offset_by_plate[plate])
    concentrations_usedWells = [WellConc[0] for WellConc in concentrations]
    concentrations_usedColumns = fromWellsToColumns(concentrations_usedWells)

    volumes_to_normalize = get96plate(layout_sheet, "Plate1 : Volume of sample to be normalized (µl)", offset_row=3,offset_col=1 + column_offset_by_plate[plate])
    volumes_to_normalize_usedWells = [WellVol[0] for WellVol in volumes_to_normalize]
    volumes_to_normalize_usedColumns = fromWellsToColumns(volumes_to_normalize_usedWells)
    volumes_to_normalize_by_col = firstValuesOfColumns(volumes_to_normalize)
    print(volumes_to_normalize_by_col)

    target_concentrations = get96plate(layout_sheet, "Plate1 : Target concentration (µM)", offset_row=3,offset_col=1 + column_offset_by_plate[plate])
    target_concentrations_usedWells = [WellConc[0] for WellConc in target_concentrations]
    target_concentrations_usedColumns = fromWellsToColumns(target_concentrations_usedWells)
    target_concentrations_dict = {wellConc[0]:wellConc[1] for wellConc in target_concentrations }

    volumes_for_OP2 = get96plate(layout_sheet, "Plate1 : Volume of normalized sample to be transfered (µl)", offset_row=3,offset_col=1 + column_offset_by_plate[plate])
    volumes_for_OP2_usedWells = [WellVol[0] for WellVol in volumes_for_OP2]
    volumes_for_OP2_usedColumns = fromWellsToColumns(volumes_for_OP2_usedWells)
    volumes_for_OP2_by_col = firstValuesOfColumns(volumes_for_OP2)

    ladder_volumes = get96plate(layout_sheet, "Plate1 : Volume of ladder (µl)", offset_row=3,offset_col=1 + column_offset_by_plate[plate])
    ladder_usedWells = [WellVol[0] for WellVol in ladder_volumes]
    ladder_usedColumns = fromWellsToColumns(ladder_usedWells)
    ladder_vol_by_col = firstValuesOfColumns(ladder_volumes)


    print("Plate " + str(plate + 1))
    print(concentrations_usedColumns)

    if OP2_PLATE=="Yes" :

        #Add ladders to OP2 plate
        addBuffer_DiffVolsCols(protocolFile,pipet300,ladder_usedWells,op2_plates[plate],LADDERS,ladder_vol_by_col)


    for col in inter_columns([concentrations_usedColumns,volumes_for_OP2_usedColumns]):

        if (NORMALIZATION=="Yes" and TRANSFER_OF_SAMPLES_FOR_NORMA == "Yes" and volumes_to_normalize_by_col[col-1]!=0) or (OP2_PLATE == "Yes" and volumes_for_OP2_by_col[col-1]!=0):
            pickup_tips_multi_WL(protocolFile, pipet20, tips_20[plate], col)

        if (NORMALIZATION=="Yes" and TRANSFER_OF_SAMPLES_FOR_NORMA == "Yes" and volumes_to_normalize_by_col[col-1]!=0) :

            aspirate_WL(protocolFile, pipet20,
                        colOfLabware(mother_plates[plate], col, 96) + ".bottom(" + str(ASP_FROM_BOTTOM) + ")", \
                        volumes_to_normalize_by_col[col-1], ASP_FLOW_RATE)
            dispense_WL(protocolFile, pipet20,
                        colOfLabware(plates_to_normalize[plate], col, 96) + ".bottom(" + str(DISP_FROM_BOTTOM) + ")", \
                        volumes_to_normalize_by_col[col-1], DISP_FLOW_RATE)

        if NORMALIZATION=="Yes":

            for wellConc in concentrations:
                well=wellConc[0]
                if getColumn(well) == col:
                    conc = wellConc[1]
                    conc_norm = target_concentrations_dict[well]
                    volume_norm = volumes_to_normalize_by_col[col-1]
                    vol_to_add = int((volume_norm * conc) / conc_norm) - volume_norm
                    if vol_to_add <= 0:
                        print("Warning, concentration not high enough in " + wellnb2str(well) + ".")
                    elif vol_to_add <= 3:
                        print("Warning, volume to dispense < 4ul in " + wellnb2str(well) + ".")
                    else:
                        move_to_WL(protocolFile, pipet300,plates_to_normalize[plate] + ".wells()[" + str(
                                       well - 1) + "].center().move(types.Point(x=-2.5,y=84,z=8))")
                        # pause_WL(protocolFile)
                        dispense(protocolFile, vol_to_add)

        if OP2_PLATE=="Yes" and volumes_for_OP2_by_col[col-1]!=0 :

            mix_WL(protocolFile,pipet20,3,15,colOfLabware(plates_to_normalize[plate], col, 96) + ".bottom(" + str(ASP_FROM_BOTTOM_OP2) +")", MIX_FLOW_RATE)

            aspirate_WL(protocolFile, pipet20,
                        colOfLabware(plates_to_normalize[plate], col, 96) + ".bottom(" + str(ASP_FROM_BOTTOM_OP2) + ")", \
                        volumes_for_OP2_by_col[col-1], ASP_FLOW_RATE_OP2)
            dispense_WL(protocolFile, pipet20,
                        colOfLabware(op2_plates[plate], col, 96) + ".bottom(" + str(DISP_FROM_BOTTOM_OP2) + ")", \
                        volumes_for_OP2_by_col[col-1], DISP_FLOW_RATE_OP2)

            mix_WL(protocolFile, pipet20, 3, 15,
                   colOfLabware(op2_plates[plate], col, 96) + ".bottom(" + str(DISP_FROM_BOTTOM_OP2) + ")", \
                   MIX_FLOW_RATE)

        if (NORMALIZATION=="Yes" and TRANSFER_OF_SAMPLES_FOR_NORMA == "Yes" and volumes_to_normalize_by_col[col-1]!=0) or (OP2_PLATE == "Yes" and volumes_for_OP2_by_col[col-1]!=0):
            return_WL(protocolFile, pipet20)

#if all went well, we save the excel file
saveExcelFile()
