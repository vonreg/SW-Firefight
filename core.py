from firefight import Weapon, Model

# blaster pistols

blaster_pistol = Weapon("Blaster Pistol", 12, 2)
heavy_blaster_pistol = Weapon("Heavy Blaster Pistol", 18, 2, ap=1)
burst_pistol = Weapon("Burst Pistol", 6, 4)

# blaster rifles

blaster_carbine = Weapon("Blaster Carbine", 18, 3)
blaster_rifle = Weapon("Blaster Rifle", 30, 3)
heavy_blaster_rifle = Weapon("Heavy Blaster Rifle", 30, 3, ap=1)

# targeting rifles

targeting_rifle = Weapon("Targeting Rifle", "inf", 2, ap=2, sniper=True)
sniper_rifle = Weapon("Sniper Rifle", "inf", 1, ap=2, sniper=True, deadly=3)
heavy_sniper_rifle = Weapon("Heavy Sniper Rifle", "inf", 1, ap=3, sniper=True, deadly=3)
# heavy_configurable_rifle = Weapon(
#     "Heavy Configurable Rifle", "inf", 1, ap=2, sniper=True, deadly=3, ammo=2, secondary_mode=...
# )

# personal repeating blasters

light_repeating_blaster = Weapon("Light Repeating Blaster", "inf", 4)
# heavy_repeater = Weapon("Heavy Repeater", secondary_mode=Weapon(.....))
# rotary_blaster = Weapon("Rotary Blaster", 24, 6, inaccurate=True)

# emplacement weapons

medium_repeating_blaster = Weapon(
    "Medium Repeating Blaster", "inf", 3, ap=1, deadly=2, fixed="Front"
)
heavy_repeating_blaster = Weapon(
    "Heavy Repeating Blaster", "inf", 3, ap=2, deadly=2, fixed="Front"
)
blaster_cannon = Weapon("Blaster Cannon", "inf", 2, ap=1, deadly=3, fixed="Front")
heavy_blaster_cannon = Weapon(
    "Heavy Blaster Cannon", "inf", 2, ap=2, deadly=3, fixed="Front"
)
repeating_ion_blaster = Weapon(
    "Repeating Ion Blaster", "inf", 3, ion=True, fixed="Front"
)
heavy_mortar = Weapon(
    "Heavy Mortar",
    "inf",
    2,
    ap=1,
    ammo=2,
    blast=5,
    indirect=True,
    suppressive=True,
    fixed="Front",
)

# missile weapons

grenade_launcher = Weapon(
    "Grenade Launcher", 18, 2, ap=1, ammo=1, blast=3, indirect=True
)
mortar = Weapon(
    "Mortar", 30, 2, ap=1, ammo=1, blast=3, indirect=True
)  # should perhaps have a "cumbersome" rule?
rocket_launcher = Weapon("Rocket Launcher", "inf", 2, ap=1, ammo=1, blast=3)
homing_shot = Weapon("Homing Shot", 18, 2, ap=2, ammo=1, seek=True)
