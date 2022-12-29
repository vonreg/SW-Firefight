class Weapon:
    def __init__(
        self,
        name,
        weapon_range,
        attacks,
        ap=0,
        ammo=None,
        sniper=False,
        blast=None,
        deadly=1,
        indirect=False,
        nonlethal=False,
        throw=False,
        rending=False,
        seek=False,
        fixed=None,
        suppressive=0,
        ion=False,
        disorient=False,
    ) -> None:
        self.name = name
        self.range = weapon_range
        self.attacks = attacks
        self.ap = ap
        self.ammo = ammo
        self.sniper = sniper
        self.blast = blast
        self.deadly = deadly
        self.indirect = indirect
        self.nonlethal = nonlethal
        self.throw = throw
        self.rending = rending
        self.seek = seek
        self.fixed = fixed
        self.suppressive = suppressive
        self.ion = ion
        self.disorient = disorient

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
        self.ap_multiplier_dict = {0: 1, 1: 1.5, 2: 2, 3: 2.5, 4: 3}
        self.ammo_multiplier_dict = {
            "Single Use": 0.5,
            1: 0.8,
            2: 0.9,
            3: 0.95,
            4: 1,
            None: 1,
        }
        self.blast_multiplier_dict = {None: 1, 3: 2, 5: 5}
        self.indirect_multiplier_dict = {False: 1, True: 1.1}
        self.nonlethal_multiplier_dict = {False: 1, True: 0.5}
        self.throw_multiplier_dict = {False: 1, True: 1.25}
        self.rending_multiplier_dict = {False: 1, True: 1.5}
        self.seek_multiplier_dict = {False: 1, True: 1.25}

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
        self.disorient_increase_multiplier_dict = {False: 0, True: 30}

    def calculate_cost(self, quality):

        effective_quality = max(quality - self.sniper, 2)
        effective_quality_cost = self.quality_cost_dict[effective_quality]
        range_multiplier = self.range_multiplier_dict[self.range]
        attacks_multiplier = self.attacks
        ap_multiplier = self.ap_multiplier_dict[self.ap]
        ammo_multiplier = self.ammo_multiplier_dict[self.ammo]
        blast_multiplier = self.blast_multiplier_dict[self.blast]
        deadly_multiplier = self.deadly
        indirect_multiplier = self.indirect_multiplier_dict[self.indirect]
        nonlethal_multiplier = self.nonlethal_multiplier_dict[self.nonlethal]
        throw_multiplier = self.throw_multiplier_dict[self.throw]
        rending_multiplier = self.rending_multiplier_dict[self.rending]
        seek_multiplier = self.seek_multiplier_dict[self.seek]

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
        disorient_cost_increase = (
            self.disorient_increase_multiplier_dict[self.disorient]
            * ammo_multiplier
            * range_multiplier
            / self.range_multiplier_dict["inf"]
        )

        if self.range == "melee":
            melee_cost_reduction = (
                -2 * effective_quality_cost * self.range_multiplier_dict["melee"]
            )
        else:
            melee_cost_reduction = 0

        weapon_cost = (
            effective_quality_cost
            * range_multiplier
            * attacks_multiplier
            * ap_multiplier
            * ammo_multiplier
            * blast_multiplier
            * deadly_multiplier
            * indirect_multiplier
            * nonlethal_multiplier
            * throw_multiplier
            * rending_multiplier
            * seek_multiplier
            + fixed_cost_reduction
            + suppressive_cost_increase
            + ion_cost_increase
            + disorient_cost_increase
            + melee_cost_reduction
        )
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
        if self.ap > 0:
            ap = ", AP[%s]" % str(self.ap)
        else:
            ap = ""
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
        if self.rending:
            rending = ", Rending"
        else:
            rending = ""
        if self.seek:
            seek = ", Seek"
        else:
            seek = ""
        if self.fixed:
            fixed = ", Fixed[%s]" % str(self.fixed)
        else:
            fixed = ""
        if self.suppressive:
            suppressive = ", Suppressive"
        else:
            suppressive = ""
        if self.ion:
            ion = ", Ion"
        else:
            ion = ""
        if self.disorient:
            disorient = ", Disorient"
        else:
            disorient = ""

        weapon_string = (
            name
            + " ("
            + weapon_range
            + attacks
            + ap
            + ammo
            + sniper
            + blast
            + deadly
            + indirect
            + nonlethal
            + throw
            + rending
            + seek
            + fixed
            + suppressive
            + ion
            + disorient
            + ")"
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

        self.ranged_weapons = []
        self.single_use_ranged_weapons = []
        self.melee_weapons = []
        self.single_use_melee_weapons = []
        self.upgrade_lists = []

    def calculate_base_model_cost(self):

        quality_cost = self.quality_cost_dict[self.quality]
        defense_cost = self.defense_cost_dict[self.defense]

        base_cost = (quality_cost + defense_cost) * self.toughness

        cover_cost = self.cover_cost_dict[self.cover] * self.toughness
        courage_cost = self.courage_cost_dict[self.courage]
        command_cost = self.command_cost_dict[self.command]
        deflect_cost = self.deflect_cost_dict[self.deflect] * self.toughness
        droid_cost = self.droid_cost_dict[self.droid]
        emplacement_cost = self.emplacement_cost_dict[self.emplacement]
        expendable_cost = self.expendable_cost_dict[self.expendable]
        fast_cost = self.fast_cost_dict[self.fast] * quality_cost
        fear_cost = self.fear_cost_dict[self.fear]
        fly_cost = self.fly_cost_dict[self.fly] * quality_cost
        heal_cost = self.heal * 10
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
        repair_cost = 10 * self.repair
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

        if weapon.range == "Melee" and weapon.ammo == "Single Use":
            self.single_use_melee_weapons.append(weapon)
        elif weapon.range == "Melee":
            self.melee_weapons.append(weapon)
        elif weapon.ammo == "Single Use":
            self.single_use_ranged_weapons.append(weapon)
        else:
            self.ranged_weapons.append(weapon)

        # if weapon.ammo == "Single Use":
        #     self.single_use_weapons.append(weapon)
        # else:
        #     self.weapons.append(weapon)

    # not yet tested!
    def unequip_weapon(self, weapon: Weapon) -> None:
        unequipped = 0
        for equipped_weapon in self.ranged_weapons:
            if weapon.name == equipped_weapon.name:
                self.ranged_weapons.remove(equipped_weapon)
                unequipped += 1
        for equipped_weapon in self.single_use_ranged_weapons:
            if weapon.name == equipped_weapon.name:
                self.single_use_ranged_weapons.remove(equipped_weapon)
                unequipped += 1
        for equipped_weapon in self.melee_weapons:
            if weapon.name == equipped_weapon.name:
                self.melee_weapons.remove(equipped_weapon)
                unequipped += 1
        for equipped_weapon in self.single_use_melee_weapons:
            if weapon.name == equipped_weapon.name:
                self.single_use_melee_weapons.remove(equipped_weapon)
                unequipped += 1
        if unequipped == 0:
            raise Exception("Matching weapon not found - could not unequipped")
        elif unequipped > 1:
            raise Exception("Multiple matching weapons found - unequipped all")

    def add_upgrade_list(self, upgrade_list: UpgradeList) -> None:

        self.upgrade_lists.append(upgrade_list.label)

    def remove_upgrade_list(self, upgrade_list: UpgradeList) -> None:

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

        total_weapon_cost = 0

        # 2 lists: weapons, and single_use_weapons
        single_use_weapons = (
            self.single_use_melee_weapons + self.single_use_ranged_weapons
        )
        weapons = self.melee_weapons + self.ranged_weapons
        single_use_weapon_costs = []
        weapon_costs = []
        weapon_costs_reduced = []

        # pay full for all single use weapons
        if len(single_use_weapons) > 0:
            for weapon in single_use_weapons:
                single_use_weapon_costs.append(weapon.calculate_cost(self.quality))

        if len(weapons) > 0:
            for weapon in weapons:
                weapon_cost = weapon.calculate_cost(self.quality)
                weapon_cost_reduced = (
                    weapon_cost
                    * weapon.ammo_multiplier_dict["Single Use"]
                    / weapon.ammo_multiplier_dict[weapon.ammo]
                )
                weapon_costs.append(weapon_cost)
                weapon_costs_reduced.append(weapon_cost_reduced)

            sorted_weapon_costs, sorted_weapon_costs_reduced = zip(
                *sorted(zip(weapon_costs, weapon_costs_reduced), reverse=True)
            )
            sorted_ranged_weapon_costs = sorted(self.ranged_weapons, reverse=True)

            for i in range(len(sorted_weapon_costs)):
                # pay full for first arsenal(X) weapons
                if i < self.arsenal:
                    total_weapon_cost += sorted_weapon_costs[i]
                # then pay weapon_cost * (ammo(Single Use)/ammo(<weapon's ammo value>))
                else:
                    total_weapon_cost += sorted_weapon_costs_reduced[i]

            if self.gunslinger:
                # add cost of most expensive weapon a second time
                # not yet right - needs to be melee weapons only
                total_weapon_cost += sorted_ranged_weapon_costs[0]

        total_cost = base_cost + total_weapon_cost

        return total_cost

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
        if self.command:
            command = "%sCommand" % comma
            comma = ", "
        else:
            command = ""
        if self.deflect:
            deflect = "%sDeflect" % comma
            comma = ", "
        else:
            deflect = ""
        if self.droid:
            droid = "%sDroid" % comma
            comma = ", "
        else:
            droid = ""
        if self.emplacement:
            emplacement = "%sEmplacement" % comma
            comma = ", "
        else:
            emplacement = ""
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
        if self.hunter:
            hunter = "%sHunter" % comma
            comma = ", "
        else:
            hunter = ""
        if self.immobile:
            immobile = "%sImmobile" % comma
            comma = ", "
        else:
            immobile = ""
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
        if self.relay:
            relay = "%sRelay" % comma
            comma = ", "
        else:
            relay = ""
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
        if self.vehicle:
            vehicle = "%sVehicle" % comma
            comma = ", "
        else:
            vehicle = ""
        if self.free_special_rule:
            free_special_rule = "%s%s" % (comma, self.free_special_rule)
        else:
            free_special_rule = ""

        special_rules = (
            arsenal
            + cover
            + courage
            + command
            + deflect
            + droid
            + emplacement
            + expendable
            + fast
            + fear
            + fly
            + gunslinger
            + heal
            + hero
            + villain
            + hunter
            + immobile
            + jedi
            + sith
            + jump
            + impact
            + impervious
            + protector
            + relay
            + relentless
            + repair
            + scout
            + shield
            + slow
            + spotter
            + take_cover
            + unique
            + vehicle
            + free_special_rule
        )

        options = ""  # blank for now... need to figure out options implementation first
        cost = str(self.calculate_total_cost())

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
        )

        return statline


