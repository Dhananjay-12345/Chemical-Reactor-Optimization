def single_reactor_economics(
flowrate,
concentration,
conversion,
product_price,
reactant_price,
operating_hours,
volume,
reactor_cost_per_m3
):

    FA0 = flowrate * concentration

    product_rate = FA0 * conversion

    revenue_per_sec = (product_rate * product_price)

    feed_cost_per_sec = (FA0 * reactant_price)

    profit_per_sec = (revenue_per_sec - feed_cost_per_sec)

    annual_profit = (
    profit_per_sec *
    3600 *
    operating_hours
    )

    capital_cost = (volume *reactor_cost_per_m3)

    if annual_profit > 0:
        payback_period = (
        capital_cost /
        annual_profit
        )
    else:
        payback_period = None

    return (
    revenue_per_sec,
    profit_per_sec,
    annual_profit,
    capital_cost,
    payback_period
    )

def compare_reactors_economics(
flowrate,
concentration,
X_cstr,
X_pfr,
product_price,
reactant_price
):

    FA0 = flowrate * concentration

    product_cstr = FA0 * X_cstr
    product_pfr = FA0 * X_pfr

    profit_cstr = (product_cstr * product_price) - (FA0 * reactant_price)

    profit_pfr = (product_pfr * product_price) - (FA0 * reactant_price)

    return (
    profit_cstr,
    profit_pfr
    )