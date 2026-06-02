from sw_firefight_engine.firefight import (
    Weapon,
    Model,
    ModelList,
    UpgradeList,
    letter_increment,
)
from sw_firefight_engine import core

tsv_file = "first_order.tsv"

megablaster = Weapon(
    "Portable Megablaster",
    30,
    4,
    pierce=1,
    inaccurate=True,
)
megablaster_mounted = Weapon(
    "Megablaster",
    "inf",
    4,
    pierce=2,
    fixed="Front",
    split_fire=True,
)

snoke = Model(
    "Supreme Leader Snoke",
    3,
    3,
    4,
    villain=True,
    dark_side=True,
    fear=True,
    deflect=True,
    slow=True,
    unique="Snoke",
    impervious=True,
)
force_defences = Weapon(
    "Force Defences",
    "Melee",
    8,
    seek=True,
    nonlethal=True,
    throw=True,
    suppressive=1,
)
snoke.equip_weapon(force_defences)
snoke.equip_weapon(core.force_push)

kylo_ren = Model(
    "Kylo Ren",
    3,
    3,
    5,
    villain=True,
    dark_side=True,
    fear=True,
    deflect=True,
    relentless=True,
    impervious=True,
    first_shot=True,
    jump=3,
    unique="Ben Solo",
)
ren_stasis = Weapon(
    "Force Stasis",
    12,
    2,
    pierce=2,
    nonlethal=True,
    seek=True,
    quickdraw=True,
    kinetic=True,
    immobilise=True,
)
kylo_ren.equip_weapon(core.lightsaber_knight)
kylo_ren.equip_weapon(core.force_choke)
kylo_ren.equip_weapon(ren_stasis)

fo_commander = Model(
    "First Order Commander",
    4,
    5,
    3,
    villain=True,
    spotter=1,
    command=True,
    disciplined=True,
)

fo_officer = Model(
    "First Order Officer", 5, 6, 2, villain=True, disciplined=True
)
fo_officer.equip_weapon(core.blaster_pistol)

stormtrooper_officer = Model("Stormtrooper Officer", 3, 4, 2, villain=True)
stormtrooper_officer.equip_weapon(core.combat_training)
stormtrooper_officer.equip_weapon(core.blaster_pistol)
stormtrooper_officer.equip_weapon(core.blaster_rifle)

stormtrooper = Model("Stormtrooper", 4, 4, 1, expendable=1)
stormtrooper.equip_weapon(core.light_blaster_rifle)

heavy_stormtrooper = Model(
    "Megablaster Heavy Trooper",
    4,
    4,
    1,
    emplacement=True,
    slow=True,
)
heavy_stormtrooper.equip_weapon(megablaster_mounted)
heavy_stormtrooper.equip_weapon(core.blaster_pistol)

flametrooper = Model(
    "Flametrooper",
    4,
    4,
    1,
    slow=True,
    impervious=True,
)
flametrooper.equip_weapon(core.flamethrower)

sith_trooper = Model(
    "MOVE Sith Trooper MOVE",
    4,
    4,
    1,
    disciplined=True,
    agile=True,
    impervious=True,
)
# sith_trooper.equip_weapon(core.combat_training)
sith_blaster = Weapon(
    "Sith Trooper Blaster",
    18,
    3,
    pierce=1,
    quickdraw=True,
    primary_fire_mode_name="Heavy Blaster Carbine",
    secondary_fire_modes=[
        Weapon("Bolt Launcher", 12, 1, pierce=2, deadly=3, ammo="Single Use")
    ],
)
sith_trooper.equip_weapon(sith_blaster)

# -*- Upgrade lists -*-

# Kylo Ren
label = "A"
upgrade_kylo = UpgradeList(label, base_model=kylo_ren)
upgrade_kylo.select_upgrade_with_model_changes_type(limit=1)
upgrade_kylo.upgrade_with_model_changes_entry(
    "Injured", wounds=4, quality=4, survivor=True, impervious=False
)
upgrade_kylo.upgrade_with_model_changes_entry(
    "Unbalanced", quality=4, impervious=False
)
upgrade_kylo.upgrade_with_model_changes_entry(
    "Supreme Leader",
    command=True,
)
upgrade_kylo.upgrade_with_model_changes_entry(
    "Ben Solo",
    fear=False,
    villain=False,
    dark_side=False,
    jedi=True,
    protector="Unit",
    protector_key="Rey",
    heal=1,
)

# FO Commander weapons