class UpgradeList:
    def __init__(self, label: str, base_model=None) -> None:
        self.label = label
        self.base_model = base_model
        # if base_model is left blank, need lots of checks to
        # verify it's possible for it to be a generic upgrade
        # all "weapon" upgrades should raise exceptions if base_model=None
        # certain special rule upgrades should raise exceptions if base_model=None (i.e. if they include qu, df, tough etc...)

    def upgrade_with_weapon(self, weapon: Weapon, lose_expendable=False):
        if type(weapon) is not Weapon:
            raise TypeError("weapon type must be Weapon")
        if not self.base_model:
            raise Exception("Weapon upgrades require a base model")

        # make a temporary copy of the model
        # equip that copy with the weapon
        # calculate the cost of the original
        # calculate the cost of the copy
        # take the cost difference; that's the upgrade cost

    def upgrade_with_one_weapon(self, weapon: Weapon, lose_expendable=False):
        if type(weapon) is not Weapon:
            raise TypeError("weapon type must be Weapon")
        if not self.base_model:
            raise Exception("Weapon upgrades require a base model")

    def replace_weapon(
        self, old_weapon: Weapon, new_weapon: Weapon, lose_expendable=False
    ):
        if type(old_weapon) is not Weapon:
            raise TypeError("old_weapon type must be Weapon")
        if type(new_weapon) is not Weapon:
            raise TypeError("new_weapon type must be Weapon")
        if not self.base_model:
            raise Exception("Weapon upgrades require a base model")

        # needs an "unequip" method in model
        # have put one in, but not tested it
