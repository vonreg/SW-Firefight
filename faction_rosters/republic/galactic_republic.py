from sw_firefight_engine.firefight import (
    Weapon,
    Model,
    ModelList,
    UpgradeList,
    letter_increment,
)
from sw_firefight_engine import core

tsv_file = "galactic_republic.tsv"

obi_wan_kenobi = Model(
    "Obi-Wan Kenobi",
    3,
    3,
    6,
    jedi=True,
    courage=True,
    deflect=True,
    jump=3,
    command=True,
    unique="Obi-Wan Kenobi",
    protector="Any",
    impervious=True,
)
obi_wan_kenobi.equip_weapon(core.lightsaber_master)
obi_wan_kenobi.equip_weapon(core.force_push)

anakin_skywalker = Model(
    "Anakin Skywalker",
    3,
    3,
    6,
    jedi=True,
    courage=True,
    fear=True,
    deflect=True,
    jump=3,
    command=True,
    unique="Anakin Skywalker",
    relentless=True,
    impervious=True,
)
anakin_skywalker.equip_weapon(core.lightsaber_heroic)
anakin_skywalker.equip_weapon(core.force_push)

ahsoka_tano_padawan = Model(
    "Ahsoka Tano (Padawan)",
    4,
    3,
    4,
    jedi=True,
    courage=True,
    relay=True,
    jump=3,
    deflect=True,
    unique="Ahsoka Tano",
)
ahsoka_tano_padawan.equip_weapon(core.lightsaber_basic)
ahsoka_tano_padawan.equip_weapon(core.force_push)

ahsoka_tano_commander = Model(
    "Ahsoka Tano (Commander)",
    3,
    3,
    5,
    jedi=True,
    courage=True,
    command=True,
    impervious=True,
    jump=3,
    deflect=True,
    unique="Ahsoka Tano",
)
ahsoka_twin_sabers = Weapon("Dual Lightsabers", "Melee", 5, pierce=2, deadly=2)
ahsoka_tano_commander.equip_weapon(ahsoka_twin_sabers)
ahsoka_tano_commander.equip_weapon(core.force_push)

jedi_master = Model(
    "Jedi Master",
    3,
    3,
    5,
    jedi=True,
    jump=3,
    deflect=True,
    courage=True,
    command=True,
    impervious=True,
)
jedi_master.equip_weapon(core.lightsaber_master)
jedi_master.equip_weapon(core.force_push)

jedi_knight = Model(
    "Jedi Knight", 3, 3, 4, jedi=True, jump=3, deflect=True, courage=True, command=True
)
jedi_knight.equip_weapon(core.lightsaber_knight)
jedi_knight.equip_weapon(core.force_push)

jedi_padawan = Model("Jedi Padawan", 4, 4, 3, jedi=True, jump=3, deflect=True)
jedi_padawan.equip_weapon(core.lightsaber_basic)

rex = Model(
    "Captain Rex",
    3,
    4,
    3,
    hero=True,
    command=True,
    spotter=1,
    take_cover=1,
    gunslinger=True,
    agile=True,
    unique="Rex",
)
rex.equip_weapon(core.dual_blaster_pistols)

clone_officer = Model(
    "Clone Officer",
    3,
    4,
    3,
    hero=True,
    take_cover=1,
)
clone_officer.equip_weapon(core.blaster_pistol)

clone_trooper = Model("Clone Trooper", 4, 4, 1)
clone_trooper.equip_weapon(core.blaster_carbine)

arc_trooper = Model("ARC Trooper", 3, 4, 1, impervious=True, scout=True, recon=4)
arc_trooper.equip_weapon(core.dual_blaster_pistols)

arf_tracker = Model(
    "ARF Tracker", 4, 4, 1, scout=True, spotter=True, disciplined=True, recon=5
)
arf_tracker.equip_weapon(core.dual_blaster_pistols)

massiff = Model(
    "Massiff",
    5,
    5,
    1,
    fast=True,
    scout=True,
    hunter="Target",
    companion="ARF Tracker",
    beast=True,
    recon=6,
    expendable=1,
)
massiff_claws = Weapon("Teeth and Claws", "Melee", 4, pierce=1)
massiff.equip_weapon(massiff_claws)

clone_scout_trooper = Model(
    "Clone Scout Trooper",
    4,
    5,
    1,
    scout=True,
    recon=6,
)
clone_scout_trooper.equip_weapon(core.blaster_carbine)

