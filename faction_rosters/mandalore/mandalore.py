from sw_firefight_engine.firefight import (
    Weapon,
    Model,
    ModelList,
    UpgradeList,
    letter_increment,
)
from sw_firefight_engine import core

tsv_file = "mandalore.tsv"

# Common Mandalorian Weapons
jetpack_rocket = Weapon(
    "Jetpack Rocket", "inf", 2, pierce=1, ammo="Single Use", blast=3
)
dart_launcher = Weapon(
    "Dart Launcher", 18, 1, pierce=2, ammo="Single Use", disorient=True
)
gauntlet_blades = Weapon("Gauntlet Blades", "Melee", 4, rending=True)
# core: whipcord launcher
# core: wrist flamethrower

""" Core mandalorians """

mandalorian_captain = Model(
    "Mandalorian Captain",
    3,
    3,
    3,
    hero=True,
    fly=True,
    fast=True,
    impervious=True,
    relay=True,
    arsenal=2,
)
mandalorian_captain.equip_weapon(core.combat_training)
mandalorian_captain.equip_weapon(core.dual_blaster_pistols)
mandalorian_captain.equip_weapon(jetpack_rocket)

mandalorian = Model(
    "Mandalorian Warrior", 4, 3, 1, fly=True, fast=True, impervious=True
)
mandalorian.equip_weapon(core.combat_training)
mandalorian.equip_weapon(core.dual_blaster_pistols)

mandalorian_veteran = Model(
    "Mandalorian Veteran", 3, 3, 2, fly=True, fast=True, impervious=True
)
mandalorian_veteran.equip_weapon(core.combat_training)
mandalorian_veteran.equip_weapon(core.dual_blaster_pistols)

# -*- Upgrade lists -*-

# Mandalorian warrior weapons
label = "A"
upgrade_mando_weapons = UpgradeList("A", base_model=mandalorian)
upgrade_mando_weapons.select_upgrade_with_weapon_type(limit=2)
upgrade_mando_weapons.upgrade_with_weapon_entry(core.blaster_carbine)
upgrade_mando_weapons.upgrade_with_weapon_entry(core.sniper_rifle)
upgrade_mando_weapons.upgrade_with_weapon_entry(core.heavy_sniper_rifle)
upgrade_mando_weapons.upgrade_with_weapon_entry(jetpack_rocket)
upgrade_mando_weapons.upgrade_with_weapon_entry(core.whipcord_launcher)
upgrade_mando_weapons.upgrade_with_weapon_entry(dart_launcher)
upgrade_mando_weapons.upgrade_with_weapon_entry(core.wrist_flamer)
upgrade_mando_weapons.upgrade_with_weapon_entry(core.concussion_grenade)
upgrade_mando_weapons.upgrade_with_weapon_entry(core.thermal_detonator)
upgrade_mando_weapons.upgrade_with_weapon_entry(core.ion_grenade)

# Mandalorian veteran weapons
label = letter_increment(label)
upgrade_mando_vet_weapons = UpgradeList(label, base_model=mandalorian_veteran)
upgrade_mando_vet_weapons.select_upgrade_with_weapon_type(limit=2)
upgrade_mando_vet_weapons.upgrade_with_weapon_entry(core.blaster_carbine)
upgrade_mando_vet_weapons.upgrade_with_weapon_entry(core.sniper_rifle)
upgrade_mando_vet_weapons.upgrade_with_weapon_entry(core.heavy_sniper_rifle)
upgrade_mando_vet_weapons.upgrade_with_weapon_entry(jetpack_rocket)
upgrade_mando_vet_weapons.upgrade_with_weapon_entry(core.whipcord_launcher)
upgrade_mando_vet_weapons.upgrade_with_weapon_entry(dart_launcher)
upgrade_mando_vet_weapons.upgrade_with_weapon_entry(core.wrist_flamer)
upgrade_mando_vet_weapons.upgrade_with_weapon_entry(core.concussion_grenade)
upgrade_mando_vet_weapons.upgrade_with_weapon_entry(core.thermal_detonator)
upgrade_mando_vet_weapons.upgrade_with_weapon_entry(core.ion_grenade)

