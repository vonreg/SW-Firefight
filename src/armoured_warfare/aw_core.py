def armoured_warfare_special_rules(transport=0):
    comma = ""
    if transport:
        transport_str = "%sTransport[%i]" % (comma,int(transport))
        comma = ", "
    else:
        transport_str = ""
    transport_cost = transport*5
    
    extra_rules_str = transport_str
    extra_rules_cost = transport_cost
    return extra_rules_str, extra_rules_cost