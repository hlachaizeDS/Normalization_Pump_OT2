from smallFunctions import *
from elementaryCommands import *
from Buffer import *


def addBuffer(protocolFile, multi_pipet, usedWells, destLabware, buffer=None, vol=0, sourceColumnIndex=0,
              bufferReservoir=0, tipcolumn=0, pickuptip=1, returntip=1):
    if buffer == None or usedWells == [] or vol == 0:
        return

    #  variables
    BLOW_OUT_DIST_FROM_TOP = 5
    CONDITIONING_VOL = buffer.conditioningVolume
    EXCESS_VOL = buffer.excessVolume
    AIR_GAP_VOL = buffer.airGapVol

    # Fetch tips
    if pickuptip == 1:
        pickup_tips_multi_WL(protocolFile, multi_pipet, buffer.tipLabware, buffer.tipcolumn[tipcolumn])

    usedColumns = fromWellsToColumns(usedWells)
    usedColumnsAndVolumes = [[col, vol] for col in usedColumns]

    while usedColumnsAndVolumes != []:
        volToAspirate = 0
        columnsAndVolumesToDispense = []
        for colVol in usedColumnsAndVolumes.copy():
            nextVol = volToAspirate + colVol[1]
            if nextVol > (buffer.tipVolume - CONDITIONING_VOL - EXCESS_VOL - AIR_GAP_VOL):
                volRemaining = (buffer.tipVolume - CONDITIONING_VOL - EXCESS_VOL - AIR_GAP_VOL) - volToAspirate
                volToAspirate = (buffer.tipVolume - CONDITIONING_VOL - EXCESS_VOL - AIR_GAP_VOL)
                columnsAndVolumesToDispense.append([colVol[0], volRemaining])
                usedColumnsAndVolumes[usedColumnsAndVolumes.index(colVol)][1] = colVol[1] - volRemaining
                break
            else:
                volToAspirate = volToAspirate + colVol[1]
                columnsAndVolumesToDispense.append(colVol)
                usedColumnsAndVolumes.remove(colVol)
                if volToAspirate == (buffer.tipVolume - CONDITIONING_VOL - EXCESS_VOL - AIR_GAP_VOL):
                    break

        aspirate_WL(protocolFile, multi_pipet,
                    colOfLabware(buffer.sourceLabware[bufferReservoir], buffer.sourceColumns[sourceColumnIndex],
                                 buffer.sourceNbWells),
                    volToAspirate + CONDITIONING_VOL + EXCESS_VOL, buffer.aspiratingFlowRate)
        delay_WL(protocolFile, 0.5)
        dispense_WL(protocolFile, multi_pipet,
                    colOfLabware(buffer.sourceLabware[bufferReservoir], buffer.sourceColumns[sourceColumnIndex],
                                 buffer.sourceNbWells),
                    CONDITIONING_VOL, buffer.dispenseFlowRate)
        if AIR_GAP_VOL != 0:
            air_gap_WL(protocolFile, multi_pipet, AIR_GAP_VOL)

        for colVol in columnsAndVolumesToDispense:
            dispense_WL(protocolFile, multi_pipet,
                        colOfLabware(destLabware, colVol[0], 96) + ".top(" + str(-buffer.distFromLWTop) + ")",
                        colVol[1] + AIR_GAP_VOL, buffer.dispenseFlowRate)
            if buffer.name == "Click mix AA":
                touch_tip_WL(protocolFile, multi_pipet, colOfLabware(destLabware, colVol[0], 96), 0.3)
            if AIR_GAP_VOL != 0:
                air_gap_WL(protocolFile, multi_pipet, AIR_GAP_VOL)

        blow_out_WL(protocolFile, multi_pipet,
                    colOfLabware(buffer.sourceLabware[bufferReservoir], buffer.sourceColumns[sourceColumnIndex],
                                 buffer.sourceNbWells) + ".top(-" + str(BLOW_OUT_DIST_FROM_TOP) + ")")

    #  Unfetch tips
    if returntip == 1:
        return_WL(protocolFile, multi_pipet)

