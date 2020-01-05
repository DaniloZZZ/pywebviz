def beer(cnt):
    if cnt == 0: return ''

    s = f"""
{cnt} bottles of beer on the wall, {cnt} bottles of beer.
Take one down and pass it around, {cnt-1} bottles of beer on the wall.
"""
    s += beer(cnt-1)
    return s

if __name__ == "__main__":
    print(beer(5))
