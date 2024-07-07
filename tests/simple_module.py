def add_vat(net_value: int | float):
    """Add VAT"""
    return net_value * 1.22


# if a run the module directly, ie: python simple_module.py the following code will be executed
if __name__ == "__main__":
    print(add_vat(20))