# assign upgrade lists
mandalorian.add_upgrade_list(upgrade_mando_weapons)
mandalorian_veteran.add_upgrade_list(upgrade_mando_vet_weapons)

# collate model lists
list_core = ModelList()
list_core.add_model_entry(mandalorian_captain)
list_core.add_model_entry(mandalorian)
list_core.add_model_entry(mandalorian_veteran)

# write latex files

list_core.file_write_latex("mandalore_core_roster.tabl")
upgrade_mando_weapons.file_write_latex()
upgrade_mando_vet_weapons.file_write_latex()

# write tsv files

list_core.file_write_tsv(tsv_file, list_title="Core")
upgrade_mando_weapons.file_write_tsv(tsv_file)
upgrade_mando_vet_weapons.file_write_tsv(tsv_file)

""" Nite Owls """

bo_katan = Model(
    "Bo-Katan Kryze",
    3,
    2,
    4,
    hero=True,
    impervious=True,
    arsenal=2,
    courage=True,
    fast=True,
    fly=True,
    command=True,
    shield=1,
)
darksaber_bo_katan = Weapon(
    "The Darksaber", "Melee", 3, pierce=3, deadly=3, unique="The Darksaber"
)
bo_katan.equip_weapon(gauntlet_blades)
bo_katan.equip_weapon(core.dual_blaster_pistols)
bo_katan.equip_weapon(jetpack_rocket)

ursa_wren_nite_owl = Model(
    "Ursa Wren",
    3,
    2,
    3,
    hero=True,
    impervious=True,
    arsenal=2,
    courage=True,
    fast=True,
    fly=True,
    relay=True,
)
ursa_wren_nite_owl.equip_weapon(core.dual_blaster_pistols)
ursa_wren_nite_owl.equip_weapon(jetpack_rocket)

# -*- Upgrade lists -*-

# Bo-Katan Darksaber

label = letter_increment(label)
upgrade_bo_darksaber = UpgradeList(label, base_model=bo_katan)
upgrade_bo_darksaber.select_upgrade_with_weapon_type(replace_weapon=gauntlet_blades)
upgrade_bo_darksaber.upgrade_with_weapon_entry(darksaber_bo_katan)

# Bo-Katan weapons

label = letter_increment(label)
upgrade_bo_weapon = UpgradeList(label, base_model=bo_katan)
upgrade_bo_weapon.select_upgrade_with_weapon_type()
upgrade_bo_weapon.upgrade_with_weapon_entry(core.whipcord_launcher)
upgrade_bo_weapon.upgrade_with_weapon_entry(dart_launcher)
upgrade_bo_weapon.upgrade_with_weapon_entry(core.wrist_flamer)
upgrade_bo_weapon.upgrade_with_weapon_entry(core.concussion_grenade)
upgrade_bo_weapon.upgrade_with_weapon_entry(core.thermal_detonator)
upgrade_bo_weapon.upgrade_with_weapon_entry(core.ion_grenade)

# assign upgrade lists

bo_katan.add_upgrade_list(upgrade_bo_darksaber)
bo_katan.add_upgrade_list(upgrade_bo_weapon)

# collate model lists

list_nite_owls = ModelList()
list_nite_owls.add_model_entry(bo_katan)
list_nite_owls.add_model_entry(ursa_wren_nite_owl)

# write latex files

list_nite_owls.file_write_latex("mandalore_nite_owls_roster.tabl")
upgrade_bo_darksaber.file_write_latex()
upgrade_bo_weapon.file_write_latex()

# write tsv files

list_nite_owls.file_write_tsv(tsv_file, list_title="Nite Owls", append=True)
upgrade_bo_darksaber.file_write_tsv(tsv_file)
upgrade_bo_weapon.file_write_tsv(tsv_file)
