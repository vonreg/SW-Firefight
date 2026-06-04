from sw_firefight_engine.firefight import (
    Weapon,
    Model,
    ModelList,
    UpgradeList,
    letter_increment,
)
from sw_firefight_engine import core

tsv_file = "galactic_empire.tsv"

emperor_palpatine = Model(
    "Emperor Palpatine",
    3,
    3,
    6,
    sith=True,
    fear=True,
    deflect=True,
    slow=True,
    jump=6,
    unique="Palpatine",
    impervious=True,
)
unlimited_power = Weapon(
    "Unlimited Power",
    "Torrent",
    3,
    pierce=2,
    throw=True,
    ion=True,
    suppressive=2,
)
emperor_palpatine.equip_weapon(unlimited_power)

darth_vader = Model(
    "Darth Vader",
    3,
    3,
    6,
    sith=True,
    fear=True,
    deflect=True,
    relentless=True,
    impervious=True,
    slow=True,
    jump=3,
    unique="Anakin Skywalker",
)
vader_lightsaber = Weapon("Lightsaber", "Melee", 4, pierce=4, deadly=3)
vader_force_choke = Weapon(
    "Force Choke", 6, 1, pierce=4, seek=True, throw=True
)
darth_vader.equip_weapon(vader_lightsaber)
darth_vader.equip_weapon(core.force_choke)

inquisitor = Model(
    "Inquisitor",
    4,
    3,
    4,
    villain=True,
    dark_side=True,
    deflect=True,
    jump=3,
    hunter="Jedi",
)
inquisitor.equip_weapon(core.lightsaber_knight)

imperial_commander = Model(
    "Imperial Commander",
    3,
    5,
    3,
    villain=True,
    spotter=1,
    command=True,
)

imperial_officer = Model(
    "Imperial Officer", 5, 6, 2, villain=True, disciplined=True
)
imperial_officer.equip_weapon(core.blaster_pistol)

isf_commander = Model(
    "ISF Commander", 3, 4, 3, villain=True, command=True, scout=True, recon=4
)
isf_commander.equip_weapon(core.blaster_rifle)
isf_commander.equip_weapon(core.combat_training)

stormtrooper_officer = Model("Stormtrooper Officer", 4, 4, 2, villain=True)
stormtrooper_officer.equip_weapon(core.blaster_rifle)

stormtrooper = Model("Stormtrooper", 5, 4, 1, expendable=1, disciplined=True)
stormtrooper.equip_weapon(core.blaster_rifle)

stormtrooper_heavy_mortar = Model(
    "Stormtrooper Heavy Mortar",
    5,
    4,
    1,
    disciplined=True,
    emplacement=True,
    slow=True,
)
stormtrooper_heavy_mortar.equip_weapon(core.heavy_mortar)
stormtrooper_heavy_mortar.equip_weapon(core.blaster_rifle)

imperial_army_trooper = Model("Imperial Army Trooper", 5, 5, 1, expendable=2)
imperial_army_trooper.equip_weapon(core.blaster_rifle)

imperial_riot_trooper = Model("Imperial Riot Trooper", 5, 4, 1, expendable=2)
imperial_riot_trooper.equip_weapon(core.truncheon)

scout_trooper = Model(
    "Scout Trooper",
    5,
    5,
    1,
    expendable=1,
    scout=True,
    disciplined=True,
    recon=5,
)
scout_trooper.equip_weapon(core.blaster_pistol)

isf_trooper = Model("ISF Trooper", 4, 4, 1, scout=True, recon=4)
isf_trooper.equip_weapon(core.blaster_rifle)

purge_trooper = Model(
    "Purge Trooper", 3, 4, 1, hunter="Jedi", impervious=True, duellist=True
)
purge_trooper.equip_weapon(core.blaster_rifle)

death_trooper = Model("Death Trooper", 3, 3, 2, fear=True)
death_trooper.equip_weapon(core.blaster_rifle)
death_trooper.equip_weapon(core.burst_pistol)

imperial_royal_guard = Model(
    "Imperial Royal Guard",
    3,
    4,
    3,
    protector="Unit",
    protector_key="Emperor Palpatine",
    courage=True,
    duellist=True,
)
force_pike = Weapon(
    "Force Pike",
    "Melee",
    3,
    pierce=1,
)
enhanced_force_pike = Weapon(
    "Enhanced Force Pike",
    "Melee",
    3,
    pierce=1,
    primary_fire_mode_name="Force Pike",
    secondary_fire_modes=[
        Weapon("Magnetic Clamp", 12, 1, nonlethal=True, immobilise=True)
    ],
)
imperial_royal_guard.equip_weapon(force_pike)
imperial_royal_guard.equip_weapon(core.heavy_blaster_pistol)

imp_speeder_bike = Model(
    "74-Z Speeder Bike",
    5,
    5,
    3,
    vehicle=True,
    impact=2,
    fast=True,
    fly=True,
    scout=True,
    recon=5,
)
speeder_blaster_cannon = Weapon(
    "Light Blaster Cannon", 18, 3, pierce=2, fixed="Front"
)
imp_speeder_bike.equip_weapon(core.light_blaster_cannon)
imp_speeder_bike.equip_weapon(core.blaster_pistol)

e_web_team = Model(
    "E-Web Team",
    5,
    5,
    3,
    emplacement=True,
    slow=True,
)
e_web = Weapon(
    "E-Web", "inf", 3, pierce=2, deadly=2, fixed="Front", split_fire=True
)
e_web_team.equip_weapon(e_web)
blaster_rifles = Weapon("Blaster Rifles", 30, 6)
e_web_team.equip_weapon(blaster_rifles)

kx_security_droid = Model(
    "KX Security Droid",
    4,
    4,
    1,
    impact=3,
    droid=True,
    impervious=True,
    slow=True,
)

dt_sentry_droid = Model(
    "DT Sentry Droid",
    4,
    4,
    2,
    impact=2,
    droid=True,
    slow=True,
    arsenal=2,
)
dt_sentry_droid.equip_weapon(core.blaster_carbine)

probe_droid = Model(
    "Probe Droid",
    5,
    4,
    2,
    droid=True,
    recon=4,
    spotter=2,
    slow=True,
    scout=True,
    fly=True,
    noncombatant=True,
)
probe_blaster = Weapon("Probe Droid Blaster", 15, 4, pierce=1)
probe_droid.equip_weapon(probe_blaster)

id_seeker_droid = Model(
    "ID Seeker Droid",
    5,
    5,
    1,
    droid=True,
    shield=1,
    protector="Any",
    scout=True,
    fly=True,
)
shock_pulse = Weapon("Shock Pulse", "Melee", 2, suppressive=1)
id_seeker_droid.equip_weapon(shock_pulse)

medical_droid = Model("Medical Droid", 6, 5, 1, droid=True, heal=1, slow=True)
lethal_injection = Weapon("Lethal Injection", "Melee", 1, deadly=3)
medical_droid.equip_weapon(lethal_injection)

astromech_droid = Model(
    "Astromech Droid", 5, 5, 1, droid=True, repair=1, slow=True
)
astromech_droid.equip_weapon(shock_pulse)

at_rt = Model(
    "Imperial AT-RT",
    5,
    4,
    4,
    vehicle=True,
    fast=True,
    cover="Front",
    jump=3,
    impact=3,
    recon=5,
)
at_rt_twin_blaster_cannon = Weapon(
    "Twin Blaster Cannon",
    18,
    4,
    pierce=2,
    fixed="Front",
    split_fire=True,
)
at_rt.equip_weapon(at_rt_twin_blaster_cannon)
at_rt.equip_weapon(core.burst_pistol)

