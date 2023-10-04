from excelRead import *
from smallFunctions import *
from commands import *
from Buffer import *
import time
from Steps_And_Parameters import *

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

if type_of_plate_on_spacer==2:
    protocolFile.write("    del protocol.deck['4']\n")
    protocolFile.write("    del protocol.deck['5']\n")
    protocolFile.write("    plate_to_normalize1 = protocol.load_labware('greiner_96well_full_area_350ul_onspacer', 4)\n")
    protocolFile.write("    plate_to_normalize2 = protocol.load_labware('greiner_96well_full_area_350ul_onspacer', 5)\n")
    protocolFile.write("\n\n")

excel_sheet = getExcelSheet(EXCEL_PATH,"Quantif")
#excel_sheet_norm = getExcelSheet(EXCEL_PATH,"Normalization")

op2_plates=[op2_plate1,op2_plate2]
mother_plates=[mother_plate1,mother_plate2]
plates_to_normalize=[plate_to_normalize1,plate_to_normalize2]

tips_20=[tiprack_20_plate1,tiprack_20_plate2]

for plate in range(2):

    if plate==0:
        concentrations=getConcentrations(excel_sheet)
    elif plate==1:
        concentrations = getConcentrations2(excel_sheet)

#----- NT 20/09/23 ----
# Besoin de remettre "for plate...."?

#for plate in range(2):

    #if plate == 0:
        #TargetConcentrations = getTargetConcentrations(excel_sheet_norm)
    #elif plate == 1:
        #TargetConcentrations = getTargetConcentrations2(excel_sheet_norm)

 # ----- end NT 20/09/23 ----

    used_wells=[wellConc[0] for wellConc in concentrations]
    used_columns=fromWellsToColumns(used_wells)
    print("Plate " + str(plate+1))
    print(used_columns)

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

    if OP2_PLATE :

        #Add ladders to OP2 plate
        addBuffer(protocolFile,pipet300,used_wells,op2_plates[plate],LADDERS,volume_ladders)

    for col in used_columns:

        if transfer_of_oligos or OP2_PLATE :
            pickup_tips_multi_WL(protocolFile, pipet20, tips_20[plate], col)

        if (NORMALIZATION and transfer_of_oligos) :

            aspirate_WL(protocolFile, pipet20,
                        colOfLabware(mother_plates[plate], col, 96) + ".bottom(" + str(ASP_FROM_BOTTOM) + ")", \
                        volume_norm, ASP_FLOW_RATE)
            dispense_WL(protocolFile, pipet20,
                        colOfLabware(plates_to_normalize[plate], col, 96) + ".bottom(" + str(DISP_FROM_BOTTOM) + ")", \
                        volume_norm, DISP_FLOW_RATE)

        if NORMALIZATION :

            for wellConc in concentrations:
                well=wellConc[0]
                if getColumn(well)==col:
                    conc=wellConc[1]
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

        if OP2_PLATE:

            mix_WL(protocolFile,pipet20,3,15,colOfLabware(plates_to_normalize[plate], col, 96) + ".bottom(" + str(ASP_FROM_BOTTOM_OP2) +")", MIX_FLOW_RATE)

            aspirate_WL(protocolFile, pipet20,
                        colOfLabware(plates_to_normalize[plate], col, 96) + ".bottom(" + str(ASP_FROM_BOTTOM_OP2) + ")", \
                        volume_op2, ASP_FLOW_RATE_OP2)
            dispense_WL(protocolFile, pipet20,
                        colOfLabware(op2_plates[plate], col, 96) + ".bottom(" + str(DISP_FROM_BOTTOM_OP2) + ")", \
                        volume_op2, DISP_FLOW_RATE_OP2)

            mix_WL(protocolFile, pipet20, 3, 15,
                   colOfLabware(op2_plates[plate], col, 96) + ".bottom(" + str(DISP_FROM_BOTTOM_OP2) + ")", \
                   MIX_FLOW_RATE)

        if transfer_of_oligos or OP2_PLATE:
            return_WL(protocolFile, pipet20)

