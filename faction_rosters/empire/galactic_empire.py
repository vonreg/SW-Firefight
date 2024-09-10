from sw_firefight_engine.firefight import (
    Weapon,
    Model,
    ModelList,
    UpgradeList,
    letter_increment,
)
from sw_firefight_engine import core

tsv_file = "galactic_empire.tsv"

emperor_palpatine = Model(
    "Emperor Palpatine",
    3,
    3,
    6,
    sith=True,
    fear=True,
    deflect=True,
    slow=True,
    jump=6,
    unique="Palpatine",
    impervious=True,
)
unlimited_power = Weapon(
    "Unlimited Power", "Torrent", 3, pierce=2, throw=True, ion=True, suppressive=2
)
emperor_palpatine.equip_weapon(unlimited_power)

darth_vader = Model(
    "Darth Vader",
    3,
    3,
    6,
    sith=True,
    fear=True,
    deflect=True,
    relentless=True,
    impervious=True,
    slow=True,
    jump=3,
    unique="Anakin Skywalker",
)
vader_lightsaber = Weapon("Lightsaber", "Melee", 4, pierce=4, deadly=3)
vader_force_choke = Weapon("Force Choke", 6, 1, pierce=4, seek=True, throw=True)
darth_vader.equip_weapon(vader_lightsaber)
darth_vader.equip_weapon(core.force_choke)

inquisitor = Model("Inquisitor", 4, 3, 4, villain=True, deflect=True, jump=3)
inquisitor.equip_weapon(core.lightsaber_knight)

isf_commander = Model(
    "ISF Commander", 3, 4, 3, villain=True, command=True, scout=True, recon=4
)
isf_commander.equip_weapon(core.blaster_rifle)
isf_commander.equip_weapon(core.combat_training)

stormtrooper_commander = Model(
    "Stormtrooper Commander", 3, 4, 3, villain=True, command=True
)
stormtrooper_commander.equip_weapon(core.blaster_rifle)

stormtrooper_captain = Model("Stormtrooper Captain", 4, 4, 3, villain=True, relay=True)
stormtrooper_captain.equip_weapon(core.blaster_rifle)

stormtrooper_sergeant = Model("Stormtrooper Sergeant", 4, 4, 2, villain=True)
stormtrooper_sergeant.equip_weapon(core.blaster_rifle)

imperial_officer = Model("Imperial Officer", 5, 6, 2, villain=True, take_cover=1)
imperial_officer.equip_weapon(core.blaster_pistol)

stormtrooper = Model("Stormtrooper", 5, 4, 1, expendable=1, disciplined=True)
stormtrooper.equip_weapon(core.blaster_rifle)

stormtrooper_heavy_mortar = Model(
    "Stormtrooper Heavy Mortar",
    5,
    4,
    1,
    disciplined=True,
    emplacement=True,
    slow=True,
)
stormtrooper_heavy_mortar.equip_weapon(core.heavy_mortar)
stormtrooper_heavy_mortar.equip_weapon(core.blaster_rifle)

imperial_army_trooper = Model("Imperial Army Trooper", 5, 5, 1, expendable=2)
imperial_army_trooper.equip_weapon(core.blaster_rifle)

imperial_riot_trooper = Model("Imperial Riot Trooper", 5, 4, 1, expendable=2)
imperial_riot_trooper.equip_weapon(core.truncheon)

scout_trooper = Model(
    "Scout Trooper", 5, 5, 1, expendable=1, scout=True, disciplined=True, recon=5
)
scout_trooper.equip_weapon(core.blaster_pistol)

isf_trooper = Model("ISF Trooper", 4, 4, 1, scout=True, recon=4)
isf_trooper.equip_weapon(core.blaster_rifle)

purge_trooper = Model("Purge Trooper", 3, 4, 1, hunter="Jedi", impervious=True)
purge_trooper.equip_weapon(core.blaster_rifle)