gav_tank = Model(
    "TX-225 Combat Assault Tank",
    5,
    3,
    8,
    vehicle="Heavy",
    slow=True,
    impact=4,
    cover="Front",
)
gav_tank.equip_weapon(core.blaster_cannon)
gav_tank.equip_weapon(core.laser_cannon_mounted)

# -*- Upgrade lists -*-

# Inquisitors

label = "A"
upgrade_inquisitor = UpgradeList(label, base_model=inquisitor)
upgrade_inquisitor.select_upgrade_with_model_changes_type()
upgrade_inquisitor.upgrade_with_model_changes_entry(
    "Grand Inquisitor",
    quality=3,
    impervious=True,
    command=True,
    unique="Grand Inquisitor",
)
upgrade_inquisitor.upgrade_with_model_changes_entry(
    "First Brother", survivor=True, scout=True, unique="Marrok"
)
upgrade_inquisitor.upgrade_with_model_changes_entry(
    "Second Sister", fast=True, unique="Trilla"
)
upgrade_inquisitor.upgrade_with_model_changes_entry(
    "Third Sister", luck=1, survivor=True, command=True, unique="Reva Sevander"
)
upgrade_inquisitor.upgrade_with_model_changes_entry(
    "Fifth Brother",
    relay=True,
    impact=1,
    disciplined=True,
    unique="Fifth Brother",
)
upgrade_inquisitor.upgrade_with_model_changes_entry(
    "Seventh Sister",
    companion="ID Seeker Droid",
    scout=True,
    recon=4,
    unique="Seventh Sister",
)
upgrade_inquisitor.upgrade_with_model_changes_entry(
    "Eighth Brother", jump=6, recon=5, unique="Eighth Brother"
)
upgrade_inquisitor.upgrade_with_model_changes_entry(
    "Ninth Sister", wounds=5, slow=True, impact=2, unique="Masana Tide"
)
upgrade_inquisitor.upgrade_with_model_changes_entry(
    "Eleventh Brother", fear=True, relentless=True, unique="Eleventh Brother"
)
upgrade_inquisitor.upgrade_with_model_changes_entry(
    "Bariss Offee",
    heal=1,
    jedi=True,
    villain=False,
    dark_side=False,
    unique="Bariss Offee",
)

label = letter_increment(label)
upgrade_inquisitor_force = UpgradeList(label, base_model=inquisitor)
upgrade_inquisitor_force.select_upgrade_with_weapon_type()
upgrade_inquisitor_force.upgrade_with_weapon_entry(core.force_choke)
upgrade_inquisitor_force.upgrade_with_weapon_entry(core.force_push)
upgrade_inquisitor_force.upgrade_with_weapon_entry(core.saber_throw)

# Imperial Commander

label = letter_increment(label)
upgrade_commander = UpgradeList(label, base_model=imperial_commander)
upgrade_commander.select_upgrade_with_model_changes_type()
upgrade_commander.upgrade_with_model_changes_entry("Combat Armour", defense=4)
upgrade_commander.upgrade_with_model_changes_entry(
    "Seeker Droid",
    companion="ID Seeker Droid",
    scout=True,
)
upgrade_commander.upgrade_with_model_changes_entry(
    "ISB", hunter="Target", recon=5
)
upgrade_commander.upgrade_with_model_changes_entry(
    "Field Agent", command=False, relay=True, agile=True
)
upgrade_commander.upgrade_with_model_changes_entry(
    "Senior Officer", spotter=2, take_cover=1
)
upgrade_commander.upgrade_with_model_changes_entry(
    "Sentinel Droid",
    droid=True,
    fear=True,
    defense=3,
    noncombatant=True,
    spotter=2,
    shield=1,
    unique="Palpatine",
)
upgrade_commander.upgrade_with_model_changes_entry(
    "Grand Moff Tarkin",
    wounds=4,
    noncombatant=True,
    spotter=3,
    unique="Wilhuff Tarkin",
)
upgrade_commander.upgrade_with_model_changes_entry(
    "Grand Admiral Thrawn",
    wounds=4,
    spotter=2,
    take_cover=2,
    disciplined=True,
    unique="Thrawn",
)
upgrade_commander.upgrade_with_model_changes_entry(
    "Director Krennic",
    wounds=4,
    companion="Death Trooper",
    unique="Orson Krennic",
)
upgrade_commander.upgrade_with_model_changes_entry(
    "Agent Kallus", wounds=4, agile=True, unique="Alexsandr Kallus"
)
upgrade_commander.upgrade_with_model_changes_entry(
    "Lord Vonreg (Jetpack)",
    wounds=4,
    fly=True,
    repair=1,
    survivor=True,
    unique="Rodjer Vonreg",
)
upgrade_commander.upgrade_with_model_changes_entry(
    "Lord Vonreg",
    wounds=4,
    slow=True,
    repair=1,
    survivor=True,
    unique="Rodjer Vonreg",
)
upgrade_commander.upgrade_with_model_changes_entry(
    "Agent Selina", unique="Selina Kast"
)

label = letter_increment(label)
upgrade_commander_melee = UpgradeList(label, base_model=imperial_commander)
upgrade_commander_melee.select_upgrade_with_weapon_type()
upgrade_commander_melee.upgrade_with_weapon_entry(core.combat_training)
upgrade_commander_melee.upgrade_with_weapon_entry(core.stun_baton)
upgrade_commander_melee.upgrade_with_weapon_entry(core.riot_baton)
chiss_martial_arts = Weapon(
    "Chiss Martial Arts", "Melee", 4, disorient=True, wargear="Thrawn"
)
upgrade_commander_melee.upgrade_with_weapon_entry(chiss_martial_arts)
selina_vibromachete = Weapon(
    "Vibromachete",
    "Melee",
    3,
    rending=1,
    inaccurate=True,
    wargear="Selina Kast",
)
upgrade_commander_melee.upgrade_with_weapon_entry(selina_vibromachete)
vonreg_vibroblades = Weapon(
    "Sith Vibroblades", "Melee", 4, rending=True, wargear="Rodjer Vonreg"
)
upgrade_commander_melee.upgrade_with_weapon_entry(vonreg_vibroblades)
vonreg_lightsaber = Weapon(
    "Trophy Lightsaber",
    "Melee",
    3,
    pierce=2,
    deadly=2,
    inaccurate=True,
    wargear="Rodjer Vonreg",
)
upgrade_commander_melee.upgrade_with_weapon_entry(vonreg_lightsaber)

