from firefight.firefight import Weapon, Model, UpgradeList
from firefight import core

print(
    "%s, Qu 5+: %.2f pts"
    % (core.blaster_rifle.name, core.blaster_rifle.calculate_cost(5))
)

heavy_blaster_rifle = Weapon("Heavy Blaster Rifle", 30, 3, ap=1)
print(
    "%s, Qu 4+: %.2f pts"
    % (heavy_blaster_rifle.name, heavy_blaster_rifle.calculate_cost(4))
)

# ion test
# suppressive test
dooku_lightning = Weapon("Force Lightning", 12, 3, ap=1, ion=True, suppressive=1)
print(
    "Dooku's %s, Qu 3+: %.2f pts"
    % (dooku_lightning.name, dooku_lightning.calculate_cost(3))
)

# fixed test
heavy_repeating_blaster = Weapon(
    "Heavy Repeating Blaster", "inf", 3, ap=2, deadly=2, fixed="Front"
)
print(
    "%s, Qu 4+: %.2f pts"
    % (heavy_repeating_blaster.name, heavy_repeating_blaster.calculate_cost(4))
)
# disorient test
dioxis_grenade = Weapon(
    "Dioxis Grenade", 12, 1, ammo="Single Use", blast=5, indirect=True, disorient=True
)
print("%s, Qu 4+: %.2f pts" % (dioxis_grenade.name, dioxis_grenade.calculate_cost(4)))

# %% Base Model Test Cases

stormtrooper = Model("Stormtrooper", 5, 4, 1, expendable=1)
print("%s: %.2f pts" % (stormtrooper.name, stormtrooper.calculate_base_model_cost()))

e_web = Model("E-Web Team", 4, 4, 3, emplacement=True, cover="Front", slow=True)
print("%s: %.2f pts" % (e_web.name, e_web.calculate_base_model_cost()))

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
print(
    "%s: %.2f pts" % (id_seeker_droid.name, id_seeker_droid.calculate_base_model_cost())
)

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
print("%s: %.2f pts" % (darth_vader.name, darth_vader.calculate_base_model_cost()))

isf_commander = Model("ISF Commander", 3, 4, 3, villain=True, command=True, scout=True)
print("%s: %.2f pts" % (isf_commander.name, isf_commander.calculate_base_model_cost()))

stormtrooper_captain = Model("Stormtrooper Captain", 4, 4, 3, villain=True, relay=True)
print(
    "%s: %.2f pts"
    % (stormtrooper_captain.name, stormtrooper_captain.calculate_base_model_cost())
)

imperial_officer = Model("Imperial Officer", 5, 6, 1, take_cover=1)
print(
    "%s: %.2f pts"
    % (imperial_officer.name, imperial_officer.calculate_base_model_cost())
)

purge_trooper = Model("Purge Trooper", 4, 4, 1, hunter="Jedi", impervious=True)
print("%s: %.2f pts" % (purge_trooper.name, purge_trooper.calculate_base_model_cost()))

medical_droid = Model("Medical Droid", 6, 5, 1, droid=True, heal=1, slow=True)
print("%s: %.2f pts" % (medical_droid.name, medical_droid.calculate_base_model_cost()))

astromech_droid = Model("Astromech Droid", 5, 5, 1, droid=True, repair=1, slow=True)
print(
    "%s: %.2f pts" % (astromech_droid.name, astromech_droid.calculate_base_model_cost())
)

droideka = Model(
    "Droideka", 4, 4, 3, vehicle="Droid", shield=2, free_special_rule="Roll"
)
print("%s: %.2f pts" % (droideka.name, droideka.calculate_base_model_cost()))

cad_bane = Model(
    "Cad Bane",
    3,
    4,
    5,
    villain=True,
    scout=True,
    courage=True,
    jump=6,
    unique="Cad Bane",
)
print("%s: %.2f pts" % (cad_bane.name, cad_bane.calculate_base_model_cost()))

oom_security_droid = Model(
    "OOM Security Droid",
    5,
    6,
    1,
    droid=True,
    expendable=2,
    protector="Unit",
    protector_key="OOM Command Droid",
)
print(
    "%s: %.2f pts"
    % (oom_security_droid.name, oom_security_droid.calculate_base_model_cost())
)

#%% test weapon strings

string_test = Weapon(
    "String Test",
    12,
    3,
    ap=1,
    ammo="Single Use",
    sniper=True,
    blast=3,
    deadly=2,
    indirect=True,
    nonlethal=True,
    throw=True,
    rending=True,
    seek=True,
    fixed="Front",
    suppressive=True,
    ion=True,
    disorient=True,
)
print(string_test.write_weapon())

# %% simple equip weapon test