death_trooper = Model("Death Trooper", 3, 3, 2, fear=True)
death_trooper.equip_weapon(core.blaster_rifle)
death_trooper.equip_weapon(core.burst_pistol)

imperial_royal_guard = Model(
    "Imperial Royal Guard",
    3,
    4,
    3,
    protector="Unit",
    protector_key="Emperor Palpatine",
    courage=True,
    # duelist
)
force_pike = Weapon(
    "Force Pike",
    "Melee",
    3,
    pierce=1,
)
enhanced_force_pike = Weapon(
    "Enhanced Force Pike",
    "Melee",
    3,
    pierce=1,
    primary_fire_mode_name="Force Pike",
    secondary_fire_modes=[
        Weapon("Magnetic Clamp", 12, 1, nonlethal=True, immobilise=True)
    ],
)
imperial_royal_guard.equip_weapon(force_pike)
imperial_royal_guard.equip_weapon(core.heavy_blaster_pistol)

imp_speeder_bike = Model(
    "74-Z Speeder Bike",
    5,
    5,
    3,
    vehicle=True,
    impact=2,
    fast=True,
    fly=True,
    scout=True,
    recon=5,
)
speeder_blaster_cannon = Weapon("Light Blaster Cannon", 18, 3, pierce=2, fixed="Front")
imp_speeder_bike.equip_weapon(core.light_blaster_cannon)
imp_speeder_bike.equip_weapon(core.blaster_pistol)

e_web_team = Model(
    "E-Web Team",
    4,
    4,
    3,
    emplacement=True,
    slow=True,
    disciplined=True,
)
e_web = Weapon("E-Web", "inf", 3, pierce=2, deadly=2, fixed="Front")
e_web_team.equip_weapon(e_web)
blaster_rifles = Weapon("Blaster Rifles", 30, 6)
e_web_team.equip_weapon(blaster_rifles)

id_seeker_droid = Model(
    "ID Seeker Droid",
    5,
    5,
    1,
    droid=True,
    shield=1,
    protector="Any",
    scout=True,
    fly=True,
)
shock_pulse = Weapon("Shock Pulse", "Melee", 2, suppressive=1)
id_seeker_droid.equip_weapon(shock_pulse)

medical_droid = Model("Medical Droid", 6, 5, 1, droid=True, heal=1, slow=True)
lethal_injection = Weapon("Lethal Injection", "Melee", 1, deadly=3)
medical_droid.equip_weapon(lethal_injection)

astromech_droid = Model("Astromech Droid", 5, 5, 1, droid=True, repair=1, slow=True)
astromech_droid.equip_weapon(shock_pulse)

# -*- Upgrade lists -*-

# ISF Commander Ranged Replace

label = "A"
upgrade_isf_command_ranged = UpgradeList(label, base_model=isf_commander)
upgrade_isf_command_ranged.select_upgrade_with_weapon_type(
    replace_weapon=core.blaster_rifle
)
upgrade_isf_command_ranged.upgrade_with_weapon_entry(core.heavy_repeater)
upgrade_isf_command_ranged.upgrade_with_weapon_entry(core.heavy_sniper_rifle)
upgrade_isf_command_ranged.upgrade_with_weapon_entry(core.heavy_configurable_rifle)

# ISF Commander Melee Replace

label = letter_increment(label)
upgrade_isf_command_melee = UpgradeList(label, base_model=isf_commander)
upgrade_isf_command_melee.select_upgrade_with_weapon_type(
    replace_weapon=core.combat_training
)
vibroblades = Weapon("Vibroblades", "Melee", 4, rending=True)
upgrade_isf_command_melee.upgrade_with_weapon_entry(vibroblades)

# Generic Officer Binoculars (Spotter[1])

label = letter_increment(label)
upgrade_electrobinoculars = UpgradeList(label)
upgrade_electrobinoculars.select_upgrade_with_rule_model_agnostic_type()
upgrade_electrobinoculars.upgrade_with_rule_model_agnostic_entry(
    "Electrobinoculars", spotter=1
)