label = letter_increment(label)
upgrade_commander_weapon = UpgradeList(label, base_model=imperial_commander)
upgrade_commander_weapon.select_upgrade_with_weapon_type(limit=1)
upgrade_commander_weapon.upgrade_with_weapon_entry(core.blaster_pistol)
upgrade_commander_weapon.upgrade_with_weapon_entry(core.heavy_blaster_pistol)
upgrade_commander_weapon.upgrade_with_weapon_entry(core.dual_blaster_pistols)
upgrade_commander_weapon.upgrade_with_weapon_entry(core.burst_pistol)
upgrade_commander_weapon.upgrade_with_weapon_entry(core.sniper_pistol)
upgrade_commander_weapon.upgrade_with_weapon_entry(core.bryar_pistol)
upgrade_commander_weapon.upgrade_with_weapon_entry(core.blaster_rifle)
krennic_pistol = Weapon(
    "Krennic's DT-29 Pistol",
    18,
    1,
    pierce=2,
    deadly=2,
    ammo=3,
    sniper=True,
    quickdraw=True,
)
upgrade_commander_weapon.upgrade_with_weapon_entry(krennic_pistol)
vonreg_wargear = Weapon(
    "Vonreg's Blasters",
    6,
    3,
    quickdraw=True,
    reciprocating=5,
    wargear="Rodjer Vonreg",
    primary_fire_mode_name="Burst Pistol",
    secondary_fire_modes=[
        Weapon("Rifle Full Auto", 30, 3, pierce=1),
        Weapon(
            "Rifle Sniper Shot",
            "inf",
            1,
            pierce=2,
            ammo=1,
            sniper=True,
            deadly=2,
        ),
    ],
)
upgrade_commander_weapon.upgrade_with_weapon_entry(vonreg_wargear)
selina_burst_pistols = Weapon(
    "Selina's Blasters",
    6,
    6,
    quickdraw=True,
    inaccurate=True,
    reciprocating=5,
    wargear="Selina Kast",
    primary_fire_mode_name="Twin Burst Pistols",
    secondary_fire_modes=[core.blaster_rifle],
)
upgrade_commander_weapon.upgrade_with_weapon_entry(selina_burst_pistols)
kallus_bo_rifle = Weapon(
    "Kallus' Bo-Rifle",
    "Melee",
    4,
    pierce=2,
    wargear="Alexsandr Kallus",
    primary_fire_mode_name="Electrostaff",
    secondary_fire_modes=[Weapon("Blaster Rifle", 30, 3)],
)
upgrade_commander_weapon.upgrade_with_weapon_entry(kallus_bo_rifle)

# Imperial Officer armour & ranks

label = letter_increment(label)
upgrade_officer = UpgradeList(label, base_model=imperial_officer)
upgrade_officer.select_upgrade_with_model_changes_type()
upgrade_officer.upgrade_with_model_changes_entry("Combat Armour", defense=4)
upgrade_officer.upgrade_with_model_changes_entry("Commlink", relay=True)
upgrade_officer.upgrade_with_model_changes_entry("Offensive Orders", spotter=2)
upgrade_officer.upgrade_with_model_changes_entry(
    "Defensive Orders", defend=True, take_cover=1
)

# Generic Officer Binoculars (Spotter[1])

label = letter_increment(label)
upgrade_electrobinoculars = UpgradeList(label)
upgrade_electrobinoculars.select_upgrade_with_rule_model_agnostic_type()
upgrade_electrobinoculars.upgrade_with_rule_model_agnostic_entry(
    "Electrobinoculars", spotter=1
)

# ISF Commander Ranged Replace

label = letter_increment(label)
upgrade_isf_command = UpgradeList(label, base_model=isf_commander)
upgrade_isf_command.select_upgrade_with_model_changes_type()
upgrade_isf_command.upgrade_with_model_changes_entry(
    "Commander Versio", agile=True, disciplined=True, unique="Iden Versio"
)
upgrade_isf_command.upgrade_with_model_changes_entry(
    "Commander Vonreg", repair=1, survivor=True, unique="Rodjer Vonreg"
)

# ISF Commander Ranged Replace

label = letter_increment(label)
upgrade_isf_command_ranged = UpgradeList(label, base_model=isf_commander)
upgrade_isf_command_ranged.select_upgrade_with_weapon_type(
    replace_weapon=core.blaster_rifle
)
upgrade_isf_command_ranged.upgrade_with_weapon_entry(core.heavy_repeater)
upgrade_isf_command_ranged.upgrade_with_weapon_entry(core.heavy_sniper_rifle)
upgrade_isf_command_ranged.upgrade_with_weapon_entry(
    core.heavy_configurable_rifle
)

# ISF Commander Melee Replace

label = letter_increment(label)
upgrade_isf_command_melee = UpgradeList(label, base_model=isf_commander)
upgrade_isf_command_melee.select_upgrade_with_weapon_type(
    replace_weapon=core.combat_training
)
upgrade_isf_command_melee.upgrade_with_weapon_entry(vonreg_vibroblades)

# Stormtrooper officers

label = letter_increment(label)
upgrade_storm_officer = UpgradeList(label, base_model=stormtrooper_officer)
upgrade_storm_officer.select_upgrade_with_model_changes_type()
upgrade_storm_officer.upgrade_with_model_changes_entry(
    "Captain",
    wounds=3,
    relay=True,
)
upgrade_storm_officer.upgrade_with_model_changes_entry(
    "Commander",
    quality=3,
    wounds=3,
    command=True,
)

# Stormtrooper weapons (replace)

label = letter_increment(label)
upgrade_storm_weapons = UpgradeList(label, base_model=stormtrooper)
upgrade_storm_weapons.select_upgrade_with_weapon_type(
    replace_weapon=core.blaster_rifle
)
upgrade_storm_weapons.upgrade_with_weapon_entry(core.blaster_pistol)
upgrade_storm_weapons.upgrade_with_weapon_entry(core.burst_pistol)
upgrade_storm_weapons.upgrade_with_weapon_entry(core.reciprocating_blaster)
upgrade_storm_weapons.upgrade_with_weapon_entry(
    core.heavy_blaster_rifle, lose_expendable=True
)
upgrade_storm_weapons.upgrade_with_weapon_entry(
    core.light_repeating_blaster, lose_expendable=True
)
upgrade_storm_weapons.upgrade_with_weapon_entry(
    core.targeting_rifle, lose_expendable=True
)
upgrade_storm_weapons.upgrade_with_weapon_entry(
    core.rotary_blaster, lose_expendable=True
)
upgrade_storm_weapons.upgrade_with_weapon_entry(
    core.sniper_rifle, lose_expendable=True
)
upgrade_storm_weapons.upgrade_with_weapon_entry(
    core.flamethrower, lose_expendable=True
)

# Stormtrooper weapons (additional)

label = letter_increment(label)
upgrade_storm_add_weap = UpgradeList(label, base_model=stormtrooper)
upgrade_storm_add_weap.select_upgrade_with_weapon_type(limit=1)
upgrade_storm_add_weap.upgrade_with_weapon_entry(core.truncheon)
upgrade_storm_add_weap.upgrade_with_weapon_entry(
    core.rocket_launcher, lose_expendable=True
)
upgrade_storm_add_weap.upgrade_with_weapon_entry(
    core.smart_rocket, lose_expendable=True
)
upgrade_storm_add_weap.upgrade_with_weapon_entry(
    core.mortar, lose_expendable=True
)
upgrade_storm_add_weap.upgrade_with_weapon_entry(
    core.ion_disruptor, lose_expendable=True
)
upgrade_storm_add_weap.upgrade_with_weapon_entry(
    core.concussion_grenade, lose_expendable=True
)
upgrade_storm_add_weap.upgrade_with_weapon_entry(
    core.thermal_detonator, lose_expendable=True
)
upgrade_storm_add_weap.upgrade_with_weapon_entry(
    core.sonic_imploder, lose_expendable=True
)
upgrade_storm_add_weap.upgrade_with_weapon_entry(
    core.ion_grenade, lose_expendable=True
)
upgrade_storm_add_weap.upgrade_with_weapon_entry(
    core.thermal_imploder, lose_expendable=True
)

