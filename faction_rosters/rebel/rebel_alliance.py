# to-do:
# Protocol droid, C3PO upgrade (take_cover!)
# Astromech, R2D2 (high quality)

from sw_firefight_engine.firefight import (
    Weapon,
    Model,
    ModelList,
    UpgradeList,
    letter_increment,
)
from sw_firefight_engine import core

tsv_file = "rebel_alliance.tsv"

luke_skywalker_hero = Model(
    "Luke Skywalker (Rebel Hero)",
    3,
    3,
    5,
    hero=True,
    courage=True,
    unique="Luke Skywalker",
)
anakin_lightsaber = Weapon(
    "Anakin's Lightsaber", "Melee", 3, pierce=2, deadly=2
)  # jedi padawan
luke_skywalker_hero.equip_weapon(core.heavy_blaster_pistol)
# upgrade to gain command?

luke_skywalker_jedi = Model(
    "Luke Skywalker (Jedi Knight)",
    3,
    3,
    6,
    jedi=True,
    courage=True,
    deflect=True,
    unique="Luke Skywalker",
    jump=3,
    relentless=True,
    impervious=True,
)
force_push = Weapon("Force Push", 12, 3, throw=True, seek=True, quickdraw=True)
luke_skywalker_jedi.equip_weapon(core.lightsaber_knight)
luke_skywalker_jedi.equip_weapon(force_push)
# upgrade to gain command?

ben_kenobi = Model(
    "Ben Kenobi",
    3,
    3,
    6,
    jedi=True,
    courage=True,
    deflect=True,
    unique="Obi-Wan Kenobi",
    command=True,
    protector="Any",
    impervious=True,
    survivor=True,
)
ben_kenobi.equip_weapon(core.lightsaber_master)
ben_kenobi.equip_weapon(core.heavy_blaster_pistol)

old_ben_kenobi = Model(
    "Old Ben Kenobi",
    3,
    4,
    5,
    jedi=True,
    courage=True,
    deflect=True,
    unique="Obi-Wan Kenobi",
    protector="Any",
)
old_ben_kenobi.equip_weapon(core.lightsaber_master)
old_ben_kenobi.equip_weapon(core.jedi_mind_trick)

ahsoka_tano = Model(
    "Ahsoka Tano",
    3,
    3,
    6,
    jedi=True,
    survivor=True,
    impervious=True,
    courage=True,
    jump=3,
    deflect=True,
    unique="Ahsoka Tano",
)
ahsoka_twin_sabers = Weapon("Dual Lightsabers", "Melee", 6, pierce=2, deadly=2)
ahsoka_tano.equip_weapon(ahsoka_twin_sabers)
ahsoka_tano.equip_weapon(core.force_push)

jedi_survivor = Model(
    "Jedi Survivor",
    3,
    3,
    5,
    jedi=True,
    survivor=True,
    impervious=True,
    courage=True,
    jump=3,
    deflect=True,
)
jedi_survivor.equip_weapon(core.lightsaber_knight)

leia = Model(
    "Princess Leia",
    3,
    5,
    4,
    command=True,
    courage=True,
    disciplined=True,
    hero=True,
    take_cover=2,
    unique="Leia Organa",
)
leia.equip_weapon(core.blaster_pistol)

han_solo = Model(
    "Han Solo", 3, 5, 4, hero=True, gunslinger=True, repair=1, unique="Han Solo"
)
han_solo.equip_weapon(core.heavy_blaster_pistol)
han_solo.equip_weapon(core.combat_training)

chewbacca = Model(
    "Chewbacca", 3, 4, 5, hero=True, fear=True, impact=2, repair=2, unique="Chewbacca"
)
bowcaster = Weapon("Bowcaster", 18, 1, pierce=2, deadly=3)
overwhelming_strength = Weapon(
    "Overwhelming Strength", "Melee", 3, rending=True, deadly=2
)
chewbacca.equip_weapon(bowcaster)
chewbacca.equip_weapon(overwhelming_strength)