# Imperial officer armour

label = letter_increment(label)
upgrade_officer_armour = UpgradeList(label, base_model=imperial_officer)
upgrade_officer_armour.select_upgrade_with_model_changes_type(limit=1)
upgrade_officer_armour.upgrade_with_model_changes_entry("Combat Armour", defense=5)
upgrade_officer_armour.upgrade_with_model_changes_entry(
    "Heavy Combat Armour", defense=4
)

# Stormtrooper weapons (replace)

label = letter_increment(label)
upgrade_storm_weapons = UpgradeList(label, base_model=stormtrooper)
upgrade_storm_weapons.select_upgrade_with_weapon_type(
    replace_weapon=core.blaster_rifle, lose_expendable=True
)
upgrade_storm_weapons.upgrade_with_weapon_entry(core.burst_pistol)
upgrade_storm_weapons.upgrade_with_weapon_entry(core.heavy_blaster_rifle)
upgrade_storm_weapons.upgrade_with_weapon_entry(core.light_repeating_blaster)
upgrade_storm_weapons.upgrade_with_weapon_entry(core.reciprocating_blaster)
upgrade_storm_weapons.upgrade_with_weapon_entry(core.rotary_blaster)
upgrade_storm_weapons.upgrade_with_weapon_entry(core.sniper_rifle)
upgrade_storm_weapons.upgrade_with_weapon_entry(core.flamethrower)

# Stormtrooper weapons (additional)

label = letter_increment(label)
upgrade_storm_add_weap = UpgradeList(label, base_model=stormtrooper)
upgrade_storm_add_weap.select_upgrade_with_weapon_type(limit=1, lose_expendable=True)
upgrade_storm_add_weap.upgrade_with_weapon_entry(core.rocket_launcher)
upgrade_storm_add_weap.upgrade_with_weapon_entry(core.mortar)
upgrade_storm_add_weap.upgrade_with_weapon_entry(core.ion_disruptor)
upgrade_storm_add_weap.upgrade_with_weapon_entry(core.concussion_grenade)
upgrade_storm_add_weap.upgrade_with_weapon_entry(core.thermal_detonator)
upgrade_storm_add_weap.upgrade_with_weapon_entry(core.sonic_imploder)
upgrade_storm_add_weap.upgrade_with_weapon_entry(core.ion_grenade)
upgrade_storm_add_weap.upgrade_with_weapon_entry(core.thermal_imploder)

# Imperial army trooper weapon replace

label = letter_increment(label)
upgrade_army = UpgradeList(label, base_model=imperial_army_trooper)
upgrade_army.select_upgrade_with_weapon_type(
    replace_weapon=core.blaster_rifle, lose_expendable=True
)
upgrade_army.upgrade_with_weapon_entry(core.rotary_blaster)
upgrade_army.upgrade_with_weapon_entry(core.heavy_blaster_rifle)
upgrade_army.upgrade_with_weapon_entry(core.reciprocating_blaster)
upgrade_army.upgrade_with_weapon_entry(core.mortar)
upgrade_army.upgrade_with_weapon_entry(core.sniper_rifle)
upgrade_army.upgrade_with_weapon_entry(core.flamethrower)

# Imperial riot trooper weapon replace

label = letter_increment(label)
upgrade_army_riot = UpgradeList(label, base_model=imperial_riot_trooper)
upgrade_army_riot.select_upgrade_with_weapon_type(limit=1)
upgrade_army_riot.upgrade_with_weapon_entry(core.blaster_pistol)
upgrade_army_riot.upgrade_with_weapon_entry(core.burst_pistol)

# ISF weapons (replace)