def addBuffer_DiffVolsCols(protocolFile, multi_pipet, usedWells, destLabware, buffer=None, volumes=[0,0,0,0,0,0,0,0,0,0,0,0], sourceColumnIndex=0,
              bufferReservoir=0, tipcolumn=0, pickuptip=1, returntip=1):
    if buffer == None or usedWells == [] or volumes == [0,0,0,0,0,0,0,0,0,0,0,0]:
        return

    #  variables
    BLOW_OUT_DIST_FROM_TOP = 5
    CONDITIONING_VOL = buffer.conditioningVolume
    EXCESS_VOL = buffer.excessVolume
    AIR_GAP_VOL = buffer.airGapVol

    # Fetch tips
    if pickuptip == 1:
        pickup_tips_multi_WL(protocolFile, multi_pipet, buffer.tipLabware, buffer.tipcolumn[tipcolumn])

    usedColumns = fromWellsToColumns(usedWells)
    usedColumnsAndVolumes = [[col, volumes[col-1]] for col in usedColumns]

    while usedColumnsAndVolumes != []:
        volToAspirate = 0
        columnsAndVolumesToDispense = []
        for colVol in usedColumnsAndVolumes.copy():
            nextVol = volToAspirate + colVol[1]
            if nextVol > (buffer.tipVolume - CONDITIONING_VOL - EXCESS_VOL - AIR_GAP_VOL):
                volRemaining = (buffer.tipVolume - CONDITIONING_VOL - EXCESS_VOL - AIR_GAP_VOL) - volToAspirate
                volToAspirate = (buffer.tipVolume - CONDITIONING_VOL - EXCESS_VOL - AIR_GAP_VOL)
                columnsAndVolumesToDispense.append([colVol[0], volRemaining])
                usedColumnsAndVolumes[usedColumnsAndVolumes.index(colVol)][1] = colVol[1] - volRemaining
                break
            else:
                volToAspirate = volToAspirate + colVol[1]
                columnsAndVolumesToDispense.append(colVol)
                usedColumnsAndVolumes.remove(colVol)
                if volToAspirate == (buffer.tipVolume - CONDITIONING_VOL - EXCESS_VOL - AIR_GAP_VOL):
                    break

        aspirate_WL(protocolFile, multi_pipet,
                    colOfLabware(buffer.sourceLabware[bufferReservoir], buffer.sourceColumns[sourceColumnIndex],
                                 buffer.sourceNbWells),
                    volToAspirate + CONDITIONING_VOL + EXCESS_VOL, buffer.aspiratingFlowRate)
        delay_WL(protocolFile, 0.5)
        dispense_WL(protocolFile, multi_pipet,
                    colOfLabware(buffer.sourceLabware[bufferReservoir], buffer.sourceColumns[sourceColumnIndex],
                                 buffer.sourceNbWells),
                    CONDITIONING_VOL, buffer.dispenseFlowRate)
        if AIR_GAP_VOL != 0:
            air_gap_WL(protocolFile, multi_pipet, AIR_GAP_VOL)

        for colVol in columnsAndVolumesToDispense:
            dispense_WL(protocolFile, multi_pipet,
                        colOfLabware(destLabware, colVol[0], 96) + ".top(" + str(-buffer.distFromLWTop) + ")",
                        colVol[1] + AIR_GAP_VOL, buffer.dispenseFlowRate)
            if buffer.name == "Click mix AA":
                touch_tip_WL(protocolFile, multi_pipet, colOfLabware(destLabware, colVol[0], 96), 0.3)
            if AIR_GAP_VOL != 0:
                air_gap_WL(protocolFile, multi_pipet, AIR_GAP_VOL)

        blow_out_WL(protocolFile, multi_pipet,
                    colOfLabware(buffer.sourceLabware[bufferReservoir], buffer.sourceColumns[sourceColumnIndex],
                                 buffer.sourceNbWells) + ".top(-" + str(BLOW_OUT_DIST_FROM_TOP) + ")")

    #  Unfetch tips
    if returntip == 1:
        return_WL(protocolFile, multi_pipet)



