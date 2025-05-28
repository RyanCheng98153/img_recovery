filename = "./databaserelease2/databaserelease2/jpeg/info.txt"
with open (filename, 'r') as f:
    lines = f.readlines()

items = dict()

for line in lines:
    key = line.split()[0]
    value = line.split()[1:]
    if key not in items:
        items[key] = [value]
    else:
        items[key].append(value)
    
    if line.startswith("woman.bmp"):
        line = line.rstrip("\n")
        # print(line.split())

# for key in items.keys():
#     print("[key]:", key)
#     for value in items[key]:
#         print(value)

src_dir = "./databaserelease2/databaserelease2/jpeg/"
target_dir = "./test_data/"

for key in items.keys():
    for value in items[key]:
        if float(value[1]) <=0 or float(value[1]) >= 1:
            continue
        src_path = src_dir + value[0]
        
        target_path = target_dir + "compressed/" + key.rstrip(".bmp") + "_" + value[1].replace(".", "_") + ".bmp"
        
        with open(src_path, 'rb') as src_file:
            with open(target_path, 'wb') as target_file:
                target_file.write(src_file.read())

src_dir = "./databaserelease2/databaserelease2/refimgs/"

for key in items.keys():
    src_path = src_dir + key
    target_path = target_dir + "original/" + key
    
    with open(src_path, 'rb') as src_file:
        with open(target_path, 'wb') as target_file:
            target_file.write(src_file.read())