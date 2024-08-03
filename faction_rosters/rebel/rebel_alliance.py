from sw_firefight_engine.firefight import (
    Weapon,
    Model,
    ModelList,
    UpgradeList,
    letter_increment,
)
from sw_firefight_engine import core

tsv_file = "rebel_alliance.tsv"

ben_kenobi = Model(
    "Old Ben Kenobi",
    3,
    3,
    6,
    jedi=True,
    courage=True,
    deflect=True,
    unique="Obi-Wan Kenobi",
    protector="Any",
    impervious=True,
)
kenobi_lightsaber = Weapon("Lightsaber", "Melee", 4, pierce=3, deadly=3)
jedi_mind_trick = Weapon("Jedi Mind Trick", 12, 3, nonlethal=True, disorient=True)
ben_kenobi.equip_weapon(kenobi_lightsaber)
ben_kenobi.equip_weapon(jedi_mind_trick)

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

# -*- Upgrade lists -*-

# Rebel weapons (replace)

label = "A"
upgrade_rebel_weapons = UpgradeList(label, base_model=rebel_trooper)
upgrade_rebel_weapons.select_upgrade_with_weapon_type(replace_weapon=core.blaster_rifle)
upgrade_rebel_weapons.upgrade_with_weapon_entry(core.rotary_blaster)
upgrade_rebel_weapons.upgrade_with_weapon_entry(core.heavy_blaster_rifle)
upgrade_rebel_weapons.upgrade_with_weapon_entry(core.sniper_rifle)
upgrade_rebel_weapons.upgrade_with_weapon_entry(core.scatterblaster)
upgrade_rebel_weapons.upgrade_with_weapon_entry(core.scattergun)
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

# AT-RT weapons

label = letter_increment(label)
upgrade_at_rt = UpgradeList(label, base_model=at_rt)
upgrade_at_rt.select_upgrade_with_weapon_type(replace_weapon=core.laser_cannon_mounted)
upgrade_at_rt.upgrade_with_weapon_entry(core.heavy_rotary_cannon_mounted)
upgrade_at_rt.upgrade_with_weapon_entry(core.heavy_flamethrower_mounted)

# assign upgrade lists

rebel_trooper.add_upgrade_list([upgrade_rebel_weapons, upgrade_rebel_weap_add])
at_rt.add_upgrade_list(upgrade_at_rt)

# collate model list

model_list = ModelList()
model_list.add_model_entry(ben_kenobi)
model_list.add_model_entry(rebel_captain)
model_list.add_model_entry(rebel_trooper)
model_list.add_model_entry(at_rt)

# write latex files

model_list.file_write_latex("rebel_roster.tabl")
upgrade_rebel_weapons.file_write_latex()
upgrade_rebel_weap_add.file_write_latex()
upgrade_at_rt.file_write_latex()

# write tsv files

model_list.file_write_tsv(tsv_file)
upgrade_rebel_weapons.file_write_tsv(tsv_file)
upgrade_rebel_weap_add.file_write_tsv(tsv_file)
upgrade_at_rt.file_write_tsv(tsv_file)
