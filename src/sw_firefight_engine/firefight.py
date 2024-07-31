from operator import attrgetter
from itertools import combinations
import copy


class Weapon:
    def __init__(
        self,
        name,
        weapon_range,
        attacks,
        pierce=0,
        ammo=None,
        sniper=False,
        blast=None,
        deadly=1,
        inaccurate=False,
        indirect=False,
        nonlethal=False,
        throw=False,
        quickdraw=False,
        reciprocating=False,
        rending=False,
        seek=False,
        slugthrower=False,
        fixed=None,
        suppressive=0,
        ion=False,
        immobilise=False,
        immobilise_roll=None,
        disorient=False,
        unique=False,
        primary_fire_mode_name=None,
        secondary_fire_modes=None,
    ) -> None:
        self.name = name
        self.range = weapon_range
        self.attacks = attacks
        self.pierce = pierce
        self.ammo = ammo
        self.sniper = sniper
        self.blast = blast
        self.deadly = deadly
        self.inaccurate = inaccurate
        self.indirect = indirect
        self.nonlethal = nonlethal
        self.throw = throw
        self.quickdraw = quickdraw
        self.reciprocating = reciprocating
        self.rending = rending
        self.seek = seek
        self.slugthrower = slugthrower
        self.fixed = fixed
        self.suppressive = suppressive
        self.ion = ion
        self.immobilise = immobilise
        self.immobilise_roll = immobilise_roll
        self.disorient = disorient
        self.unique = unique
        self.primary_fire_mode_name = primary_fire_mode_name
        self.secondary_fire_modes = secondary_fire_modes

        if self.range == "Torrent":
            self.torrent = True
        else:
            self.torrent = False

        self.quality_cost_dict = {6: 2, 5: 4, 4: 6, 3: 8, 2: 12}
        self.defense_cost_dict = {6: 2, 5: 4, 4: 6, 3: 8, 2: 12}
        self.range_multiplier_dict = {
            "Melee": 0.3,
            "Torrent": 0.4,
            6: 0.4,
            12: 0.5,
            18: 0.6,
            24: 0.65,
            30: 0.7,
            "inf": 0.7,
        }
        self.pierce_multiplier_dict = {0: 1, 1: 1.5, 2: 2, 3: 2.5, 4: 3}
        self.ammo_multiplier_dict = {
            "Single Use": 0.5,
            1: 0.8,
            2: 0.9,
            3: 0.95,
            4: 1,
            None: 1,
        }
        self.reduced_multiplier_dict = {
            "Single Use": 0.5,
            1: 0.55,
            2: 0.6,
            3: 0.63,
            4: 0.65,
            None: 0.65,
        }
        self.blast_multiplier_dict = {None: 1, 3: 2, 5: 5}
        self.indirect_multiplier_dict = {False: 1, True: 1.1}
        self.nonlethal_multiplier_dict = {False: 1, True: 0.5}
        self.throw_multiplier_dict = {False: 1, True: 1.25}
        self.quickdraw_multiplier_dict = {False: 1, True: 1.3}
        self.rending_multiplier_dict = {False: 1, True: 1.5}
        self.seek_multiplier_dict = {False: 1, True: 1.25}
        self.slugthrower_multiplier_dict = {False: 1, True: 1.25}

        self.fixed_reduction_multiplier_dict = {
            None: 0,
            "Front": 0.5,
            "Left": 0.5,
            "Right": 0.5,
            "Rear": 0.5,
            "Sides": 0.35,
            "Front, Sides": 0.25,
            "Rear, Sides": 0.25,
        }
        self.ion_increase_multiplier_dict = {False: 0, True: 30}
        self.immobilise_increase_multiplier_dict = {False: 0, True: 15}
        self.disorient_increase_multiplier_dict = {False: 0, True: 30}

    def calculate_cost(self, quality):

        effective_quality = min(max(quality - self.sniper + self.inaccurate, 2), 6)
        effective_quality_cost = self.quality_cost_dict[effective_quality]
        range_multiplier = self.range_multiplier_dict[self.range]
        attacks_multiplier = self.attacks
        pierce_multiplier = self.pierce_multiplier_dict[self.pierce]
        ammo_multiplier = self.ammo_multiplier_dict[self.ammo]
        blast_multiplier = self.blast_multiplier_dict[self.blast]
        deadly_multiplier = self.deadly
        indirect_multiplier = self.indirect_multiplier_dict[self.indirect]
        nonlethal_multiplier = self.nonlethal_multiplier_dict[self.nonlethal]
        throw_multiplier = self.throw_multiplier_dict[self.throw]

        if self.torrent:
            torrent_multiplier = 3 * (10 / effective_quality_cost)
        else:
            torrent_multiplier = 1

        quickdraw_multiplier = self.quickdraw_multiplier_dict[self.quickdraw]

        if self.reciprocating:
            reciprocating_multiplier = 1 + (
                min(self.quality_cost_dict[self.reciprocating], effective_quality_cost)
                / effective_quality_cost
            )
        else:
            reciprocating_multiplier = 1

        rending_multiplier = self.rending_multiplier_dict[self.rending]
        seek_multiplier = self.seek_multiplier_dict[self.seek]
        slugthrower_multiplier = self.slugthrower_multiplier_dict[self.slugthrower]

        fixed_cost_reduction = (
            -1
            * effective_quality_cost
            * self.fixed_reduction_multiplier_dict[self.fixed]
        )
        suppressive_cost_increase = (
            10
            * self.suppressive
            * ammo_multiplier
            * range_multiplier
            / self.range_multiplier_dict["inf"]
        )
        ion_cost_increase = (
            self.ion_increase_multiplier_dict[self.ion]
            * ammo_multiplier
            * range_multiplier
            / self.range_multiplier_dict["inf"]
        )
        if self.immobilise_roll:
            immobilise_multiplier = 1 + (
                min(
                    self.quality_cost_dict[self.immobilise_roll], effective_quality_cost
                )
                / effective_quality_cost
            )
        else:
            immobilise_multiplier = 1
        immobilise_cost_increase = (
            self.immobilise_increase_multiplier_dict[self.immobilise]
            * ammo_multiplier
            * immobilise_multiplier
            * range_multiplier
            / self.range_multiplier_dict["inf"]
        )
        disorient_cost_increase = (
            self.disorient_increase_multiplier_dict[self.disorient]
            * ammo_multiplier
            * range_multiplier
            / self.range_multiplier_dict["inf"]
        )
        if self.torrent == True and self.blast == None:
            disorient_cost_increase *= effective_quality_cost / 8

        if self.range == "melee":
            melee_cost_reduction = (
                -2 * effective_quality_cost * self.range_multiplier_dict["melee"]
            )
        else:
            melee_cost_reduction = 0

        primary_cost = (
            effective_quality_cost
            * range_multiplier
            * attacks_multiplier
            * pierce_multiplier
            * ammo_multiplier
            * blast_multiplier
            * deadly_multiplier
            * indirect_multiplier
            * nonlethal_multiplier
            * throw_multiplier
            * torrent_multiplier
            * quickdraw_multiplier
            * reciprocating_multiplier
            * rending_multiplier
            * seek_multiplier
            * slugthrower_multiplier
            + fixed_cost_reduction
            + suppressive_cost_increase
            + ion_cost_increase
            + immobilise_cost_increase
            + disorient_cost_increase
            + melee_cost_reduction
        )

        if self.secondary_fire_modes:
            weapons = self.secondary_fire_modes.copy()
            weapons.insert(0, self)

            weapon_indices = range(len(weapons))

            weapon_combinations = list(combinations(weapon_indices, 1))

            all_cost_options = []
            for weapon_combination in weapon_combinations:
                combination_costs = []
                for i in weapon_indices:
                    if i == 0:
                        weapon = self
                        full_cost = primary_cost
                    else:
                        weapon = weapons[i]
                        full_cost = weapon.calculate_cost(quality)

                    if i in weapon_combination:
                        combination_costs.append(full_cost)
                    else:
                        reduced_cost = (
                            full_cost
                            * weapon.reduced_multiplier_dict[weapon.ammo]
                            / weapon.ammo_multiplier_dict[weapon.ammo]
                        )
                        combination_costs.append(reduced_cost)

                combination_cost = sum(combination_costs)
                all_cost_options.append(combination_cost)

            weapon_cost = max(all_cost_options)

        else:
            weapon_cost = primary_cost

        return weapon_cost

    def write_weapon(self):

        name = self.name
        if self.range == "inf":
            weapon_range = "\u221e, "
        elif self.range == "Melee":
            weapon_range = ""
        elif self.range == "Torrent":
            weapon_range = "Torrent, "
        elif type(self.range) is int:
            weapon_range = '%i", ' % self.range

        attacks = "A%s" % str(self.attacks)
        if self.pierce > 0:
            pierce = ", Pierce[%s]" % str(self.pierce)
        else:
            pierce = ""
        if self.ammo:
            ammo = ", Ammo[%s]" % str(self.ammo)
        else:
            ammo = ""
        if self.sniper:
            sniper = ", Sniper"
        else:
            sniper = ""
        if self.blast:
            blast = ', Blast[%s"]' % str(self.blast)
        else:
            blast = ""
        if self.deadly > 1:
            deadly = ", Deadly[%s]" % str(self.deadly)
        else:
            deadly = ""
        if self.inaccurate:
            inaccurate = ", Inaccurate"
        else:
            inaccurate = ""
        if self.indirect:
            indirect = ", Indirect"
        else:
            indirect = ""
        if self.nonlethal:
            nonlethal = ", Nonlethal"
        else:
            nonlethal = ""
        if self.throw:
            throw = ", Throw"
        else:
            throw = ""
        if self.quickdraw:
            quickdraw = ", Quickdraw"
        else:
            quickdraw = ""
        if self.reciprocating:
            reciprocating = ", Reciprocating[%s+]" % str(self.reciprocating)
        else:
            reciprocating = ""
        if self.rending:
            rending = ", Rending"
        else:
            rending = ""
        if self.seek:
            seek = ", Seek"
        else:
            seek = ""
        if self.slugthrower:
            slugthrower = ", Slugthrower"
        else:
            slugthrower = ""
        if self.fixed:
            fixed = ", Fixed[%s]" % str(self.fixed)
        else:
            fixed = ""
        if self.suppressive:
            suppressive = ", Suppressive[%s]" % str(self.suppressive)
        else:
            suppressive = ""
        if self.ion:
            ion = ", Ion"
        else:
            ion = ""
        if self.immobilise:
            if self.immobilise_roll:
                immobilise = ", Immobilise[%s+]" % str(self.immobilise_roll)
            else:
                immobilise = ", Immobilise"
        else:
            immobilise = ""
        if self.disorient:
            disorient = ", Disorient"
        else:
            disorient = ""
        if self.unique:
            unique = ", Unique[%s]" % self.unique
        else:
            unique = ""

        if self.primary_fire_mode_name:
            primary_fire_mode_name = (
                " - pick one to attack: %s" % self.primary_fire_mode_name
            )
        else:
            primary_fire_mode_name = ""

        secondary_fire_mode_string = ""
        if self.secondary_fire_modes:
            for secondary_fire_mode in self.secondary_fire_modes:

                secondary_fire_mode_string += (
                    "; %s" % secondary_fire_mode.write_weapon()
                )

        weapon_string = (
            name
            + primary_fire_mode_name
            + " ("
            + weapon_range
            + attacks
            + pierce
            + ammo
            + sniper
            + inaccurate
            + blast
            + deadly
            + disorient
            + indirect
            + ion
            + immobilise
            + nonlethal
            + quickdraw
            + reciprocating
            + rending
            + seek
            + slugthrower
            + suppressive
            + throw
            + fixed
            + unique
            + ")"
            + secondary_fire_mode_string
        )
        return weapon_string