def cleavedTransferEppenToInvitek(protocolFile, multi_pipet, usedWells, fromLabware, toLabware, tipBox, volume):
    if usedWells == [] or volume == 0:
        return

    TIPS_VOLUME = 300

    NB_OF_MIXES = 3
    VOLUME_OF_MIXES = 150

    DIST_FROM_EPPEN_BOTTOM_HIGH = 4.5
    DIST_FROM_EPPEN_BOTTOM_LOW = 0.5
    DIST_FROM_INVITEK_TOP = 7

    MIXING_FLOW_RATE = 1.5
    ASP_FLOW_RATE = 1.5
    DISP_FLOW_RATE = 1.5

    usedColumns = fromWellsToColumns(usedWells)
    for col in usedColumns:
        pickup_tips_multi_WL(protocolFile, multi_pipet, tipBox, col)

        volToTransfer = volume
        while (volToTransfer != 0):
            if volToTransfer > TIPS_VOLUME:
                vol = TIPS_VOLUME
            else:
                vol = volToTransfer

            if volToTransfer > 300:
                comment_WL(protocolFile, 'mixing')
                mix_WL(protocolFile, multi_pipet, NB_OF_MIXES, VOLUME_OF_MIXES,
                       colOfLabware(fromLabware, col, 96) + ".bottom(" + str(DIST_FROM_EPPEN_BOTTOM_HIGH) + ")",
                       MIXING_FLOW_RATE)
                aspirate_WL(protocolFile, multi_pipet,
                            colOfLabware(fromLabware, col, 96) + ".bottom(" + str(DIST_FROM_EPPEN_BOTTOM_HIGH) + ")",
                            vol, ASP_FLOW_RATE)
                dispense_WL(protocolFile, multi_pipet,
                            colOfLabware(toLabware, col, 96) + ".top(" + str(-DIST_FROM_INVITEK_TOP) + ")",
                            vol, DISP_FLOW_RATE)

            else:
                comment_WL(protocolFile, 'mixing')
                mix_WL(protocolFile, multi_pipet, NB_OF_MIXES, VOLUME_OF_MIXES,
                       colOfLabware(fromLabware, col, 96) + ".bottom(" + str(DIST_FROM_EPPEN_BOTTOM_LOW) + ")",
                       MIXING_FLOW_RATE)
                aspirate_WL(protocolFile, multi_pipet,
                            colOfLabware(fromLabware, col, 96) + ".bottom(" + str(DIST_FROM_EPPEN_BOTTOM_LOW) + ")",
                            vol, ASP_FLOW_RATE)
                dispense_WL(protocolFile, multi_pipet,
                            colOfLabware(toLabware, col, 96) + ".top(" + str(-DIST_FROM_INVITEK_TOP) + ")",
                            vol, DISP_FLOW_RATE)

            blow_out_WL(protocolFile, multi_pipet,
                        colOfLabware(toLabware, col, 96) + ".top(" + str(-DIST_FROM_INVITEK_TOP) + ")")
            touch_tip_WL(protocolFile, multi_pipet, colOfLabware(toLabware, col, 96), 1, -0.5)

            volToTransfer = volToTransfer - vol

        drop_WL(protocolFile, multi_pipet)