clone_commando = Model(
    "Clone Commando",
    3,
    4,
    1,
    impervious=True,
    scout=True,
    disciplined=True,
    shield=1,
    hunter="Target",
    recon=4,
    survivor=1,
)
reconfigurable_blaster = Weapon("Reconfigurable Blaster", 18, 4, suppressive=1)
sniper_config = Weapon("Sniper Config", "inf", 1, pierce=2, sniper=True, deadly=2)
anti_armour_config = Weapon("Anti-Armour Config", 12, 2, pierce=2, deadly=2)
grenade_launcher_config = Weapon(
    "Grenade Launcher Config", 18, 2, pierce=1, ammo=1, blast=3, indirect=True
)
clone_commando.equip_weapon(core.vibroblade)
clone_commando.equip_weapon(reconfigurable_blaster)

barc_speeder = Model(
    "BARC Speeder",
    4,
    4,
    3,
    vehicle=True,
    impact=2,
    fast=True,
    fly=True,
    scout=True,
    recon=5,
)
blaster_cannon_array = Weapon("Blaster Cannon Array", 18, 4, pierce=2, fixed="Front")
barc_speeder.equip_weapon(blaster_cannon_array)

heavy_barc_speeder = Model(
    "BARC Heavy Weapons Speeder",
    4,
    4,
    4,
    vehicle=True,
    impact=2,
    fast=True,
    fly=True,
    arsenal=2,
)
sidecar_laser = Weapon("Sidecar Light Repeating Blaster", 18, 4, fixed="Front, Rear")
sidecar_ion = Weapon("Sidecar Ion Repeater", 18, 3, ion=True, fixed="Front, Rear")
heavy_barc_speeder.equip_weapon(blaster_cannon_array)
heavy_barc_speeder.equip_weapon(sidecar_laser)

at_rt = Model(
    "AT-RT", 4, 3, 4, vehicle=True, fast=True, cover="Front", jump=3, impact=3
)
at_rt.equip_weapon(core.laser_cannon_mounted)
at_rt.equip_weapon(core.grenade_launcher)

astromech_droid = Model("Astromech Droid", 5, 5, 1, droid=True, repair=1, slow=True)
shock_pulse = Weapon("Shock Pulse", "Melee", 2, suppressive=1)
astromech_droid.equip_weapon(shock_pulse)

protocol_droid = Model(
    "Protocol Droid",
    5,
    5,
    1,
    droid=True,
    slow=True,
    noncombatant=True,
    manual_points_adjustment=8,
)

# To-Do
# BARC Speeder
# BARC Speeder w/ Sidecar
# Clone Commandos (2 W, thick armour, shield, impervious)
# Generic Jedi (with rank, force & lightsaber upgrades)

# -*- Upgrade lists -*-

# Rex Jetpack

label = "A"
upgrade_rex_equip = UpgradeList(label, base_model=rex)
upgrade_rex_equip.select_upgrade_with_model_changes_type()
upgrade_rex_equip.upgrade_with_model_changes_entry("Jetpack", fly=True, fast=True)

# Clone Officer Ranks

label = letter_increment(label)
upgrade_officer_rank = UpgradeList(label, base_model=clone_officer)
upgrade_officer_rank.select_upgrade_with_model_changes_type()
upgrade_officer_rank.upgrade_with_model_changes_entry("Lieutenant", relay=True)
upgrade_officer_rank.upgrade_with_model_changes_entry("Captain", command=True)
upgrade_officer_rank.upgrade_with_model_changes_entry(
    "Commander", command=True, take_cover=2
)
upgrade_officer_rank.upgrade_with_model_changes_entry(
    "ARC Commander", command=True, take_cover=2, impervious=True, scout=True
)
upgrade_officer_rank.upgrade_with_model_changes_entry(
    "Marshal Commander",
    command=True,
    spotter=2,
    take_cover=2,
)

# Clone Officer Equipment

label = letter_increment(label)
upgrade_officer_equip = UpgradeList(label, base_model=clone_officer)
upgrade_officer_equip.select_upgrade_with_model_changes_type()
upgrade_officer_equip.upgrade_with_model_changes_entry("Naval Uniform", defense=6)
upgrade_officer_equip.upgrade_with_model_changes_entry("Jetpack", fly=True, fast=True)

# Clone Officer Weapons