class Model:
    def __init__(
        self,
        name,
        quality,
        defense,
        toughness,
        arsenal=1,
        cover=None,
        courage=False,
        command=False,
        deflect=False,
        disciplined=False,
        droid=False,
        emplacement=False,
        expendable=0,
        fast=False,
        fear=False,
        fly=False,
        gunslinger=False,
        heal=0,
        hero=False,
        villain=False,
        hunter=None,
        immobile=False,
        jedi=False,
        sith=False,
        jump=0,
        impact=0,
        impervious=False,
        protector=None,
        protector_key=None,
        relay=False,
        relentless=False,
        repair=0,
        scout=False,
        shield=0,
        slow=False,
        spotter=0,
        take_cover=0,
        unique=False,
        vehicle=False,
        free_special_rule=None,
    ) -> None:
        self.name = name
        self.quality = quality
        self.defense = defense
        self.toughness = toughness
        self.arsenal = arsenal
        self.cover = cover
        self.courage = courage
        self.command = command
        self.deflect = deflect
        self.disciplined = disciplined
        self.droid = droid
        self.emplacement = emplacement
        self.expendable = expendable
        self.fast = fast
        self.fear = fear
        self.fly = fly
        self.heal = heal
        self.hero = hero
        self.gunslinger = gunslinger
        self.villain = villain
        self.hunter = hunter
        self.immobile = immobile
        self.jedi = jedi
        self.sith = sith
        self.jump = jump
        self.impact = impact
        self.impervious = impervious
        self.protector = protector
        self.protector_key = protector_key
        self.relay = relay
        self.relentless = relentless
        self.repair = repair
        self.scout = scout
        self.shield = shield
        self.slow = slow
        self.spotter = spotter
        self.take_cover = take_cover
        self.unique = unique
        self.vehicle = vehicle
        self.free_special_rule = free_special_rule

        self.quality_cost_dict = {6: 2, 5: 4, 4: 6, 3: 8, 2: 12}
        self.defense_cost_dict = {6: 2, 5: 4, 4: 6, 3: 8, 2: 12}

        self.cover_cost_dict = {
            None: 0,
            "Front": 2,
            "Left": 2,
            "Right": 2,
            "Rear": 2,
            "Sides": 4,
            "Front, Sides": 6,
            "Rear, Sides": 6,
        }
        self.courage_cost_dict = {False: 0, True: 5}
        self.command_cost_dict = {False: 0, True: 10}
        self.deflect_cost_dict = {False: 0, True: 2}
        self.droid_cost_dict = {False: 0, True: 0}
        self.emplacement_cost_dict = {False: 0, True: 0}
        self.expendable_cost_dict = {0: 0, 1: 0, 2: 0, 3: 0}
        self.fast_cost_dict = {False: 0, True: 1}
        self.fear_cost_dict = {False: 0, True: 5}
        self.fly_cost_dict = {False: 0, True: 1}
        self.hero_villain_cost_dict = {False: 0, True: 0}
        self.hunter_cost_dict = {None: 0, "Jedi": 0.5, "Sith": 0.5}
        self.immobile_cost_dict = {False: 0, True: -3}
        self.jedi_sith_cost_dict = {False: 0, True: 0}
        self.jump_cost_dict = {0: 0, 3: 0.5, 6: 1}
        self.impervious_cost_dict = {False: 0, True: 6}
        self.protector_cost_dict = {None: 0, "Unit": 1, "Any": 1}
        if self.protector == "Unit" and self.protector_key is None:
            raise Exception(
                'Must specify protector_key=<unit name> if protector="Unit"'
            )
        self.relay_cost_dict = {False: 0, True: 5}
        self.relentless_cost_dict = {False: 0, True: 1}
        self.scout_cost_dict = {False: 0, True: 1}
        self.slow_cost_dict = {False: 0, True: -1}
        self.vehicle_cost_dict = {False: 0, True: 0, "Droid": 0}

        if hero & villain:
            raise Exception("Cannot select both Hero and Villain")
        if jedi & sith:
            raise Exception("Cannot select both Jedi and Sith")

        self.weapons = []

        self.upgrade_lists = []

    def calculate_base_model_cost(self):

        quality_cost = self.quality_cost_dict[self.quality]
        defense_cost = self.defense_cost_dict[self.defense]

        base_cost = (quality_cost + defense_cost) * self.toughness

        cover_cost = self.cover_cost_dict[self.cover] * self.toughness
        courage_cost = self.courage_cost_dict[self.courage]
        command_cost = self.command_cost_dict[self.command]
        deflect_cost = self.deflect_cost_dict[self.deflect] * self.toughness
        disciplined_cost = (
            self.disciplined
            * (self.quality_cost_dict[self.quality - 1] - quality_cost)
            * self.toughness
        )
        droid_cost = self.droid_cost_dict[self.droid]
        emplacement_cost = self.emplacement_cost_dict[self.emplacement]
        expendable_cost = self.expendable_cost_dict[self.expendable]
        fast_cost = self.fast_cost_dict[self.fast] * quality_cost
        fear_cost = self.fear_cost_dict[self.fear]
        fly_cost = self.fly_cost_dict[self.fly] * quality_cost
        heal_cost = quality_cost * self.heal
        hero_cost = self.hero_villain_cost_dict[self.hero]
        villain_cost = self.hero_villain_cost_dict[self.villain]
        hunter_cost = self.hunter_cost_dict[self.hunter] * quality_cost
        immobile_cost = self.immobile_cost_dict[self.immobile] * quality_cost
        jedi_cost = self.jedi_sith_cost_dict[self.jedi]
        sith_cost = self.jedi_sith_cost_dict[self.sith]
        jump_cost = self.jump_cost_dict[self.jump] * quality_cost
        impact_cost = self.impact * 3
        impervious_cost = self.impervious_cost_dict[self.impervious] * self.toughness
        protector_cost = self.protector_cost_dict[self.protector] * defense_cost
        relay_cost = self.relay_cost_dict[self.relay]
        relentless_cost = self.relentless_cost_dict[self.relentless] * quality_cost
        repair_cost = quality_cost * self.repair
        scout_cost = self.scout_cost_dict[self.scout] * quality_cost
        shield_cost = self.shield * (10 + quality_cost)
        # logic here: essentially +1 Toughness w/ 3+ save (would cost 8 + Quality cost)
        # then adding +2 pts for recovery chance
        slow_cost = self.slow_cost_dict[self.slow] * quality_cost
        spotter_cost = self.spotter * 5
        take_cover_cost = self.take_cover * 5
        vehicle_cost = self.vehicle_cost_dict[self.vehicle]

        base_model_cost = (
            base_cost
            + cover_cost
            + courage_cost
            + command_cost
            + deflect_cost
            + disciplined_cost
            + droid_cost
            + emplacement_cost
            + expendable_cost
            + fast_cost
            + fear_cost
            + fly_cost
            + heal_cost
            + hero_cost
            + villain_cost
            + hunter_cost
            + immobile_cost
            + jedi_cost
            + sith_cost
            + jump_cost
            + impact_cost
            + impervious_cost
            + protector_cost
            + relay_cost
            + relentless_cost
            + repair_cost
            + scout_cost
            + shield_cost
            + slow_cost
            + spotter_cost
            + take_cover_cost
            + vehicle_cost
        )

        return base_model_cost

    def equip_weapon(self, weapon: Weapon) -> None:

        self.weapons.append(weapon)

    def unequip_weapon(self, weapon: Weapon) -> None:

        unequipped = 0
        for equipped_weapon in self.weapons:
            if weapon.name == equipped_weapon.name:
                self.weapons.remove(equipped_weapon)
                unequipped += 1
        if unequipped == 0:
            raise Exception("Matching weapon not found - could not be unequipped")
        elif unequipped > 1:
            raise Exception("Multiple matching weapons found - unequipped all")

    def add_upgrade_list(self, upgrade_list) -> None:
        # should add a check in case the upgrade list has a base model
        # if it does, it MUST be this model
        if type(upgrade_list) is not list:
            upgrade_list = [upgrade_list]
        upgrade_list_string = ""
        for i in range(len(upgrade_list)):
            upgrade_list_single = upgrade_list[i]
            if i == 0:
                delim = ""
            else:
                delim = "/"
            upgrade_list_string = (
                upgrade_list_string + delim + upgrade_list_single.label
            )
        self.upgrade_lists.append(upgrade_list_string)

    def remove_upgrade_list(self, upgrade_list) -> None:

        removed = 0
        for upgrade_list in self.upgrade_lists:
            if upgrade_list.label == upgrade_list:
                self.upgrade_lists.remove(upgrade_list)
                removed += 1

        if removed == 0:
            raise Exception("Matching upgrade list not found - could not remove")
        elif removed > 1:
            raise Exception("Multiple matching upgrade lists found - removed all")

    def calculate_total_cost(self) -> None:

        base_cost = self.calculate_base_model_cost()

        weapons_range_getter = attrgetter("range")

        melee_weapons = [
            weapon for weapon in self.weapons if weapons_range_getter(weapon) == "Melee"
        ]
        ranged_weapons = [
            weapon for weapon in self.weapons if weapons_range_getter(weapon) != "Melee"
        ]

        if len(melee_weapons) > 0:
            melee_weapons_cost = self.model_weapon_cost(melee_weapons, 1)
        else:
            melee_weapons_cost = 0

        if len(ranged_weapons) > 0:
            ranged_weapons_cost = self.model_weapon_cost(
                ranged_weapons, self.arsenal, gunslinger=self.gunslinger
            )
        else:
            ranged_weapons_cost = 0

        total_cost = base_cost + melee_weapons_cost + ranged_weapons_cost

        return total_cost

    def model_weapon_cost(self, weapons, arsenal, gunslinger=False):

        weapon_indices = range(len(weapons))

        weapon_combinations = list(combinations(weapon_indices, arsenal))

        all_cost_options = []
        for weapon_combination in weapon_combinations:
            highest_non_ammo_cost = 0
            combination_costs = []
            for i in weapon_indices:
                weapon = weapons[i]
                full_cost = weapon.calculate_cost(self.quality)

                if i in weapon_combination:
                    combination_costs.append(full_cost)
                else:
                    reduced_cost = (
                        full_cost
                        * weapon.reduced_multiplier_dict[weapon.ammo]
                        / weapon.ammo_multiplier_dict[weapon.ammo]
                    )
                    combination_costs.append(reduced_cost)

                if combination_costs[i] > highest_non_ammo_cost and weapon.ammo is None:
                    highest_non_ammo_cost = combination_costs[i]

            combination_cost = sum(combination_costs)
            if gunslinger:
                combination_cost += highest_non_ammo_cost
            all_cost_options.append(combination_cost)

        weapon_cost = round(max(all_cost_options))

        return weapon_cost

    def write_statline(self):

        name = self.name
        quality = "%s+" % str(self.quality)
        defense = "%s+" % str(self.defense)
        toughness = "%s" % str(self.toughness)

        if not self.weapons:
            weapons = ""
        elif len(self.weapons) == 1:
            weapons = self.weapons[0].write_weapon()
        elif len(self.weapons) > 1:
            weapons = ""
            comma = ""
            for weapon in self.weapons:
                weapons = weapons + comma + weapon.write_weapon()
                comma = ", "
        else:
            raise Exception("Unexpected equipped weapons value")

        # special rules
        comma = ""
        if self.jedi:
            jedi = "%sJedi" % comma
            comma = ", "
        else:
            jedi = ""
        if self.sith:
            sith = "%sSith" % comma
            comma = ", "
        else:
            sith = ""
        if self.hero:
            hero = "%sHero" % comma
            comma = ", "
        else:
            hero = ""
        if self.villain:
            villain = "%sVillain" % comma
            comma = ", "
        else:
            villain = ""
        if self.droid:
            droid = "%sDroid" % comma
            comma = ", "
        else:
            droid = ""
        if self.vehicle:
            vehicle = "%sVehicle" % comma
            comma = ", "
        else:
            vehicle = ""
        if self.emplacement:
            emplacement = "%sEmplacement" % comma
            comma = ", "
        else:
            emplacement = ""
        if self.command:
            command = "%sCommand" % comma
            comma = ", "
        else:
            command = ""
        if self.relay:
            relay = "%sRelay" % comma
            comma = ", "
        else:
            relay = ""
        if self.arsenal != 1:
            arsenal = "%sArsenal[%s]" % (comma, str(self.arsenal))
            comma = ", "
        else:
            arsenal = ""
        if self.cover:
            cover = "%sCover[%s]" % (comma, str(self.cover))
            comma = ", "
        else:
            cover = ""
        if self.courage:
            courage = "%sCourage" % comma
            comma = ", "
        else:
            courage = ""
        if self.deflect:
            deflect = "%sDeflect" % comma
            comma = ", "
        else:
            deflect = ""
        if self.disciplined:
            disciplined = "%sDisciplined" % comma
            comma = ", "
        else:
            disciplined = ""
        if self.expendable:
            expendable = "%sExpendable[%s]" % (comma, str(self.expendable))
            comma = ", "
        else:
            expendable = ""
        if self.fast:
            fast = "%sFast" % comma
            comma = ", "
        else:
            fast = ""
        if self.fear:
            fear = "%sFear" % comma
            comma = ", "
        else:
            fear = ""
        if self.fly:
            fly = "%sFly" % comma
            comma = ", "
        else:
            fly = ""
        if self.gunslinger:
            gunslinger = "%sGunslinger" % comma
            comma = ", "
        else:
            gunslinger = ""
        if self.heal:
            heal = "%sHeal[%s]" % (comma, str(self.heal))
            comma = ", "
        else:
            heal = ""
        if self.hunter:
            hunter = "%sHunter[%s]" % (comma, self.hunter)
            comma = ", "
        else:
            hunter = ""
        if self.immobile:
            immobile = "%sImmobile" % comma
            comma = ", "
        else:
            immobile = ""
        if self.jump:
            jump = '%sJump[%s"]' % (comma, str(self.jump))
            comma = ", "
        else:
            jump = ""
        if self.impact:
            impact = "%sImpact[%s]" % (comma, str(self.impact))
            comma = ", "
        else:
            impact = ""
        if self.impervious:
            impervious = "%sImpervious" % comma
            comma = ", "
        else:
            impervious = ""
        if self.protector == "Any":
            protector = "%sProtector" % comma
            comma = ", "
        elif self.protector == "Unit":
            protector = "%sProtector[%s]" % (comma, self.protector_key)
        else:
            protector = ""
        if self.relentless:
            relentless = "%sRelentless" % comma
            comma = ", "
        else:
            relentless = ""
        if self.repair:
            repair = "%sRepair[%s]" % (comma, str(self.repair))
            comma = ", "
        else:
            repair = ""
        if self.scout:
            scout = "%sScout" % comma
            comma = ", "
        else:
            scout = ""
        if self.shield:
            shield = "%sShield[%s]" % (comma, str(self.shield))
            comma = ", "
        else:
            shield = ""
        if self.slow:
            slow = "%sSlow" % comma
            comma = ", "
        else:
            slow = ""
        if self.spotter:
            spotter = "%sSpotter[%s]" % (comma, str(self.spotter))
            comma = ", "
        else:
            spotter = ""
        if self.take_cover:
            take_cover = "%sTake Cover[%s]" % (comma, str(self.take_cover))
            comma = ", "
        else:
            take_cover = ""
        if self.unique:
            unique = "%sUnique[%s]" % (comma, str(self.unique))
            comma = ", "
        else:
            unique = ""
        if self.free_special_rule:
            free_special_rule = "%s%s" % (comma, self.free_special_rule)
        else:
            free_special_rule = ""

        special_rules = (
            jedi
            + sith
            + hero
            + villain
            + droid
            + vehicle
            + emplacement
            + command
            + relay
            + arsenal
            + cover
            + courage
            + deflect
            + disciplined
            + expendable
            + fast
            + fear
            + fly
            + gunslinger
            + heal
            + hunter
            + immobile
            + jump
            + impact
            + impervious
            + protector
            + relentless
            + repair
            + scout
            + shield
            + slow
            + spotter
            + take_cover
            + unique
            + free_special_rule
        )

        options = ""  # blank for now... need to figure out options implementation first
        if len(self.upgrade_lists) > 0:
            for i in range(len(self.upgrade_lists)):
                upgrade_list = self.upgrade_lists[i]
                if i == 0:
                    delim = ""
                else:
                    delim = ", "
                options += delim + upgrade_list

        cost = "%i" % self.calculate_total_cost()

        statline = (
            name
            + "\t"
            + quality
            + "\t"
            + defense
            + "\t"
            + toughness
            + "\t"
            + weapons
            + "\t"
            + special_rules
            + "\t"
            + options
            + "\t"
            + cost
            + "\n"
        )

        return statline


