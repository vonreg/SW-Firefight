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
wrist_blaster = Weapon("Wrist Blaster", 6, 2, quickdraw=True)
dart_launcher = Weapon(
    "Dart Launcher", 18, 1, pierce=2, ammo="Single Use", disorient=True
)
gauntlet_blades = Weapon("Gauntlet Blades", "Melee", 4, rending=True)
beskad = Weapon("Beskad", "Melee", 4, pierce=2, rending=True)
# core: whipcord launcher
# core: wrist flamethrower
darksaber = Weapon(
    "The Darksaber", "Melee", 3, pierce=3, deadly=3, unique="The Darksaber"
)

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
mandalorian_captain.equip_weapon(wrist_blaster)
mandalorian_captain.equip_weapon(jetpack_rocket)

mandalorian = Model(
    "Mandalorian Warrior", 4, 3, 1, fly=True, fast=True, impervious=True
)
mandalorian.equip_weapon(core.combat_training)
mandalorian.equip_weapon(wrist_blaster)

mandalorian_commando = Model(
    "Mandalorian Commando", 3, 3, 2, fly=True, fast=True, impervious=True
)
mandalorian_commando.equip_weapon(core.combat_training)
mandalorian_commando.equip_weapon(wrist_blaster)


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

# Mandalorian captain weapons

label = "A"
upgrade_captain_weapons = UpgradeList(label, base_model=mandalorian_captain)
upgrade_captain_weapons.select_upgrade_with_weapon_type()
upgrade_captain_weapons.upgrade_with_weapon_entry(beskad, manual_points_adjustment=-6)
upgrade_captain_weapons.upgrade_with_weapon_entry(
    core.dual_blaster_pistols, manual_points_adjustment=-6
)
upgrade_captain_weapons.upgrade_with_weapon_entry(
    core.blaster_carbine, manual_points_adjustment=-6
)
upgrade_captain_weapons.upgrade_with_weapon_entry(
    core.targeting_rifle, manual_points_adjustment=-6
)
upgrade_captain_weapons.upgrade_with_weapon_entry(
    core.sniper_rifle, manual_points_adjustment=-6
)
upgrade_captain_weapons.upgrade_with_weapon_entry(
    core.heavy_sniper_rifle, manual_points_adjustment=-6
)
upgrade_captain_weapons.upgrade_with_weapon_entry(jetpack_rocket)
upgrade_captain_weapons.upgrade_with_weapon_entry(core.whipcord_launcher)
upgrade_captain_weapons.upgrade_with_weapon_entry(dart_launcher)
upgrade_captain_weapons.upgrade_with_weapon_entry(core.wrist_flamer)
upgrade_captain_weapons.upgrade_with_weapon_entry(core.concussion_grenade)
upgrade_captain_weapons.upgrade_with_weapon_entry(core.thermal_detonator)
upgrade_captain_weapons.upgrade_with_weapon_entry(core.ion_grenade)

# Mandalorian warrior weapons

label = letter_increment(label)
upgrade_mando_weapons = UpgradeList(label, base_model=mandalorian)
upgrade_mando_weapons.select_upgrade_with_weapon_type(limit=2)
upgrade_mando_weapons.upgrade_with_weapon_entry(beskad, manual_points_adjustment=-6)
upgrade_mando_weapons.upgrade_with_weapon_entry(
    core.dual_blaster_pistols, manual_points_adjustment=-6
)
upgrade_mando_weapons.upgrade_with_weapon_entry(
    core.blaster_carbine, manual_points_adjustment=-6
)
upgrade_mando_weapons.upgrade_with_weapon_entry(
    core.targeting_rifle, manual_points_adjustment=-6
)
upgrade_mando_weapons.upgrade_with_weapon_entry(
    core.sniper_rifle, manual_points_adjustment=-6
)
upgrade_mando_weapons.upgrade_with_weapon_entry(
    core.heavy_sniper_rifle, manual_points_adjustment=-6
)
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
upgrade_mando_vet_weapons.select_upgrade_with_weapon_type()
upgrade_mando_vet_weapons.upgrade_with_weapon_entry(beskad, manual_points_adjustment=-6)
upgrade_mando_vet_weapons.upgrade_with_weapon_entry(
    core.dual_blaster_pistols, manual_points_adjustment=-6
)
upgrade_mando_vet_weapons.upgrade_with_weapon_entry(
    core.blaster_carbine, manual_points_adjustment=-6
)
upgrade_mando_vet_weapons.upgrade_with_weapon_entry(
    core.targeting_rifle, manual_points_adjustment=-6
)
upgrade_mando_vet_weapons.upgrade_with_weapon_entry(
    core.sniper_rifle, manual_points_adjustment=-6
)
upgrade_mando_vet_weapons.upgrade_with_weapon_entry(
    core.heavy_sniper_rifle, manual_points_adjustment=-6
)
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
mandalorian_captain.add_upgrade_list(upgrade_captain_weapons)
mandalorian.add_upgrade_list(upgrade_mando_weapons)
mandalorian_commando.add_upgrade_list(upgrade_mando_vet_weapons)
scavenged_at_rt.add_upgrade_list(upgrade_at_rt)

