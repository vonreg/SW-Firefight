from sw_firefight_engine.firefight import (
    Weapon,
    Model,
    ModelList,
    UpgradeList,
    letter_increment,
)
from sw_firefight_engine import core

tsv_file = "seperatist_alliance.tsv"

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
dooku_lightning = Weapon(
    "Force Lightning", 12, 3, pierce=1, ion=True, suppressive=1, throw=True
)
dooku.equip_weapon(core.lightsaber_heroic)
dooku.equip_weapon(dooku_lightning)

general_grievous = Model(
    "General Grievous",
    3,
    3,
    8,
    villain=True,
    fear=True,
    relentless=True,
    command=True,
    impact=2,
    unique="Grievous",
)
grievous_trophy_lightsabers = Weapon("Trophy Lightsabers", "Melee", 12, rending=True)
general_grievous.equip_weapon(grievous_trophy_lightsabers)

darth_maul = Model(
    "Darth Maul",
    3,
    3,
    6,
    sith=True,
    fear=True,
    deflect=True,
    jump=3,
    fast=True,
    unique="Maul",
)
maul_double_lightsaber = Weapon(
    "Double-bladed Lightsaber", "Melee", 3, pierce=3, deadly=3
)  # edit this (core.lightsaber_master?)
darth_maul.equip_weapon(maul_double_lightsaber)
darth_maul.equip_weapon(core.saber_throw)

asajj_ventress = Model(
    "Asajj Ventress",
    4,
    4,
    5,
    sith=True,
    fear=True,
    hunter="Jedi",
    scout=True,
    fast=True,
    jump=3,
)
ventress_sabers = Weapon("Dual Lightsabers", "Melee", 5, pierce=2, deadly=2)
ventress_force_choke = Weapon("Force Choke", "Torrent", 1, pierce=4)
asajj_ventress.equip_weapon(ventress_sabers)
asajj_ventress.equip_weapon(ventress_force_choke)

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
bane_dual_pistols = Weapon("Dual Pistols", 18, 4, pierce=1, sniper=True)
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

b1_rocket_droid = Model("B1 Rocket Droid", 6, 6, 1, droid=True, expendable=1, fly=True)
b1_rocket_droid.equip_weapon(core.light_blaster_rifle)

d1_aerial_battle_droid = Model(
    "D1 Aerial Battle Droid", 6, 6, 1, droid=True, expendable=2, fly=True, fast=True
)
wing_blasters = Weapon("Wing Blasters", 12, 4)
d1_aerial_battle_droid.equip_weapon(wing_blasters)

b2_super_battle_droid = Model("B2 Super Battle Droid", 5, 5, 2, droid=True, slow=True)
wrist_blaster = Weapon("Wrist Blaster", 18, 3, pierce=1)
b2_super_battle_droid.equip_weapon(wrist_blaster)

b2_rp_super_battle_droid = Model(
    "B2-RP Super Battle Droid", 5, 5, 2, droid=True, fly=True
)
b2_rp_super_battle_droid.equip_weapon(wrist_blaster)

b2_super_rocket_trooper = Model(
    "B2 Super Rocket Trooper", 5, 5, 2, droid=True, fly=True, fast=True
)
dual_heavy_wrist_blasters = Weapon(
    "Dual Heavy Wrist Blasters", 12, 4, pierce=1, reciprocating=6
)
b2_super_rocket_trooper.equip_weapon(dual_heavy_wrist_blasters)

aqua_droid = Model("AQ Aqua Droid", 5, 5, 2, droid=True, slow=True)
aqua_droid.equip_weapon(core.light_laser_cannon)

bx_commando_droid = Model(
    "BX Commando Droid", 4, 5, 1, droid=True, fast=True, jump=3, scout=True, recon=4
)
bx_commando_droid.equip_weapon(core.blaster_carbine)

magnaguard = Model(
    "IG-100 Magnaguard",
    4,
    4,
    3,
    droid=True,
    protector="Unit",
    protector_key="Villain/Sith",
    relentless=True,
)
laser_dart = Weapon("Laser Dart", 12, 2, quickdraw=True)
magnaguard.equip_weapon(core.electrostaff)
magnaguard.equip_weapon(laser_dart)

