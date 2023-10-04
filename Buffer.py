class Buffer():

    def __init__(self, name, tipLabware, tipColumn, tipVolume, sourceLabware, sourceNbWells, sourceColumns,
                 aspiratingFlowRate, dispenseFlowRate, distFromLWTop, conditioningVolume, excessVolume, airGapVol):
        self.name = name
        self.tipLabware = tipLabware
        self.tipcolumn = tipColumn
        self.tipVolume = tipVolume
        self.sourceLabware = sourceLabware
        self.sourceColumns = sourceColumns  # list !
        self.sourceNbWells = sourceNbWells  # of source labware
        self.aspiratingFlowRate = aspiratingFlowRate
        self.dispenseFlowRate = dispenseFlowRate
        self.distFromLWTop = distFromLWTop  # when dispensing
        self.conditioningVolume = conditioningVolume  # volume to aspirate and dispense before 'add Buffer' action
        self.excessVolume = excessVolume  # volume to aspirate in excess to dispense the right volume
        self.airGapVol = airGapVol  # air gap volume between each dispense


# Buffers definition
# name,tipLabware,tipColumn,tipVolume,sourceLabware,sourceNbWells,sourceColumns,aspiratingFlowRate,dispenseFlowRate,distFromLWTop,conditioningVolume,excessVolume, airGapVol
WATER = Buffer(
    name="water",
    tipLabware="tiprack_300",
    tipColumn=[1, 2],
    tipVolume=300,
    sourceLabware=["BufferReservoir", "BufferSpeReservoir"],
    sourceNbWells=4,
    sourceColumns=[1],
    aspiratingFlowRate=1.5,
    dispenseFlowRate=3.0,
    distFromLWTop=2,
    conditioningVolume=0,
    excessVolume=0,
    airGapVol=0
)

LADDERS = Buffer(
    name="Ladders",
    tipLabware="tiprack_300",
    tipColumn=[1],
    tipVolume=300,
    sourceLabware=["LadderReservoir"],
    sourceNbWells=4,
    sourceColumns=[1],
    aspiratingFlowRate=1.5,
    dispenseFlowRate=10.0,
    distFromLWTop=14,
    conditioningVolume=0,
    excessVolume=14,
    airGapVol=0
)

TTSTPK = Buffer(
    name="TTSTPK",
    tipLabware="tiprack_300",
    tipColumn=[3, 4],
    tipVolume=300,
    sourceLabware=["BufferReservoir", "BufferSpeReservoir"],
    sourceNbWells=4,
    sourceColumns=[2],
    aspiratingFlowRate=1.5,
    dispenseFlowRate=3.0,
    distFromLWTop=2,
    conditioningVolume=0,
    excessVolume=0,
    airGapVol=0
)
TH1X = Buffer(
    name="TH1X",
    tipLabware="tiprack_300",
    tipColumn=[5, 6],
    tipVolume=300,
    sourceLabware=["BufferReservoir", "BufferSpeReservoir"],
    sourceNbWells=4,
    sourceColumns=[3],
    aspiratingFlowRate=1.5,
    dispenseFlowRate=3.0,
    distFromLWTop=2,
    conditioningVolume=0,
    excessVolume=0,
    airGapVol=0
)
ETHANOL_WASH = Buffer(  # for Full vacuum
    name="ETHANOL_WASH",
    tipLabware="tiprack_300",
    tipColumn=[9],
    tipVolume=300,
    sourceLabware=["BufferReservoir", "BufferSpeReservoir"],
    sourceNbWells=4,
    sourceColumns=[4],
    aspiratingFlowRate=1.5,
    dispenseFlowRate=1.5,
    distFromLWTop=2,
    conditioningVolume=0,
    excessVolume=0,
    airGapVol=0
)
TH1X_transfer = Buffer(
    name="TH1X_transfer",
    tipLabware="tiprack_300",
    tipColumn=[5, 6],
    tipVolume=300,
    sourceLabware=["BufferReservoir", "BufferSpeReservoir"],
    sourceNbWells=4,
    sourceColumns=[3],
    aspiratingFlowRate=1.5,
    dispenseFlowRate=3.0,
    distFromLWTop=3,
    conditioningVolume=25,
    excessVolume=10,
    airGapVol=5
)
ISOPROP = Buffer(
    name="ISOPROP",
    tipLabware="tiprack_300",
    tipColumn=[7],
    tipVolume=300,
    sourceLabware=["BufferReservoir"],
    sourceNbWells=4,
    sourceColumns=[1],
    aspiratingFlowRate=1.5,
    dispenseFlowRate=1.5,
    distFromLWTop=3,
    conditioningVolume=25,
    excessVolume=0,
    airGapVol=0
)
ETHANOL = Buffer(
    name="ETHANOL",
    tipLabware="tiprack_300",
    tipColumn=[9, 10],
    tipVolume=300,
    sourceLabware=["BufferReservoir", "BufferSpeReservoir"],
    sourceNbWells=4,
    sourceColumns=[3, 4],
    aspiratingFlowRate=1.5,
    dispenseFlowRate=1.5,
    distFromLWTop=3,
    conditioningVolume=0,
    excessVolume=0,
    airGapVol=0
)