def cleavedTransferFilterToInvitek(protocolFile, multi_pipet, usedWells, buffer, fromLabware, toLabware, tipBox,
                                   mix_vol=50, endoV_mix_vol=100, sourceColumnIndex=0, bufferReservoir=0):
    if not usedWells:
        return

    TIPS_VOLUME = 300
    SYNTH_WELL_VOL = 200  # "maximum" volume usable in synthesis plate
    ENDOV_MIX_VOL = endoV_mix_vol
    SYNTH_MIX_VOL = mix_vol
    ISOP_DESALT_MIN_VOL = 50
    INVITEK_MIX_VOL = 100

    DIST_FROM_FILTER_BOTTOM_1 = 0.7
    DIST_FROM_FILTER_BOTTOM_2 = 0.4
    DIST_FROM_FILTER_BOTTOM_3 = 0
    DIST_FROM_DESALT_TOP = 5
    DIST_FROM_DESALT_TOP_MIX = 25

    ASP_FLOW_RATE = 0.8
    DISP_FLOW_RATE = 1.5
    MIX_FLOW_RATE = 1

    NBR_OF_MIXES = 3
    DIST_FROM_FILTER_BOTTOM_MIX = 1

    usedColumns = fromWellsToColumns(usedWells)
    for col in usedColumns:
        pickup_tips_multi_WL(protocolFile, multi_pipet, tipBox, col)

        isop_tot_vol = 3 * ENDOV_MIX_VOL
        Vol_tot = isop_tot_vol + ENDOV_MIX_VOL
        if Vol_tot <= SYNTH_WELL_VOL:
            isop_synth_vol = isop_tot_vol
            isop_desalt_vol = ISOP_DESALT_MIN_VOL
        else:
            isop_synth_vol = SYNTH_WELL_VOL - ENDOV_MIX_VOL
            if isop_tot_vol - isop_synth_vol < ISOP_DESALT_MIN_VOL:
                isop_desalt_vol = ISOP_DESALT_MIN_VOL
            else:
                isop_desalt_vol = isop_tot_vol - isop_synth_vol

        isop_desalt_vol2 = isop_desalt_vol
        while (isop_desalt_vol2 != 0):
            if isop_desalt_vol2 > TIPS_VOLUME - 10:
                vol1 = TIPS_VOLUME - 10
            else:
                vol1 = isop_desalt_vol2

            aspirate_WL(protocolFile, multi_pipet,
                        colOfLabware(buffer.sourceLabware[bufferReservoir], buffer.sourceColumns[sourceColumnIndex],
                                     buffer.sourceNbWells), vol1, buffer.aspiratingFlowRate)
            air_gap_WL(protocolFile, multi_pipet, 10)
            dispense_WL(protocolFile, multi_pipet, colOfLabware(toLabware, col, 96)
                        + ".top(" + str(-DIST_FROM_DESALT_TOP) + ")", vol1 + 10, DISP_FLOW_RATE)
            blow_out_WL(protocolFile, multi_pipet, colOfLabware(toLabware, col, 96)
                        + ".top(" + str(-DIST_FROM_DESALT_TOP) + ")")

            isop_desalt_vol2 = isop_desalt_vol2 - vol1

        isop_synth_vol2 = isop_synth_vol
        while (isop_synth_vol2 != 0):
            if isop_synth_vol2 > TIPS_VOLUME - 10:
                vol2 = TIPS_VOLUME - 10
            else:
                vol2 = isop_synth_vol2

            aspirate_WL(protocolFile, multi_pipet,
                        colOfLabware(buffer.sourceLabware[bufferReservoir], buffer.sourceColumns[sourceColumnIndex],
                                     buffer.sourceNbWells), vol2, buffer.aspiratingFlowRate)
            air_gap_WL(protocolFile, multi_pipet, 10)
            dispense_WL(protocolFile, multi_pipet, colOfLabware(fromLabware, col, 96), vol2 + 10, DISP_FLOW_RATE)
            isop_synth_vol2 = isop_synth_vol2 - vol2

        mix_WL(protocolFile, multi_pipet, NBR_OF_MIXES, SYNTH_MIX_VOL,
               colOfLabware(fromLabware, col, 96) + ".bottom(" + str(DIST_FROM_FILTER_BOTTOM_MIX) + ")", ASP_FLOW_RATE)

        vol_to_transfer = ENDOV_MIX_VOL + isop_synth_vol
        while (vol_to_transfer != 0):
            if vol_to_transfer >= TIPS_VOLUME - 50:
                vol3 = TIPS_VOLUME - 50
            else:
                vol3 = vol_to_transfer

            aspirate_WL(protocolFile, multi_pipet,
                        colOfLabware(fromLabware, col, 96) + ".bottom(" + str(DIST_FROM_FILTER_BOTTOM_1) + ")", vol3,
                        ASP_FLOW_RATE)
            aspirate_WL(protocolFile, multi_pipet,
                        colOfLabware(fromLabware, col, 96) + ".bottom(" + str(DIST_FROM_FILTER_BOTTOM_2) + ")", 25,
                        ASP_FLOW_RATE)
            aspirate_WL(protocolFile, multi_pipet,
                        colOfLabware(fromLabware, col, 96) + ".bottom(" + str(DIST_FROM_FILTER_BOTTOM_3) + ")", 25,
                        ASP_FLOW_RATE)
            delay_WL(protocolFile, 2)
            dispense_WL(protocolFile, multi_pipet,
                        colOfLabware(toLabware, col, 96) + ".top(" + str(-DIST_FROM_DESALT_TOP) + ")",
                        vol3 + 50, DISP_FLOW_RATE)
            mix_WL(protocolFile, multi_pipet, NBR_OF_MIXES, INVITEK_MIX_VOL,
                   colOfLabware(toLabware, col, 96) + ".top(" + str(-DIST_FROM_DESALT_TOP_MIX) + ")", MIX_FLOW_RATE)
            blow_out_WL(protocolFile, multi_pipet,
                        colOfLabware(toLabware, col, 96) + ".top(" + str(-DIST_FROM_DESALT_TOP_MIX) + ")")
            touch_tip_WL(protocolFile, multi_pipet, colOfLabware(toLabware, col, 96))

            vol_to_transfer = vol_to_transfer - vol3

        drop_WL(protocolFile, multi_pipet)