# Stormtrooper specialisms

label = letter_increment(label)
upgrade_storm_special = UpgradeList(label, base_model=stormtrooper)
upgrade_storm_special.select_upgrade_with_model_changes_type(limit=1)
upgrade_storm_special.upgrade_with_model_changes_entry(
    "Riot Trooper", defense=3
)
upgrade_storm_special.upgrade_with_model_changes_entry(
    "Range Trooper", slow=True, impervious=True
)
upgrade_storm_special.upgrade_with_model_changes_entry(
    "Jetpack Trooper", fast=True, fly=True
)

label = letter_increment(label)
upgrade_storm_limited = UpgradeList(label, base_model=stormtrooper)
upgrade_storm_limited.select_upgrade_with_model_changes_type()
upgrade_storm_limited.upgrade_with_model_changes_entry(
    "Limited Supply", expendable=False, manual_points_adjustment=2
)

# Imperial army trooper weapon replace

label = letter_increment(label)
upgrade_army = UpgradeList(label, base_model=imperial_army_trooper)
upgrade_army.select_upgrade_with_weapon_type(
    replace_weapon=core.blaster_rifle, lose_expendable=True
)
upgrade_army.upgrade_with_weapon_entry(core.rotary_blaster)
upgrade_army.upgrade_with_weapon_entry(core.heavy_blaster_rifle)
upgrade_army.upgrade_with_weapon_entry(core.reciprocating_blaster)
upgrade_army.upgrade_with_weapon_entry(core.mortar)
upgrade_army.upgrade_with_weapon_entry(core.sniper_rifle)
upgrade_army.upgrade_with_weapon_entry(core.flamethrower)

# Imperial riot trooper weapon replace

label = letter_increment(label)
upgrade_army_riot = UpgradeList(label, base_model=imperial_riot_trooper)
upgrade_army_riot.select_upgrade_with_weapon_type(limit=1)
upgrade_army_riot.upgrade_with_weapon_entry(core.blaster_pistol)
upgrade_army_riot.upgrade_with_weapon_entry(core.burst_pistol)

# ISF weapons (replace)

label = letter_increment(label)
upgrade_isf_weapons = UpgradeList(label, base_model=isf_trooper)
upgrade_isf_weapons.select_upgrade_with_weapon_type(
    replace_weapon=core.blaster_rifle
)
upgrade_isf_weapons.upgrade_with_weapon_entry(core.heavy_blaster_rifle)
upgrade_isf_weapons.upgrade_with_weapon_entry(core.sniper_rifle)
upgrade_isf_weapons.upgrade_with_weapon_entry(core.heavy_repeater)

# ISF weapons (additional)

label = letter_increment(label)
upgrade_isf_add_weap = UpgradeList(label, base_model=isf_trooper)
upgrade_isf_add_weap.select_upgrade_with_weapon_type(limit=1)
upgrade_isf_add_weap.upgrade_with_weapon_entry(core.concussion_grenade)
upgrade_isf_add_weap.upgrade_with_weapon_entry(core.thermal_detonator)
upgrade_isf_add_weap.upgrade_with_weapon_entry(core.sonic_imploder)
upgrade_isf_add_weap.upgrade_with_weapon_entry(core.ion_grenade)
upgrade_isf_add_weap.upgrade_with_weapon_entry(
    core.dioxis_grenade
)  # cheap compared to old calculator?
upgrade_isf_add_weap.upgrade_with_weapon_entry(core.thermal_imploder)

# ISF specialisms

label = letter_increment(label)
upgrade_isf_special = UpgradeList(label, base_model=isf_trooper)
upgrade_isf_special.select_upgrade_with_model_changes_type(limit=1)
upgrade_isf_special.upgrade_with_model_changes_entry(
    "Electrobinoculars", spotter=1
)
upgrade_isf_special.upgrade_with_model_changes_entry("Medic", heal=1)
upgrade_isf_special.upgrade_with_model_changes_entry("Engineer", repair=1)

# Purge Trooper weapon

label = letter_increment(label)
upgrade_purge = UpgradeList(label, base_model=purge_trooper)
upgrade_purge.select_upgrade_with_weapon_type(
    replace_weapon=core.blaster_rifle
)
electrobaton = Weapon("Electrobaton", "Melee", 4, pierce=1, suppressive=1)
electrohammer = Weapon(
    "Electrohammer", "Melee", 2, pierce=2, deadly=2, suppressive=1
)
upgrade_purge.upgrade_with_weapon_entry(electrobaton)
upgrade_purge.upgrade_with_weapon_entry(core.electrostaff)
upgrade_purge.upgrade_with_weapon_entry(electrohammer)
upgrade_purge.upgrade_with_weapon_entry(core.heavy_blaster_rifle)
upgrade_purge.upgrade_with_weapon_entry(core.heavy_configurable_rifle)

# Death Trooper weapon (replace)

label = letter_increment(label)
upgrade_death_weap = UpgradeList(label, base_model=death_trooper)
upgrade_death_weap.select_upgrade_with_weapon_type(
    replace_weapon=core.blaster_rifle
)
upgrade_death_weap.upgrade_with_weapon_entry(core.heavy_configurable_rifle)

# Death Trooper weapon (additional)

label = letter_increment(label)
upgrade_death_add_weap = UpgradeList(label, base_model=death_trooper)
upgrade_death_add_weap.select_upgrade_with_weapon_type(limit=1)
upgrade_death_add_weap.upgrade_with_weapon_entry(core.sonic_imploder)
upgrade_death_add_weap.upgrade_with_weapon_entry(core.frag_grenade)

# IRG Weapons

label = letter_increment(label)
upgrade_irg = UpgradeList(label, base_model=imperial_royal_guard)
upgrade_irg.select_upgrade_with_weapon_type(replace_weapon=force_pike)
upgrade_irg.upgrade_with_weapon_entry(core.electrostaff)
upgrade_irg.upgrade_with_weapon_entry(enhanced_force_pike)

# E-web Crew

label = letter_increment(label)
upgrade_eweb = UpgradeList(label, base_model=e_web_team)
upgrade_eweb.select_upgrade_with_model_changes_type()
upgrade_eweb.upgrade_with_model_changes_entry(
    "Stormtrooper Crew", defense=4, disciplined=True
)

# KX Droid weapons

label = letter_increment(label)
upgrade_kx = UpgradeList(label, base_model=kx_security_droid)
upgrade_kx.select_upgrade_with_weapon_type()
upgrade_kx.upgrade_with_weapon_entry(electrobaton)
upgrade_kx.upgrade_with_weapon_entry(core.electrostaff)
upgrade_kx.upgrade_with_weapon_entry(core.heavy_blaster_pistol)
upgrade_kx.upgrade_with_weapon_entry(core.burst_pistol)
upgrade_kx.upgrade_with_weapon_entry(core.blaster_rifle)
upgrade_kx.upgrade_with_weapon_entry(core.reciprocating_blaster)
upgrade_kx.upgrade_with_weapon_entry(core.heavy_blaster_rifle)
upgrade_kx.upgrade_with_weapon_entry(core.sonic_imploder)

# DT Sentry weapons