# collate model lists
list_core = ModelList()
list_core.add_model_entry(mandalorian_captain)
list_core.add_model_entry(mandalorian)
list_core.add_model_entry(mandalorian_commando)
list_core.add_model_entry(scavenged_at_rt)

# write latex files

list_core.file_write_latex("mandalore_core_roster.tabl")
upgrade_captain_weapons.file_write_latex()
upgrade_mando_weapons.file_write_latex()
upgrade_mando_vet_weapons.file_write_latex()
upgrade_at_rt.file_write_latex()

# write tsv files

list_core.file_write_tsv(tsv_file, list_title="Core")
upgrade_captain_weapons.file_write_tsv(tsv_file)
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
    unique="Bo-Katan Kryze",
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
    unique="Ursa Wren",
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
    unique="Sabine Wren",
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
    unique="Tristan Wren",
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

# Sabine shield

label = letter_increment(label)
upgrade_sabine_shield = UpgradeList(label, base_model=sabine_wren)
upgrade_sabine_shield.select_upgrade_with_model_changes_type()
upgrade_sabine_shield.upgrade_with_model_changes_entry("Combat Shield", shield=1)

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
    free_special_rule='Repulsor[6"]',
)

label = letter_increment(label)
upgrade_sabine_weapon = UpgradeList(label, base_model=sabine_wren)
upgrade_sabine_weapon.select_upgrade_with_weapon_type()
upgrade_sabine_weapon.upgrade_with_weapon_entry(repulsor, manual_points_adjustment=1)
upgrade_sabine_weapon.upgrade_with_weapon_entry(core.whipcord_launcher)
upgrade_sabine_weapon.upgrade_with_weapon_entry(core.wrist_flamer)
upgrade_sabine_weapon.upgrade_with_weapon_entry(paralysing_dart_launcher)
upgrade_sabine_weapon.upgrade_with_weapon_entry(jetpack_rocket)

# assign upgrade lists

sabine_wren.add_upgrade_list(upgrade_sabine_darksaber)
sabine_wren.add_upgrade_list(upgrade_sabine_shield)
sabine_wren.add_upgrade_list(upgrade_sabine_weapon)

# collate model list

list_clan_wren = ModelList()
list_clan_wren.add_model_entry(ursa_wren)
list_clan_wren.add_model_entry(sabine_wren)
list_clan_wren.add_model_entry(tristan_wren)

# write latex files

list_clan_wren.file_write_latex("mandalore_clan_wren_roster.tabl")
upgrade_sabine_darksaber.file_write_latex()
upgrade_sabine_shield.file_write_latex()
upgrade_sabine_weapon.file_write_latex()

# write tsv files

list_clan_wren.file_write_tsv(tsv_file, list_title="Clan Wren", append=True)
upgrade_sabine_darksaber.file_write_tsv(tsv_file)
upgrade_sabine_shield.file_write_tsv(tsv_file)
upgrade_sabine_weapon.file_write_tsv(tsv_file)

""" Protectors of Concord Dawn """
# Fenn Rau
# Just use core Mandos

""" Deathwatch/Maul Loyalists """

