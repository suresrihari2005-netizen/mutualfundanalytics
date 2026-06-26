def free_cash_flow(cfo, cfi):
    return cfo + cfi


def cfo_quality(cfo, pat):
    if pat == 0:
        return None
    return cfo / pat


def capex_intensity(investing_activity, sales):
    if sales == 0:
        return None
    return (abs(investing_activity) / sales) * 100


def fcf_conversion(fcf, operating_profit):
    if operating_profit == 0:
        return None
    return (fcf / operating_profit) * 100


def capital_allocation_label(cfo, cfi, cff):
    pattern = (
        "+" if cfo >= 0 else "-",
        "+" if cfi >= 0 else "-",
        "+" if cff >= 0 else "-"
    )

    labels = {
        ("+", "-", "-"): "Reinvestor",
        ("+", "+", "+"): "Cash Accumulator",
        ("-", "+", "+"): "Distress",
        ("-", "-", "+"): "Debt Funded Growth"
    }

    return labels.get(pattern, "Other")