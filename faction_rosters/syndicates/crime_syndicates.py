from sw_firefight_engine.firefight import (
    Weapon,
    Model,
    ModelList,
    UpgradeList,
    letter_increment,
)
from sw_firefight_engine import core

tsv_file = "crime_syndicates.tsv"

""" Crimson Dawn """

# common weapons
percussive_cannon = Weapon(
    "Percussive Cannon", 15, 1, pierce=2, deadly=3, ammo=2, sniper=True, suppressive=1
)

# models
hylobon_captain = Model(
    "Hylobon Captain", 4, 5, 3, relay=True, villain=True, spotter=2, disciplined=True
)
hylobon_captain.equip_weapon(core.combat_training)
hylobon_captain.equip_weapon(percussive_cannon)

hylobon_enforcer = Model("Hylobon Enforcer", 5, 5, 1, disciplined=True)
hylobon_enforcer.equip_weapon(core.combat_training)
hylobon_enforcer.equip_weapon(percussive_cannon)

# collate model list

list_crimson_dawn = ModelList()
list_crimson_dawn.add_model_entry(hylobon_captain)
list_crimson_dawn.add_model_entry(hylobon_enforcer)

# write latex files

list_crimson_dawn.file_write_latex("syndicates_crimson_dawn_roster.tabl")

# write tsv files

list_crimson_dawn.file_write_tsv(tsv_file, list_title="Crimson Dawn")

""" Pyke Syndicate """

pyke_capo = Model("Pyke Capo", 4, 5, 3, command=True, take_cover=1, villain=True)
pyke_capo.equip_weapon(core.blaster_pistol)

pyke_soldier = Model("Pyke Soldier", 5, 5, 1, expendable=1)
pyke_soldier.equip_weapon(core.blaster_pistol)

# -*- Upgrade lists -*-

label = "A"
upgrade_pyke_replace = UpgradeList(label, base_model=pyke_soldier)
upgrade_pyke_replace.select_upgrade_with_weapon_type(replace_weapon=core.blaster_pistol)
upgrade_pyke_replace.upgrade_with_weapon_entry(core.blaster_rifle)

label = letter_increment(label)
upgrade_pyke_add = UpgradeList(label, base_model=pyke_soldier)
upgrade_pyke_add.select_upgrade_with_weapon_type(limit=1, lose_expendable=True)
upgrade_pyke_add.upgrade_with_weapon_entry(core.sniper_rifle)
upgrade_pyke_add.upgrade_with_weapon_entry(core.heavy_sniper_rifle)
upgrade_pyke_add.upgrade_with_weapon_entry(core.truncheon)
upgrade_pyke_add.upgrade_with_weapon_entry(core.stun_spear)
upgrade_pyke_add.upgrade_with_weapon_entry(core.electrowhip)
upgrade_pyke_add.upgrade_with_weapon_entry(core.thermal_detonator)
upgrade_pyke_add.upgrade_with_weapon_entry(core.concussion_grenade)
upgrade_pyke_add.upgrade_with_weapon_entry(core.ion_grenade)
upgrade_pyke_add.upgrade_with_weapon_entry(core.dioxis_grenade)
upgrade_pyke_add.upgrade_with_weapon_entry(core.frag_grenade)
upgrade_pyke_add.upgrade_with_weapon_entry(core.sonic_imploder)
upgrade_pyke_add.upgrade_with_weapon_entry(core.thermal_imploder)

# assign upgrade lists

pyke_soldier.add_upgrade_list(upgrade_pyke_replace)
pyke_soldier.add_upgrade_list(upgrade_pyke_add)

# collate model list

list_pykes = ModelList()
list_pykes.add_model_entry(pyke_capo)
list_pykes.add_model_entry(pyke_soldier)

# write latex files

list_pykes.file_write_latex("syndicates_pykes_roster.tabl")
upgrade_pyke_replace.file_write_latex()
upgrade_pyke_add.file_write_latex()

# write tsv files

list_pykes.file_write_tsv(tsv_file, list_title="Pyke Syndicate", append=True)
upgrade_pyke_replace.file_write_tsv(tsv_file)
upgrade_pyke_add.file_write_tsv(tsv_file)

""" Black Sun """

# common weapons
double_blaster = Weapon("Double Blaster", 9, 4, inaccurate=True)
mag_det = Weapon(
    "Mag-Det Charge",
    6,
    1,
    pierce=3,
    blast=3,
    deadly=2,
    indirect=True,
    seek=True,
    ammo="Single Use",
)

# models

black_sun_vigo = Model("Black Sun Vigo", 4, 4, 3, command=True, spotter=2, villain=True)
black_sun_vigo.equip_weapon(core.combat_training)
black_sun_vigo.equip_weapon(double_blaster)