lando = Model(
    "Lando Calrissian", 3, 5, 4, hero=True, unique="Lando Calrissian", gunslinger=True
)
lando.equip_weapon(core.sniper_pistol)

andor = Model(
    "Cassian Andor",
    3,
    5,
    3,
    hero=True,
    scout=True,
    recon=4,
    hunter="Target",
    relay=True,
)
andor.equip_weapon(core.blaster_pistol)

k2so = Model(
    "K-2SO",
    3,
    4,
    2,
    droid=True,
    hero=True,
    impervious=True,
    spotter=1,
    take_cover=1,
    companion="Cassian Andor",
)
k2so.equip_weapon(overwhelming_strength)  # from chewie

rebel_officer = Model(
    "Rebel Officer",
    4,
    5,
    3,
    hero=True,
    take_cover=1,
    spotter=1,
    command=True,
    disciplined=True,
)
rebel_officer.equip_weapon(core.heavy_blaster_pistol)

rebel_hero = Model(
    "Rebel Hero",
    3,
    5,
    3,
    hero=True,
    courage=True,
)
rebel_hero.equip_weapon(core.blaster_pistol)

rebel_gunslinger = Model(
    "Rebel Gunslinger",
    3,
    5,
    2,
    hero=True,
    gunslinger=True,
)
rebel_gunslinger.equip_weapon(core.blaster_pistol)
# upgrades: more pistol options, none with ammo

rebel_trooper = Model("Rebel Trooper", 4, 5, 1)
rebel_trooper.equip_weapon(core.blaster_rifle)

at_rt = Model(
    "AT-RT", 4, 3, 4, vehicle=True, fast=True, cover="Front", jump=3, impact=3
)
at_rt.equip_weapon(core.laser_cannon_mounted)
at_rt.equip_weapon(core.blaster_rifle)

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

# -*- Upgrade lists -*-

# Luke lightsaber

label = "A"
upgrade_luke_lightsaber = UpgradeList(label, base_model=luke_skywalker_hero)
upgrade_luke_lightsaber.select_upgrade_with_weapon_type()
upgrade_luke_lightsaber.upgrade_with_weapon_entry(anakin_lightsaber)

# Generic command upgrade

label = letter_increment(label)
upgrade_command = UpgradeList(label)
upgrade_command.select_upgrade_with_rule_model_agnostic_type()
upgrade_command.upgrade_with_rule_model_agnostic_entry("Leadership", command=True)

# Ben kenobi blaster -> force push

label = letter_increment(label)
upgrade_kenobi_blaster = UpgradeList(label, base_model=ben_kenobi)
upgrade_kenobi_blaster.select_upgrade_with_weapon_type(
    replace_weapon=core.heavy_blaster_pistol
)
upgrade_kenobi_blaster.upgrade_with_weapon_entry(force_push)

# Jedi survivor master lightsaber

label = letter_increment(label)
upgrade_jedi_lightsaber = UpgradeList(label, base_model=jedi_survivor)
upgrade_jedi_lightsaber.select_upgrade_with_weapon_type(
    replace_weapon=core.lightsaber_knight
)
upgrade_jedi_lightsaber.upgrade_with_weapon_entry(core.lightsaber_master)

# Jedi survivor sidearm and force power

label = letter_increment(label)
upgrade_jedi_sidearm = UpgradeList(label, base_model=jedi_survivor)
upgrade_jedi_sidearm.select_upgrade_with_weapon_type()
upgrade_jedi_sidearm.upgrade_with_weapon_entry(core.force_push)
upgrade_jedi_sidearm.upgrade_with_weapon_entry(core.jedi_mind_trick)
upgrade_jedi_sidearm.upgrade_with_weapon_entry(core.saber_throw)
upgrade_jedi_sidearm.upgrade_with_weapon_entry(core.blaster_pistol)
upgrade_jedi_sidearm.upgrade_with_weapon_entry(core.heavy_blaster_pistol)
upgrade_jedi_sidearm.upgrade_with_weapon_entry(core.burst_pistol)
upgrade_jedi_sidearm.upgrade_with_weapon_entry(core.bryar_pistol)

