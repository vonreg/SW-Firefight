from sw_firefight_engine.firefight import (
    Weapon,
    Model,
    ModelList,
    UpgradeList,
    letter_increment,
)
from armoured_warfare.aw_core import armoured_warfare_special_rules as aw_rules

tsv_file = "separatist_alliance.tsv"

hover = aw_rules(hover=True)

mtt_aw_rules = aw_rules(transport=5)
mtt = Model(
    "MTT",
    4,
    3,
    5,
    slow=True,
    vehicle="Heavy, Droid",
    impervious=True,
    free_special_rule=mtt_aw_rules[0],
    manual_points_adjustment=mtt_aw_rules[1],
)
mtt_blasters = Weapon(
    "Blaster Cannons",
    18,
    2,
    pierce=2,
    fixed="Front",
    split_fire=True,
)
mtt.equip_weapon(mtt_blasters)

aat = Model(
    "AAT",
    4,
    3,
    3,
    arsenal=2,
    vehicle="Heavy, Droid"
)
aat_heavy_laser_turret = Weapon(
    "Heavy Laser Cannon",
    24,
    2,
    pierce=1,
    deadly=2,
)
aat_lasers = Weapon(
    "Laser Cannons",
    15,
    2,
    pierce=1,
    fixed="Front",
    quickdraw=True,
)
aat_ordnance = Weapon(
    "Ordnance Launcher",
    12,
    2,
    pierce=2,
    seek=True,
    ammo=1,
    fixed="Front",
)
aat.equip_weapon(aat_heavy_laser_turret)
aat.equip_weapon(aat_lasers)
aat.equip_weapon(aat_ordnance)

snail = Model(
    "NR-N99 Tank Droid",
    4,
    4,
    3,
    arsenal=2,
    vehicle="Heavy, Droid",
)
snail_blasters = Weapon(
    "Heavy Repeating Blasters",
    18,
    4,
    pierce=1,
    fixed="Front",
)
snail_ion = Weapon(
    "Ion Cannons",
    9,
    1,
    ion=True,
    ammo="Single Use",
    fixed="Front",
)
snail_ordnance = Weapon(
    "Ordnance Launcher",
    12,
    2,
    pierce=2,
    seek=True,
    ammo="Single Use",
    fixed="Front",
)
snail.equip_weapon(snail_blasters)
snail.equip_weapon(snail_ion)
snail.equip_weapon(snail_ordnance)

hailfire = Model(
    "Hailfire Droid",
    4,
    4,
    2,
    vehicle="Heavy, Droid",
    fast=True,
)
hailfire_missile = Weapon(
    "Hailfire Missile Launcher",
    24,
    1,
    rending=True,
    deadly=3,
    fixed="Front",
    indirect=True,
    seek=True,
    quickdraw=True,
    ammo=2,
    primary_fire_mode_name="Guided Missile",
    secondary_fire_modes=[
        Weapon(
            "Barrage",
            12,
            2,
            ammo="Single Use",
            blast=5,
            indirect=True,
            inaccurate=True,
            fixed="Front",
            quickdraw=True,
        )
    ]
)
hailfire.equip_weapon(hailfire_missile)

dwarf_spider_squad = Model("Dwarf Spider Droid Squadron", 4, 5, 2, vehicle="Droid", slow=True)
dwarf_spider_lasers = Weapon("Laser Cannons", 18, 2, sniper=True, pierce=2)
dwarf_spider_squad.equip_weapon(dwarf_spider_lasers)

stap_squad = Model(
    "STAP Speeder Squadron",
    4,
    6,
    2,
    fast=True,
    agile=True,
    scout=True,
    recon=5,
    vehicle="Droid",
    free_special_rule=hover[0],
    manual_points_adjustment=hover[1],
)
stap_blasters = Weapon("Blaster Cannons", 12, 3, quickdraw=True)
stap_squad.equip_weapon(stap_blasters)

# collate model list

model_list = ModelList()
model_list.add_model_entry(mtt)
model_list.add_model_entry(aat)
model_list.add_model_entry(snail)
model_list.add_model_entry(hailfire)
model_list.add_model_entry(dwarf_spider_squad)
model_list.add_model_entry(stap_squad)

# write latex file

model_list.file_write_latex("separatist_epic_roster.tabl")

# write tsv file

model_list.file_write_tsv(tsv_file)