label = letter_increment(label)
upgrade_officer_weapons = UpgradeList(label, base_model=clone_officer)
upgrade_officer_weapons.select_upgrade_with_weapon_type(
    replace_weapon=core.blaster_pistol
)
upgrade_officer_weapons.upgrade_with_weapon_entry(core.dual_blaster_pistols)
upgrade_officer_weapons.upgrade_with_weapon_entry(core.blaster_carbine)
upgrade_officer_weapons.upgrade_with_weapon_entry(core.rotary_blaster)
upgrade_officer_weapons.upgrade_with_weapon_entry(core.heavy_blaster_rifle)
upgrade_officer_weapons.upgrade_with_weapon_entry(core.targeting_rifle)

# Clone Officer Dual Pistols

label = letter_increment(label)
upgrade_officer_sidearm = UpgradeList(label, base_model=clone_officer)
upgrade_officer_sidearm.select_upgrade_with_weapon_type()
upgrade_officer_sidearm.upgrade_with_weapon_entry(core.blaster_pistol)
upgrade_officer_sidearm.upgrade_with_weapon_entry(core.dual_blaster_pistols)

# Generic Officer Binoculars (Spotter[1])

label = letter_increment(label)
upgrade_electrobinoculars = UpgradeList(label)
upgrade_electrobinoculars.select_upgrade_with_rule_model_agnostic_type()
upgrade_electrobinoculars.upgrade_with_rule_model_agnostic_entry(
    "Electrobinoculars", spotter=1
)

# Clone weapons (replace)

label = letter_increment(label)
upgrade_clone_weapons = UpgradeList(label, base_model=clone_trooper)
upgrade_clone_weapons.select_upgrade_with_weapon_type(
    replace_weapon=core.blaster_carbine
)
upgrade_clone_weapons.upgrade_with_weapon_entry(core.blaster_pistol)
upgrade_clone_weapons.upgrade_with_weapon_entry(core.rotary_blaster)
upgrade_clone_weapons.upgrade_with_weapon_entry(core.heavy_blaster_rifle)
upgrade_clone_weapons.upgrade_with_weapon_entry(core.scatterblaster)

# Clone weapons (additional)

label = letter_increment(label)
upgrade_clone_weap_add = UpgradeList(label, base_model=clone_trooper)
upgrade_clone_weap_add.select_upgrade_with_weapon_type(limit=1)
upgrade_clone_weap_add.upgrade_with_weapon_entry(core.rocket_launcher)
upgrade_clone_weap_add.upgrade_with_weapon_entry(core.sniper_rifle)
upgrade_clone_weap_add.upgrade_with_weapon_entry(core.mortar)
upgrade_clone_weap_add.upgrade_with_weapon_entry(core.thermal_detonator)
upgrade_clone_weap_add.upgrade_with_weapon_entry(core.ion_grenade)
upgrade_clone_weap_add.upgrade_with_weapon_entry(core.frag_grenade)

# Clone Specialists

label = letter_increment(label)
upgrade_clone_specialists = UpgradeList(label, base_model=clone_trooper)
upgrade_clone_specialists.select_upgrade_with_model_changes_type()
upgrade_clone_specialists.upgrade_with_model_changes_entry("Veteran", disciplined=True)
upgrade_clone_specialists.upgrade_with_model_changes_entry(
    "ARF Trooper", scout=True, recon=5
)
upgrade_clone_specialists.upgrade_with_model_changes_entry("Medic", heal=1)
upgrade_clone_specialists.upgrade_with_model_changes_entry("Engineer", repair=1)
upgrade_clone_specialists.upgrade_with_model_changes_entry(
    "Comms Technician", relay=True
)
upgrade_clone_specialists.upgrade_with_model_changes_entry(
    "Jetpack Trooper", fly=True, fast=True
)
upgrade_clone_specialists.upgrade_with_model_changes_entry("Naval Uniform", defense=6)
upgrade_clone_specialists.upgrade_with_model_changes_entry(
    "Sergeant", wounds=2, disciplined=True, hero=True
)

# ARC Trooper Weapons

label = letter_increment(label)
upgrade_arc_weapons = UpgradeList(label, base_model=arc_trooper)
upgrade_arc_weapons.select_upgrade_with_weapon_type()
upgrade_arc_weapons.upgrade_with_weapon_entry(core.blaster_carbine)
upgrade_arc_weapons.upgrade_with_weapon_entry(core.rotary_blaster)
upgrade_arc_weapons.upgrade_with_weapon_entry(core.heavy_blaster_rifle)
upgrade_arc_weapons.upgrade_with_weapon_entry(core.targeting_rifle)

