#%%


class Weapon:
    def __init__(
        self,
        range,
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
        fixed=False,
        suppressive=None,
        ion=None,
        disorient=None,
    ) -> None:
        self.range = range
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

        if self.range == "torrent":
            self.torrent = True
        else:
            self.torrent = False

        self.quality_cost_dict = {6: 2, 5: 4, 4: 6, 3: 8, 2: 12}
        self.defense_cost_dict = {6: 2, 5: 4, 4: 6, 3: 8, 2: 12}
        self.range_multiplier_dict = {
            "melee": 0.3,
            "torrent": 0.4,
            6: 0.4,
            12: 0.5,
            18: 0.6,
            24: 0.65,
            30: 0.7,
            "inf": 0.7,
        }
        self.ap_multiplier_dict = {0: 1, 1: 1.5, 2: 2, 3: 2.5, 4: 3}
        self.ammo_multiplier_dict = {"S": 0.5, 1: 0.8, 2: 0.9, 3: 0.95, 4: 1, None: 1}
        self.blast_multiplier_dict = {None: 1, 3: 2, 5: 5}
        self.indirect_multiplier_dict = {False: 1, True: 1.1}
        self.nonlethal_multiplier_dict = {False: 1, True: 0.5}
        self.throw_multiplier_dict = {False: 1, True: 1.25}
        self.rending_multiplier_dict = {False: 1, True: 1.5}
        self.seek_multiplier_dict = {False: 1, True: 1.25}

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

        # fixed
        # suppressive
        # ion
        # disorient

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
            # + additions
            + melee_cost_reduction
        )
        return weapon_cost


# class Model:
#     def __init__(
#         self,
#         quality,
#         defense,
#         toughness,
#         arsenal=None,
#         cover=None,
#         courage=False,
#         command=False,
#         deflect=False,
#         droid=False,
#         emplacement=False,
#         expendable=False,
#         fast=False,
#         fear=False,
#         fly=False,
#         heal=False,
#         hero_villain=False,
#         hunter=False,
#         immobile=False,
#         jedi_sith=False,
#         jump=False,
#         impact=None,
#         impervious=False,
#         protector=False,
#         relay=False,
#         relentless=False,
#         repair=None,
#         scout=False,
#         shield=None,
#         slow=False,
#         spotter=None,
#         take_cover=None,
#         vehicle=None,
#     ) -> None:
#         self.quality = quality
#         self.defense = defense
#         self.toughness = toughness
#         self.arsenal = arsenal
#         self.cover = cover
#         self.courage = courage
#         self.command = command
#         self.deflect = deflect
#         self.droid = droid
#         self.emplacement = emplacement
#         self.expendable = expendable
#         self.fast = fast
#         self.fear = fear
#         self.fly = fly
#         self.heal = heal
#         self.hero_villain = hero_villain
#         self.hunter = hunter
#         self.immobile = immobile
#         self.jedi_sith = jedi_sith
#         self.jump = jump
#         self.impact = impact
#         self.impervious = impervious
#         self.protector = protector
#         self.relay = relay
#         self.relentless = relentless
#         self.repair = repair
#         self.scout = scout
#         self.shield = shield
#         self.slow = slow
#         self.spotter = spotter
#         self.take_cover = take_cover
#         self.vehicle = vehicle

#     def equip_weapon(self, weapon) -> None:
#         pass

testgun = Weapon("inf", 3, ap=0, seek=True)
cost = testgun.calculate_cost(4)
print(cost)


#%% Test Cases:

blaster_rifle = Weapon(30, 3)
print("Blaster Rifle, Qu 5+: %.2f pts" % blaster_rifle.calculate_cost(5))

heavy_blaster_rifle = Weapon(30, 3, ap=1)
print("Blaster Rifle, Qu 4+: %.2f pts" % blaster_rifle.calculate_cost(4))

# %%
