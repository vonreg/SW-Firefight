from firefight.firefight import Weapon, Model, UpgradeList
from firefight import core

with open("galactic_republic.tsv", "w", encoding="utf-8") as file:

    obi_wan_kenobi = Model(
        "Obi-Wan Kenobi",
        3,
        3,
        6,
        jedi=True,
        courage=True,
        deflect=True,
        jump=6,
        unique="Obi-Wan Kenobi",
        protector="Any",
        impervious=True,
    )
    kenobi_lightsaber = Weapon("Lightsaber", "Melee", 4, ap=3, deadly=3)
    jedi_mind_trick = Weapon("Jedi Mind Trick", 12, 3, nonlethal=True, disorient=True)
    force_push = Weapon("Force Push", 12, 3, throw=True, seek=True, quickdraw=True)
    obi_wan_kenobi.equip_weapon(kenobi_lightsaber)
    obi_wan_kenobi.equip_weapon(jedi_mind_trick)
    obi_wan_kenobi.equip_weapon(force_push)

    clone_sergeant = Model(
        "Clone Sergeant (with Electrobinoculars)",
        3,
        4,
        2,
        hero=True,
        spotter=1,
    )
    clone_sergeant.equip_weapon(core.blaster_rifle)

    clone_trooper = Model("Clone Trooper", 4, 4, 1)
    clone_trooper.equip_weapon(core.blaster_rifle)

    at_rt = Model(
        "AT-RT", 4, 3, 4, vehicle=True, fast=True, cover="Front", jump=3, impact=3
    )
    at_rt.equip_weapon(core.laser_cannon_mounted)
    at_rt.equip_weapon(core.grenade_launcher)

    ### Upgrade lists ###

    # A

    upgrade_list_A = UpgradeList("A", base_model=clone_trooper)
    upgrade_list_A.select_upgrade_with_weapon_type(replace_weapon=core.blaster_rifle)
    upgrade_list_A.upgrade_with_weapon_entry(core.rotary_blaster)
    upgrade_list_A.upgrade_with_weapon_entry(core.heavy_blaster_rifle)
    upgrade_list_A.upgrade_with_weapon_entry(core.scatterblaster)

    # B

    upgrade_list_B = UpgradeList("B", base_model=clone_trooper)
    upgrade_list_B.select_upgrade_with_weapon_type(limit=1)
    upgrade_list_B.upgrade_with_weapon_entry(core.rocket_launcher)
    upgrade_list_B.upgrade_with_weapon_entry(core.mortar)
    upgrade_list_B.upgrade_with_weapon_entry(core.thermal_detonator)
    upgrade_list_B.upgrade_with_weapon_entry(core.ion_grenade)
    upgrade_list_B.upgrade_with_weapon_entry(core.frag_grenade)

    # C

    upgrade_list_C = UpgradeList("C", base_model=at_rt)
    upgrade_list_C.select_upgrade_with_weapon_type(
        replace_weapon=core.laser_cannon_mounted
    )
    upgrade_list_C.upgrade_with_weapon_entry(core.heavy_rotary_cannon_mounted)
    upgrade_list_C.upgrade_with_weapon_entry(core.heavy_flamethrower_mounted)

    # assign upgrade lists

    clone_trooper.add_upgrade_list([upgrade_list_A, upgrade_list_B])
    at_rt.add_upgrade_list(upgrade_list_C)

    # print all

    file.write(core.header)
    file.write(obi_wan_kenobi.write_statline())
    file.write(clone_sergeant.write_statline())
    file.write(clone_trooper.write_statline())
    file.write(at_rt.write_statline())

    file.write("\n")
    file.write(upgrade_list_A.write_upgrade_list())
    file.write("\n")
    file.write(upgrade_list_B.write_upgrade_list())
    file.write("\n")
    file.write(upgrade_list_C.write_upgrade_list())
