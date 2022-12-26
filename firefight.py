#%%


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

        attacks = str(self.attacks)
        ap = ", AP[%s]" % str(self.ap)
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
        if self.deadly:
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
            suppressive = ", Suppressive[%s]" % str(self.suppressive)
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
        # ignoring arsenal for now; may not need it to exist in the rules?
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

    def calculate_cost(self):

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
        shield_cost = self.shield * (
            10 + quality_cost
        )  # don't understand the logic here? Should it be defense?
        slow_cost = self.slow_cost_dict[self.slow] * quality_cost
        spotter_cost = self.spotter * 5
        take_cover_cost = self.take_cover * 5
        vehicle_cost = self.vehicle_cost_dict[self.vehicle]

        model_cost = (
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

        return model_cost

    def equip_weapon(self, weapon) -> None:
        pass


#%% Weapon Test Cases:

blaster_rifle = Weapon("Blaster Rifle", 30, 3)
print("%s, Qu 5+: %.2f pts" % (blaster_rifle.name, blaster_rifle.calculate_cost(5)))

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
print("%s: %.2f pts" % (stormtrooper.name, stormtrooper.calculate_cost()))

e_web = Model("E-Web Team", 4, 4, 3, emplacement=True, cover="Front", slow=True)
print("%s: %.2f pts" % (e_web.name, e_web.calculate_cost()))

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
print("%s: %.2f pts" % (id_seeker_droid.name, id_seeker_droid.calculate_cost()))

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
print("%s: %.2f pts" % (darth_vader.name, darth_vader.calculate_cost()))

isf_commander = Model("ISF Commander", 3, 4, 3, villain=True, command=True, scout=True)
print("%s: %.2f pts" % (isf_commander.name, isf_commander.calculate_cost()))

stormtrooper_captain = Model("Stormtrooper Captain", 4, 4, 3, villain=True, relay=True)
print(
    "%s: %.2f pts" % (stormtrooper_captain.name, stormtrooper_captain.calculate_cost())
)

imperial_officer = Model("Imperial Officer", 5, 6, 1, take_cover=1)
print("%s: %.2f pts" % (imperial_officer.name, imperial_officer.calculate_cost()))

purge_trooper = Model("Purge Trooper", 4, 4, 1, hunter="Jedi", impervious=True)
print("%s: %.2f pts" % (purge_trooper.name, purge_trooper.calculate_cost()))

medical_droid = Model("Medical Droid", 6, 5, 1, droid=True, heal=1, slow=True)
print("%s: %.2f pts" % (medical_droid.name, medical_droid.calculate_cost()))

astromech_droid = Model("Astromech Droid", 5, 5, 1, droid=True, repair=1, slow=True)
print("%s: %.2f pts" % (astromech_droid.name, astromech_droid.calculate_cost()))

droideka = Model(
    "Droideka", 4, 4, 3, vehicle="Droid", shield=2, free_special_rule="Roll"
)
print("%s: %.2f pts" % (droideka.name, droideka.calculate_cost()))

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
print("%s: %.2f pts" % (cad_bane.name, cad_bane.calculate_cost()))

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
print("%s: %.2f pts" % (oom_security_droid.name, oom_security_droid.calculate_cost()))

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