label = letter_increment(label)
upgrade_commander = UpgradeList(label, base_model=fo_commander)
upgrade_commander.select_upgrade_with_model_changes_type()
upgrade_commander.upgrade_with_model_changes_entry("Combat Armour", defense=4)
upgrade_commander.upgrade_with_model_changes_entry(
    "Field Agent", command=False, relay=True, agile=True
)
upgrade_commander.upgrade_with_model_changes_entry(
    "High Command", spotter=2, take_cover=1
)
upgrade_commander.upgrade_with_model_changes_entry(
    "Imperial Veteran", survivor=True
)
upgrade_commander.upgrade_with_model_changes_entry(
    "Allegiant General Pryde",
    spotter=1,
    take_cover=2,
    disciplined=True,
    survivor=True,
    unique="Enric Pryde",
)
upgrade_commander.upgrade_with_model_changes_entry(
    "General Hux",
    spotter=2,
    take_cover=1,
    disciplined=True,
    fear=True,
    unique="Armitage Hux",
)

label = letter_increment(label)
upgrade_commander_melee = UpgradeList(label, base_model=fo_commander)
upgrade_commander_melee.select_upgrade_with_weapon_type()
upgrade_commander_melee.upgrade_with_weapon_entry(core.combat_training)
upgrade_commander_melee.upgrade_with_weapon_entry(core.riot_baton)

label = letter_increment(label)
upgrade_commander_weapon = UpgradeList(label, base_model=fo_commander)
upgrade_commander_weapon.select_upgrade_with_weapon_type(limit=1)
upgrade_commander_weapon.upgrade_with_weapon_entry(core.blaster_pistol)
upgrade_commander_weapon.upgrade_with_weapon_entry(core.blaster_rifle)

# FO Officer roles

label = letter_increment(label)
upgrade_officer = UpgradeList(label, base_model=fo_officer)
upgrade_officer.select_upgrade_with_model_changes_type()
upgrade_officer.upgrade_with_model_changes_entry("Commlink", relay=True)
upgrade_officer.upgrade_with_model_changes_entry("Offensive Orders", spotter=2)
upgrade_officer.upgrade_with_model_changes_entry(
    "Defensive Orders", defend=True, take_cover=1
)

# Generic Officer Binoculars (Spotter[1])

label = letter_increment(label)
upgrade_electrobinoculars = UpgradeList(label)
upgrade_electrobinoculars.select_upgrade_with_rule_model_agnostic_type()
upgrade_electrobinoculars.upgrade_with_rule_model_agnostic_entry(
    "Electrobinoculars", spotter=1
)

# FO Stormtrooper Officers

label = letter_increment(label)
upgrade_storm_officer = UpgradeList(label, base_model=stormtrooper_officer)
upgrade_storm_officer.select_upgrade_with_model_changes_type()
upgrade_storm_officer.upgrade_with_model_changes_entry(
    "Sergeant",
    relay=True,
)
upgrade_storm_officer.upgrade_with_model_changes_entry(
    "Captain",
    wounds=3,
    command=True,
)
upgrade_storm_officer.upgrade_with_model_changes_entry(
    "Captain Cardinal",
    wounds=3,
    command=True,
    protector="Any",
    unique="Archex",
)
upgrade_storm_officer.upgrade_with_model_changes_entry(
    "Captain Phasma",
    wounds=3,
    command=True,
    impervious=True,
    relentless=True,
    unique="Phasma",
)

# Phasma's weapon
label = letter_increment(label)
upgrade_phasma_baton = UpgradeList(label, base_model=stormtrooper_officer)
upgrade_phasma_baton.select_upgrade_with_weapon_type(
    replace_weapon=core.combat_training
)
phasma_baton = Weapon(
    "Quicksilver Baton", "Melee", 4, pierce=2, wargear="Phasma"
)
upgrade_phasma_baton.upgrade_with_weapon_entry(phasma_baton)

# Stormtrooper weapons (replace)

label = letter_increment(label)
upgrade_storm_weapons = UpgradeList(label, base_model=stormtrooper)
upgrade_storm_weapons.select_upgrade_with_weapon_type(
    replace_weapon=core.light_blaster_rifle
)
upgrade_storm_weapons.upgrade_with_weapon_entry(core.blaster_pistol)
upgrade_storm_weapons.upgrade_with_weapon_entry(core.blaster_rifle)
upgrade_storm_weapons.upgrade_with_weapon_entry(core.blaster_carbine)

# Stormtrooper weapons (additional)

