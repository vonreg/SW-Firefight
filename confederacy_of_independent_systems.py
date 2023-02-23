from firefight.firefight import Weapon, Model, UpgradeList
from firefight import core

with open("confederacy_of_independent_systems.tsv", "w", encoding="utf-8") as file:

    dooku = Model(
        "Count Dooku",
        3,
        3,
        6,
        sith=True,
        fear=True,
        deflect=True,
        relentless=True,
        jump=3,
        unique="Dooku",
        impervious=True,
    )
    dooku_lightsaber = Weapon("Lightsaber", "Melee", 4, ap=3, deadly=3)
    dooku_lightning = Weapon("Force Lightning", 12, 3, ap=1, ion=True, suppressive=1)
    dooku.equip_weapon(dooku_lightsaber)
    dooku.equip_weapon(dooku_lightning)

    general_grievous = Model(
        "General Grievous",
        3,
        3,
        7,
        villain=True,
        fear=True,
        relentless=True,
        command=True,
        impact=2,
        unique="Grievous",
    )
    grievous_trophy_lightsabers = Weapon(
        "Trophy Lightsabers", "Melee", 10, rending=True
    )
    general_grievous.equip_weapon(grievous_trophy_lightsabers)

    darth_maul = Model(
        "Darth Maul",
        3,
        4,
        6,
        sith=True,
        fear=True,
        deflect=True,
        relentless=True,
        jump=3,
        unique="Maul",
    )
    maul_double_lightsaber = Weapon(
        "Double-bladed Lightsaber", "Melee", 4, ap=2, deadly=3
    )
    maul_saber_throw = Weapon("Saber Throw", 12, 2, ap=2, deadly=3, quickdraw=True)
    darth_maul.equip_weapon(maul_double_lightsaber)
    darth_maul.equip_weapon(maul_saber_throw)

    asajj_ventress = Model(
        "Asajj Ventress",
        4,
        4,
        5,
        sith=True,
        fear=True,
        relentless=True,
        hunter="Jedi",
        scout=True,
        fast=True,
        jump=6,
    )
    ventress_sabers = Weapon("Dual Lightsabers", "Melee", 6, ap=2, deadly=2)
    ventress_force_choke = Weapon("Force Choke", "Torrent", 1, ap=4)

    cad_bane = Model(
        "Cad Bane",
        3,
        4,
        5,
        villain=True,
        scout=True,
        courage=True,
        jump=6,
        unique="Cad Bane",
    )
    bane_dual_pistols = Weapon("Dual Pistols", 18, 4, ap=1, sniper=True)
    bane_electro_gauntlets = Weapon("Electro Gauntlets", "Melee", 4, suppressive=1)
    cad_bane.equip_weapon(bane_dual_pistols)
    cad_bane.equip_weapon(bane_electro_gauntlets)

    super_tactical_droid = Model(
        "Super Tactical Droid",
        3,
        4,
        3,
        villain=True,
        droid=True,
        command=True,
        relay=True,
        spotter=2,
        take_cover=1,
    )
    calculated_strikes = Weapon("Calculated Strikes", "Melee", 3)
    super_tactical_droid.equip_weapon(core.light_blaster_rifle)
    super_tactical_droid.equip_weapon(calculated_strikes)

    tactical_droid = Model(
        "Tactical Droid",
        4,
        4,
        2,
        villain=True,
        droid=True,
        command=True,
        spotter=1,
        take_cover=1,
    )
    tactical_droid.equip_weapon(core.light_blaster_rifle)

    oom_command_droid = Model(
        "OOM Command Droid", 5, 6, 1, villain=True, droid=True, relay=True, spotter=1
    )
    oom_command_droid.equip_weapon(core.light_blaster_rifle)

    oom_security_droid = Model(
        "OOM Security Droid",
        5,
        6,
        1,
        droid=True,
        expendable=1,
        protector="Unit",
        protector_key="OOM Command Droid",
    )
    oom_security_droid.equip_weapon(core.light_blaster_rifle)

    b1_battle_droid = Model("B1 Battle Droid", 6, 6, 1, droid=True, expendable=2)
    b1_battle_droid.equip_weapon(core.light_blaster_rifle)

    b1_rocket_droid = Model(
        "B1 Rocket Droid", 6, 6, 1, droid=True, expendable=1, fly=True
    )
    b1_rocket_droid.equip_weapon(core.light_blaster_rifle)

    d1_aerial_battle_droid = Model(
        "D1 Aerial Battle Droid", 6, 6, 1, droid=True, expendable=2, fly=True, fast=True
    )
    wing_blasters = Weapon("Wing Blasters", 12, 4)
    d1_aerial_battle_droid.equip_weapon(wing_blasters)

    b2_super_battle_droid = Model(
        "B2 Super Battle Droid", 5, 5, 2, droid=True, slow=True
    )
    wrist_blaster = Weapon("Wrist Blaster", 18, 3, ap=1)
    b2_super_battle_droid.equip_weapon(wrist_blaster)

    b2_rp_super_battle_droid = Model(
        "B2-RP Super Battle Droid", 5, 5, 2, droid=True, fly=True
    )
    b2_rp_super_battle_droid.equip_weapon(wrist_blaster)

    b2_super_rocket_trooper = Model(
        "B2 Super Rocket Trooper", 5, 5, 2, droid=True, fly=True, fast=True
    )
    dual_heavy_wrist_blasters = Weapon(
        "Dual Heavy Wrist Blasters", 12, 4, ap=1, reciprocating=6
    )
    b2_super_rocket_trooper.equip_weapon(dual_heavy_wrist_blasters)

    aqua_droid = Model("AQ Aqua Droid", 5, 5, 2, droid=True, slow=True)
    aqua_droid.equip_weapon(core.light_laser_cannon)

    bx_commando_droid = Model(
        "BX Commando Droid", 4, 5, 1, droid=True, fast=True, jump=3, scout=True
    )
    bx_commando_droid.equip_weapon(core.blaster_carbine)

    magnaguard = Model(
        "IG-100 Magnaguard", 4, 4, 3, droid=True, protector="Any", relentless=True
    )
    laser_dart = Weapon("Laser Dart", 12, 2, quickdraw=True)
    magnaguard.equip_weapon(core.electrostaff)
    magnaguard.equip_weapon(laser_dart)

    droideka = Model(
        "Droideka", 4, 4, 3, vehicle="Droid", shield=2, free_special_rule="Roll"
    )
    blaster_cannons = Weapon(
        "Blaster Cannons", 24, 3, ap=2, fixed="Front", suppressive=1
    )
    droideka.equip_weapon(blaster_cannons)

    dwarf_spider_droid = Model(
        "DSD1 Dwarf Spider Droid", 4, 3, 4, vehicle="Droid", slow=True
    )
    dwarf_spider_droid.equip_weapon(core.laser_cannon_mounted)

    b1_emplacement_team = Model(
        "B1 Emplacement Team", 6, 6, 3, cover="Front", droid=True, emplacement=True
    )
    b1_emplacement_team.equip_weapon(core.light_blaster_cannon)

    # Sniper Droideka
    # STAPs
    # Crab Droid(s)
    # Octuptarra
    # Droid Emplacement (various options)
    # Asajj Ventress
    # Savage Opress

    ### Upgrade lists ###

    # A

    upgrade_list_A = UpgradeList("A", base_model=general_grievous)
    upgrade_list_A.select_upgrade_with_weapon_type()
    upgrade_list_A.upgrade_with_weapon_entry(core.blaster_rifle)

    # B

    upgrade_list_B = UpgradeList("B", base_model=cad_bane)
    upgrade_list_B.select_upgrade_with_weapon_type(limit=1)
    upgrade_list_B.upgrade_with_weapon_entry(core.whipcord_launcher)
    upgrade_list_B.upgrade_with_weapon_entry(core.wrist_flamer)

    # C

    upgrade_list_C = UpgradeList("C", base_model=super_tactical_droid)
    upgrade_list_C.select_upgrade_with_weapon_type(replace_weapon=calculated_strikes)
    vibroblade_mastery = Weapon("Vibroblade Mastery", "Melee", 4, rending=True)
    upgrade_list_C.upgrade_with_weapon_entry(vibroblade_mastery)

    # D: electrobinoculars

    # E

    upgrade_list_E = UpgradeList("E", base_model=b1_battle_droid)
    upgrade_list_E.select_upgrade_with_weapon_type(lose_expendable=True)
    upgrade_list_E.upgrade_with_weapon_entry(core.rocket_launcher)

    # F

    upgrade_list_F = UpgradeList("F", base_model=b1_battle_droid)
    upgrade_list_F.select_upgrade_with_weapon_type(
        replace_weapon=core.light_blaster_rifle, lose_expendable=True
    )
    upgrade_list_F.upgrade_with_weapon_entry(core.heavy_blaster_rifle)
    upgrade_list_F.upgrade_with_weapon_entry(core.radiation_cannon)
    upgrade_list_F.upgrade_with_weapon_entry(core.sniper_rifle)

    # G

    # upgrade_list_G = UpgradeList("G", base_model=b1_rocket_droid)
    # upgrade_list_G.select_upgrade_with_weapon_type()
    # upgrade_list_G.upgrade_with_weapon_entry(fusion_cutter) # gives repair[1]

    # H

    upgrade_list_H = UpgradeList("H", base_model=b2_super_battle_droid)
    upgrade_list_H.select_upgrade_with_weapon_type(replace_weapon=wrist_blaster)
    wrist_repeater = Weapon("Wrist Repeater", 18, 4, ap=1)
    upgrade_list_H.upgrade_with_weapon_entry(wrist_repeater)

    # I

    upgrade_list_I = UpgradeList("I", base_model=b2_super_battle_droid)
    upgrade_list_I.select_upgrade_with_weapon_type()
    wrist_rocket = Weapon("Wrist Rocket", 30, 2, ap=1, ammo=1, blast=3)
    upgrade_list_I.upgrade_with_weapon_entry(wrist_rocket)

    # J

    upgrade_list_J = UpgradeList("J", base_model=bx_commando_droid)
    upgrade_list_J.select_upgrade_with_weapon_type(replace_weapon=core.blaster_carbine)
    upgrade_list_J.upgrade_with_weapon_entry(core.heavy_sniper_rifle)
    # blaster&shield???

    # K

    upgrade_list_K = UpgradeList("K", base_model=bx_commando_droid)
    upgrade_list_K.select_upgrade_with_weapon_type(limit=1)
    upgrade_list_K.upgrade_with_weapon_entry(core.vibroblade)
    upgrade_list_K.upgrade_with_weapon_entry(core.concussion_grenade)
    upgrade_list_K.upgrade_with_weapon_entry(core.thermal_detonator)
    upgrade_list_K.upgrade_with_weapon_entry(core.dioxis_grenade)

    # L

    upgrade_list_L = UpgradeList("L", base_model=magnaguard)
    upgrade_list_L.select_upgrade_with_weapon_type(replace_weapon=core.electrostaff)
    upgrade_list_L.upgrade_with_weapon_entry(core.electrowhip)
    upgrade_list_L.upgrade_with_weapon_entry(core.rocket_launcher)

    # M

    upgrade_list_M = UpgradeList("M", base_model=magnaguard)
    upgrade_list_M.select_upgrade_with_weapon_type(limit=1)
    upgrade_list_M.upgrade_with_weapon_entry(core.concussion_grenade)
    upgrade_list_M.upgrade_with_weapon_entry(core.thermal_detonator)
    upgrade_list_M.upgrade_with_weapon_entry(core.dioxis_grenade)

    # N

    upgrade_list_N = UpgradeList("N", base_model=dwarf_spider_droid)
    upgrade_list_N.select_upgrade_with_weapon_type(
        replace_weapon=core.laser_cannon_mounted
    )
    upgrade_list_N.upgrade_with_weapon_entry(core.ion_blaster_mounted)
    upgrade_list_N.upgrade_with_weapon_entry(core.heavy_flamethrower_mounted)

    # O

    upgrade_list_O = UpgradeList("O", base_model=b1_emplacement_team)
    upgrade_list_O.select_upgrade_with_weapon_type(
        replace_weapon=core.light_blaster_cannon
    )
    upgrade_list_O.upgrade_with_weapon_entry(core.blaster_cannon)
    upgrade_list_O.upgrade_with_weapon_entry(core.heavy_blaster_cannon)
    upgrade_list_O.upgrade_with_weapon_entry(core.medium_repeating_blaster)
    upgrade_list_O.upgrade_with_weapon_entry(core.heavy_repeating_blaster)

    general_grievous.add_upgrade_list(upgrade_list_A)
    cad_bane.add_upgrade_list(upgrade_list_B)
    super_tactical_droid.add_upgrade_list(upgrade_list_C)
    b1_battle_droid.add_upgrade_list([upgrade_list_E, upgrade_list_F])
    b2_super_battle_droid.add_upgrade_list([upgrade_list_H, upgrade_list_I])
    bx_commando_droid.add_upgrade_list([upgrade_list_J, upgrade_list_K])
    magnaguard.add_upgrade_list([upgrade_list_L, upgrade_list_M])
    dwarf_spider_droid.add_upgrade_list(upgrade_list_N)
    b1_emplacement_team.add_upgrade_list(upgrade_list_O)

    # print all

    file.write(core.header)
    file.write(dooku.write_statline())
    file.write(general_grievous.write_statline())
    file.write(darth_maul.write_statline())
    file.write(cad_bane.write_statline())
    file.write(super_tactical_droid.write_statline())
    file.write(tactical_droid.write_statline())
    file.write(oom_command_droid.write_statline())
    file.write(oom_security_droid.write_statline())
    file.write(b1_battle_droid.write_statline())
    file.write(b1_rocket_droid.write_statline())
    file.write(d1_aerial_battle_droid.write_statline())
    file.write(b2_super_battle_droid.write_statline())
    file.write(b2_rp_super_battle_droid.write_statline())
    file.write(b2_super_rocket_trooper.write_statline())
    file.write(aqua_droid.write_statline())
    file.write(bx_commando_droid.write_statline())
    file.write(magnaguard.write_statline())
    file.write(droideka.write_statline())
    file.write(dwarf_spider_droid.write_statline())
    file.write(b1_emplacement_team.write_statline())

    file.write("\n")
    file.write(upgrade_list_A.write_upgrade_list())
    file.write("\n")
    file.write(upgrade_list_B.write_upgrade_list())
    file.write("\n")
    file.write(upgrade_list_C.write_upgrade_list())
    file.write("\n")
    file.write(upgrade_list_E.write_upgrade_list())
    file.write("\n")
    file.write(upgrade_list_F.write_upgrade_list())
    file.write("\n")
    # file.write(upgrade_list_G.write_upgrade_list())
    # file.write("\n")
    file.write(upgrade_list_H.write_upgrade_list())
    file.write("\n")
    file.write(upgrade_list_I.write_upgrade_list())
    file.write("\n")
    file.write(upgrade_list_J.write_upgrade_list())
    file.write("\n")
    file.write(upgrade_list_K.write_upgrade_list())
    file.write("\n")
    file.write(upgrade_list_L.write_upgrade_list())
    file.write("\n")
    file.write(upgrade_list_M.write_upgrade_list())
    file.write("\n")
    file.write(upgrade_list_N.write_upgrade_list())
    file.write("\n")
    file.write(upgrade_list_O.write_upgrade_list())