# Leia weapon

label = letter_increment(label)
upgrade_leia_weapon = UpgradeList(label, base_model=leia)
upgrade_leia_weapon.select_upgrade_with_weapon_type(replace_weapon=core.blaster_pistol)
upgrade_leia_weapon.upgrade_with_weapon_entry(core.blaster_carbine)
upgrade_leia_weapon.upgrade_with_weapon_entry(core.lightsaber_basic)

# Leia jedi

label = letter_increment(label)
upgrade_leia_jedi = UpgradeList(label, base_model=leia)
upgrade_leia_jedi.select_upgrade_with_weapon_type(replace_weapon=core.blaster_pistol)
upgrade_leia_jedi.upgrade_with_model_changes_entry(
    "Jedi Training",
    hero=False,
    jedi=True,
    jump=3,
    deflect=True,
)

# Andor Pistols

label = letter_increment(label)
upgrade_andor = UpgradeList(label, base_model=andor)
upgrade_andor.select_upgrade_with_weapon_type(replace_weapon=core.blaster_pistol)
upgrade_andor.upgrade_with_weapon_entry(core.bryar_pistol)
upgrade_andor.upgrade_with_weapon_entry(core.convertible_pistol)

# K2SO Pistol

label = letter_increment(label)
upgrade_k2so = UpgradeList(label, base_model=k2so)
upgrade_k2so.select_upgrade_with_weapon_type()
upgrade_k2so.upgrade_with_weapon_entry(core.burst_pistol)

# Rebel officer

label = letter_increment(label)
upgrade_officer = UpgradeList(label, base_model=rebel_officer)
upgrade_officer.select_upgrade_with_model_changes_type(limit=1)
upgrade_officer.upgrade_with_model_changes_entry("Pathfinder", scout=True, recon=5)
upgrade_officer.upgrade_with_model_changes_entry("Combat Armour", defense=4)
upgrade_officer.upgrade_with_model_changes_entry(
    "Saw Gererra",
    slow=True,
    fear=True,
    survivor=True,
    disciplined=False,
    unique="Saw Gerrera",
)

# Rebel hero

label = letter_increment(label)
upgrade_rebel_hero = UpgradeList(label, base_model=rebel_hero)
upgrade_rebel_hero.select_upgrade_with_model_changes_type(limit=2)
upgrade_rebel_hero.upgrade_with_model_changes_entry("Pathfinder", scout=True, recon=5)
upgrade_rebel_hero.upgrade_with_model_changes_entry("Veteran", disciplined=True)
upgrade_rebel_hero.upgrade_with_model_changes_entry("Mechanic", repair=1)
upgrade_rebel_hero.upgrade_with_model_changes_entry("Medic", heal=1)
upgrade_rebel_hero.upgrade_with_model_changes_entry("Comms Technician", relay=True)
upgrade_rebel_hero.upgrade_with_model_changes_entry("Leadership", command=True)
upgrade_rebel_hero.upgrade_with_model_changes_entry("Combat Armour", defense=4)
upgrade_rebel_hero.upgrade_with_model_changes_entry("Jetpack", fly=True, fast=True)
upgrade_rebel_hero.upgrade_with_model_changes_entry("Clone Survivor", survivor=True)

label = letter_increment(label)
upgrade_rebel_hero_weapons = UpgradeList(label, base_model=rebel_hero)
upgrade_rebel_hero_weapons.select_upgrade_with_weapon_type(
    replace_weapon=core.blaster_pistol
)
upgrade_rebel_hero_weapons.upgrade_with_weapon_entry(core.heavy_blaster_pistol)
upgrade_rebel_hero_weapons.upgrade_with_weapon_entry(core.dual_blaster_pistols)
upgrade_rebel_hero_weapons.upgrade_with_weapon_entry(core.bryar_pistol)
upgrade_rebel_hero_weapons.upgrade_with_weapon_entry(core.sniper_pistol)
upgrade_rebel_hero_weapons.upgrade_with_weapon_entry(core.convertible_pistol)
upgrade_rebel_hero_weapons.upgrade_with_weapon_entry(core.blaster_carbine)
upgrade_rebel_hero_weapons.upgrade_with_weapon_entry(core.blaster_rifle)
upgrade_rebel_hero_weapons.upgrade_with_weapon_entry(core.rotary_blaster)
upgrade_rebel_hero_weapons.upgrade_with_weapon_entry(core.heavy_blaster_rifle)
upgrade_rebel_hero_weapons.upgrade_with_weapon_entry(core.light_repeating_blaster)
upgrade_rebel_hero_weapons.upgrade_with_weapon_entry(core.sniper_rifle)