droideka = Model(
    "Droideka", 4, 4, 3, vehicle="Droid", shield=2, free_special_rule="Roll"
)
blaster_cannons = Weapon(
    "Blaster Cannons", 24, 3, pierce=2, fixed="Front", suppressive=1
)
droideka.equip_weapon(blaster_cannons)

droideka_sniper = Model(
    "Droideka Sniper", 4, 4, 3, vehicle="Droid", cover="Front", free_special_rule="Roll"
)
sniper_cannon = Weapon(
    "Sniper Cannon",
    "inf",
    2,
    pierce=2,
    deadly=2,
    fixed="Front",
    suppressive=1,
    sniper=True,
)
droideka_sniper.equip_weapon(sniper_cannon)

dwarf_spider_droid = Model(
    "DSD1 Dwarf Spider Droid", 4, 3, 4, vehicle="Droid", slow=True
)
dwarf_spider_droid.equip_weapon(core.laser_cannon_mounted)

b1_emplacement_team = Model(
    "B1 Emplacement Team", 6, 6, 3, cover="Front", droid=True, emplacement=True
)
b1_emplacement_team.equip_weapon(core.light_blaster_cannon)

stap = Model(
    "STAP Rider",
    5,
    5,
    3,
    vehicle="Droid",
    impact=2,
    fast=True,
    fly=True,
    recon=6,
    scout=True,
)
stap_blaster_cannons = Weapon(
    "Blaster Cannons", 18, 3, pierce=2, fixed="Front", suppressive=1
)
stap.equip_weapon(stap_blaster_cannons)

# Crab Droid(s)
# Octuptarra
# Savage Opress; see Crime Lords

# -*- Upgrade lists -*-

# Grievous

label = "A"
upgrade_grievous = UpgradeList(label, base_model=general_grievous)
upgrade_grievous.select_upgrade_with_weapon_type()
upgrade_grievous.upgrade_with_weapon_entry(core.blaster_rifle)

# Cad Bane

label = letter_increment(label)
upgrade_bane = UpgradeList(label, base_model=cad_bane)
upgrade_bane.select_upgrade_with_weapon_type(limit=1)
upgrade_bane.upgrade_with_weapon_entry(core.whipcord_launcher)
upgrade_bane.upgrade_with_weapon_entry(core.wrist_flamer)

# super_tac

label = letter_increment(label)
upgrade_super_tac = UpgradeList(label, base_model=super_tactical_droid)
upgrade_super_tac.select_upgrade_with_weapon_type(replace_weapon=calculated_strikes)
vibroblade_mastery = Weapon("Vibroblade Mastery", "Melee", 4, rending=True)
upgrade_super_tac.upgrade_with_weapon_entry(vibroblade_mastery)

# D: electrobinoculars (Spotter[1])

label = letter_increment(label)
upgrade_electrobinoculars = UpgradeList(label)
upgrade_electrobinoculars.select_upgrade_with_rule_model_agnostic_type()
upgrade_electrobinoculars.upgrade_with_rule_model_agnostic_entry(
    "Electrobinoculars", spotter=1
)

# Targeting orders: Spotter[2]?

# B1 weapon (replace)

label = letter_increment(label)
upgrade_b1_weapons = UpgradeList(label, base_model=b1_battle_droid)
upgrade_b1_weapons.select_upgrade_with_weapon_type(
    replace_weapon=core.light_blaster_rifle, lose_expendable=True
)
upgrade_b1_weapons.upgrade_with_weapon_entry(core.heavy_blaster_rifle)
upgrade_b1_weapons.upgrade_with_weapon_entry(core.radiation_cannon)
upgrade_b1_weapons.upgrade_with_weapon_entry(core.sniper_rifle)

# B1 weapon (add)

label = letter_increment(label)
upgrade_b1_weap_add = UpgradeList(label, base_model=b1_battle_droid)
upgrade_b1_weap_add.select_upgrade_with_weapon_type(lose_expendable=True)
upgrade_b1_weap_add.upgrade_with_weapon_entry(core.rocket_launcher)

# G