def addAA(protocolFile, multi_pipet, usedWells, destLabware, buffer=None, vol=0, sourceColumnIndex=0,
          bufferReservoir=0):
    if not usedWells:
        return

    CONDITIONING_VOL = buffer.conditioningVolume
    AIR_GAP_VOL = buffer.airGapVol

    DIST_FROM_DEST_TOP = 10

    ASP_FLOW_RATE = buffer.aspiratingFlowRate
    DISP_FLOW_RATE = 2

    NBR_OF_MIXES = 3
    VOL_MIX = 15
    MIX_FLOW_RATE = 5
    DIST_FROM_FILTER_TOP_MIX = 10

    usedColumns = fromWellsToColumns(usedWells)
    for col in usedColumns:
        pickup_tips_multi_WL(protocolFile, multi_pipet, buffer.tipLabware, col)

        aspirate_WL(protocolFile, multi_pipet,
                    colOfLabware(buffer.sourceLabware[bufferReservoir], buffer.sourceColumns[sourceColumnIndex],
                                 buffer.sourceNbWells), vol + CONDITIONING_VOL, ASP_FLOW_RATE)
        delay_WL(protocolFile, 0.5)
        dispense_WL(protocolFile, multi_pipet,
                    colOfLabware(buffer.sourceLabware[bufferReservoir], buffer.sourceColumns[sourceColumnIndex],
                                 buffer.sourceNbWells), CONDITIONING_VOL, buffer.dispenseFlowRate)

        air_gap_WL(protocolFile, multi_pipet, AIR_GAP_VOL)
        dispense_WL(protocolFile, multi_pipet, colOfLabware(destLabware, col, 96)
                    + ".top(" + str(-DIST_FROM_DEST_TOP) + ")", vol + AIR_GAP_VOL, DISP_FLOW_RATE)

        mix_WL(protocolFile, multi_pipet, NBR_OF_MIXES, VOL_MIX, colOfLabware(destLabware, col, 96)
               + ".top(" + str(-DIST_FROM_FILTER_TOP_MIX) + ")", MIX_FLOW_RATE)
        drop_WL(protocolFile, multi_pipet)