class ModelList:
    def __init__(self) -> None:
        self.models = []
        self.header = "Name\tQu\tDf\tT\tWeapons\tSpecial Rules\tOptions\tCost\n"

    def add_model_entry(self, model: Model):
        self.models.append(model)

    def file_write_tsv(self, filename):
        # works in write mode; assumes this will be done first to create file
        with open(filename, "w", encoding="utf-8") as file:
            file.write(self.header)
            for model in self.models:
                file.write(model.write_statline())


class UpgradeList:
    # need 2 main types:
    # - weapon upgrades (includes upgrade with, upgrade with one etc, upgrade with (lose Expendable), replace (with all the options))
    # - special rule upgrades (somehow need to figure out which can be model-independent, and how to cost those)
    def __init__(self, label: str, base_model=None) -> None:
        self.label = label
        self.base_model = base_model
        self.upgrades = []
        self.upgrade_type = None
        # if base_model is left blank, need lots of checks to
        # verify it's possible for it to be a generic upgrade
        # all "weapon" upgrades should raise exceptions if base_model=None
        # certain special rule upgrades should raise exceptions if base_model=None (i.e. if they include qu, df, tough etc...)
        # But, will probably just do this later

    # "upgrade with weapon"

    def select_upgrade_with_weapon_type(
        self, replace_weapon=None, limit=None, lose_expendable=False
    ):
        if not self.base_model:
            raise Exception("Weapon upgrades require a base model")
        if lose_expendable:
            lose_expendable_string = " (lose Expendable)"
        else:
            lose_expendable_string = ""
        if limit == None:
            limit_string = ""
        elif limit == 1:
            limit_string = " one"
        elif limit == 2:
            limit_string = " two"
        else:
            raise Exception("limit must be None, 1 or 2")

        self.upgrade_list_type = "Weapon"

        if replace_weapon is None:
            type_string = "Upgrade with"
            self.model_copy = copy.deepcopy(self.base_model)
        else:
            if type(replace_weapon) is not Weapon:
                raise TypeError("replaced weapon type must be Weapon")
            type_string = "Replace " + replace_weapon.name + " with"
            self.model_copy = copy.deepcopy(self.base_model)
            self.model_copy.unequip_weapon(replace_weapon)

        self.upgrade_list_header = (
            self.label
            + " | "
            + type_string
            + limit_string
            + lose_expendable_string
            + ":\tCost"
        )

    def upgrade_with_weapon_entry(self, weapon: Weapon):
        if type(weapon) is not Weapon:
            raise TypeError("weapon type must be Weapon")
        # should also have a case for multiple weapons in 1 entry; can just be an option in this function
        # this would also work for "replace" upgrade types, just with an extra conditional
        if not self.upgrade_list_type == "Weapon":
            raise Exception('This entry is valid only for "Weapon" type upgrade lists')

        entry_model_copy = copy.deepcopy(self.model_copy)
        entry_model_copy.equip_weapon(weapon)

        original_cost = self.base_model.calculate_total_cost()
        new_cost = entry_model_copy.calculate_total_cost()

        upgrade_cost = new_cost - original_cost

        # will need to modify this if enabling equipping multiple weapons in 1 upgrade
        upgrade_string = weapon.write_weapon() + "\t%i" % round(upgrade_cost)

        self.upgrades.append(upgrade_string)

    def write_upgrade_list(self):
        upgrade_list_string = ""
        upgrade_list_string += self.upgrade_list_header + "\n"
        for upgrade_string in self.upgrades:
            upgrade_list_string += upgrade_string + "\n"
        return upgrade_list_string

    def file_write_tsv(self, filename):
        # works in append mode; assumes this will be done after writing model list
        with open(filename, "a", encoding="utf-8") as file:
            file.write("\n")
            file.write(self.write_upgrade_list())