clone_trooper = Model("Clone Trooper", 4, 4, 1)

zap_stick = Weapon("ZZZAP!", "Melee", 3, ammo="Single Use")

# clone_trooper.equip_weapon(blaster_rifle)
clone_trooper.equip_weapon(zap_stick)
clone_trooper.equip_weapon(heavy_repeating_blaster)
print(clone_trooper.weapons)

# %% test model strings

print(clone_trooper.write_statline())

with open("testfile.tsv", "w", encoding="utf-8") as file:
    file.write(clone_trooper.write_statline())

string_test = Model(
    "String Test",
    3,
    4,
    1,
    arsenal=2,
    cover="Front",
    courage=True,
    command=True,
    deflect=True,
    droid=True,
    emplacement=True,
    expendable=2,
    fast=True,
    fear=True,
    fly=True,
    heal=1,
    hero=True,
    villain=False,
    hunter="Jedi",
    immobile=True,
    jedi=False,
    sith=True,
    jump=6,
    impact=2,
    impervious=True,
    protector="Unit",
    protector_key="Darth Vader",
    relay=True,
    relentless=True,
    repair=2,
    scout=True,
    shield=2,
    slow=True,
    spotter=1,
    take_cover=2,
    unique="Test",
    vehicle=True,
    free_special_rule="TestingFreeRules, TestingTesting",
)
print(string_test.write_statline())

#%%

rebel_trooper = Model("Rebel Trooper", 4, 5, 1)

# rebel_trooper.equip_weapon(core.blaster_pistol)
# print(rebel_trooper.write_statline())
# rebel_trooper.unequip_weapon(core.blaster_pistol)

# rebel_trooper.equip_weapon(core.burst_pistol)
# print(rebel_trooper.write_statline())
# rebel_trooper.unequip_weapon(core.burst_pistol)

# rebel_trooper.equip_weapon(core.blaster_rifle)
# print(rebel_trooper.write_statline())
# rebel_trooper.unequip_weapon(core.blaster_rifle)

# rebel_trooper.equip_weapon(core.heavy_blaster_rifle)
# print(rebel_trooper.write_statline())
# rebel_trooper.unequip_weapon(core.heavy_blaster_rifle)

# rebel_trooper.equip_weapon(core.light_repeating_blaster)
# print(rebel_trooper.write_statline())
# rebel_trooper.unequip_weapon(core.light_repeating_blaster)

# rebel_trooper.equip_weapon(core.reciprocating_blaster)
# print(rebel_trooper.write_statline())
# rebel_trooper.unequip_weapon(core.reciprocating_blaster)

# rebel_trooper.equip_weapon(core.rotary_blaster)
# print(rebel_trooper.write_statline())
# rebel_trooper.unequip_weapon(core.rotary_blaster)

rebel_trooper.equip_weapon(core.heavy_repeater)
print(rebel_trooper.write_statline())
rebel_trooper.unequip_weapon(core.heavy_repeater)

print(rebel_trooper.write_statline())

# %%

rebel_trooper.equip_weapon(core.heavy_blaster_rifle)
print(rebel_trooper.write_statline())
rebel_trooper.unequip_weapon(core.heavy_blaster_rifle)

rebel_trooper.equip_weapon(core.heavy_blaster_rifle)
rebel_trooper.equip_weapon(core.thermal_detonator)
print(rebel_trooper.write_statline())
rebel_trooper.unequip_weapon(core.heavy_blaster_rifle)
rebel_trooper.unequip_weapon(core.thermal_detonator)

# %% Testing upgrade lists

stormtrooper.equip_weapon(core.blaster_rifle)
upgrade_list_A = UpgradeList("A", base_model=stormtrooper)
stormtrooper.add_upgrade_list(upgrade_list_A)
upgrade_list_B = UpgradeList("B", base_model=stormtrooper)
upgrade_list_C = UpgradeList("C", base_model=stormtrooper)
stormtrooper.add_upgrade_list([upgrade_list_B, upgrade_list_C])
upgrade_list_D = UpgradeList("D", base_model=stormtrooper)
upgrade_list_E = UpgradeList("E", base_model=stormtrooper)
stormtrooper.add_upgrade_list([upgrade_list_D, upgrade_list_E])
print(stormtrooper.write_statline())

upgrade_list_A.select_upgrade_with_weapon_type()
upgrade_list_A.upgrade_with_weapon_entry(core.thermal_detonator)
upgrade_list_A.upgrade_with_weapon_entry(core.concussion_grenade)
upgrade_list_A.upgrade_with_weapon_entry(core.thermal_imploder)
upgrade_list_A.upgrade_with_weapon_entry(core.dioxis_grenade)
upgrade_list_A.print_upgrade_list()
