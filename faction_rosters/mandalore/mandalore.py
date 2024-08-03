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

mandalorian_commando = Model(
    "Mandalorian Commando", 3, 3, 2, fly=True, fast=True, impervious=True
)
mandalorian_commando.equip_weapon(core.combat_training)
mandalorian_commando.equip_weapon(core.dual_blaster_pistols)

beskad_duelist = Model(
    "Beskad Duelist",
    3,
    3,
    2,
    fly=True,
    fast=True,
    impervious=True,
)
beskad = Weapon("Beskad", "Melee", 4, pierce=2, rending=True)
beskad_duelist.equip_weapon(beskad)
beskad_duelist.equip_weapon(core.dual_blaster_pistols)

scavenged_at_rt = Model(
    "Scavenged AT-RT",
    4,
    3,
    4,
    vehicle=True,
    fast=True,
    cover="Front",
    jump=3,
    impact=3,
)
scavenged_at_rt.equip_weapon(core.laser_cannon_mounted)
scavenged_at_rt.equip_weapon(core.blaster_rifle)

# -*- Upgrade lists -*-

# Mandalorian warrior weapons
label = "A"
upgrade_mando_weapons = UpgradeList("A", base_model=mandalorian)
upgrade_mando_weapons.select_upgrade_with_weapon_type(limit=2)
upgrade_mando_weapons.upgrade_with_weapon_entry(core.blaster_carbine)
upgrade_mando_weapons.upgrade_with_weapon_entry(core.targeting_rifle)
upgrade_mando_weapons.upgrade_with_weapon_entry(core.sniper_rifle)
upgrade_mando_weapons.upgrade_with_weapon_entry(core.heavy_sniper_rifle)
upgrade_mando_weapons.upgrade_with_weapon_entry(jetpack_rocket)
upgrade_mando_weapons.upgrade_with_weapon_entry(core.whipcord_launcher)
upgrade_mando_weapons.upgrade_with_weapon_entry(dart_launcher)
upgrade_mando_weapons.upgrade_with_weapon_entry(core.wrist_flamer)
upgrade_mando_weapons.upgrade_with_weapon_entry(core.concussion_grenade)
upgrade_mando_weapons.upgrade_with_weapon_entry(core.thermal_detonator)
upgrade_mando_weapons.upgrade_with_weapon_entry(core.ion_grenade)

# Mandalorian commando weapons
label = letter_increment(label)
upgrade_mando_vet_weapons = UpgradeList(label, base_model=mandalorian_commando)
upgrade_mando_vet_weapons.select_upgrade_with_weapon_type(limit=2)
upgrade_mando_vet_weapons.upgrade_with_weapon_entry(core.blaster_carbine)
upgrade_mando_vet_weapons.upgrade_with_weapon_entry(core.targeting_rifle)
upgrade_mando_vet_weapons.upgrade_with_weapon_entry(core.sniper_rifle)
upgrade_mando_vet_weapons.upgrade_with_weapon_entry(core.heavy_sniper_rifle)
upgrade_mando_vet_weapons.upgrade_with_weapon_entry(jetpack_rocket)
upgrade_mando_vet_weapons.upgrade_with_weapon_entry(core.whipcord_launcher)
upgrade_mando_vet_weapons.upgrade_with_weapon_entry(dart_launcher)
upgrade_mando_vet_weapons.upgrade_with_weapon_entry(core.wrist_flamer)
upgrade_mando_vet_weapons.upgrade_with_weapon_entry(core.concussion_grenade)
upgrade_mando_vet_weapons.upgrade_with_weapon_entry(core.thermal_detonator)
upgrade_mando_vet_weapons.upgrade_with_weapon_entry(core.ion_grenade)

# AT-RT weapons

label = letter_increment(label)
upgrade_at_rt = UpgradeList(label, base_model=scavenged_at_rt)
upgrade_at_rt.select_upgrade_with_weapon_type(replace_weapon=core.laser_cannon_mounted)
upgrade_at_rt.upgrade_with_weapon_entry(core.heavy_rotary_cannon_mounted)
upgrade_at_rt.upgrade_with_weapon_entry(core.heavy_flamethrower_mounted)

# assign upgrade lists
mandalorian.add_upgrade_list(upgrade_mando_weapons)
mandalorian_commando.add_upgrade_list(upgrade_mando_vet_weapons)
scavenged_at_rt.add_upgrade_list(upgrade_at_rt)


# collate model lists
list_core = ModelList()
list_core.add_model_entry(mandalorian_captain)
list_core.add_model_entry(mandalorian)
list_core.add_model_entry(mandalorian_commando)
list_core.add_model_entry(beskad_duelist)
list_core.add_model_entry(scavenged_at_rt)

