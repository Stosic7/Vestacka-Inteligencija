def boje(hex_boja):
    return {
        "Red": int(hex_boja[1:3], 16),
        "Green": int(hex_boja[3:5], 16),
        "Blue": int(hex_boja[5:7], 16)
    }

print(boje("#FA1AA0"))