# ARC Trooper Grenades

label = letter_increment(label)
upgrade_arc_grenades = UpgradeList(label, base_model=arc_trooper)
upgrade_arc_grenades.select_upgrade_with_weapon_type(limit=1)
upgrade_arc_grenades.upgrade_with_weapon_entry(core.concussion_grenade)
upgrade_arc_grenades.upgrade_with_weapon_entry(core.thermal_detonator)
upgrade_arc_grenades.upgrade_with_weapon_entry(core.ion_grenade)
upgrade_arc_grenades.upgrade_with_weapon_entry(core.frag_grenade)
upgrade_arc_grenades.upgrade_with_weapon_entry(core.thermal_imploder)

# ARC Trooper Equipment (Jetpack)

label = letter_increment(label)
upgrade_arc_equip = UpgradeList(label, base_model=arc_trooper)
upgrade_arc_equip.select_upgrade_with_model_changes_type()
upgrade_arc_equip.upgrade_with_model_changes_entry("Jetpack", fly=True, fast=True)

# scout trooper

label = letter_increment(label)
upgrade_scout = UpgradeList(label, base_model=clone_scout_trooper)
upgrade_scout.select_upgrade_with_weapon_type(replace_weapon=core.blaster_carbine)
upgrade_scout.upgrade_with_weapon_entry(core.heavy_blaster_rifle)
upgrade_scout.upgrade_with_weapon_entry(core.targeting_rifle)

# Commando

label = letter_increment(label)
upgrade_commando_weaps = UpgradeList(label, base_model=clone_commando)
upgrade_commando_weaps.select_upgrade_with_weapon_type()
upgrade_commando_weaps.upgrade_with_weapon_entry(sniper_config)
upgrade_commando_weaps.upgrade_with_weapon_entry(anti_armour_config)
upgrade_commando_weaps.upgrade_with_weapon_entry(grenade_launcher_config)
upgrade_commando_weaps.upgrade_with_weapon_entry(core.thermal_detonator)
upgrade_commando_weaps.upgrade_with_weapon_entry(core.concussion_grenade)
upgrade_commando_weaps.upgrade_with_weapon_entry(core.ion_grenade)
upgrade_commando_weaps.upgrade_with_weapon_entry(core.sonic_imploder)
upgrade_commando_weaps.upgrade_with_weapon_entry(core.thermal_imploder)

# BARC weapons

label = letter_increment(label)
upgrade_barc_heavy = UpgradeList(label, base_model=heavy_barc_speeder)
upgrade_barc_heavy.select_upgrade_with_weapon_type(replace_weapon=sidecar_laser)
upgrade_barc_heavy.upgrade_with_weapon_entry(core.rocket_launcher)
upgrade_barc_heavy.upgrade_with_weapon_entry(sidecar_ion)

# AT-RT weapons

label = letter_increment(label)
upgrade_at_rt = UpgradeList(label, base_model=at_rt)
upgrade_at_rt.select_upgrade_with_weapon_type(replace_weapon=core.laser_cannon_mounted)
upgrade_at_rt.upgrade_with_weapon_entry(core.heavy_rotary_cannon_mounted)
upgrade_at_rt.upgrade_with_weapon_entry(core.heavy_flamethrower_mounted)

# R2-D2
label = letter_increment(label)
upgrade_r2d2 = UpgradeList(label, base_model=astromech_droid)
upgrade_r2d2.select_upgrade_with_model_changes_type()
upgrade_r2d2.upgrade_with_model_changes_entry(
    "R2-D2",
    survivor=True,
    impervious=True,
    quality=3,
    impact=1,
    unique="R2-D2",
)

# C-3PO
label = letter_increment(label)
upgrade_c3po = UpgradeList(label, base_model=protocol_droid)
upgrade_c3po.select_upgrade_with_model_changes_type()
upgrade_c3po.upgrade_with_model_changes_entry(
    "C-3PO",
    survivor=True,
    impervious=True,
    take_cover=2,
    manual_points_adjustment=-8,
    unique="C-3PO",
)

# assign upgrade lists