# Rebel weapons (replace)

label = letter_increment(label)
upgrade_rebel_weapons = UpgradeList(label, base_model=rebel_trooper)
upgrade_rebel_weapons.select_upgrade_with_weapon_type(replace_weapon=core.blaster_rifle)
upgrade_rebel_weapons.upgrade_with_weapon_entry(core.blaster_pistol)
upgrade_rebel_weapons.upgrade_with_weapon_entry(core.heavy_blaster_pistol)
upgrade_rebel_weapons.upgrade_with_weapon_entry(core.dual_blaster_pistols)
upgrade_rebel_weapons.upgrade_with_weapon_entry(core.convertible_pistol)
upgrade_rebel_weapons.upgrade_with_weapon_entry(core.blaster_carbine)
upgrade_rebel_weapons.upgrade_with_weapon_entry(core.rotary_blaster)
upgrade_rebel_weapons.upgrade_with_weapon_entry(core.heavy_blaster_rifle)
upgrade_rebel_weapons.upgrade_with_weapon_entry(core.light_repeating_blaster)
upgrade_rebel_weapons.upgrade_with_weapon_entry(core.scatterblaster)
upgrade_rebel_weapons.upgrade_with_weapon_entry(core.scattergun)
upgrade_rebel_weapons.upgrade_with_weapon_entry(core.targeting_rifle)
upgrade_rebel_weapons.upgrade_with_weapon_entry(core.sniper_rifle)
upgrade_rebel_weapons.upgrade_with_weapon_entry(core.heavy_sniper_rifle)
upgrade_rebel_weapons.upgrade_with_weapon_entry(core.cycler_rifle)

# Rebel weapons (additional)

label = letter_increment(label)
upgrade_rebel_weap_add = UpgradeList(label, base_model=rebel_trooper)
upgrade_rebel_weap_add.select_upgrade_with_weapon_type(limit=1)
upgrade_rebel_weap_add.upgrade_with_weapon_entry(core.homing_launcher)
upgrade_rebel_weap_add.upgrade_with_weapon_entry(core.grenade_launcher)
upgrade_rebel_weap_add.upgrade_with_weapon_entry(core.ion_torpedo)
upgrade_rebel_weap_add.upgrade_with_weapon_entry(core.rocket_launcher)
upgrade_rebel_weap_add.upgrade_with_weapon_entry(core.ion_disruptor)
upgrade_rebel_weap_add.upgrade_with_weapon_entry(core.concussion_grenade)
upgrade_rebel_weap_add.upgrade_with_weapon_entry(core.thermal_detonator)
upgrade_rebel_weap_add.upgrade_with_weapon_entry(core.ion_grenade)
upgrade_rebel_weap_add.upgrade_with_weapon_entry(core.frag_grenade)
upgrade_rebel_weap_add.upgrade_with_weapon_entry(core.thermal_imploder)

# rebel trooper upgrade types (choose 1):
# pathfinder (scout & recon)
# shock trooper (armour)
# clone veteran (survivor)

# rebel trooper specialisms:
# see rebel hero

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

