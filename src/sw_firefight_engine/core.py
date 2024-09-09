from sw_firefight_engine.firefight import Weapon

# blaster pistols

blaster_pistol = Weapon("Blaster Pistol", 12, 2, quickdraw=True)
dual_blaster_pistols = Weapon(
    "Dual Blaster Pistols", 12, 4, quickdraw=True, split_fire=True, split_fire_range=6
)
heavy_blaster_pistol = Weapon("Heavy Blaster Pistol", 18, 2, pierce=1, quickdraw=True)
burst_pistol = Weapon("Burst Pistol", 6, 3, quickdraw=True, reciprocating=5)
bryar_pistol = Weapon(
    "Bryar Pistol",
    12,
    2,
    quickdraw=True,
    primary_fire_mode_name="Light shot",
    secondary_fire_modes=[Weapon("Heavy Shot", 18, 1, pierce=2, ammo=1, deadly=2)],
)
convertible_pistol = Weapon(
    "Convertible Blaster Pistol",
    12,
    2,
    pierce=1,
    quickdraw=True,
    primary_fire_mode_name="Pistol Config",
    secondary_fire_modes=[
        Weapon("Rifle Config", 18, 3),
        Weapon("Sniper Config", "inf", 1, pierce=2, ammo=1, sniper=True, deadly=2),
    ],
)
sniper_pistol = Weapon("Sniper Pistol", 18, 2, sniper=True, quickdraw=True)

# blaster rifles

blaster_carbine = Weapon("Blaster Carbine", 18, 3, quickdraw=True)
light_blaster_rifle = Weapon("Light Blaster Rifle", 18, 3)
blaster_rifle = Weapon("Blaster Rifle", 30, 3)
reciprocating_blaster = Weapon("Reciprocating Blaster", 30, 3, reciprocating=6)
heavy_blaster_rifle = Weapon("Heavy Blaster Rifle", 30, 3, pierce=1)
scatterblaster = Weapon("Scatterblaster", 12, 2, pierce=2, deadly=2)

# targeting rifles

targeting_rifle = Weapon("Targeting Rifle", "inf", 2, pierce=2, sniper=True)
sniper_rifle = Weapon("Sniper Rifle", "inf", 1, pierce=2, sniper=True, deadly=2)
heavy_sniper_rifle = Weapon(
    "Heavy Sniper Rifle", "inf", 1, pierce=2, ammo=2, sniper=True, deadly=3
)
heavy_configurable_rifle = Weapon(
    "Heavy Configurable Rifle",
    30,
    3,
    pierce=1,
    primary_fire_mode_name="Full Auto",
    secondary_fire_modes=[
        Weapon("Sniper Shot", "inf", 1, pierce=2, ammo=1, sniper=True, deadly=2)
    ],
)

# personal repeating blasters

light_repeating_blaster = Weapon("Light Repeating Blaster", 30, 4)
heavy_repeater = Weapon(
    "Heavy Repeater",
    18,
    4,
    primary_fire_mode_name="Main Barrels",
    secondary_fire_modes=[Weapon("Concussion Blast", 12, 2, pierce=1, ammo=1, blast=3)],
)
rotary_blaster = Weapon("Rotary Blaster", 24, 6, inaccurate=True)

# laser cannons

light_laser_cannon = Weapon("Light Laser Cannon", 30, 2, pierce=2)
laser_cannon_mounted = Weapon(
    "Laser Cannon", "inf", 2, pierce=2, deadly=3, fixed="Front"
)
heavy_rotary_cannon_mounted = Weapon(
    "Heavy Rotary Cannon", 24, 5, pierce=2, deadly=2, fixed="Front", inaccurate=True
)

# emplacement weapons

medium_repeating_blaster = Weapon(
    "Medium Repeating Blaster", "inf", 3, pierce=1, deadly=2, fixed="Front"
)
heavy_repeating_blaster = Weapon(
    "Heavy Repeating Blaster", "inf", 3, pierce=2, deadly=2, fixed="Front"
)
light_blaster_cannon = Weapon("Light Blaster Cannon", "inf", 3, pierce=2, fixed="Front")
blaster_cannon = Weapon("Blaster Cannon", "inf", 2, pierce=2, deadly=2, fixed="Front")
heavy_blaster_cannon = Weapon(
    "Heavy Blaster Cannon", "inf", 2, pierce=2, deadly=3, fixed="Front"
)
repeating_ion_blaster = Weapon(
    "Repeating Ion Blaster", "inf", 3, ion=True, fixed="Front"
)
heavy_mortar = Weapon(
    "Heavy Mortar",
    "inf",
    2,
    pierce=1,
    ammo=2,
    blast=5,
    indirect=True,
    suppressive=True,
    fixed="Front",
)