# upgrade_list_G = UpgradeList("G", base_model=b1_rocket_droid)
# upgrade_list_G.select_upgrade_with_weapon_type()
# upgrade_list_G.upgrade_with_weapon_entry(fusion_cutter) # gives repair[1]

# B2 weapon (replace)

label = letter_increment(label)
upgrade_b2_weapons = UpgradeList(label, base_model=b2_super_battle_droid)
upgrade_b2_weapons.select_upgrade_with_weapon_type(replace_weapon=wrist_blaster)
wrist_repeater = Weapon("Wrist Repeater", 18, 4, pierce=1)
upgrade_b2_weapons.upgrade_with_weapon_entry(wrist_repeater)

# B2 weapon (add)

label = letter_increment(label)
upgrade_b2_weap_add = UpgradeList(label, base_model=b2_super_battle_droid)
upgrade_b2_weap_add.select_upgrade_with_weapon_type()
wrist_rocket = Weapon("Wrist Rocket", 30, 2, pierce=1, ammo=1, blast=3)
upgrade_b2_weap_add.upgrade_with_weapon_entry(wrist_rocket)

# BX weapon (replace)

label = letter_increment(label)
upgrade_bx_weapons = UpgradeList(label, base_model=bx_commando_droid)
upgrade_bx_weapons.select_upgrade_with_weapon_type(replace_weapon=core.blaster_carbine)
upgrade_bx_weapons.upgrade_with_weapon_entry(core.heavy_sniper_rifle)
# blaster&shield???

# BX weapon (add)

label = letter_increment(label)
upgrade_bx_weap_add = UpgradeList(label, base_model=bx_commando_droid)
upgrade_bx_weap_add.select_upgrade_with_weapon_type(limit=1)
upgrade_bx_weap_add.upgrade_with_weapon_entry(core.vibroblade)
upgrade_bx_weap_add.upgrade_with_weapon_entry(core.concussion_grenade)
upgrade_bx_weap_add.upgrade_with_weapon_entry(core.thermal_detonator)
upgrade_bx_weap_add.upgrade_with_weapon_entry(core.dioxis_grenade)

# Magnaguard weapon (replace)

label = letter_increment(label)
upgrade_magnaguard_weap = UpgradeList(label, base_model=magnaguard)
upgrade_magnaguard_weap.select_upgrade_with_weapon_type(
    replace_weapon=core.electrostaff
)
upgrade_magnaguard_weap.upgrade_with_weapon_entry(core.electrowhip)
upgrade_magnaguard_weap.upgrade_with_weapon_entry(core.rocket_launcher)

# Magnaguard weapon (add)

label = letter_increment(label)
upgrade_magnaguard_weap_add = UpgradeList(label, base_model=magnaguard)
upgrade_magnaguard_weap_add.select_upgrade_with_weapon_type(limit=1)
upgrade_magnaguard_weap_add.upgrade_with_weapon_entry(core.concussion_grenade)
upgrade_magnaguard_weap_add.upgrade_with_weapon_entry(core.thermal_detonator)
upgrade_magnaguard_weap_add.upgrade_with_weapon_entry(core.dioxis_grenade)

# Dwarf spider droid weapon

label = letter_increment(label)
upgrade_dsd = UpgradeList(label, base_model=dwarf_spider_droid)
upgrade_dsd.select_upgrade_with_weapon_type(replace_weapon=core.laser_cannon_mounted)
upgrade_dsd.upgrade_with_weapon_entry(core.ion_blaster_mounted)
upgrade_dsd.upgrade_with_weapon_entry(core.heavy_flamethrower_mounted)

# B1 emplacement team weapon

label = letter_increment(label)
upgrade_b1team_weapon = UpgradeList(label, base_model=b1_emplacement_team)
upgrade_b1team_weapon.select_upgrade_with_weapon_type(
    replace_weapon=core.light_blaster_cannon
)
upgrade_b1team_weapon.upgrade_with_weapon_entry(core.blaster_cannon)
upgrade_b1team_weapon.upgrade_with_weapon_entry(core.heavy_blaster_cannon)
upgrade_b1team_weapon.upgrade_with_weapon_entry(core.medium_repeating_blaster)
upgrade_b1team_weapon.upgrade_with_weapon_entry(core.heavy_repeating_blaster)

