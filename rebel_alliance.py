from firefight.firefight import Weapon, Model, UpgradeList
from firefight import core

with open("rebel_alliance.tsv", "w", encoding="utf-8") as file:

    rebel_captain = Model(
        "Rebel Captain (with Electrobinoculars)",
        3,
        5,
        3,
        hero=True,
        take_cover=2,
    )
    rebel_captain.equip_weapon(core.heavy_blaster_pistol)

    rebel_trooper = Model("Rebel Trooper", 4, 5, 1)
    rebel_trooper.equip_weapon(core.blaster_rifle)

    at_rt = Model(
        "AT-RT", 4, 3, 4, vehicle=True, fast=True, cover="Front", jump=3, impact=3
    )
    at_rt.equip_weapon(core.laser_cannon_mounted)
    at_rt.equip_weapon(core.blaster_rifle)

    ### Upgrade lists ###

    # A

    upgrade_list_A = UpgradeList("A", base_model=rebel_trooper)
    upgrade_list_A.select_upgrade_with_weapon_type(replace_weapon=core.blaster_rifle)
    upgrade_list_A.upgrade_with_weapon_entry(core.rotary_blaster)
    upgrade_list_A.upgrade_with_weapon_entry(core.heavy_blaster_rifle)
    upgrade_list_A.upgrade_with_weapon_entry(core.sniper_rifle)
    upgrade_list_A.upgrade_with_weapon_entry(core.scatterblaster)
    upgrade_list_A.upgrade_with_weapon_entry(core.scattergun)
    upgrade_list_A.upgrade_with_weapon_entry(core.heavy_sniper_rifle)
    upgrade_list_A.upgrade_with_weapon_entry(core.cycler_rifle)

    # B

    upgrade_list_B = UpgradeList("B", base_model=rebel_trooper)
    upgrade_list_B.select_upgrade_with_weapon_type(limit=1)
    upgrade_list_B.upgrade_with_weapon_entry(core.homing_launcher)
    upgrade_list_B.upgrade_with_weapon_entry(core.grenade_launcher)
    upgrade_list_B.upgrade_with_weapon_entry(core.ion_torpedo)
    upgrade_list_B.upgrade_with_weapon_entry(core.rocket_launcher)
    upgrade_list_B.upgrade_with_weapon_entry(core.ion_disruptor)
    upgrade_list_B.upgrade_with_weapon_entry(core.concussion_grenade)
    upgrade_list_B.upgrade_with_weapon_entry(core.thermal_detonator)
    upgrade_list_B.upgrade_with_weapon_entry(core.ion_grenade)
    upgrade_list_B.upgrade_with_weapon_entry(core.frag_grenade)
    upgrade_list_B.upgrade_with_weapon_entry(core.thermal_imploder)

    # C

    upgrade_list_C = UpgradeList("C", base_model=at_rt)
    upgrade_list_C.select_upgrade_with_weapon_type(
        replace_weapon=core.laser_cannon_mounted
    )
    upgrade_list_C.upgrade_with_weapon_entry(core.heavy_rotary_cannon_mounted)
    upgrade_list_C.upgrade_with_weapon_entry(core.heavy_flamethrower_mounted)

    # assign upgrade lists

    rebel_trooper.add_upgrade_list([upgrade_list_A, upgrade_list_B])
    at_rt.add_upgrade_list(upgrade_list_C)

    # print all

    file.write(core.header)
    file.write(rebel_captain.write_statline())
    file.write(rebel_trooper.write_statline())
    file.write(at_rt.write_statline())

    file.write("\n")
    file.write(upgrade_list_A.write_upgrade_list())
    file.write("\n")
    file.write(upgrade_list_B.write_upgrade_list())
    file.write("\n")
    file.write(upgrade_list_C.write_upgrade_list())