def addAA_multi_source(protocolFile, multi_pipet, usedWells, destLabware, buffer=None, vol=0, source_list=None,
                       sourceColumnIndex=0, bufferReservoir=0):
    if not usedWells:
        return

    CONDITIONING_VOL = buffer.conditioningVolume
    AIR_GAP_VOL = buffer.airGapVol

    DIST_FROM_DEST_TOP = 10

    ASP_FLOW_RATE = buffer.aspiratingFlowRate
    DISP_FLOW_RATE = 2

    NBR_OF_MIXES = 3
    VOL_MIX = 15
    MIX_FLOW_RATE = 5
    DIST_FROM_FILTER_TOP_MIX = 10

    usedColumns = fromWellsToColumns(usedWells)
    for col in usedColumns:
        pickup_tips_multi_WL(protocolFile, multi_pipet, buffer.tipLabware, col)

        aspirate_WL(protocolFile, multi_pipet,
                    colOfLabware(buffer.sourceLabware[bufferReservoir], source_list[usedColumns.index(col)],
                                 buffer.sourceNbWells), vol + CONDITIONING_VOL, ASP_FLOW_RATE)
        # delay_WL(protocolFile, 0.5)
        # dispense_WL(protocolFile, multi_pipet,
        #             colOfLabware(buffer.sourceLabware[bufferReservoir], source_list[usedColumns.index(col)],
        #                          buffer.sourceNbWells), CONDITIONING_VOL, buffer.dispenseFlowRate)
        #
        # air_gap_WL(protocolFile, multi_pipet, AIR_GAP_VOL)
        dispense_WL(protocolFile, multi_pipet, colOfLabware(destLabware, col, 96)
                    + ".top(" + str(-DIST_FROM_DEST_TOP) + ")", vol + AIR_GAP_VOL, DISP_FLOW_RATE)

        mix_WL(protocolFile, multi_pipet, NBR_OF_MIXES, VOL_MIX, colOfLabware(destLabware, col, 96)
               + ".top(" + str(-DIST_FROM_FILTER_TOP_MIX) + ")", MIX_FLOW_RATE)
        drop_WL(protocolFile, multi_pipet)


def addLabels_one_well(protocolFile, multi_pipet, labels_list, destLabware, buffer=None, vol=0, bufferReservoir=0):
    if buffer == None or labels_list == [] or vol == 0:
        return

    #  variables
    BLOW_OUT_DIST_FROM_TOP = 5
    CONDITIONING_VOL = buffer.conditioningVolume
    EXCESS_VOL = buffer.excessVolume
    AIR_GAP_VOL = buffer.airGapVol
    TIPS_VOLUME = buffer.tipVolume - max(CONDITIONING_VOL, AIR_GAP_VOL) - EXCESS_VOL
    ASP_FLOW_RATE = buffer.aspiratingFlowRate
    DISP_FLOW_RATE = buffer.dispenseFlowRate
    fromLabware = buffer.sourceLabware[bufferReservoir]

    for label_wells in labels_list:
        source_index = labels_list.index(label_wells)
        if label_wells == []:
            continue
        pickup_tips_multi_one_tip_WL(protocolFile, multi_pipet, buffer.tipLabware, labels_list.index(label_wells) + 1,
                                     1)

        while label_wells != []:

            maxNbToDisp = TIPS_VOLUME // vol

            if len(label_wells) > maxNbToDisp:
                nbToDisp = maxNbToDisp
            else:
                nbToDisp = len(label_wells)

            volumeToAspirate = nbToDisp * vol
            wellsToUse = label_wells[:nbToDisp]
            label_wells = label_wells[nbToDisp:]

            aspirate_WL(protocolFile, multi_pipet,
                        fromLabware + ".wells()[" + str(source_index) + "]",
                        volumeToAspirate + CONDITIONING_VOL + EXCESS_VOL, ASP_FLOW_RATE)
            delay_WL(protocolFile, 0.5)
            dispense_WL(protocolFile, multi_pipet,
                        fromLabware + ".wells()[" + str(source_index) + "]", CONDITIONING_VOL,
                        DISP_FLOW_RATE)

            for well in wellsToUse:
                air_gap_WL(protocolFile, multi_pipet, AIR_GAP_VOL)
                dispense_WL(protocolFile, multi_pipet,
                            destLabware + ".wells()[" + str(well) + "].top(" + str(-buffer.distFromLWTop) + ")",
                            vol + AIR_GAP_VOL, DISP_FLOW_RATE)
            air_gap_WL(protocolFile, multi_pipet, AIR_GAP_VOL)
            blow_out_WL(protocolFile, multi_pipet,
                        fromLabware + ".wells()[" + str(source_index) + "].top(" + str(-BLOW_OUT_DIST_FROM_TOP) + ")")

        drop_WL(protocolFile, multi_pipet)