black_sun_captain = Model(
    "Black Sun Captain", 4, 4, 3, relay=True, hunter="Target", villain=True
)
black_sun_captain.equip_weapon(core.combat_training)
black_sun_captain.equip_weapon(double_blaster)

black_sun_soldier = Model("Black Sun Enforcer", 4, 4, 1, expendable=1)
black_sun_soldier.equip_weapon(core.combat_training)
black_sun_soldier.equip_weapon(double_blaster)

# -*- Upgrade lists -*-

label = letter_increment(label)
upgrade_black_sun = UpgradeList(label, base_model=black_sun_soldier)
upgrade_black_sun.select_upgrade_with_weapon_type(limit=2, lose_expendable=True)
upgrade_black_sun.upgrade_with_weapon_entry(core.scattergun)
upgrade_black_sun.upgrade_with_weapon_entry(core.thermal_detonator)
upgrade_black_sun.upgrade_with_weapon_entry(core.concussion_grenade)
upgrade_black_sun.upgrade_with_weapon_entry(mag_det)
upgrade_black_sun.upgrade_with_weapon_entry(core.frag_grenade)
upgrade_black_sun.upgrade_with_weapon_entry(core.thermal_imploder)

# assign upgrade lists

black_sun_soldier.add_upgrade_list(upgrade_black_sun)

# collate model list

list_black_sun = ModelList()
list_black_sun.add_model_entry(black_sun_vigo)
list_black_sun.add_model_entry(black_sun_captain)
list_black_sun.add_model_entry(black_sun_soldier)

# write latex files

list_black_sun.file_write_latex("syndicates_black_sun_roster.tabl")
upgrade_black_sun.file_write_latex()

# write tsv files

list_black_sun.file_write_tsv(tsv_file, list_title="Black Sun", append=True)
upgrade_black_sun.file_write_tsv(tsv_file)

""" Crime Lords """

# common weapons
force_choke = Weapon("Force Choke", 6, 1, pierce=2, seek=True, throw=True)

# models
maul = Model(
    "Maul",
    3,
    4,
    6,
    sith=True,
    fear=True,
    deflect=True,
    jump=3,
    unique="Maul",
    command=True,
    impervious=True,
    free_special_rule="Crime Lord",
)
maul_lightsaber = Weapon("Lightsaber", "Melee", 3, pierce=2, deadly=3)
maul_darksaber = Weapon("The Darksaber", "Melee", 5, pierce=2, deadly=3)
maul_double_lightsaber = Weapon(
    "Double-bladed Lightsaber", "Melee", 4, pierce=3, deadly=3
)
maul_saber_throw = Weapon("Saber Throw", 12, 2, pierce=2, deadly=3, quickdraw=True)
maul.equip_weapon(maul_lightsaber)
maul.equip_weapon(maul_saber_throw)
maul.equip_weapon(force_choke)

savage = Model(
    "Savage Opress",
    4,
    3,
    6,
    sith=True,
    fear=True,
    jump=3,
    unique="Savage Opress",
    impervious=True,
    impact=2,
)
savage_double_lightsaber = Weapon(
    "Double-bladed Lightsaber", "Melee", 4, pierce=2, deadly=3
)
savage.equip_weapon(savage_double_lightsaber)
savage.equip_weapon(force_choke)

# -*- Upgrade lists -*-

label = letter_increment(label)
upgrade_maul = UpgradeList(label, base_model=maul)
upgrade_maul.select_upgrade_with_weapon_type(replace_weapon=maul_lightsaber)
upgrade_maul.upgrade_with_weapon_entry(maul_double_lightsaber)
upgrade_maul.upgrade_with_weapon_entry(maul_darksaber)

# assign upgrade lists

maul.add_upgrade_list(upgrade_maul)

# collate model list

list_lords = ModelList()
list_lords.add_model_entry(maul)
list_lords.add_model_entry(savage)

# write latex files

list_lords.file_write_latex("syndicates_crime_lords_roster.tabl")
upgrade_maul.file_write_latex()

# write tsv files

list_lords.file_write_tsv(tsv_file, list_title="Crime Lords", append=True)
upgrade_maul.file_write_tsv(tsv_file)

""" The Hutts """

# models
greedo = Model(
    "Greedo",
    5,
    5,
    3,
    villain=True,
    unique="Greedo",
    gunslinger=True,
)
greedo.equip_weapon(core.heavy_blaster_pistol)
greedo.equip_weapon(core.thermal_detonator)
greedo.equip_weapon(core.dioxis_grenade)

# collate model list

list_hutts = ModelList()
list_hutts.add_model_entry(greedo)

# write latex files

list_hutts.file_write_latex("syndicates_hutts_roster.tabl")

# write tsv files

list_hutts.file_write_tsv(tsv_file, list_title="The Hutts", append=True)