ENDOV = Buffer(
    name="EndoV",
    tipLabware="tiprack_300",
    tipColumn=[11, 12],
    tipVolume=300,
    sourceLabware=["EnzymeReservoir"],
    sourceNbWells=12,
    sourceColumns=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12],
    aspiratingFlowRate=2,
    dispenseFlowRate=3,
    distFromLWTop=15,
    conditioningVolume=10,
    excessVolume=15,
    airGapVol=10
)

ENDOV_DG3 = Buffer(
    name="EndoV",
    tipLabware="tiprack_300",
    tipColumn=[11, 12],
    tipVolume=300,
    sourceLabware=["EnzymeReservoir"],
    sourceNbWells=12,
    sourceColumns=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12],
    aspiratingFlowRate=2,
    dispenseFlowRate=2,
    distFromLWTop=2,
    conditioningVolume=10,
    excessVolume=15,
    airGapVol=10
)

ENDOQ_DG3 = Buffer(
    name="EndoQ",
    tipLabware="tiprack_300",
    tipColumn=[8, 9, 10],
    tipVolume=300,
    sourceLabware=["EnzymeReservoir"],
    sourceNbWells=12,
    sourceColumns=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12],
    aspiratingFlowRate=2,
    dispenseFlowRate=2,
    distFromLWTop=2,
    conditioningVolume=10,
    excessVolume=15,
    airGapVol=10
)


CLICK_MIX_color = Buffer(
    name="Click mix color",
    tipLabware="tiprack_300_click",
    tipColumn=[1],
    tipVolume=300,
    sourceLabware=["ClickMixReservoir"],
    sourceNbWells=12,
    sourceColumns=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11],
    aspiratingFlowRate=2,
    dispenseFlowRate=2,
    distFromLWTop=1,
    conditioningVolume=10,
    excessVolume=15,
    airGapVol=10
)

CLICK_MIX_color_v2 = Buffer(
    name="Click mix color v2",
    tipLabware="tiprack_300_click_v2",
    tipColumn=[],  # will be a well nbr called in the function not implemented here
    tipVolume=300,
    sourceLabware=["EnzymeReservoir"],
    sourceNbWells=12,
    sourceColumns=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12],
    aspiratingFlowRate=2,
    dispenseFlowRate=2,
    distFromLWTop=1,
    conditioningVolume=10,
    excessVolume=15,
    airGapVol=10
)

CLICK_MIX_AA = Buffer(
    name="Click mix AA",
    tipLabware="tiprack_20_AA",
    tipColumn=[1],
    tipVolume=20,
    sourceLabware=["ClickMixReservoir"],
    sourceNbWells=12,
    sourceColumns=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12],
    aspiratingFlowRate=2,
    dispenseFlowRate=5,
    distFromLWTop=1,
    conditioningVolume=5,
    excessVolume=0,
    airGapVol=5
)

CLICK_MIX_AA_v2 = Buffer(
    name="Click mix AA v2",
    tipLabware="tiprack_20_AA",
    tipColumn=[1],
    tipVolume=20,
    sourceLabware=["ClickMixReservoir"],
    sourceNbWells=12,
    sourceColumns=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12],
    aspiratingFlowRate=2,
    dispenseFlowRate=5,
    distFromLWTop=1,
    conditioningVolume=0,
    excessVolume=0,
    airGapVol=0
)

W2 = Buffer(
    name="W2",
    tipLabware="tiprack_300_click",
    tipColumn=[10],
    tipVolume=300,
    sourceLabware=["BufferSpeReservoir"],  # take same name as for PSP wash to avoid creating to labwares
    sourceNbWells=4,
    sourceColumns=[1],
    aspiratingFlowRate=1.5,
    dispenseFlowRate=3.0,
    distFromLWTop=1,
    conditioningVolume=0,
    excessVolume=0,
    airGapVol=0
)