rex.add_upgrade_list(upgrade_rex_equip)
clone_officer.add_upgrade_list(upgrade_officer_rank)
clone_officer.add_upgrade_list(upgrade_officer_equip)
clone_officer.add_upgrade_list(upgrade_officer_weapons)
clone_officer.add_upgrade_list(upgrade_officer_sidearm)
clone_officer.add_upgrade_list(upgrade_electrobinoculars)
clone_trooper.add_upgrade_list([upgrade_clone_weapons, upgrade_clone_weap_add])
clone_trooper.add_upgrade_list(upgrade_clone_specialists)
clone_trooper.add_upgrade_list(upgrade_electrobinoculars)
arc_trooper.add_upgrade_list(upgrade_arc_weapons)
arc_trooper.add_upgrade_list(upgrade_arc_grenades)
arc_trooper.add_upgrade_list(upgrade_arc_equip)
clone_scout_trooper.add_upgrade_list(upgrade_scout)
clone_commando.add_upgrade_list(upgrade_commando_weaps)
heavy_barc_speeder.add_upgrade_list(upgrade_barc_heavy)
at_rt.add_upgrade_list(upgrade_at_rt)
astromech_droid.add_upgrade_list(upgrade_r2d2)
protocol_droid.add_upgrade_list(upgrade_c3po)

# collate model list

model_list = ModelList()
model_list.add_model_entry(obi_wan_kenobi)
model_list.add_model_entry(anakin_skywalker)
model_list.add_model_entry(ahsoka_tano_padawan)
model_list.add_model_entry(ahsoka_tano_commander)
model_list.add_model_entry(jedi_master)
model_list.add_model_entry(jedi_knight)
model_list.add_model_entry(jedi_padawan)
model_list.add_model_entry(rex)
model_list.add_model_entry(clone_officer)
model_list.add_model_entry(clone_trooper)
model_list.add_model_entry(arc_trooper)
model_list.add_model_entry(arf_tracker)
model_list.add_model_entry(massiff)
model_list.add_model_entry(clone_scout_trooper)
model_list.add_model_entry(clone_commando)
model_list.add_model_entry(barc_speeder)
model_list.add_model_entry(heavy_barc_speeder)
model_list.add_model_entry(at_rt)
model_list.add_model_entry(astromech_droid)
model_list.add_model_entry(protocol_droid)

# write latex file

model_list.file_write_latex("republic_roster.tabl")
upgrade_rex_equip.file_write_latex()
upgrade_officer_rank.file_write_latex()
upgrade_officer_equip.file_write_latex()
upgrade_officer_weapons.file_write_latex()
upgrade_officer_sidearm.file_write_latex()
upgrade_electrobinoculars.file_write_latex()
upgrade_clone_weapons.file_write_latex()
upgrade_clone_weap_add.file_write_latex()
upgrade_clone_specialists.file_write_latex()
upgrade_arc_weapons.file_write_latex()
upgrade_arc_grenades.file_write_latex()
upgrade_arc_equip.file_write_latex()
upgrade_scout.file_write_latex()
upgrade_commando_weaps.file_write_latex()
upgrade_barc_heavy.file_write_latex()
upgrade_at_rt.file_write_latex()
upgrade_r2d2.file_write_latex()
upgrade_c3po.file_write_latex()

# write tsv file

model_list.file_write_tsv(tsv_file)
upgrade_rex_equip.file_write_tsv(tsv_file)
upgrade_officer_rank.file_write_tsv(tsv_file)
upgrade_officer_equip.file_write_tsv(tsv_file)
upgrade_officer_weapons.file_write_tsv(tsv_file)
upgrade_officer_sidearm.file_write_tsv(tsv_file)
upgrade_electrobinoculars.file_write_tsv(tsv_file)
upgrade_clone_weapons.file_write_tsv(tsv_file)
upgrade_clone_weap_add.file_write_tsv(tsv_file)
upgrade_clone_specialists.file_write_tsv(tsv_file)
upgrade_arc_weapons.file_write_tsv(tsv_file)
upgrade_arc_grenades.file_write_tsv(tsv_file)
upgrade_arc_equip.file_write_tsv(tsv_file)
upgrade_scout.file_write_tsv(tsv_file)
upgrade_commando_weaps.file_write_tsv(tsv_file)
upgrade_barc_heavy.file_write_tsv(tsv_file)
upgrade_at_rt.file_write_tsv(tsv_file)
upgrade_r2d2.file_write_tsv(tsv_file)
upgrade_c3po.file_write_tsv(tsv_file)
