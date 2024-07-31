from sw_firefight_engine.firefight import Weapon, Model, ModelList, UpgradeList
from sw_firefight_engine import core

file = "galactic_republic.tsv"

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
kenobi_lightsaber = Weapon("Lightsaber", "Melee", 4, pierce=3, deadly=3)
force_push = Weapon("Force Push", 12, 3, throw=True, seek=True, quickdraw=True)
obi_wan_kenobi.equip_weapon(kenobi_lightsaber)
obi_wan_kenobi.equip_weapon(force_push)

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
anakin_lightsaber = Weapon("Lightsaber", "Melee", 4, pierce=3, deadly=3)
anakin_skywalker.equip_weapon(anakin_lightsaber)
anakin_skywalker.equip_weapon(force_push)

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

# -*- Upgrade lists -*-

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
upgrade_list_C.select_upgrade_with_weapon_type(replace_weapon=core.laser_cannon_mounted)
upgrade_list_C.upgrade_with_weapon_entry(core.heavy_rotary_cannon_mounted)
upgrade_list_C.upgrade_with_weapon_entry(core.heavy_flamethrower_mounted)

# assign upgrade lists

clone_trooper.add_upgrade_list([upgrade_list_A, upgrade_list_B])
at_rt.add_upgrade_list(upgrade_list_C)

# collate model list

model_list = ModelList()
model_list.add_model_entry(obi_wan_kenobi)
model_list.add_model_entry(anakin_skywalker)
model_list.add_model_entry(clone_sergeant)
model_list.add_model_entry(clone_trooper)
model_list.add_model_entry(at_rt)

# write file

model_list.file_write_tsv(file)
upgrade_list_A.file_write_tsv(file)
upgrade_list_B.file_write_tsv(file)
upgrade_list_C.file_write_tsv(file)