WB1 = Buffer(
    name="WB1",
    tipLabware="tiprack_300_click",
    tipColumn=[9],
    tipVolume=300,
    sourceLabware=["BufferSpeReservoir"],  # take same name as for PSP wash to avoid creating to labwares
    sourceNbWells=4,
    sourceColumns=[1],
    aspiratingFlowRate=1.5,
    dispenseFlowRate=3.0,
    distFromLWTop=1,
    conditioningVolume=0,
    excessVolume=0,
    airGapVol=0
)

EB = Buffer(
    name="EB",
    tipLabware="tiprack_300_click",
    tipColumn=[11],
    tipVolume=300,
    sourceLabware=["BufferSpeReservoir"],
    sourceNbWells=12,
    sourceColumns=[3],
    aspiratingFlowRate=2,
    dispenseFlowRate=2,
    distFromLWTop=1,
    conditioningVolume=10,
    excessVolume=15,
    airGapVol=10
)

OctdU = Buffer(
    name="OctdU",
    tipLabware="tiprack_300_click",
    tipColumn=[12],
    tipVolume=300,
    sourceLabware=["BufferSpeReservoir"],
    sourceNbWells=12,
    sourceColumns=[4],
    aspiratingFlowRate=2,
    dispenseFlowRate=2,
    distFromLWTop=1,
    conditioningVolume=10,
    excessVolume=15,
    airGapVol=10
)

CLICK_ISOP = Buffer(
    name="ISOP",
    tipLabware="tiprack_300_click",
    tipColumn=[5],
    tipVolume=300,
    sourceLabware=["BufferClickReservoir"],
    sourceNbWells=4,
    sourceColumns=[4],
    aspiratingFlowRate=1.5,
    dispenseFlowRate=1.5,
    distFromLWTop=1,
    conditioningVolume=0,
    excessVolume=0,
    airGapVol=5
)

CLICK_EDTA = Buffer(
    name="EDTA",
    tipLabware="tiprack_300_click",
    tipColumn=[7],
    tipVolume=300,
    sourceLabware=["BufferClickReservoir"],
    sourceNbWells=4,
    sourceColumns=[3],
    aspiratingFlowRate=1.5,
    dispenseFlowRate=3.0,
    distFromLWTop=1,
    conditioningVolume=0,
    excessVolume=0,
    airGapVol=0
)

CLICK_H2O_WASH = Buffer(
    name="H2O",
    tipLabware="tiprack_300_click",
    tipColumn=[3],
    tipVolume=300,
    sourceLabware=["BufferClickReservoir"],
    sourceNbWells=4,
    sourceColumns=[1, 2],
    aspiratingFlowRate=1.5,
    dispenseFlowRate=3.0,
    distFromLWTop=1,
    conditioningVolume=0,
    excessVolume=0,
    airGapVol=0
)

class BufferP1000():

    def __init__(self, name, tipLabware, tipWell, tipVolume, sourceLabware, sourceWell, aspiratingFlowRate,
                 dispenseFlowRate, mixingFlowRate, sourceLWBottom, destLWBottom, conditioningVolume, excessVolume,
                 airGapVol, tipReturn):
        self.name = name
        self.tipLabware = tipLabware
        self.tipWell = tipWell
        self.tipVolume = tipVolume
        self.sourceLabware = sourceLabware
        self.sourceWell = sourceWell  # source falcon
        self.aspiratingFlowRate = aspiratingFlowRate
        self.dispenseFlowRate = dispenseFlowRate
        self.mixingFlowRate = mixingFlowRate
        self.sourceLWBottom = sourceLWBottom  # dist from Lw bottom when aspirating
        self.destLWBottom = destLWBottom  # dist from Lw bottom when dispensing
        self.conditioningVolume = conditioningVolume  # volume to aspirate and dispense before 'add Buffer' action
        self.excessVolume = excessVolume  # volume to aspirate in excess to dispense the right volume
        self.airGapVol = airGapVol  # air gap volume between each dispense
        self.tipReturn = tipReturn  # if == 0 -> tip will be discarded, if == 1 -> tip will be returned to the tipbox


EndoV = BufferP1000(
    name="EndoV",
    tipLabware="tiprack_1000",
    tipWell=0,
    tipVolume=1000,
    sourceLabware="falcons",
    sourceWell=0,
    aspiratingFlowRate=0.8,
    dispenseFlowRate=0.8,
    mixingFlowRate=1.0,
    sourceLWBottom=3,
    destLWBottom=10,
    conditioningVolume=25,
    excessVolume=15,
    airGapVol=20,
    tipReturn=0
)