luke_skywalker_hero.add_upgrade_list(upgrade_luke_lightsaber)
luke_skywalker_hero.add_upgrade_list(upgrade_command)
ben_kenobi.add_upgrade_list(upgrade_kenobi_blaster)
ahsoka_tano.add_upgrade_list(upgrade_command)
jedi_survivor.add_upgrade_list(upgrade_command)
jedi_survivor.add_upgrade_list(upgrade_jedi_lightsaber)
jedi_survivor.add_upgrade_list(upgrade_jedi_sidearm)
leia.add_upgrade_list(upgrade_leia_weapon)
leia.add_upgrade_list(upgrade_leia_jedi)
han_solo.add_upgrade_list(upgrade_command)
lando.add_upgrade_list(upgrade_command)
andor.add_upgrade_list(upgrade_andor)
k2so.add_upgrade_list(upgrade_k2so)
rebel_officer.add_upgrade_list(upgrade_officer)
rebel_hero.add_upgrade_list(upgrade_rebel_hero)
rebel_hero.add_upgrade_list(upgrade_rebel_hero_weapons)
rebel_trooper.add_upgrade_list([upgrade_rebel_weapons, upgrade_rebel_weap_add])
at_rt.add_upgrade_list(upgrade_at_rt)
astromech_droid.add_upgrade_list(upgrade_r2d2)
protocol_droid.add_upgrade_list(upgrade_c3po)

# collate model list

model_list = ModelList()
model_list.add_model_entry(luke_skywalker_hero)
model_list.add_model_entry(luke_skywalker_jedi)
model_list.add_model_entry(ben_kenobi)
model_list.add_model_entry(old_ben_kenobi)
model_list.add_model_entry(ahsoka_tano)
model_list.add_model_entry(jedi_survivor)
model_list.add_model_entry(leia)
model_list.add_model_entry(han_solo)
model_list.add_model_entry(chewbacca)
model_list.add_model_entry(lando)
model_list.add_model_entry(andor)
model_list.add_model_entry(k2so)
model_list.add_model_entry(rebel_officer)
model_list.add_model_entry(rebel_hero)
model_list.add_model_entry(rebel_gunslinger)
model_list.add_model_entry(rebel_trooper)
model_list.add_model_entry(at_rt)
model_list.add_model_entry(astromech_droid)
model_list.add_model_entry(protocol_droid)

# write latex files

model_list.file_write_latex("rebel_roster.tabl")
upgrade_luke_lightsaber.file_write_latex()
upgrade_command.file_write_latex()
upgrade_kenobi_blaster.file_write_latex()
upgrade_jedi_lightsaber.file_write_latex()
upgrade_jedi_sidearm.file_write_latex()
upgrade_leia_weapon.file_write_latex()
upgrade_leia_jedi.file_write_latex()
upgrade_andor.file_write_latex()
upgrade_k2so.file_write_latex()
upgrade_officer.file_write_latex()
upgrade_rebel_hero.file_write_latex()
upgrade_rebel_hero_weapons.file_write_latex()
upgrade_rebel_weapons.file_write_latex()
upgrade_rebel_weap_add.file_write_latex()
upgrade_at_rt.file_write_latex()
upgrade_r2d2.file_write_latex()
upgrade_c3po.file_write_latex()

# write tsv files

model_list.file_write_tsv(tsv_file)
upgrade_luke_lightsaber.file_write_tsv(tsv_file)
upgrade_command.file_write_tsv(tsv_file)
upgrade_kenobi_blaster.file_write_tsv(tsv_file)
upgrade_jedi_lightsaber.file_write_tsv(tsv_file)
upgrade_jedi_sidearm.file_write_tsv(tsv_file)
upgrade_leia_weapon.file_write_tsv(tsv_file)
upgrade_leia_jedi.file_write_tsv(tsv_file)
upgrade_andor.file_write_tsv(tsv_file)
upgrade_k2so.file_write_tsv(tsv_file)
upgrade_officer.file_write_latex(tsv_file)
upgrade_rebel_hero.file_write_tsv(tsv_file)
upgrade_rebel_hero_weapons.file_write_tsv(tsv_file)
upgrade_rebel_weapons.file_write_tsv(tsv_file)
upgrade_rebel_weap_add.file_write_tsv(tsv_file)
upgrade_at_rt.file_write_tsv(tsv_file)
upgrade_r2d2.file_write_tsv(tsv_file)
upgrade_c3po.file_write_tsv(tsv_file)
