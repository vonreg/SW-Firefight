from sw_firefight_engine.firefight import (
    Weapon,
    Model,
    ModelList,
    UpgradeList,
    letter_increment,
)

tsv_file = "galactic_republic.tsv"

atte = Model(
    "AT-TE",
    4,
    3,
    4,
    arsenal=2,
    slow=True,
    impervious=True,
    vehicle="Heavy"
)
atte_mass_driver = Weapon(
    "Mass Driver Cannon",
    24,
    1,
    pierce=2,
    rending=True,
    deadly=3,
)
atte_front_lasers = Weapon(
    "Front Laser Cannons",
    12,
    4,
    fixed="Front",
    quickdraw=True,
)
atte_rear_lasers = Weapon(
    "Rear Laser Cannons",
    12,
    2,
    fixed="Rear",
    quickdraw=True,
)
atte.equip_weapon(atte_mass_driver)
atte.equip_weapon(atte_front_lasers)
atte.equip_weapon(atte_rear_lasers)

saber = Model(
    "Saber Tank",
    4,
    4,
    3,
    arsenal=2,
    vehicle="Heavy",
)
saber_cannons = Weapon(
    "Heavy Laser Cannons",
    18,
    2,
    pierce=2,
    fixed="Front",
)
saber_ordnance = Weapon(
    "Ordnance Launcher",
    12,
    2,
    pierce=2,
    seek=True,
    ammo=1,
    fixed="Front",
)
saber_turret_laser = Weapon(
    "Twin Laser Turret",
    15,
    2,
    pierce=1,
)
saber_turret_beam = Weapon(
    "Beam Cannon Turret",
    18,
    2,
    deadly=2,
    split_fire=True,
)
saber.equip_weapon(saber_cannons)
saber.equip_weapon(saber_ordnance)

label = "A"
upgrade_saber = UpgradeList(label, base_model=saber)
upgrade_saber.select_upgrade_with_weapon_type(limit=1)
upgrade_saber.upgrade_with_weapon_entry(saber_turret_laser)
upgrade_saber.upgrade_with_weapon_entry(saber_turret_beam)

saber.add_upgrade_list(upgrade_saber)

at_rt_squad = Model("AT-RT Squadron", 4, 5, 2, fast=True, vehicle=True)
at_rt_lasers = Weapon("Laser Cannons", 15, 3, pierce=1, quickdraw=True)
at_rt_squad.equip_weapon(at_rt_lasers)

barc_squad = Model(
    "BARC Speeder Squadron",
    4,
    6,
    2,
    fast=True,
    fly=True,
    scout=True,
    recon=5,
    vehicle=True,
)
barc_blasters = Weapon("Blaster Cannons", 12, 3, quickdraw=True)
barc_squad.equip_weapon(barc_blasters)

# collate model list

model_list = ModelList()
model_list.add_model_entry(atte)
model_list.add_model_entry(saber)
model_list.add_model_entry(at_rt_squad)
model_list.add_model_entry(barc_squad)

# write latex file

model_list.file_write_latex("republic_epic_roster.tabl")
upgrade_saber.file_write_latex()

# write tsv file

model_list.file_write_tsv(tsv_file)
upgrade_saber.file_write_tsv(tsv_file)
