
def parse_price(price_str: str):
    price_str = price_str.lower()

    if "k" in price_str:
        return float(price_str.replace("k", "")) * 1000
    elif "l" in price_str:
        return float(price_str.replace("l", "")) * 100000
    else:
        return float(price_str)