pre_vizsla = Model(
    "Pre Vizsla",
    3,
    2,
    3,
    villain=True,
    impervious=True,
    fast=True,
    fly=True,
    command=True,
    hunter="Jedi",
    unique="Pre Vizsla",
)
pre_vizsla.equip_weapon(darksaber)
pre_vizsla.equip_weapon(core.dual_blaster_pistols)
pre_vizsla.equip_weapon(wrist_blaster)
pre_vizsla.equip_weapon(dart_launcher)
pre_vizsla.equip_weapon(core.wrist_flamer)
pre_vizsla.equip_weapon(jetpack_rocket)
pre_vizsla.equip_weapon(core.whipcord_launcher)

rook_kast = Model(
    "Rook Kast",
    3,
    2,
    2,
    villain=True,
    impervious=True,
    fast=True,
    fly=True,
    relay=True,
    unique="Rook Kast",
)
rook_kast.equip_weapon(core.blaster_carbine)
rook_kast.equip_weapon(jetpack_rocket)
rook_kast.equip_weapon(core.whipcord_launcher)

# -*- Upgrade lists -*-

label = letter_increment(label)
upgrade_rook = UpgradeList(label, base_model=rook_kast)
upgrade_rook.select_upgrade_with_weapon_type(replace_weapon=core.blaster_carbine)
upgrade_rook.upgrade_with_weapon_entry(core.dual_blaster_pistols)


# assign upgrade lists

rook_kast.add_upgrade_list(upgrade_rook)

# collate model list

list_deathwatch = ModelList()
list_deathwatch.add_model_entry(pre_vizsla)
list_deathwatch.add_model_entry(rook_kast)

# write latex files

list_deathwatch.file_write_latex("mandalore_deathwatch_roster.tabl")
upgrade_rook.file_write_latex()

# write tsv files

list_deathwatch.file_write_tsv(tsv_file, list_title="Deathwatch", append=True)
upgrade_rook.file_write_tsv(tsv_file)

# Can also include Gar Saxon and Bo-Katan (see other lists)
# Can choose for this to be either Deathwatch or Maul Loyalists.
# Deathwatch: cautious allies with CIS
# Maul Loyalists: see Shadow Collective/crime lords.

""" The Tribe """

din_djarin = Model(
    "Din Djarin",
    3,
    3,
    4,
    hero=True,
    impervious=True,
    arsenal=2,
    hunter="Target",
    protector="Unit",
    protector_key="Grogu",
    unique="Din Djarin",
)
din_djarin.equip_weapon(core.vibroblade)
din_djarin.equip_weapon(core.heavy_blaster_pistol)

whistling_birds = Weapon(
    "Whistling Birds",
    6,
    6,
    rending=True,
    ammo="Single Use",
    indirect=True,
    seek=True,
    split_fire=True,
)
amban_rifle = Weapon(
    "Amban Rifle",
    "inf",
    1,
    pierce=2,
    ammo=1,
    sniper=True,
    deadly=3,
    primary_fire_mode_name="Disintegrating Shot",
    secondary_fire_modes=[
        Weapon("Electro-pulse", "Melee", 3, immobilise=True, immobilise_roll=4)
    ],
)
beskad = Weapon("Beskad", "Melee", 4, pierce=2, rending=True)

beskar_spear = Weapon(
    "Beskar Spear",
    "Melee",
    4,
    pierce=2,
    rending=True,
)

grogu = Model(
    "Grogu",
    6,
    3,
    2,
    disciplined=True,
    jump=3,
    jedi=True,
    protector="Unit",
    protector_key="Din Djarin",
    heal=4,
    slow=True,
    noncombatant=True,
    unique="Grogu",
    companion="Din Djarin",
)
force_push = Weapon("Force Push", 6, 3, throw=True, seek=True, quickdraw=True)
force_choke = Weapon("Force Choke", 6, 2, pierce=4, seek=True, quickdraw=True)
grogu.equip_weapon(force_push)
grogu.equip_weapon(force_choke)

armourer = Model(
    "The Armourer",
    3,
    2,
    3,
    hero=True,
    impervious=True,
    courage=True,
    fast=True,
    fly=True,
    command=True,
    unique="The Armourer",
)
hammer_and_tongs = Weapon("Hammer and Tongs", "Melee", 4, rending=True, suppressive=2)
armourer.equip_weapon(hammer_and_tongs)