label = letter_increment(label)
upgrade_isf_weapons = UpgradeList(label, base_model=isf_trooper)
upgrade_isf_weapons.select_upgrade_with_weapon_type(replace_weapon=core.blaster_rifle)
upgrade_isf_weapons.upgrade_with_weapon_entry(core.heavy_blaster_rifle)
upgrade_isf_weapons.upgrade_with_weapon_entry(core.sniper_rifle)
upgrade_isf_weapons.upgrade_with_weapon_entry(core.heavy_repeater)

# ISF weapons (additional)

label = letter_increment(label)
upgrade_isf_add_weap = UpgradeList(label, base_model=isf_trooper)
upgrade_isf_add_weap.select_upgrade_with_weapon_type(limit=1)
upgrade_isf_add_weap.upgrade_with_weapon_entry(core.concussion_grenade)
upgrade_isf_add_weap.upgrade_with_weapon_entry(core.thermal_detonator)
upgrade_isf_add_weap.upgrade_with_weapon_entry(core.sonic_imploder)
upgrade_isf_add_weap.upgrade_with_weapon_entry(core.ion_grenade)
upgrade_isf_add_weap.upgrade_with_weapon_entry(
    core.dioxis_grenade
)  # cheap compared to old calculator?
upgrade_isf_add_weap.upgrade_with_weapon_entry(core.thermal_imploder)

# ISF specialisms

label = letter_increment(label)
upgrade_isf_special = UpgradeList(label, base_model=isf_trooper)
upgrade_isf_special.select_upgrade_with_model_changes_type(limit=1)
upgrade_isf_special.upgrade_with_model_changes_entry("Electrobinoculars", spotter=1)
upgrade_isf_special.upgrade_with_model_changes_entry("Medic", heal=1)
upgrade_isf_special.upgrade_with_model_changes_entry("Engineer", repair=1)

# Purge Trooper weapon

label = letter_increment(label)
upgrade_purge = UpgradeList(label, base_model=purge_trooper)
upgrade_purge.select_upgrade_with_weapon_type(replace_weapon=core.blaster_rifle)
upgrade_purge.upgrade_with_weapon_entry(core.electrostaff)
upgrade_purge.upgrade_with_weapon_entry(core.heavy_blaster_rifle)
upgrade_purge.upgrade_with_weapon_entry(core.heavy_configurable_rifle)

# Death Trooper weapon (replace)

label = letter_increment(label)
upgrade_death_weap = UpgradeList(label, base_model=death_trooper)
upgrade_death_weap.select_upgrade_with_weapon_type(replace_weapon=core.blaster_rifle)
upgrade_death_weap.upgrade_with_weapon_entry(core.heavy_configurable_rifle)

# Death Trooper weapon (additional)

label = letter_increment(label)
upgrade_death_add_weap = UpgradeList(label, base_model=death_trooper)
upgrade_death_add_weap.select_upgrade_with_weapon_type(limit=1)
upgrade_death_add_weap.upgrade_with_weapon_entry(core.sonic_imploder)
upgrade_death_add_weap.upgrade_with_weapon_entry(core.frag_grenade)

# IRG Weapons

label = letter_increment(label)
upgrade_irg = UpgradeList(label, base_model=imperial_royal_guard)
upgrade_irg.select_upgrade_with_weapon_type(replace_weapon=force_pike)
upgrade_irg.upgrade_with_weapon_entry(core.electrostaff)
upgrade_irg.upgrade_with_weapon_entry(enhanced_force_pike)

# assign upgrade lists

