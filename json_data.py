import json

# считываем из json файла
with open("data.json", "r", encoding='utf-8') as f:
    data = json.load(f)


def data_bus_to_station():
    data_bus = dict()

    for stat, bus_sp in data.items():
        for bus in bus_sp:
            data_bus[bus] = []

    for bus, stat_sp in data_bus.items():
        for stat, bus_sp in data.items():
            if bus in bus_sp:
                stat_sp.append(stat)

    with open("data_bus.json", "w") as f:
        json.dump(data_bus, f,
                  sort_keys=False,
                  indent=4,
                  ensure_ascii=False,
                  separators=(",", ": "))


print("Введите название улицы: ", end="")
name = input()

print("Введите все автобусы через пробел:")
bus = input().split()

data[name] = bus

with open("data.json", "w", encoding="utf-8") as f:
    json.dump(data, f,
              sort_keys=False,
              indent=4,
              ensure_ascii=False,
              separators=(",", ": "))

# Для доп файла автобусы к станциям
data_bus_to_station()