def addLabels_one_col(protocolFile, multi_pipet, labels_list, destLabware, buffer=None, vol=0, bufferReservoir=0):
    if buffer == None or labels_list == [] or vol == 0:
        return

    #  variables
    BLOW_OUT_DIST_FROM_TOP = 5
    CONDITIONING_VOL = buffer.conditioningVolume
    EXCESS_VOL = buffer.excessVolume
    AIR_GAP_VOL = buffer.airGapVol
    TIPS_VOLUME = buffer.tipVolume - max(CONDITIONING_VOL, AIR_GAP_VOL) - EXCESS_VOL
    ASP_FLOW_RATE = buffer.aspiratingFlowRate
    DISP_FLOW_RATE = buffer.dispenseFlowRate
    fromLabware = buffer.sourceLabware[bufferReservoir]

    for label_cols in labels_list:
        source_index = labels_list.index(label_cols)
        if label_cols == []:
            continue
        pickup_tips_multi_WL(protocolFile, multi_pipet, buffer.tipLabware, labels_list.index(label_cols) + 1)

        while label_cols:

            maxNbToDisp = TIPS_VOLUME // vol

            if len(label_cols) > maxNbToDisp:
                nbToDisp = maxNbToDisp
            else:
                nbToDisp = len(label_cols)

            volumeToAspirate = nbToDisp * vol
            colsToUse = label_cols[:nbToDisp]
            label_cols = label_cols[nbToDisp:]

            aspirate_WL(protocolFile, multi_pipet,
                        fromLabware + ".wells()[" + str(source_index) + "]",
                        volumeToAspirate + CONDITIONING_VOL + EXCESS_VOL, ASP_FLOW_RATE)
            delay_WL(protocolFile, 0.5)
            dispense_WL(protocolFile, multi_pipet,
                        fromLabware + ".wells()[" + str(source_index) + "]", CONDITIONING_VOL,
                        DISP_FLOW_RATE)

            for col in colsToUse:
                air_gap_WL(protocolFile, multi_pipet, AIR_GAP_VOL)
                dispense_WL(protocolFile, multi_pipet,
                            colOfLabware(destLabware, col, 96) + ".top(" + str(-buffer.distFromLWTop) + ")",
                            vol + AIR_GAP_VOL, DISP_FLOW_RATE)
            air_gap_WL(protocolFile, multi_pipet, AIR_GAP_VOL)
            blow_out_WL(protocolFile, multi_pipet,
                        fromLabware + ".wells()[" + str(source_index) + "].top(" + str(-BLOW_OUT_DIST_FROM_TOP) + ")")

        drop_WL(protocolFile, multi_pipet)


def addBuffer_P1000(protocolFile, single_pipet, buffer, usedWells, fromLabware, toLabware, tipBox, volume,
                    mix_nbr_falcon=0):
    DIST_FROM_FALCON_BOTTOM = buffer.sourceLWBottom
    DIST_FROM_DEST_PLATE_BOTTOM = buffer.destLWBottom

    MIX_FLOW_RATE = buffer.mixingFlowRate
    ASP_FLOW_RATE = buffer.aspiratingFlowRate
    DISP_FLOW_RATE = buffer.dispenseFlowRate

    FALCON_POSITION = buffer.sourceWell
    TIP_POSITION = buffer.tipWell

    EXCESS_VOL = buffer.excessVolume
    CONDITIONING_VOL = buffer.conditioningVolume
    AIR_GAP_VOL = buffer.airGapVol

    NBR_OF_MIXES = mix_nbr_falcon
    VOL_OF_MIXES = 900

    TIPS_VOLUME = (volume * 8 + CONDITIONING_VOL + EXCESS_VOL) - max(AIR_GAP_VOL, CONDITIONING_VOL) - EXCESS_VOL
    # 8wells by 8wells dispense

    pickup_tips_single_WL(protocolFile, single_pipet, tipBox, TIP_POSITION)
    if NBR_OF_MIXES != 0:
        mix_WL(protocolFile, single_pipet, NBR_OF_MIXES, VOL_OF_MIXES,
               fromLabware + ".wells()[" + str(FALCON_POSITION) + "].bottom(" + str(DIST_FROM_FALCON_BOTTOM) + ")",
               MIX_FLOW_RATE)

    while usedWells != []:

        maxNbToDisp = TIPS_VOLUME // volume

        if len(usedWells) > maxNbToDisp:
            nbToDisp = maxNbToDisp
        else:
            nbToDisp = len(usedWells)

        volumeToAspirate = nbToDisp * volume
        wellsToUse = usedWells[:nbToDisp]
        usedWells = usedWells[nbToDisp:]

        aspirate_WL(protocolFile, single_pipet,
                    fromLabware + ".wells()[" + str(FALCON_POSITION) + "].bottom(" + str(DIST_FROM_FALCON_BOTTOM) + ")",
                    volumeToAspirate + CONDITIONING_VOL + EXCESS_VOL, ASP_FLOW_RATE)
        delay_WL(protocolFile, 0.5)
        air_gap_WL(protocolFile, single_pipet, AIR_GAP_VOL)
        dispense_WL(protocolFile, single_pipet,
                    fromLabware + ".wells()[" + str(FALCON_POSITION) + "].top()", CONDITIONING_VOL + AIR_GAP_VOL,
                    DISP_FLOW_RATE)

        for well in wellsToUse:
            air_gap_WL(protocolFile, single_pipet, AIR_GAP_VOL)
            dispense_WL(protocolFile, single_pipet,
                        toLabware + ".wells()[" + str(well - 1) + "].bottom(" + str(DIST_FROM_DEST_PLATE_BOTTOM) + ")",
                        volume + AIR_GAP_VOL, DISP_FLOW_RATE)
        air_gap_WL(protocolFile, single_pipet, AIR_GAP_VOL)
        blow_out_WL(protocolFile, single_pipet, fromLabware + ".wells()[" + str(FALCON_POSITION) + "]")

    if buffer.tipReturn == 1:
        return_WL(protocolFile, single_pipet)
    else:
        drop_WL(protocolFile, single_pipet)


