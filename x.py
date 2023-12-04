def x(input: int) -> dict[int,int]:
    price: int = input*1.075
    result: dict[int, int] = {}
    result[price/48] = price/36
    return result