paz_vizsla = Model(
    "Paz Vizsla",
    3,
    2,
    3,
    hero=True,
    impervious=True,
    fly=True,
    relay=True,
    slow=True,
    unique="Paz Vizsla",
)
repeating_blaster = Weapon("Repeating Blaster", 24, 6, split_fire=True)
paz_vizsla.equip_weapon(core.vibroblade)
paz_vizsla.equip_weapon(repeating_blaster)

# -*- Upgrade lists -*-

# Din armour & jetpack

label = letter_increment(label)
upgrade_din_equipment = UpgradeList(label, base_model=din_djarin)
upgrade_din_equipment.select_upgrade_with_model_changes_type()
upgrade_din_equipment.upgrade_with_model_changes_entry("Full Beskar Armour", defense=2)
upgrade_din_equipment.upgrade_with_model_changes_entry("Jetpack", fast=True, fly=True)

# Din gadgets

label = letter_increment(label)
upgrade_din_gadgets = UpgradeList(label, base_model=din_djarin)
upgrade_din_gadgets.select_upgrade_with_weapon_type()
upgrade_din_gadgets.upgrade_with_weapon_entry(core.whipcord_launcher)
upgrade_din_gadgets.upgrade_with_weapon_entry(core.wrist_flamer)
upgrade_din_gadgets.upgrade_with_weapon_entry(whistling_birds)
upgrade_din_gadgets.upgrade_with_weapon_entry(core.thermal_detonator)

# din primary weapons

label = letter_increment(label)
upgrade_din_weapons = UpgradeList(label, base_model=din_djarin)
upgrade_din_weapons.select_upgrade_with_weapon_type(
    limit=1, replace_weapon=core.vibroblade
)
upgrade_din_weapons.upgrade_with_weapon_entry(amban_rifle)
upgrade_din_weapons.upgrade_with_weapon_entry(beskar_spear)
upgrade_din_weapons.upgrade_with_weapon_entry(darksaber)

# Grogu model changes

label = letter_increment(label)
upgrade_grogu_model = UpgradeList(label, base_model=grogu)
upgrade_grogu_model.select_upgrade_with_model_changes_type()
upgrade_grogu_model.upgrade_with_model_changes_entry("Beskar Armour", impervious=True)
upgrade_grogu_model.upgrade_with_model_changes_entry(
    "Hover Crib", slow=False, jump=False, fly=True
)
upgrade_grogu_model.upgrade_with_model_changes_entry("Run", slow=False)

# assign upgrade lists

din_djarin.add_upgrade_list(upgrade_din_equipment)
din_djarin.add_upgrade_list(upgrade_din_gadgets)
din_djarin.add_upgrade_list(upgrade_din_weapons)
grogu.add_upgrade_list(upgrade_grogu_model)

# collate model list

list_tribe = ModelList()
list_tribe.add_model_entry(din_djarin)
list_tribe.add_model_entry(grogu)
list_tribe.add_model_entry(armourer)
list_tribe.add_model_entry(paz_vizsla)

# write latex files

list_tribe.file_write_latex("mandalore_tribe_roster.tabl")
upgrade_din_equipment.file_write_latex()
upgrade_din_gadgets.file_write_latex()
upgrade_din_weapons.file_write_latex()
upgrade_grogu_model.file_write_latex()

# write tsv files

list_tribe.file_write_tsv(tsv_file, list_title="The Tribe", append=True)
upgrade_din_equipment.file_write_tsv(tsv_file)
upgrade_din_gadgets.file_write_tsv(tsv_file)
upgrade_din_weapons.file_write_tsv(tsv_file)
upgrade_grogu_model.file_write_tsv(tsv_file)

""" The Fetts """

jango_fett = Model(
    "Jango Fett",
    3,
    2,
    3,
    villain=True,
    impervious=True,
    gunslinger=True,
    fast=True,
    fly=True,
    hunter="Target",
    unique="Jango Fett",
)
jango_fett.equip_weapon(core.combat_training)
jango_fett.equip_weapon(core.dual_blaster_pistols)
jango_fett.equip_weapon(jetpack_rocket)
jango_fett.equip_weapon(core.whipcord_launcher)
jango_fett.equip_weapon(core.wrist_flamer)