isf_commander.add_upgrade_list(upgrade_isf_command_ranged)
isf_commander.add_upgrade_list(upgrade_isf_command_melee)
isf_commander.add_upgrade_list(upgrade_electrobinoculars)
stormtrooper_commander.add_upgrade_list(upgrade_electrobinoculars)
stormtrooper_captain.add_upgrade_list(upgrade_electrobinoculars)
stormtrooper_sergeant.add_upgrade_list(upgrade_electrobinoculars)
imperial_officer.add_upgrade_list(upgrade_electrobinoculars)
imperial_officer.add_upgrade_list(upgrade_officer_armour)
stormtrooper.add_upgrade_list([upgrade_storm_weapons, upgrade_storm_add_weap])
scout_trooper.add_upgrade_list(upgrade_electrobinoculars)
imperial_army_trooper.add_upgrade_list(upgrade_army)
imperial_riot_trooper.add_upgrade_list(upgrade_army_riot)
isf_trooper.add_upgrade_list([upgrade_isf_weapons, upgrade_isf_add_weap])
isf_trooper.add_upgrade_list(upgrade_isf_special)
purge_trooper.add_upgrade_list(upgrade_purge)
death_trooper.add_upgrade_list(upgrade_death_weap)
death_trooper.add_upgrade_list(upgrade_death_add_weap)
imperial_royal_guard.add_upgrade_list(upgrade_irg)

# collate model list

model_list = ModelList()
model_list.add_model_entry(emperor_palpatine)
model_list.add_model_entry(darth_vader)
model_list.add_model_entry(inquisitor)
model_list.add_model_entry(isf_commander)
model_list.add_model_entry(stormtrooper_commander)
model_list.add_model_entry(stormtrooper_captain)
model_list.add_model_entry(stormtrooper_sergeant)
model_list.add_model_entry(imperial_officer)
model_list.add_model_entry(stormtrooper)
model_list.add_model_entry(stormtrooper_heavy_mortar)
model_list.add_model_entry(imperial_army_trooper)
model_list.add_model_entry(imperial_riot_trooper)
model_list.add_model_entry(scout_trooper)
model_list.add_model_entry(isf_trooper)
model_list.add_model_entry(purge_trooper)
model_list.add_model_entry(death_trooper)
model_list.add_model_entry(imperial_royal_guard)
model_list.add_model_entry(imp_speeder_bike)
model_list.add_model_entry(e_web_team)
model_list.add_model_entry(id_seeker_droid)
model_list.add_model_entry(medical_droid)
model_list.add_model_entry(astromech_droid)

# write latex files

model_list.file_write_latex("empire_roster.tabl")

upgrade_isf_command_ranged.file_write_latex()
upgrade_isf_command_melee.file_write_latex()
upgrade_electrobinoculars.file_write_latex()
upgrade_officer_armour.file_write_latex()
upgrade_storm_weapons.file_write_latex()
upgrade_storm_add_weap.file_write_latex()
upgrade_army.file_write_latex()
upgrade_army_riot.file_write_latex()
upgrade_isf_weapons.file_write_latex()
upgrade_isf_add_weap.file_write_latex()
upgrade_isf_special.file_write_latex()
upgrade_purge.file_write_latex()
upgrade_death_weap.file_write_latex()
upgrade_death_add_weap.file_write_latex()
upgrade_irg.file_write_latex()

# write tsv files

model_list.file_write_tsv(tsv_file)

upgrade_isf_command_ranged.file_write_tsv(tsv_file)
upgrade_isf_command_melee.file_write_tsv(tsv_file)
upgrade_electrobinoculars.file_write_tsv(tsv_file)
upgrade_officer_armour.file_write_tsv(tsv_file)
upgrade_storm_weapons.file_write_tsv(tsv_file)
upgrade_storm_add_weap.file_write_tsv(tsv_file)
upgrade_army.file_write_tsv(tsv_file)
upgrade_army_riot.file_write_tsv(tsv_file)
upgrade_isf_weapons.file_write_tsv(tsv_file)
upgrade_isf_add_weap.file_write_tsv(tsv_file)
upgrade_isf_special.file_write_tsv(tsv_file)
upgrade_purge.file_write_tsv(tsv_file)
upgrade_death_weap.file_write_tsv(tsv_file)
upgrade_death_add_weap.file_write_tsv(tsv_file)
upgrade_irg.file_write_tsv(tsv_file)
