def TowerOfHonai(disks,FromRod,ToRod,AuxRod):
    if disks == 1:
        print('Moved disk 1 from',FromRod,"To",ToRod)
        return

    TowerOfHonai(disks-1,FromRod,AuxRod,ToRod)
    print('Move disk',disks,'FromRod',FromRod,'ToRod',ToRod)
    TowerOfHonai(disks-1,AuxRod,ToRod,FromRod)


print("For 2 Disks")
TowerOfHonai(2,"S",'D','T')

print("\n\n For 3 Disks")
TowerOfHonai(3,"S",'D','T')