label = letter_increment(label)
upgrade_storm_add_weap = UpgradeList(label, base_model=stormtrooper)
upgrade_storm_add_weap.select_upgrade_with_weapon_type(limit=1)
upgrade_storm_add_weap.upgrade_with_weapon_entry(core.blaster_pistol)
upgrade_storm_add_weap.upgrade_with_weapon_entry(
    core.riot_baton
)  # lose expendable?
# laser axe (lose expendable)
# stun spear (lose expendable)
upgrade_storm_add_weap.upgrade_with_weapon_entry(
    megablaster, lose_expendable=True
)
# megablaster
# sniper megablaster
upgrade_storm_add_weap.upgrade_with_weapon_entry(
    core.grenade_launcher, lose_expendable=True
)
upgrade_storm_add_weap.upgrade_with_weapon_entry(
    core.homing_launcher, lose_expendable=True
)
upgrade_storm_add_weap.upgrade_with_weapon_entry(
    core.ion_torpedo, lose_expendable=True
)
upgrade_storm_add_weap.upgrade_with_weapon_entry(
    core.concussion_grenade, lose_expendable=True
)
upgrade_storm_add_weap.upgrade_with_weapon_entry(
    core.thermal_detonator, lose_expendable=True
)
upgrade_storm_add_weap.upgrade_with_weapon_entry(
    core.ion_grenade, lose_expendable=True
)
upgrade_storm_add_weap.upgrade_with_weapon_entry(
    core.thermal_imploder, lose_expendable=True
)

# Stormtrooper specialisms

label = letter_increment(label)
upgrade_storm_special = UpgradeList(label, base_model=stormtrooper)
upgrade_storm_special.select_upgrade_with_model_changes_type(limit=1)
upgrade_storm_special.upgrade_with_model_changes_entry(
    "Riot Shield", defense=3
)
upgrade_storm_special.upgrade_with_model_changes_entry(
    "Squad Leader",
    wounds=2,
    villain=True,
    disciplined=True,
)

# assign upgrade lists

kylo_ren.add_upgrade_list(upgrade_kylo)
fo_commander.add_upgrade_list(upgrade_commander)
fo_commander.add_upgrade_list(upgrade_commander_melee)
fo_commander.add_upgrade_list(upgrade_commander_weapon)
fo_officer.add_upgrade_list(upgrade_officer)
fo_officer.add_upgrade_list(upgrade_electrobinoculars)
stormtrooper_officer.add_upgrade_list(upgrade_electrobinoculars)
stormtrooper_officer.add_upgrade_list(upgrade_storm_officer)
stormtrooper_officer.add_upgrade_list(upgrade_phasma_baton)
stormtrooper.add_upgrade_list(upgrade_storm_weapons)
stormtrooper.add_upgrade_list(upgrade_storm_add_weap)
stormtrooper.add_upgrade_list(upgrade_storm_special)

# collate model list

model_list = ModelList()
model_list.add_model_entry(snoke)
model_list.add_model_entry(kylo_ren)
model_list.add_model_entry(fo_commander)
model_list.add_model_entry(fo_officer)
model_list.add_model_entry(stormtrooper_officer)
model_list.add_model_entry(stormtrooper)
model_list.add_model_entry(heavy_stormtrooper)
model_list.add_model_entry(flametrooper)
model_list.add_model_entry(sith_trooper)  # MOVE!!!!

# write latex files

model_list.file_write_latex("first_order_roster.tabl")

upgrade_kylo.file_write_latex()
upgrade_commander.file_write_latex()
upgrade_commander_melee.file_write_latex()
upgrade_commander_weapon.file_write_latex()
upgrade_officer.file_write_latex()
upgrade_phasma_baton.file_write_latex()
upgrade_electrobinoculars.file_write_latex()
upgrade_storm_officer.file_write_latex()
upgrade_storm_weapons.file_write_latex()
upgrade_storm_add_weap.file_write_latex()
upgrade_storm_special.file_write_latex()

# write tsv files

model_list.file_write_tsv(tsv_file)

upgrade_kylo.file_write_tsv(tsv_file)
upgrade_commander.file_write_tsv(tsv_file)
upgrade_commander_melee.file_write_tsv(tsv_file)
upgrade_commander_weapon.file_write_tsv(tsv_file)
upgrade_officer.file_write_tsv(tsv_file)
upgrade_phasma_baton.file_write_tsv(tsv_file)
upgrade_electrobinoculars.file_write_tsv(tsv_file)
upgrade_storm_officer.file_write_tsv(tsv_file)
upgrade_storm_weapons.file_write_tsv(tsv_file)
upgrade_storm_add_weap.file_write_tsv(tsv_file)
upgrade_storm_special.file_write_tsv(tsv_file)
