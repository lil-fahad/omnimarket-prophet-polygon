logging.basicConfig(level=logging.INFO)
import logging
def recommend_options(price, prediction, risk="neutral", horizon="short"):
    """
    وظيفة: recommend_options
    """
    expected_change = prediction - price
    pct_change = expected_change / price

    strategies = []

    if pct_change > 0.05:
        strategies.append("شراء Call")
        if horizon == "short":
            strategies.append("شراء Vertical Call Spread")
    elif pct_change < -0.05:
        strategies.append("شراء Put")
        if horizon == "short":
            strategies.append("شراء Vertical Put Spread")
    else:
        strategies.append("فتح Straddle أو Strangle")

    if risk == "hedge":
        strategies.append("استخدام Covered Call أو Protective Put")

    return {
        "expected_change_pct": round(pct_change * 100, 2),
        "strategy": strategies
    }