# write latex files

list_core.file_write_latex("mandalore_core_roster.tabl")
upgrade_mando_weapons.file_write_latex()
upgrade_mando_vet_weapons.file_write_latex()
upgrade_at_rt.file_write_latex()

# write tsv files

list_core.file_write_tsv(tsv_file, list_title="Core")
upgrade_mando_weapons.file_write_tsv(tsv_file)
upgrade_mando_vet_weapons.file_write_tsv(tsv_file)
upgrade_at_rt.file_write_tsv(tsv_file)

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
darksaber = Weapon(
    "The Darksaber", "Melee", 3, pierce=3, deadly=3, unique="The Darksaber"
)
bo_katan.equip_weapon(core.combat_training)
bo_katan.equip_weapon(core.dual_blaster_pistols)
bo_katan.equip_weapon(jetpack_rocket)

# -*- Upgrade lists -*-

# Bo-Katan Melee

label = letter_increment(label)
upgrade_bo_melee = UpgradeList(label, base_model=bo_katan)
upgrade_bo_melee.select_upgrade_with_weapon_type(replace_weapon=core.combat_training)
upgrade_bo_melee.upgrade_with_weapon_entry(gauntlet_blades)
upgrade_bo_melee.upgrade_with_weapon_entry(darksaber)

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

bo_katan.add_upgrade_list(upgrade_bo_melee)
bo_katan.add_upgrade_list(upgrade_bo_weapon)

# collate model lists

list_nite_owls = ModelList()
list_nite_owls.add_model_entry(bo_katan)

# write latex files

list_nite_owls.file_write_latex("mandalore_nite_owls_roster.tabl")
upgrade_bo_melee.file_write_latex()
upgrade_bo_weapon.file_write_latex()

# write tsv files

list_nite_owls.file_write_tsv(tsv_file, list_title="Nite Owls", append=True)
upgrade_bo_melee.file_write_tsv(tsv_file)
upgrade_bo_weapon.file_write_tsv(tsv_file)

""" Clan Wren """
ursa_wren = Model(
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
    command=True,
)
ursa_wren.equip_weapon(core.combat_training)
ursa_wren.equip_weapon(core.dual_blaster_pistols)
ursa_wren.equip_weapon(jetpack_rocket)


sabine_wren = Model(
    "Sabine Wren",
    3,
    2,
    3,
    hero=True,
    impervious=True,
    gunslinger=True,
    arsenal=2,
    courage=True,
    fast=True,
    fly=True,
)
sabine_wren.equip_weapon(core.combat_training)
sabine_wren.equip_weapon(core.dual_blaster_pistols)
explosives = Weapon("Explosives", 12, 2, pierce=1, ammo=1, blast=3, indirect=True)
sabine_wren.equip_weapon(explosives)

tristan_wren = Model(
    "Tristan Wren",
    3,
    2,
    2,
    hero=True,
    impervious=True,
    fast=True,
    fly=True,
)
tristan_wren.equip_weapon(core.combat_training)
tristan_wren.equip_weapon(core.dual_blaster_pistols)
tristan_wren.equip_weapon(core.targeting_rifle)

# -*- Upgrade lists -*-

# Sabine Darksaber

label = letter_increment(label)
upgrade_sabine_darksaber = UpgradeList(label, base_model=sabine_wren)
upgrade_sabine_darksaber.select_upgrade_with_weapon_type(
    replace_weapon=core.combat_training
)
upgrade_sabine_darksaber.upgrade_with_weapon_entry(darksaber)

# Sabine weapons

paralysing_dart_launcher = Weapon(
    "Paralysing Dart Launcher",
    18,
    1,
    immobilise=True,
    ammo="Single Use",
    disorient=True,
)
repulsor = Weapon(
    "Repulsor",
    6,
    1,
    # nonlethal=True,
    ammo="Single Use",
    suppressive=1,
    throw=True,
)

label = letter_increment(label)
upgrade_sabine_weapon = UpgradeList(label, base_model=sabine_wren)
upgrade_sabine_weapon.select_upgrade_with_weapon_type()
upgrade_sabine_weapon.upgrade_with_weapon_entry(repulsor)
upgrade_sabine_weapon.upgrade_with_weapon_entry(core.whipcord_launcher)
upgrade_sabine_weapon.upgrade_with_weapon_entry(core.wrist_flamer)
upgrade_sabine_weapon.upgrade_with_weapon_entry(paralysing_dart_launcher)
upgrade_sabine_weapon.upgrade_with_weapon_entry(jetpack_rocket)

