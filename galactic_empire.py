from firefight.firefight import Weapon, Model, UpgradeList
from firefight import core

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
)
unlimited_power = Weapon(
    "Unlimited Power", "Torrent", 3, ap=2, throw=True, ion=True, suppressive=2
)
emperor_palpatine.equip_weapon(unlimited_power)
print(
    emperor_palpatine.write_statline()
)  # this is too cheap, something weird going on with weapon

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
vader_lightsaber = Weapon("Lightsaber", "Melee", 4, ap=4, deadly=3)
vader_force_choke = Weapon("Force Choke", 6, 1, ap=4, seek=True, throw=True)
darth_vader.equip_weapon(vader_lightsaber)
darth_vader.equip_weapon(vader_force_choke)
print(darth_vader.write_statline())

inquisitor = Model("Inquisitor", 4, 3, 4, villain=True, deflect=True, jump=3)
inquisitor_lightsaber = Weapon("Lightsaber", "Melee", 3, ap=3, deadly=3)
inquisitor.equip_weapon(inquisitor_lightsaber)
print(inquisitor.write_statline())

isf_commander = Model("ISF Commander", 3, 4, 3, villain=True, command=True, scout=True)
isf_commander.equip_weapon(core.blaster_rifle)
isf_commander.equip_weapon(core.combat_training)
print(isf_commander.write_statline())

stormtrooper_commander = Model(
    "Stormtrooper Commander", 3, 4, 3, villain=True, command=True
)
stormtrooper_commander.equip_weapon(core.blaster_rifle)
print(stormtrooper_commander.write_statline())

stormtrooper_captain = Model("Stormtrooper Captain", 4, 4, 3, villain=True, relay=True)
stormtrooper_captain.equip_weapon(core.blaster_rifle)
print(stormtrooper_captain.write_statline())

stormtrooper_sergeant = Model("Stormtrooper Sergeant", 4, 4, 2, villain=True)
stormtrooper_sergeant.equip_weapon(core.blaster_rifle)
print(stormtrooper_sergeant.write_statline())

imperial_officer = Model("Imperial Officer", 5, 6, 1, take_cover=1)
imperial_officer.equip_weapon(core.blaster_pistol)
print(imperial_officer.write_statline())

stormtrooper = Model("Stormtrooper", 5, 4, 1, expendable=1)
stormtrooper.equip_weapon(core.blaster_rifle)
print(stormtrooper.write_statline())

scout_trooper = Model("Scout Trooper", 5, 5, 1, expendable=1, scout=True)
scout_trooper.equip_weapon(core.blaster_pistol)
print(scout_trooper.write_statline())

isf_trooper = Model("ISF Trooper", 4, 4, 1, scout=True)
isf_trooper.equip_weapon(core.blaster_rifle)
print(isf_trooper.write_statline())

purge_trooper = Model("Purge Trooper", 3, 4, 1, hunter="Jedi", impervious=True)
purge_trooper.equip_weapon(core.blaster_rifle)
print(purge_trooper.write_statline())

death_trooper = Model("Death Trooper", 3, 3, 2, fear=True)
death_trooper.equip_weapon(core.blaster_rifle)
death_trooper.equip_weapon(core.burst_pistol)
print(death_trooper.write_statline())

imperial_royal_guard = Model(
    "Imperial Royal Guard", 3, 4, 3, protector="Unit", protector_key="Emperor Palpatine"
)
force_pike = Weapon("Force Pike", "Melee", 3, ap=1)
imperial_royal_guard.equip_weapon(force_pike)
imperial_royal_guard.equip_weapon(core.heavy_blaster_pistol)
print(imperial_royal_guard.write_statline())

imp_speeder_bike = Model(
    "74-Z Speeder Bike", 5, 5, 3, vehicle=True, impact=2, fast=True, fly=True
)
imp_speeder_bike.equip_weapon(core.light_blaster_cannon)
imp_speeder_bike.equip_weapon(core.blaster_pistol)
print(imp_speeder_bike.write_statline())

e_web_team = Model("E-Web Team", 4, 4, 3, emplacement=True, cover="Front", slow=True)
e_web = Weapon("E-Web", "inf", 3, ap=2, deadly=2, fixed="Front")
e_web_team.equip_weapon(e_web)
blaster_rifles = Weapon("Blaster Rifles", 30, 6)
e_web_team.equip_weapon(blaster_rifles)
print(e_web_team.write_statline())

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
print(id_seeker_droid.write_statline())

medical_droid = Model("Medical Droid", 6, 5, 1, droid=True, heal=1, slow=True)
lethal_injection = Weapon("Lethal Injection", "Melee", 1, deadly=3)
medical_droid.equip_weapon(lethal_injection)
print(medical_droid.write_statline())

astromech_droid = Model("Astromech Droid", 5, 5, 1, droid=True, repair=1, slow=True)
astromech_droid.equip_weapon(shock_pulse)
print(astromech_droid.write_statline())
