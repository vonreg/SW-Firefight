from firefight.firefight import Weapon, Model, UpgradeList
from firefight import core

with open("galactic_empire.tsv", "w", encoding="utf-8") as file:

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
        "Unlimited Power", "Torrent", 3, pierce=2, throw=True, ion=True, suppressive=2
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
    vader_force_choke = Weapon("Force Choke", 6, 1, pierce=4, seek=True, throw=True)
    darth_vader.equip_weapon(vader_lightsaber)
    darth_vader.equip_weapon(vader_force_choke)

    inquisitor = Model("Inquisitor", 4, 3, 4, villain=True, deflect=True, jump=3)
    inquisitor_lightsaber = Weapon("Lightsaber", "Melee", 3, pierce=3, deadly=3)
    inquisitor.equip_weapon(inquisitor_lightsaber)

    isf_commander = Model(
        "ISF Commander", 3, 4, 3, villain=True, command=True, scout=True
    )
    isf_commander.equip_weapon(core.blaster_rifle)
    isf_commander.equip_weapon(core.combat_training)

    stormtrooper_commander = Model(
        "Stormtrooper Commander", 3, 4, 3, villain=True, command=True
    )
    stormtrooper_commander.equip_weapon(core.blaster_rifle)

    stormtrooper_captain = Model(
        "Stormtrooper Captain", 4, 4, 3, villain=True, relay=True
    )
    stormtrooper_captain.equip_weapon(core.blaster_rifle)

    stormtrooper_sergeant = Model("Stormtrooper Sergeant", 4, 4, 2, villain=True)
    stormtrooper_sergeant.equip_weapon(core.blaster_rifle)

    imperial_officer = Model("Imperial Officer", 5, 6, 2, villain=True, take_cover=1)
    imperial_officer.equip_weapon(core.blaster_pistol)

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
        "Scout Trooper", 5, 5, 1, expendable=1, scout=True, disciplined=True
    )
    scout_trooper.equip_weapon(core.blaster_pistol)

    isf_trooper = Model("ISF Trooper", 4, 4, 1, scout=True)
    isf_trooper.equip_weapon(core.blaster_rifle)

    purge_trooper = Model("Purge Trooper", 3, 4, 1, hunter="Jedi", impervious=True)
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
        "74-Z Speeder Bike", 5, 5, 3, vehicle=True, impact=2, fast=True, fly=True
    )
    imp_speeder_bike.equip_weapon(core.light_blaster_cannon)
    imp_speeder_bike.equip_weapon(core.blaster_pistol)

    e_web_team = Model(
        "E-Web Team",
        4,
        4,
        3,
        emplacement=True,
        cover="Front",
        slow=True,
        disciplined=True,
    )
    e_web = Weapon("E-Web", "inf", 3, pierce=2, deadly=2, fixed="Front")
    e_web_team.equip_weapon(e_web)
    blaster_rifles = Weapon("Blaster Rifles", 30, 6)
    e_web_team.equip_weapon(blaster_rifles)

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

    astromech_droid = Model("Astromech Droid", 5, 5, 1, droid=True, repair=1, slow=True)
    astromech_droid.equip_weapon(shock_pulse)

    ### Upgrade lists ###

    # A

    upgrade_list_A = UpgradeList("A", base_model=isf_commander)
    upgrade_list_A.select_upgrade_with_weapon_type(replace_weapon=core.blaster_rifle)
    upgrade_list_A.upgrade_with_weapon_entry(core.heavy_repeater)
    upgrade_list_A.upgrade_with_weapon_entry(core.heavy_sniper_rifle)
    upgrade_list_A.upgrade_with_weapon_entry(core.heavy_configurable_rifle)

    # B

    upgrade_list_B = UpgradeList("B", base_model=isf_commander)
    upgrade_list_B.select_upgrade_with_weapon_type(replace_weapon=core.combat_training)
    vibroblades = Weapon("Vibroblades", "Melee", 4, rending=True)
    upgrade_list_B.upgrade_with_weapon_entry(vibroblades)

    # C
    # D

    # E

    upgrade_list_E = UpgradeList("E", base_model=stormtrooper)
    upgrade_list_E.select_upgrade_with_weapon_type(
        replace_weapon=core.blaster_rifle, lose_expendable=True
    )
    upgrade_list_E.upgrade_with_weapon_entry(core.burst_pistol)
    upgrade_list_E.upgrade_with_weapon_entry(core.heavy_blaster_rifle)
    upgrade_list_E.upgrade_with_weapon_entry(core.light_repeating_blaster)
    upgrade_list_E.upgrade_with_weapon_entry(core.reciprocating_blaster)
    upgrade_list_E.upgrade_with_weapon_entry(core.rotary_blaster)
    upgrade_list_E.upgrade_with_weapon_entry(core.sniper_rifle)
    upgrade_list_E.upgrade_with_weapon_entry(core.flamethrower)

    # F

    upgrade_list_F = UpgradeList("F", base_model=stormtrooper)
    upgrade_list_F.select_upgrade_with_weapon_type(limit=1, lose_expendable=True)
    upgrade_list_F.upgrade_with_weapon_entry(core.rocket_launcher)
    upgrade_list_F.upgrade_with_weapon_entry(core.mortar)
    upgrade_list_F.upgrade_with_weapon_entry(core.ion_disruptor)
    upgrade_list_F.upgrade_with_weapon_entry(core.concussion_grenade)
    upgrade_list_F.upgrade_with_weapon_entry(core.thermal_detonator)
    upgrade_list_F.upgrade_with_weapon_entry(core.sonic_imploder)
    upgrade_list_F.upgrade_with_weapon_entry(core.ion_grenade)
    upgrade_list_F.upgrade_with_weapon_entry(core.thermal_imploder)

    # G

    upgrade_list_G = UpgradeList("G", base_model=imperial_army_trooper)
    upgrade_list_G.select_upgrade_with_weapon_type(
        replace_weapon=core.blaster_rifle, lose_expendable=True
    )
    upgrade_list_G.upgrade_with_weapon_entry(core.rotary_blaster)
    upgrade_list_G.upgrade_with_weapon_entry(core.heavy_blaster_rifle)
    upgrade_list_G.upgrade_with_weapon_entry(core.reciprocating_blaster)
    upgrade_list_G.upgrade_with_weapon_entry(core.mortar)
    upgrade_list_G.upgrade_with_weapon_entry(core.sniper_rifle)
    upgrade_list_G.upgrade_with_weapon_entry(core.flamethrower)

    # H

    upgrade_list_H = UpgradeList("H", base_model=imperial_riot_trooper)
    upgrade_list_H.select_upgrade_with_weapon_type(limit=1)
    upgrade_list_H.upgrade_with_weapon_entry(core.blaster_pistol)
    upgrade_list_H.upgrade_with_weapon_entry(core.burst_pistol)

    # I

    upgrade_list_I = UpgradeList("I", base_model=isf_trooper)
    upgrade_list_I.select_upgrade_with_weapon_type(replace_weapon=core.blaster_rifle)
    upgrade_list_I.upgrade_with_weapon_entry(core.heavy_blaster_rifle)
    upgrade_list_I.upgrade_with_weapon_entry(core.sniper_rifle)
    upgrade_list_I.upgrade_with_weapon_entry(core.heavy_repeater)

    # J

    upgrade_list_J = UpgradeList("J", base_model=isf_trooper)
    upgrade_list_J.select_upgrade_with_weapon_type(limit=1)
    upgrade_list_J.upgrade_with_weapon_entry(core.concussion_grenade)
    upgrade_list_J.upgrade_with_weapon_entry(core.thermal_detonator)
    upgrade_list_J.upgrade_with_weapon_entry(core.sonic_imploder)
    upgrade_list_J.upgrade_with_weapon_entry(core.ion_grenade)
    upgrade_list_J.upgrade_with_weapon_entry(
        core.dioxis_grenade
    )  # cheap compared to old calculator?
    upgrade_list_J.upgrade_with_weapon_entry(core.thermal_imploder)

    # K

    # L

    upgrade_list_L = UpgradeList("L", base_model=purge_trooper)
    upgrade_list_L.select_upgrade_with_weapon_type(replace_weapon=core.blaster_rifle)
    upgrade_list_L.upgrade_with_weapon_entry(core.electrostaff)
    upgrade_list_L.upgrade_with_weapon_entry(core.heavy_blaster_rifle)
    upgrade_list_L.upgrade_with_weapon_entry(core.heavy_configurable_rifle)

    # M

    upgrade_list_M = UpgradeList("M", base_model=death_trooper)
    upgrade_list_M.select_upgrade_with_weapon_type(replace_weapon=core.blaster_rifle)
    upgrade_list_M.upgrade_with_weapon_entry(core.heavy_configurable_rifle)

    # N

    upgrade_list_N = UpgradeList("N", base_model=death_trooper)
    upgrade_list_N.select_upgrade_with_weapon_type(limit=1)
    upgrade_list_N.upgrade_with_weapon_entry(core.sonic_imploder)
    upgrade_list_N.upgrade_with_weapon_entry(core.frag_grenade)

    # O

    upgrade_list_O = UpgradeList("O", base_model=imperial_royal_guard)
    upgrade_list_O.select_upgrade_with_weapon_type(replace_weapon=force_pike)
    upgrade_list_O.upgrade_with_weapon_entry(core.electrostaff)
    upgrade_list_O.upgrade_with_weapon_entry(enhanced_force_pike)

    # assign upgrade lists

    isf_commander.add_upgrade_list(upgrade_list_A)
    isf_commander.add_upgrade_list(upgrade_list_B)
    stormtrooper.add_upgrade_list([upgrade_list_E, upgrade_list_F])
    imperial_army_trooper.add_upgrade_list(upgrade_list_G)
    imperial_riot_trooper.add_upgrade_list(upgrade_list_H)
    isf_trooper.add_upgrade_list([upgrade_list_I, upgrade_list_J])
    purge_trooper.add_upgrade_list(upgrade_list_L)
    death_trooper.add_upgrade_list(upgrade_list_M)
    death_trooper.add_upgrade_list(upgrade_list_N)
    imperial_royal_guard.add_upgrade_list(upgrade_list_O)

    # print all

    file.write(core.header)
    file.write(emperor_palpatine.write_statline())
    file.write(darth_vader.write_statline())
    file.write(inquisitor.write_statline())
    file.write(isf_commander.write_statline())
    file.write(stormtrooper_commander.write_statline())
    file.write(stormtrooper_captain.write_statline())
    file.write(stormtrooper_sergeant.write_statline())
    file.write(imperial_officer.write_statline())
    file.write(stormtrooper.write_statline())
    file.write(stormtrooper_heavy_mortar.write_statline())
    file.write(imperial_army_trooper.write_statline())
    file.write(imperial_riot_trooper.write_statline())
    file.write(scout_trooper.write_statline())
    file.write(isf_trooper.write_statline())
    file.write(purge_trooper.write_statline())
    file.write(death_trooper.write_statline())
    file.write(imperial_royal_guard.write_statline())
    file.write(imp_speeder_bike.write_statline())
    file.write(e_web_team.write_statline())
    file.write(id_seeker_droid.write_statline())
    file.write(medical_droid.write_statline())
    file.write(astromech_droid.write_statline())

    file.write("\n")
    file.write(upgrade_list_A.write_upgrade_list())
    file.write("\n")
    file.write(upgrade_list_B.write_upgrade_list())
    file.write("\n")
    file.write(upgrade_list_E.write_upgrade_list())
    file.write("\n")
    file.write(upgrade_list_F.write_upgrade_list())
    file.write("\n")
    file.write(upgrade_list_G.write_upgrade_list())
    file.write("\n")
    file.write(upgrade_list_H.write_upgrade_list())
    file.write("\n")
    file.write(upgrade_list_I.write_upgrade_list())
    file.write("\n")
    file.write(upgrade_list_J.write_upgrade_list())
    file.write("\n")
    file.write(upgrade_list_L.write_upgrade_list())
    file.write("\n")
    file.write(upgrade_list_M.write_upgrade_list())
    file.write("\n")
    file.write(upgrade_list_N.write_upgrade_list())
    file.write("\n")
    file.write(upgrade_list_O.write_upgrade_list())