label = letter_increment(label)
upgrade_sentry = UpgradeList(label, base_model=dt_sentry_droid)
upgrade_sentry.select_upgrade_with_weapon_type()
upgrade_sentry.upgrade_with_weapon_entry(core.electrostaff)
upgrade_sentry.upgrade_with_weapon_entry(electrohammer)
upgrade_sentry.upgrade_with_weapon_entry(core.blaster_carbine)
upgrade_sentry.upgrade_with_weapon_entry(core.smart_rocket)
assault_cannon = Weapon(
    "Assault Cannon", 24, 6, pierce=1, inaccurate=True, split_fire=True
)
upgrade_sentry.upgrade_with_weapon_entry(assault_cannon)
upgrade_sentry.upgrade_with_weapon_entry(core.frag_launcher)

# AT-RT pilot weapons

label = letter_increment(label)
upgrade_atrt = UpgradeList(label, base_model=at_rt)
upgrade_atrt.select_upgrade_with_weapon_type()
upgrade_atrt.upgrade_with_weapon_entry(core.targeting_rifle)
upgrade_atrt.upgrade_with_weapon_entry(core.sniper_rifle)
upgrade_atrt.upgrade_with_weapon_entry(core.heavy_sniper_rifle)

# assign upgrade lists

inquisitor.add_upgrade_list(upgrade_inquisitor)
inquisitor.add_upgrade_list(upgrade_inquisitor_force)
imperial_commander.add_upgrade_list(upgrade_commander)
imperial_commander.add_upgrade_list(upgrade_commander_melee)
imperial_commander.add_upgrade_list(upgrade_commander_weapon)
imperial_officer.add_upgrade_list(upgrade_officer)
imperial_officer.add_upgrade_list(upgrade_electrobinoculars)
isf_commander.add_upgrade_list(upgrade_electrobinoculars)
isf_commander.add_upgrade_list(upgrade_isf_command)
isf_commander.add_upgrade_list(upgrade_isf_command_ranged)
isf_commander.add_upgrade_list(upgrade_isf_command_melee)
stormtrooper_officer.add_upgrade_list(upgrade_electrobinoculars)
stormtrooper_officer.add_upgrade_list(upgrade_storm_officer)
stormtrooper.add_upgrade_list([upgrade_storm_weapons, upgrade_storm_add_weap])
stormtrooper.add_upgrade_list(upgrade_storm_special)
stormtrooper.add_upgrade_list(upgrade_storm_limited)
scout_trooper.add_upgrade_list(upgrade_electrobinoculars)
imperial_army_trooper.add_upgrade_list(upgrade_army)
imperial_riot_trooper.add_upgrade_list(upgrade_army_riot)
isf_trooper.add_upgrade_list([upgrade_isf_weapons, upgrade_isf_add_weap])
isf_trooper.add_upgrade_list(upgrade_isf_special)
purge_trooper.add_upgrade_list(upgrade_purge)
death_trooper.add_upgrade_list(upgrade_death_weap)
death_trooper.add_upgrade_list(upgrade_death_add_weap)
imperial_royal_guard.add_upgrade_list(upgrade_irg)
e_web_team.add_upgrade_list(upgrade_eweb)
kx_security_droid.add_upgrade_list(upgrade_kx)
dt_sentry_droid.add_upgrade_list(upgrade_sentry)
at_rt.add_upgrade_list(upgrade_atrt)

# collate model list

model_list = ModelList()
model_list.add_model_entry(emperor_palpatine)
model_list.add_model_entry(darth_vader)
model_list.add_model_entry(inquisitor)
model_list.add_model_entry(imperial_commander)
model_list.add_model_entry(imperial_officer)
model_list.add_model_entry(isf_commander)
model_list.add_model_entry(stormtrooper_officer)
model_list.add_model_entry(stormtrooper)
model_list.add_model_entry(stormtrooper_heavy_mortar)
model_list.add_model_entry(imperial_army_trooper)
model_list.add_model_entry(imperial_riot_trooper)
model_list.add_model_entry(scout_trooper)
model_list.add_model_entry(isf_trooper)
model_list.add_model_entry(purge_trooper)
model_list.add_model_entry(death_trooper)
model_list.add_model_entry(imperial_royal_guard)
model_list.add_model_entry(imp_speeder_bike)
model_list.add_model_entry(e_web_team)
model_list.add_model_entry(kx_security_droid)
model_list.add_model_entry(dt_sentry_droid)
model_list.add_model_entry(probe_droid)
model_list.add_model_entry(id_seeker_droid)
model_list.add_model_entry(medical_droid)
model_list.add_model_entry(astromech_droid)
model_list.add_model_entry(at_rt)
model_list.add_model_entry(gav_tank)

# write latex files

model_list.file_write_latex("empire_roster.tabl")

upgrade_inquisitor.file_write_latex()
upgrade_inquisitor_force.file_write_latex()
upgrade_commander.file_write_latex()
upgrade_commander_melee.file_write_latex()
upgrade_commander_weapon.file_write_latex()
upgrade_officer.file_write_latex()
upgrade_electrobinoculars.file_write_latex()
upgrade_isf_command.file_write_latex()
upgrade_isf_command_ranged.file_write_latex()
upgrade_isf_command_melee.file_write_latex()
upgrade_storm_officer.file_write_latex()
upgrade_storm_weapons.file_write_latex()
upgrade_storm_add_weap.file_write_latex()
upgrade_storm_special.file_write_latex()
upgrade_storm_limited.file_write_latex()
upgrade_army.file_write_latex()
upgrade_army_riot.file_write_latex()
upgrade_isf_weapons.file_write_latex()
upgrade_isf_add_weap.file_write_latex()
upgrade_isf_special.file_write_latex()
upgrade_purge.file_write_latex()
upgrade_death_weap.file_write_latex()
upgrade_death_add_weap.file_write_latex()
upgrade_irg.file_write_latex()
upgrade_eweb.file_write_latex()
upgrade_kx.file_write_latex()
upgrade_sentry.file_write_latex()
upgrade_atrt.file_write_latex()

# write tsv files

model_list.file_write_tsv(tsv_file)

upgrade_inquisitor.file_write_tsv(tsv_file)
upgrade_inquisitor_force.file_write_tsv(tsv_file)
upgrade_commander.file_write_tsv(tsv_file)
upgrade_commander_melee.file_write_tsv(tsv_file)
upgrade_commander_weapon.file_write_tsv(tsv_file)
upgrade_officer.file_write_tsv(tsv_file)
upgrade_electrobinoculars.file_write_tsv(tsv_file)
upgrade_isf_command.file_write_tsv(tsv_file)
upgrade_isf_command_ranged.file_write_tsv(tsv_file)
upgrade_isf_command_melee.file_write_tsv(tsv_file)
upgrade_storm_officer.file_write_tsv(tsv_file)
upgrade_storm_weapons.file_write_tsv(tsv_file)
upgrade_storm_add_weap.file_write_tsv(tsv_file)
upgrade_storm_special.file_write_tsv(tsv_file)
upgrade_storm_limited.file_write_tsv(tsv_file)
upgrade_army.file_write_tsv(tsv_file)
upgrade_army_riot.file_write_tsv(tsv_file)
upgrade_isf_weapons.file_write_tsv(tsv_file)
upgrade_isf_add_weap.file_write_tsv(tsv_file)
upgrade_isf_special.file_write_tsv(tsv_file)
upgrade_purge.file_write_tsv(tsv_file)
upgrade_death_weap.file_write_tsv(tsv_file)
upgrade_death_add_weap.file_write_tsv(tsv_file)
upgrade_irg.file_write_tsv(tsv_file)
upgrade_eweb.file_write_tsv(tsv_file)
upgrade_kx.file_write_tsv(tsv_file)
upgrade_sentry.file_write_tsv(tsv_file)
upgrade_atrt.file_write_tsv(tsv_file)

