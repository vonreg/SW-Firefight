from sw_firefight_engine.firefight import Weapon, Model, ModelList, UpgradeList
from sw_firefight_engine import core

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
grievous_trophy_lightsabers = Weapon("Trophy Lightsabers", "Melee", 10, rending=True)
general_grievous.equip_weapon(grievous_trophy_lightsabers)
general_grievous.equip_weapon(core.blaster_pistol)

d1_aerial_battle_droid = Model(
    "D1 Aerial Battle Droid", 6, 6, 1, droid=True, expendable=2, fly=True, fast=True
)
wing_blasters = Weapon("Wing Blasters", 12, 4)
d1_aerial_battle_droid.equip_weapon(wing_blasters)

b2_super_battle_droid = Model("B2 Super Battle Droid", 5, 5, 2, droid=True, slow=True)
wrist_blaster = Weapon("Wrist Blaster", 18, 3, pierce=1)
b2_super_battle_droid.equip_weapon(wrist_blaster)

upgrade_list_A = UpgradeList("A", base_model=general_grievous)
upgrade_list_A.select_upgrade_with_weapon_type()
upgrade_list_A.upgrade_with_weapon_entry(core.blaster_rifle)
upgrade_list_A.upgrade_with_weapon_entry(core.heavy_blaster_rifle)
upgrade_list_A.upgrade_with_weapon_entry(core.blaster_carbine)
upgrade_list_A.upgrade_with_weapon_entry(core.heavy_repeater)

upgrade_list_A.file_write_latex("upgrade_A.tex")

general_grievous.add_upgrade_list(upgrade_list_A)

model_list = ModelList()
model_list.add_model_entry(general_grievous)
model_list.add_model_entry(d1_aerial_battle_droid)
model_list.add_model_entry(b2_super_battle_droid)
model_list.add_model_entry(general_grievous)
model_list.file_write_latex("model_list.tex")