# assign upgrade lists

general_grievous.add_upgrade_list(upgrade_grievous)
cad_bane.add_upgrade_list(upgrade_bane)
super_tactical_droid.add_upgrade_list(upgrade_super_tac)
b1_battle_droid.add_upgrade_list(upgrade_electrobinoculars)
b1_battle_droid.add_upgrade_list([upgrade_b1_weapons, upgrade_b1_weap_add])
oom_security_droid.add_upgrade_list(upgrade_electrobinoculars)
b2_super_battle_droid.add_upgrade_list([upgrade_b2_weapons, upgrade_b2_weap_add])
bx_commando_droid.add_upgrade_list(upgrade_electrobinoculars)
bx_commando_droid.add_upgrade_list([upgrade_bx_weapons, upgrade_bx_weap_add])
magnaguard.add_upgrade_list(upgrade_electrobinoculars)
magnaguard.add_upgrade_list([upgrade_magnaguard_weap, upgrade_magnaguard_weap_add])
dwarf_spider_droid.add_upgrade_list(upgrade_dsd)
b1_emplacement_team.add_upgrade_list(upgrade_b1team_weapon)

# collate model list
model_list = ModelList()
model_list.add_model_entry(dooku)
model_list.add_model_entry(general_grievous)
model_list.add_model_entry(darth_maul)
model_list.add_model_entry(asajj_ventress)
model_list.add_model_entry(cad_bane)
model_list.add_model_entry(super_tactical_droid)
model_list.add_model_entry(tactical_droid)
model_list.add_model_entry(oom_command_droid)
model_list.add_model_entry(oom_security_droid)
model_list.add_model_entry(b1_battle_droid)
model_list.add_model_entry(b1_rocket_droid)
model_list.add_model_entry(d1_aerial_battle_droid)
model_list.add_model_entry(b2_super_battle_droid)
model_list.add_model_entry(b2_rp_super_battle_droid)
model_list.add_model_entry(b2_super_rocket_trooper)
model_list.add_model_entry(aqua_droid)
model_list.add_model_entry(bx_commando_droid)
model_list.add_model_entry(magnaguard)
model_list.add_model_entry(droideka)
model_list.add_model_entry(droideka_sniper)
model_list.add_model_entry(dwarf_spider_droid)
model_list.add_model_entry(stap)
model_list.add_model_entry(b1_emplacement_team)

# write latex file

model_list.file_write_latex("seperatist_roster.tabl")
upgrade_grievous.file_write_latex()
upgrade_bane.file_write_latex()
upgrade_super_tac.file_write_latex()
upgrade_electrobinoculars.file_write_latex()
upgrade_b1_weapons.file_write_latex()
upgrade_b1_weap_add.file_write_latex()
upgrade_b2_weapons.file_write_latex()
upgrade_b2_weap_add.file_write_latex()
upgrade_bx_weapons.file_write_latex()
upgrade_bx_weap_add.file_write_latex()
upgrade_magnaguard_weap.file_write_latex()
upgrade_magnaguard_weap_add.file_write_latex()
upgrade_dsd.file_write_latex()
upgrade_b1team_weapon.file_write_latex()


# write tsv file

model_list.file_write_tsv(tsv_file)
upgrade_grievous.file_write_tsv(tsv_file)
upgrade_bane.file_write_tsv(tsv_file)
upgrade_super_tac.file_write_tsv(tsv_file)
upgrade_electrobinoculars.file_write_tsv(tsv_file)
upgrade_b1_weapons.file_write_tsv(tsv_file)
upgrade_b1_weap_add.file_write_tsv(tsv_file)
upgrade_b2_weapons.file_write_tsv(tsv_file)
upgrade_b2_weap_add.file_write_tsv(tsv_file)
upgrade_bx_weapons.file_write_tsv(tsv_file)
upgrade_bx_weap_add.file_write_tsv(tsv_file)
upgrade_magnaguard_weap.file_write_tsv(tsv_file)
upgrade_magnaguard_weap_add.file_write_tsv(tsv_file)
upgrade_dsd.file_write_tsv(tsv_file)
upgrade_b1team_weapon.file_write_tsv(tsv_file)