""" Imperial Remnants """

tex_upgrade_name = "upgrade_remnant_"

# models

remnant_warlord = Model(
    "Remnant Warlord",
    3,
    5,
    3,
    villain=True,
    spotter=1,
    command=True,
    survivor=True,
)

dark_trooper = Model(
    "Dark Trooper",
    3,
    3,
    2,
    slow=True,
    fly=True,
    impervious=True,
    duellist=True,
    survivor=True,
    droid=True,
    entourage="Moff Gideon",
)
crushing_punch = Weapon(
    "Crushing Punch",
    "Melee",
    2,
    pierce=1,
    deadly=2,
    reciprocating=6,
    inaccurate=True,
)
dark_trooper.equip_weapon(crushing_punch)

praetorian_guard = Model(
    "Praetorian Guard",
    3,
    4,
    3,
    protector="Unit",
    protector_key="Villain",
    impervious=True,
    courage=True,
    duellist=True,
)
praetorian_whip = Weapon(
    "Electro-Chain Whip",
    "Melee",
    3,
    pierce=2,
    suppressive=1,
    primary_fire_mode_name="Sword mode",
    secondary_fire_modes=[
        Weapon(
            "Whip mode",
            "Melee",
            3,
            pierce=1,
            suppressive=1,
            immobilise=True,
            immobilise_roll=5,
        )
    ],
)
praetorian_glaive = Weapon(
    "Electro-Bisento",
    "Melee",
    3,
    pierce=2,
    deadly=2,
)
praetorian_split_spear = Weapon(
    "Vibro-Abir Blade",
    "Melee",
    3,
    pierce=3,
    primary_fire_mode_name="Spear Mode",
    secondary_fire_modes=[
        Weapon(
            "Split mode",
            "Melee",
            4,
            pierce=2,
        )
    ],
)
praetorian_guard.equip_weapon(force_pike)

# -*- Upgrade lists -*-

label = "A"
upgrade_warlord = UpgradeList(label, base_model=remnant_warlord)
upgrade_warlord.select_upgrade_with_model_changes_type()
upgrade_warlord.upgrade_with_model_changes_entry("Combat Armour", defense=4)
upgrade_warlord.upgrade_with_model_changes_entry(
    "Seeker Droid",
    companion="ID Seeker Droid",
    scout=True,
)
upgrade_warlord.upgrade_with_model_changes_entry(
    "ISB", hunter="Target", recon=5
)
upgrade_warlord.upgrade_with_model_changes_entry(
    "Field Agent", command=False, relay=True, agile=True
)
upgrade_warlord.upgrade_with_model_changes_entry(
    "Senior Officer", spotter=2, take_cover=1
)
upgrade_warlord.upgrade_with_model_changes_entry(
    "Sentinel Droid",
    droid=True,
    fear=True,
    defense=3,
    noncombatant=True,
    spotter=2,
    shield=1,
    unique="Palpatine",
)
upgrade_warlord.upgrade_with_model_changes_entry(
    "Captain Pellaeon",
    wounds=4,
    command=False,
    relay=True,
    spotter=2,
    take_cover=1,
    recon=4,
    unique="Gilad Pellaeon",
)
upgrade_warlord.upgrade_with_model_changes_entry(
    "Lord Vonreg",
    wounds=4,
    slow=True,
    repair=1,
    survivor=True,
    unique="Rodjer Vonreg",
)
upgrade_warlord.upgrade_with_model_changes_entry(
    "Lord Vonreg (Jetpack)",
    wounds=4,
    fly=True,
    repair=1,
    survivor=True,
    unique="Rodjer Vonreg",
)
upgrade_warlord.upgrade_with_model_changes_entry(
    "Lord Vonreg (Dark Trooper Armour)",
    defense=2,
    wounds=4,
    fly=True,
    repair=1,
    impervious=True,
    survivor=True,
    unique="Rodjer Vonreg",
)
upgrade_warlord.upgrade_with_model_changes_entry(
    "Agent Selina", unique="Selina Kast"
)
upgrade_warlord.upgrade_with_model_changes_entry(
    "Selina Kast, Daughter of Mandalore",
    unique="Selina Kast",
    defense=3,
    fast=True,
    fly=True,
    impervious=True,
)

label = letter_increment(label)
upgrade_warlord_melee = UpgradeList(label, base_model=remnant_warlord)
upgrade_warlord_melee.select_upgrade_with_weapon_type()
upgrade_warlord_melee.upgrade_with_weapon_entry(core.combat_training)
upgrade_warlord_melee.upgrade_with_weapon_entry(core.stun_baton)
upgrade_warlord_melee.upgrade_with_weapon_entry(core.riot_baton)
chiss_martial_arts = Weapon(
    "Chiss Martial Arts", "Melee", 4, disorient=True, wargear="Thrawn"
)
upgrade_warlord_melee.upgrade_with_weapon_entry(chiss_martial_arts)
selina_vibromachete = Weapon(
    "Vibromachete",
    "Melee",
    3,
    rending=True,
    inaccurate=True,
    wargear="Selina Kast",
)
upgrade_warlord_melee.upgrade_with_weapon_entry(selina_vibromachete)
selina_beskad = Weapon(
    "Beskad",
    "Melee",
    4,
    pierce=2,
    rending=True,
    wargear="Selina Kast",
)
upgrade_warlord_melee.upgrade_with_weapon_entry(selina_beskad)
vonreg_vibroblades = Weapon(
    "Sith Vibroblades", "Melee", 4, rending=True, wargear="Rodjer Vonreg"
)
upgrade_warlord_melee.upgrade_with_weapon_entry(vonreg_vibroblades)
vonreg_lightsaber = Weapon(
    "Trophy Lightsaber",
    "Melee",
    3,
    pierce=2,
    deadly=2,
    inaccurate=True,
    wargear="Rodjer Vonreg",
)
upgrade_warlord_melee.upgrade_with_weapon_entry(vonreg_lightsaber)

label = letter_increment(label)
upgrade_warlord_weapon = UpgradeList(label, base_model=remnant_warlord)
upgrade_warlord_weapon.select_upgrade_with_weapon_type(limit=1)
upgrade_warlord_weapon.upgrade_with_weapon_entry(core.blaster_pistol)
upgrade_warlord_weapon.upgrade_with_weapon_entry(core.heavy_blaster_pistol)
upgrade_warlord_weapon.upgrade_with_weapon_entry(core.dual_blaster_pistols)
upgrade_warlord_weapon.upgrade_with_weapon_entry(core.burst_pistol)
upgrade_warlord_weapon.upgrade_with_weapon_entry(core.sniper_pistol)
upgrade_warlord_weapon.upgrade_with_weapon_entry(core.bryar_pistol)
upgrade_warlord_weapon.upgrade_with_weapon_entry(core.blaster_rifle)
vonreg_wargear = Weapon(
    "Vonreg's Blasters",
    6,
    3,
    quickdraw=True,
    reciprocating=5,
    wargear="Rodjer Vonreg",
    primary_fire_mode_name="Burst Pistol",
    secondary_fire_modes=[
        Weapon("Rifle Full Auto", 30, 3, pierce=1),
        Weapon(
            "Rifle Sniper Shot",
            "inf",
            1,
            pierce=2,
            ammo=1,
            sniper=True,
            deadly=2,
        ),
    ],
)
upgrade_warlord_weapon.upgrade_with_weapon_entry(vonreg_wargear)
selina_burst_pistols = Weapon(
    "Selina's Blasters",
    6,
    6,
    quickdraw=True,
    inaccurate=True,
    reciprocating=5,
    wargear="Selina Kast",
    primary_fire_mode_name="Twin Burst Pistols",
    secondary_fire_modes=[core.blaster_rifle],
)
upgrade_warlord_weapon.upgrade_with_weapon_entry(selina_burst_pistols)

