# S'il n'y a pas de normalisation, mais juste la préparation OP2,
# il est quand même nécessaire de renseigner le fichier Exel,
# en indiquant la concentration initiale dans les puits à transférer.

# --> Possibilité de traiter des plaques partielles,
# en ne mettant aucune information dans les puits qui ne doivent pas être transférés.
# AJouter manuellement 30µl de ladder dans les puits non transférés, avant OP2.

'-----------------------------'
NORMALIZATION =1
volume_norm = 10 #volume of sample to take
conc_norm = 1          #concentration to normalize to
transfer_of_oligos =1 # 1 to transfer, 0 not to transfer
type_of_plate_on_spacer = 1 # 1 for Axygen (standard), 2 for full or half areas from Greiner
'-----------------------------'
OP2_PLATE = 1
volume_op2 = 4 #volume of sample to take for OP2 plate
volume_ladders = 26 #volume of ladders to pipet

'-----------------------------'
