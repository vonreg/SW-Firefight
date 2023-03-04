from firefight.firefight import Weapon, Model, UpgradeList
from firefight import core

with open("mandalore.tsv", "w", encoding="utf-8") as file:

    # Common Mandalorian Weapons
    jetpack_rocket = Weapon(
        "Jetpack Rocket", "inf", 2, pierce=1, ammo="Single Use", blast=3
    )
    dart_launcher = Weapon(
        "Dart Launcher", 18, 1, pierce=2, ammo="Single Use", disorient=True
    )
    gauntlet_blades = Weapon("Gauntlet Blades", "Melee", 4, rending=True)
    # core: whipcord launcher
    # core: wrist flamethrower

    bo_katan = Model(
        "Bo-Katan Kryze",
        3,
        2,
        5,
        hero=True,
        impervious=True,
        arsenal=2,
        courage=True,
        fast=True,
        fly=True,
        command=True,
        shield=1,
    )
    darksaber_bo_katan = Weapon(
        "The Darksaber", "Melee", 3, pierce=3, deadly=3, unique="The Darksaber"
    )
    bo_katan.equip_weapon(gauntlet_blades)
    bo_katan.equip_weapon(core.dual_blaster_pistols)
    bo_katan.equip_weapon(jetpack_rocket)

    mandalorian = Model("Mandalorian", 3, 3, 2, fly=True, fast=True, impervious=True)
    mandalorian.equip_weapon(core.combat_training)
    mandalorian.equip_weapon(core.dual_blaster_pistols)
    mandalorian.equip_weapon(jetpack_rocket)

    ### Upgrade lists ###

    # A

    upgrade_list_A = UpgradeList("A", base_model=bo_katan)
    upgrade_list_A.select_upgrade_with_weapon_type(replace_weapon=gauntlet_blades)
    upgrade_list_A.upgrade_with_weapon_entry(darksaber_bo_katan)

    # B

    upgrade_list_B = UpgradeList("B", base_model=bo_katan)
    upgrade_list_B.select_upgrade_with_weapon_type()
    upgrade_list_B.upgrade_with_weapon_entry(core.whipcord_launcher)
    upgrade_list_B.upgrade_with_weapon_entry(dart_launcher)
    upgrade_list_B.upgrade_with_weapon_entry(core.wrist_flamer)
    upgrade_list_B.upgrade_with_weapon_entry(core.concussion_grenade)
    upgrade_list_B.upgrade_with_weapon_entry(core.thermal_detonator)
    upgrade_list_B.upgrade_with_weapon_entry(core.ion_grenade)

    # C

    upgrade_list_C = UpgradeList("C", base_model=mandalorian)
    upgrade_list_C.select_upgrade_with_weapon_type(limit=1)
    upgrade_list_C.upgrade_with_weapon_entry(core.blaster_carbine)
    upgrade_list_C.upgrade_with_weapon_entry(core.sniper_rifle)
    upgrade_list_C.upgrade_with_weapon_entry(core.heavy_sniper_rifle)
    upgrade_list_C.upgrade_with_weapon_entry(core.whipcord_launcher)
    upgrade_list_C.upgrade_with_weapon_entry(dart_launcher)
    upgrade_list_C.upgrade_with_weapon_entry(core.wrist_flamer)
    upgrade_list_C.upgrade_with_weapon_entry(core.concussion_grenade)
    upgrade_list_C.upgrade_with_weapon_entry(core.thermal_detonator)
    upgrade_list_C.upgrade_with_weapon_entry(core.ion_grenade)

    # assign upgrade lists

    bo_katan.add_upgrade_list(upgrade_list_A)
    bo_katan.add_upgrade_list(upgrade_list_B)
    mandalorian.add_upgrade_list(upgrade_list_C)

    # print all

    file.write(core.header)
    file.write(bo_katan.write_statline())
    file.write(mandalorian.write_statline())

    file.write("\n")
    file.write(upgrade_list_A.write_upgrade_list())
    file.write("\n")
    file.write(upgrade_list_B.write_upgrade_list())
    file.write("\n")
    file.write(upgrade_list_C.write_upgrade_list())