# Boba: various upgrades including gaffi stick, ee3 (carbine), knee rockets, wrist blaster, arsenal 2 (or 3?), whipcord, cycler rifle

boba_fett = Model(
    "Boba Fett",
    3,
    2,
    4,
    villain=True,
    impervious=True,
    arsenal=3,
    fast=True,
    fly=True,
    hunter="Target",
    unique="Boba Fett",
)
boba_fett.equip_weapon(core.combat_training)
boba_fett.equip_weapon(core.blaster_carbine)
gaderffi_stick = Weapon("Gaderffi Stick", "Melee", 4, pierce=2, deadly=2)
rocket_darts = Weapon("Rocket Darts", 12, 2, quickdraw=True)

# -*- Upgrade lists -*-

label = letter_increment(label)
upgrade_boba_melee = UpgradeList(label, base_model=boba_fett)
upgrade_boba_melee.select_upgrade_with_weapon_type(replace_weapon=core.combat_training)
upgrade_boba_melee.upgrade_with_weapon_entry(gaderffi_stick)
upgrade_boba_melee.upgrade_with_weapon_entry(core.vibroblade)

label = letter_increment(label)
upgrade_boba_main_weapon = UpgradeList(label, base_model=boba_fett)
upgrade_boba_main_weapon.select_upgrade_with_weapon_type(
    replace_weapon=core.blaster_carbine
)
upgrade_boba_main_weapon.upgrade_with_weapon_entry(core.heavy_blaster_pistol)
upgrade_boba_main_weapon.upgrade_with_weapon_entry(core.cycler_rifle)

label = letter_increment(label)
upgrade_boba_gadgets = UpgradeList(label, base_model=boba_fett)
upgrade_boba_gadgets.select_upgrade_with_weapon_type()
upgrade_boba_gadgets.upgrade_with_weapon_entry(jetpack_rocket)
upgrade_boba_gadgets.upgrade_with_weapon_entry(rocket_darts)
upgrade_boba_gadgets.upgrade_with_weapon_entry(wrist_blaster)
upgrade_boba_gadgets.upgrade_with_weapon_entry(core.wrist_flamer)
upgrade_boba_gadgets.upgrade_with_weapon_entry(core.thermal_detonator)

label = letter_increment(label)
upgrade_boba_unarmoured = UpgradeList(label, base_model=boba_fett)
upgrade_boba_unarmoured.select_upgrade_with_model_changes_type()
upgrade_boba_unarmoured.upgrade_with_model_changes_entry(
    "Unarmoured", defense=4, impervious=False, fly=False, fast=False
)
upgrade_boba_unarmoured.upgrade_with_model_changes_entry(
    "Tusken Training", relentless=True, courage=True, villain=False, hero=True
)
upgrade_boba_unarmoured.upgrade_with_model_changes_entry("Daimyo", command=True)

# assign upgrade lists

boba_fett.add_upgrade_list(upgrade_boba_melee)
boba_fett.add_upgrade_list(upgrade_boba_main_weapon)
boba_fett.add_upgrade_list(upgrade_boba_gadgets)
boba_fett.add_upgrade_list(upgrade_boba_unarmoured)

# collate model list

list_fett = ModelList()
list_fett.add_model_entry(jango_fett)
list_fett.add_model_entry(boba_fett)

# write latex files

list_fett.file_write_latex("mandalore_fett_roster.tabl")
upgrade_boba_melee.file_write_latex()
upgrade_boba_main_weapon.file_write_latex()
upgrade_boba_gadgets.file_write_latex()
upgrade_boba_unarmoured.file_write_latex()

# write tsv files

list_fett.file_write_tsv(tsv_file, list_title="The Fetts", append=True)
upgrade_boba_melee.file_write_tsv(tsv_file)
upgrade_boba_main_weapon.file_write_tsv(tsv_file)
upgrade_boba_gadgets.file_write_tsv(tsv_file)
upgrade_boba_unarmoured.file_write_tsv(tsv_file)

""" Clan Saxon """

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
    unique="Gar Saxon",
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
    unique="Tiber Saxon",
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