# Sabine shield

label = letter_increment(label)
upgrade_sabine_shield = UpgradeList(label, base_model=sabine_wren)
upgrade_sabine_shield.select_upgrade_with_model_changes_type()
upgrade_sabine_shield.upgrade_with_model_changes_entry("Combat Shield", shield=1)

# assign upgrade lists

sabine_wren.add_upgrade_list(upgrade_sabine_darksaber)
sabine_wren.add_upgrade_list(upgrade_sabine_weapon)
sabine_wren.add_upgrade_list(upgrade_sabine_shield)

# collate model list

list_clan_wren = ModelList()
list_clan_wren.add_model_entry(ursa_wren)
list_clan_wren.add_model_entry(sabine_wren)
list_clan_wren.add_model_entry(tristan_wren)

# write latex files

list_clan_wren.file_write_latex("mandalore_clan_wren_roster.tabl")
upgrade_sabine_darksaber.file_write_latex()
upgrade_sabine_weapon.file_write_latex()
upgrade_sabine_shield.file_write_latex()

# write tsv files

list_clan_wren.file_write_tsv(tsv_file, list_title="Clan Wren", append=True)
upgrade_sabine_darksaber.file_write_tsv(tsv_file)
upgrade_sabine_weapon.file_write_tsv(tsv_file)
upgrade_sabine_shield.file_write_tsv(tsv_file)

# Sabine Wren - can be taken in a Rebel list.
# Usra Wren - can be taken in Nite Owls
# Cautious allies with Imperial Super Commandos & Empire
# Allies with Nite Owls & Rebels

""" Protectors of Concord Dawn """
# Fenn Rau

""" Deathwatch/Maul Loyalists """

# Pre Vizsla, Rook Kast
# Can also include Gar Saxon and Bo-Katan (see other lists)
# Can choose for this to be either Deathwatch or Maul Loyalists.
# Deathwatch: cautious allies with CIS
# Maul Loyalists: see Shadow Collective/crime lords.
# Bo-Katan can be included in this army, but if it is a Maul Loyalists army, she is a cautious ally.

""" The Tribe """

""" Clan Saxon """
# Gar Saxon
# Tiber Saxon

gar_saxon = Model(
    "Gar Saxon",
    3,
    2,
    3,
    villain=True,
    impervious=True,
    arsenal=2,
    fast=True,
    fly=True,
    command=True,
    shield=1,
)
gar_saxon.equip_weapon(core.combat_training)
gar_saxon.equip_weapon(core.dual_blaster_pistols)
gar_saxon.equip_weapon(jetpack_rocket)

tiber_saxon = Model(
    "Tiber Saxon",
    3,
    4,
    3,
    villain=True,
    fast=True,
    fly=True,
    command=True,
    spotter=1,
)
tiber_saxon.equip_weapon(core.combat_training)
tiber_saxon.equip_weapon(core.targeting_rifle)

# -*- Upgrade lists -*-

# Gar Saxon Darksaber

label = letter_increment(label)
upgrade_gar_darksaber = UpgradeList(label, base_model=gar_saxon)
upgrade_gar_darksaber.select_upgrade_with_weapon_type(
    replace_weapon=core.combat_training
)
upgrade_gar_darksaber.upgrade_with_weapon_entry(darksaber)

# Gar Saxon weapons

label = letter_increment(label)
upgrade_gar_weapon = UpgradeList(label, base_model=gar_saxon)
upgrade_gar_weapon.select_upgrade_with_weapon_type()
upgrade_gar_weapon.upgrade_with_weapon_entry(core.wrist_flamer)
upgrade_gar_weapon.upgrade_with_weapon_entry(core.heavy_sniper_rifle)

# assign upgrade lists

gar_saxon.add_upgrade_list(upgrade_gar_darksaber)
gar_saxon.add_upgrade_list(upgrade_gar_weapon)

# collate model lists

list_imperial_supercommandos = ModelList()
list_imperial_supercommandos.add_model_entry(gar_saxon)
list_imperial_supercommandos.add_model_entry(tiber_saxon)

# write latex files

list_imperial_supercommandos.file_write_latex("mandalore_clan_saxon_roster.tabl")
upgrade_gar_darksaber.file_write_latex()
upgrade_gar_weapon.file_write_latex()

# write tsv files

list_imperial_supercommandos.file_write_tsv(
    tsv_file, list_title="Clan Saxon", append=True
)
upgrade_gar_darksaber.file_write_tsv(tsv_file)
upgrade_gar_weapon.file_write_tsv(tsv_file)