# Dark Trooper programming

label = letter_increment(label)
upgrade_darktrooper_programming = UpgradeList(label, base_model=dark_trooper)
upgrade_darktrooper_programming.select_upgrade_with_model_changes_type(limit=1)
upgrade_darktrooper_programming.upgrade_with_model_changes_entry(
    "Retinue Programming",
    protector="Unit",
    protector_key="Moff Gideon",
)
upgrade_darktrooper_programming.upgrade_with_model_changes_entry(
    "Hunter Programming", hunter="Target"
)
upgrade_darktrooper_programming.upgrade_with_model_changes_entry(
    "Reprogrammed Loyalty",
    entourage=False,
    protector="Unit",
    protector_key="Villain",
    manual_points_adjustment=10,
)

# Dark Trooper weapons

label = letter_increment(label)
upgrade_darktrooper_weapons = UpgradeList(label, base_model=dark_trooper)
upgrade_darktrooper_weapons.select_upgrade_with_weapon_type(limit=1)
upgrade_darktrooper_weapons.upgrade_with_weapon_entry(core.heavy_blaster_rifle)
upgrade_darktrooper_weapons.upgrade_with_weapon_entry(assault_cannon)
upgrade_darktrooper_weapons.upgrade_with_weapon_entry(core.frag_launcher)

label = letter_increment(label)
upgrade_darktrooper_melee = UpgradeList(label, base_model=dark_trooper)
upgrade_darktrooper_melee.select_upgrade_with_weapon_type(
    replace_weapon=crushing_punch
)
greatblade = Weapon("Greatblade", "Melee", 3, pierce=2, deadly=2)
upgrade_darktrooper_melee.upgrade_with_weapon_entry(greatblade)

# Praetorian Guard weapons

label = letter_increment(label)
upgrade_praetorian_melee = UpgradeList(label, base_model=praetorian_guard)
upgrade_praetorian_melee.select_upgrade_with_weapon_type(
    replace_weapon=force_pike
)
upgrade_praetorian_melee.upgrade_with_weapon_entry(praetorian_whip)
upgrade_praetorian_melee.upgrade_with_weapon_entry(praetorian_split_spear)
upgrade_praetorian_melee.upgrade_with_weapon_entry(praetorian_glaive)

label = letter_increment(label)
upgrade_praetorian_ranged = UpgradeList(label, base_model=praetorian_guard)
upgrade_praetorian_ranged.select_upgrade_with_weapon_type()
upgrade_praetorian_ranged.upgrade_with_weapon_entry(core.heavy_blaster_pistol)

# assign upgrade lists

remnant_warlord.add_upgrade_list(upgrade_warlord_melee)
remnant_warlord.add_upgrade_list(upgrade_warlord_weapon)
dark_trooper.add_upgrade_list(upgrade_darktrooper_programming)
dark_trooper.add_upgrade_list(
    [upgrade_darktrooper_weapons, upgrade_darktrooper_melee]
)
praetorian_guard.add_upgrade_list(upgrade_praetorian_melee)
praetorian_guard.add_upgrade_list(upgrade_praetorian_ranged)

# collate model list

list_remnant = ModelList()

list_remnant.add_model_entry(remnant_warlord)
list_remnant.add_model_entry(dark_trooper)
list_remnant.add_model_entry(praetorian_guard)

# write latex files

list_remnant.file_write_latex("galactic_empire_remnant_roster.tabl")
upgrade_warlord.file_write_latex(tex_upgrade_name)
upgrade_warlord_melee.file_write_latex(tex_upgrade_name)
upgrade_warlord_weapon.file_write_latex(tex_upgrade_name)
upgrade_darktrooper_programming.file_write_latex(tex_upgrade_name)
upgrade_darktrooper_weapons.file_write_latex(tex_upgrade_name)
upgrade_darktrooper_melee.file_write_latex(tex_upgrade_name)
upgrade_praetorian_melee.file_write_latex(tex_upgrade_name)
upgrade_praetorian_ranged.file_write_latex(tex_upgrade_name)

# write tsv files

list_remnant.file_write_tsv(
    tsv_file, list_title="Imperial Remnant", append=True
)
upgrade_warlord.file_write_tsv(tsv_file)
upgrade_warlord_melee.file_write_tsv(tsv_file)
upgrade_warlord_weapon.file_write_tsv(tsv_file)
upgrade_darktrooper_programming.file_write_tsv(tsv_file)
upgrade_darktrooper_weapons.file_write_tsv(tsv_file)
upgrade_darktrooper_melee.file_write_tsv(tsv_file)
upgrade_praetorian_melee.file_write_tsv(tsv_file)
upgrade_praetorian_ranged.file_write_tsv(tsv_file)

""" Gideon's Remnant """

tex_upgrade_name = "upgrade_remnant_gideon_"

# models

moff_gideon = Model(
    "Moff Gideon",
    3,
    4,
    4,
    villain=True,
    unique="Moff Gideon",
    fear=True,
    spotter=2,
    command=True,
    survivor=True,
    hunter="Target",
    recon=4,
)
moff_gideon.equip_weapon(core.blaster_pistol)

# -*- Upgrade lists -*-

# Gideon Equipment

label = "A"
upgrade_gideon_armour = UpgradeList(label, base_model=moff_gideon)
upgrade_gideon_armour.select_upgrade_with_model_changes_type()
upgrade_gideon_armour.upgrade_with_model_changes_entry(
    "Dark Trooper Armour",
    defense=2,
    impervious=True,
    fly=True,
)

# Gideon Darksaber

label = letter_increment(label)
upgrade_gideon_darksaber = UpgradeList(label, base_model=moff_gideon)
upgrade_gideon_darksaber.select_upgrade_with_weapon_type()
darksaber = Weapon(
    "The Darksaber", "Melee", 3, pierce=2, deadly=3, unique="The Darksaber"
)
upgrade_gideon_darksaber.upgrade_with_weapon_entry(darksaber)

# Gideon Armour Weapons

label = letter_increment(label)
upgrade_gideon_weapons = UpgradeList(label, base_model=moff_gideon)
upgrade_gideon_weapons.select_upgrade_with_weapon_type()
heavy_electrostaff = Weapon(
    "Heavy Electrostaff",
    "Melee",
    3,
    pierce=2,
    deadly=2,
    suppressive=1,
    throw=True,
)
upgrade_gideon_weapons.upgrade_with_weapon_entry(heavy_electrostaff)
upgrade_gideon_weapons.upgrade_with_weapon_entry(core.whipcord_launcher)
upgrade_gideon_weapons.upgrade_with_weapon_entry(core.wrist_flamer)
concussion_rocket = Weapon(
    "Concussion Rocket",
    12,
    1,
    ammo=1,
    blast=3,
    suppressive=1,
)
upgrade_gideon_weapons.upgrade_with_weapon_entry(concussion_rocket)