def wash(protocolFile, message, comport, incubation_time, vacuum_time, multi_pipet, usedWells, destLabware, buffer=None,
         vol=0, sourceColumnIndex=0, bufferReservoir=0, tipcolumn=0, pickuptip=1, returntip=1):
    if message != '':
        comment_WL(protocolFile, message)
    addBuffer(protocolFile, multi_pipet, usedWells, destLabware, buffer, vol, sourceColumnIndex, bufferReservoir,
              tipcolumn, pickuptip, returntip)
    incubate(protocolFile, comport, incubation_time)
    vacuum(protocolFile, comport, vacuum_time)


def cycle_wash(protocolFile, message, cycle_nbr, comport, incubation_time, vacuum_time, multi_pipet, usedWells,
               destLabware, buffer=None, vol=0, sourceColumnIndex=0, bufferReservoir=0, tipcolumn=0, pickuptip=1,
               returntip=1):
    for cycle in range(cycle_nbr):
        if message != '':
            new_message = message + ' n' + str(cycle+1)
        else:
            new_message = message
        wash(protocolFile, new_message, comport, incubation_time, vacuum_time, multi_pipet, usedWells, destLabware, buffer,
             vol, sourceColumnIndex, bufferReservoir, tipcolumn, pickuptip, returntip)


def special_wash(protocolFile, message, comport, incubation_time, vacuum_time, multi_pipet, usualWells, SpecialWells,
                 destLabware, buffer=None, vol=0, sourceColumnIndex=0):
    if message != '':
        comment_WL(protocolFile, message)
    addBuffer(protocolFile, multi_pipet, usualWells, destLabware, buffer, vol, sourceColumnIndex, 0, 0)
    addBuffer(protocolFile, multi_pipet, SpecialWells, destLabware, buffer, vol, sourceColumnIndex, 1, 1)
    incubate(protocolFile, comport, incubation_time)
    vacuum(protocolFile, comport, vacuum_time)


def special_cycle_wash(protocolFile, message, cycle_nbr, comport, incubation_time, vacuum_time, multi_pipet, usualWells,
                       SpecialWells, destLabware, buffer=None, vol=0, sourceColumnIndex=0):
    for cycle in range(cycle_nbr):
        if message != '':
            new_message = message + ' n' + str(cycle+1)
        else:
            new_message = message
        special_wash(protocolFile, new_message, comport, incubation_time, vacuum_time, multi_pipet, usualWells,
                     SpecialWells, destLabware, buffer, vol, sourceColumnIndex)
