def armoured_warfare_special_rules(hover=False, transport=0):
    comma = ""
    hover_cost_dict = {True: 2, False: 0}
    if hover:
        hover_str = "%sHover" % comma
        comma = ", "
    else:
        hover_str = ""
    if transport:
        transport_str = "%sTransport[%i]" % (comma,int(transport))
        comma = ", "
    else:
        transport_str = ""

    hover_cost = hover_cost_dict[hover]
    transport_cost = transport*5

    extra_rules_str = hover_str + transport_str
    extra_rules_cost = hover_cost + transport_cost

    return extra_rules_str, extra_rules_cost