# assign upgrade lists

moff_gideon.add_upgrade_list(upgrade_gideon_armour)
moff_gideon.add_upgrade_list(
    [upgrade_gideon_darksaber, upgrade_gideon_weapons]
)

# collate model list

list_remnant_gideon = ModelList()
list_remnant_gideon.add_model_entry(moff_gideon)

# write latex files

list_remnant_gideon.file_write_latex("galactic_empire_gideon_roster.tabl")
upgrade_gideon_armour.file_write_latex(tex_upgrade_name)
upgrade_gideon_darksaber.file_write_latex(tex_upgrade_name)
upgrade_gideon_weapons.file_write_latex(tex_upgrade_name)

# write tsv files

list_remnant_gideon.file_write_tsv(
    tsv_file, list_title="Gideon's Remnant", append=True
)
upgrade_gideon_armour.file_write_tsv(tsv_file)
upgrade_gideon_darksaber.file_write_tsv(tsv_file)
upgrade_gideon_weapons.file_write_tsv(tsv_file)

""" Thrawn's Return """

tex_upgrade_name = "upgrade_remnant_thrawn_"

# models

thrawn = Model(
    "Grand Admiral Thrawn",
    3,
    5,
    4,
    villain=True,
    command=True,
    spotter=2,
    take_cover=2,
    survivor=True,
    disciplined=True,
    unique="Thrawn",
)
thrawn.equip_weapon(chiss_martial_arts)
thrawn.equip_weapon(core.blaster_pistol)

great_mothers = Model(
    "The Great Mothers",
    3,
    5,
    6,
    villain=True,
    dark_side=True,
    noncombatant=True,
    immobile=True,
    defend=True,
    emplacement=True,
    impervious=True,
    unique="The Great Mothers",
    free_special_rule="Dark Magicks",
)

morgan_elsbeth = Model(
    "Morgan Elsbeth",
    3,
    3,
    3,
    villain=True,
    command=True,
    defend=True,
    survivor=True,
    unique="Morgan Elsbeth",
)
morgan_elsbeth.equip_weapon(core.combat_training)

baylan_skoll = Model(
    "Baylan Skoll",
    3,
    3,
    4,
    villain=True,
    dark_side=True,
    deflect=True,
    slow=True,
    jump=3,
    survivor=True,
    impervious=True,
    unique="Baylan Skoll",
)
baylan_skoll.equip_weapon(core.lightsaber_master)
baylan_skoll.equip_weapon(core.force_choke)

shin_hati = Model(
    "Shin Hati",
    4,
    4,
    3,
    villain=True,
    dark_side=True,
    deflect=True,
    jump=3,
    unique="Shin Hati",
    command=True,
)
shin_hati.equip_weapon(core.lightsaber_basic)
shin_hati.equip_weapon(core.force_choke)

marrok = Model(
    "Marrok",
    4,
    3,
    4,
    villain=True,
    dark_side=True,
    deflect=True,
    jump=3,
    survivor=True,
    scout=True,
    hunter="Jedi",
    unique="Marrok",
)
marrok.equip_weapon(core.lightsaber_knight)

night_trooper = Model("Night Trooper", 5, 4, 1, disciplined=True)
night_trooper.equip_weapon(core.combat_training)
night_trooper.equip_weapon(core.blaster_rifle)

# -*- Upgrade lists -*-

label = "A"
upgrade_morgan = UpgradeList(label, base_model=morgan_elsbeth)
upgrade_morgan.select_upgrade_with_model_changes_type()
upgrade_morgan.upgrade_with_model_changes_entry(
    "Gift of Shadow",
    dark_side=True,
    fear=True,
    hunter="Target",
    manual_points_adjustment=2,  # since dark side is usually free
)

label = letter_increment(label)
upgrade_morgan_weap = UpgradeList(label, base_model=morgan_elsbeth)
upgrade_morgan_weap.select_upgrade_with_weapon_type(
    replace_weapon=core.combat_training
)
beskar_spear = Weapon(
    "Beskar Spear",
    "Melee",
    4,
    pierce=2,
    rending=True,
    unique="Beskar Spear",
)
upgrade_morgan_weap.upgrade_with_weapon_entry(beskar_spear)
blade_of_talzin = Weapon(
    "Blade of Talzin",
    "Melee",
    4,
    sniper=True,
    rending=True,
    deadly=2,
    unique="Blade of Talzin",
    wargear="Dark Side",
)
upgrade_morgan_weap.upgrade_with_weapon_entry(blade_of_talzin)

# Night Troopers: Enoch and Zombies

label = letter_increment(label)
upgrade_night_trooper = UpgradeList(label, base_model=night_trooper)
upgrade_night_trooper.select_upgrade_with_model_changes_type(limit=1)
upgrade_night_trooper.upgrade_with_model_changes_entry(
    "Captain Enoch",
    wounds=3,
    quality=4,
    relay=True,
    protector="Unit",
    protector_key="Thrawn",
    unique="Enoch",
)
upgrade_night_trooper.upgrade_with_model_changes_entry(
    "Zombie Night Trooper",
    survivor=True,
    impervious=True,
    impact=1,
    beast=True,
    slow=True,
    entourage="The Great Mothers or Gift of Shadow",
)
upgrade_night_trooper.upgrade_with_model_changes_entry(
    "Zombie Death Trooper",
    defense=3,
    wounds=2,
    survivor=True,
    impervious=True,
    impact=2,
    beast=True,
    slow=True,
    entourage="The Great Mothers or Gift of Shadow",
)

# assign upgrade lists

morgan_elsbeth.add_upgrade_list(upgrade_morgan)
morgan_elsbeth.add_upgrade_list(upgrade_morgan_weap)
remnant_warlord.add_upgrade_list(upgrade_warlord)
night_trooper.add_upgrade_list(upgrade_night_trooper)

# collate model list

list_remnant_thrawn = ModelList()
list_remnant_thrawn.add_model_entry(thrawn)
list_remnant_thrawn.add_model_entry(great_mothers)
list_remnant_thrawn.add_model_entry(morgan_elsbeth)
list_remnant_thrawn.add_model_entry(baylan_skoll)
list_remnant_thrawn.add_model_entry(shin_hati)
list_remnant_thrawn.add_model_entry(marrok)
list_remnant_thrawn.add_model_entry(night_trooper)

# write latex files

list_remnant_thrawn.file_write_latex("galactic_empire_thrawn_roster.tabl")
upgrade_morgan.file_write_latex(tex_upgrade_name)
upgrade_morgan_weap.file_write_latex(tex_upgrade_name)
upgrade_night_trooper.file_write_latex(tex_upgrade_name)

# write tsv files

list_remnant_thrawn.file_write_tsv(
    tsv_file, list_title="Thrawn's Return", append=True
)
upgrade_morgan.file_write_tsv(tsv_file)
upgrade_morgan_weap.file_write_tsv(tsv_file)
upgrade_night_trooper.file_write_tsv(tsv_file)

""" The Eternal Sanction """

tex_upgrade_name = "upgrade_eternal_sanction_"

# -*- Upgrade lists -*-

# assign upgrade lists

# collate model list

# list_eternal_sanction.add_model_entry(vonreg)
# list_eternal_sanction.add_model_entry(selina)

# write latex files

# write tsv files