# slugthrowers

scattergun = Weapon(
    "Scatter Gun", 6, 2, pierce=2, reciprocating=5, slugthrower=True, quickdraw=True
)
cycler_rifle = Weapon(
    "Cycler Rifle", "inf", 1, pierce=3, deadly=3, ammo=1, slugthrower=True
)

# missile weapons

grenade_launcher = Weapon(
    "Grenade Launcher", 18, 2, pierce=1, ammo=1, blast=3, indirect=True
)
homing_launcher = Weapon("Homing Launcher", 24, 2, pierce=2, ammo=1, seek=True)
ion_torpedo = Weapon("Ion Torpedo", 24, 1, ammo=1, ion=True, seek=True)
mortar = Weapon(
    "Mortar", 30, 2, pierce=1, ammo=1, blast=3, indirect=True
)  # should perhaps have a "cumbersome" rule?
rocket_launcher = Weapon("Rocket Launcher", "inf", 2, pierce=1, ammo=1, blast=3)

# grenades

thermal_detonator = Weapon(
    "Thermal Detonator", 12, 2, pierce=1, ammo="Single Use", blast=3, indirect=True
)
concussion_grenade = Weapon(
    "Concussion Grenade",
    12,
    1,
    ammo="Single Use",
    blast=3,
    indirect=True,
    suppressive=1,
)
ion_grenade = Weapon(
    "Ion Grenade", 12, 1, ammo="Single Use", blast=3, indirect=True, ion=True
)
dioxis_grenade = Weapon(
    "Dioxis Grenade", 12, 1, ammo="Single Use", blast=5, indirect=True, disorient=True
)
sonic_imploder = Weapon(
    "Sonic Imploder", 6, 1, ammo="Single Use", blast=5, indirect=True, suppressive=2
)
thermal_imploder = Weapon(
    "Thermal Imploder",
    6,
    1,
    pierce=2,
    ammo="Single Use",
    blast=5,
    indirect=True,
    deadly=3,
)
frag_grenade = Weapon("Frag Grenade", 12, 2, ammo="Single Use", blast=5, indirect=True)

# Melee weapons

combat_training = Weapon("Combat Training", "Melee", 3)
vibroblade = Weapon("Vibroblade", "Melee", 3, rending=1)
truncheon = Weapon("Truncheon", "Melee", 2, suppressive=1)
stun_spear = Weapon("Stun Spear", "Melee", 2, suppressive=2, pierce=1)
electrostaff = Weapon("Electrostaff", "Melee", 4, pierce=2)
electrowhip = Weapon(
    "Electrowhip", "Melee", 3, pierce=2, immobilise=True, immobilise_roll=5
)

# Lightsabers

lightsaber_basic = Weapon("Lightsaber", "Melee", 3, pierce=2, deadly=2)
lightsaber_knight = Weapon("Lightsaber", "Melee", 3, pierce=2, deadly=3)
lightsaber_master = Weapon("Lightsaber", "Melee", 3, pierce=3, deadly=3)
lightsaber_heroic = Weapon("Lightsaber", "Melee", 4, pierce=3, deadly=3)

# Force Powers

force_push = Weapon("Force Push", 12, 2, throw=True, seek=True, quickdraw=True)
jedi_mind_trick = Weapon(
    "Jedi Mind Trick",
    6,
    3,
    seek=True,
    nonlethal=True,
    disorient=True,
)
saber_throw = Weapon(
    "Saber Throw", 12, 2, pierce=2, deadly=2, quickdraw=True, ammo="Single Use"
)
force_choke = Weapon(
    "Force Choke",
    6,
    1,
    pierce=4,
    seek=True,
    throw=True,
)

# Miscellaneous

flamethrower = Weapon("Flamethrower", "Torrent", 2, pierce=1)
wrist_flamer = Weapon(
    "Wrist-mounted Flamethrower", "Torrent", 2, pierce=2, ammo="Single Use"
)
heavy_flamethrower_mounted = Weapon(
    "Heavy Flamethrower", "Torrent", 3, pierce=1, fixed="Front"
)
ion_disruptor = Weapon("Ion Disruptor", "inf", 2, ammo=1, blast=3, ion=True)
ion_blaster_mounted = Weapon(
    "Ion Blaster", "inf", 1, ammo=2, blast=3, ion=True, deadly=3, fixed="Front"
)
whipcord_launcher = Weapon(
    "Whipcord Launcher", 6, 1, ammo="Single Use", immobilise=True, nonlethal=True
)
radiation_cannon = Weapon("Radiation Cannon", 24, 3, disorient=True)
