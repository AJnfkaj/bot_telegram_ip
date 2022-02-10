import json

with open("data.json", "r", encoding='utf-8') as f:
    data = json.load(f)

with open("data_bus.json", "r", encoding='utf-8') as f:
    data_bus = json.load(f)

def check_ost(ost):
    if ost in data.keys():
        return 1
    else:
        return 0

def search_way_0(start, finish):
    answer = ""

    ost1 = set(data[start])
    ost2 = set(data[finish])

    way = ost1.intersection(ost2)
    way = list(way)
    way.sort()

    if len(way) == 0:
        return 0
    else:
        answer += ("Можно добраться на следующих автобусах без пересадок:" + "\n" + "\n")
        for i in way:
            answer += str(i) + " "
        return answer


def search_way_1(start, finish):
    bus_st = data[start]
    bus_fn = set(data[finish])

    ost_already = []

    answer = ''
    answer += ("Можно добраться с 1-й пересадкой:\n")
    answer += "\n"

    for bus in bus_st:
        ost_bus = data_bus[bus]
        for ost in ost_bus:
            bus_1 = set(data[ost])
            bus_to_fn = bus_fn.intersection(bus_1)

            if len(bus_to_fn) > 0 and (ost not in ost_already):
                bus_to_ost = set()
                bus_ost = set(data[ost])
                bus_to_ost = bus_ost.intersection(set(bus_st))

                x = ("Садитесь на:"+"\n")
                for i in bus_to_ost:
                    x+= i +" "
                answer += str(x) + "\n"
                y = ("Выходите на " + ost)
                answer += str(y) + "\n"
                z = ("Садитесь на" + "\n")
                for i in bus_to_fn:
                    z+= i +" "

                answer += str(z) + "\n"
                answer += "________________" +"\n"+"\n"
            ost_already.append(ost)
    return answer



def main(start, finish):
    answer = search_way_0(start, finish)
    if answer == 0:
        answer = search_way_1(start, finish)
    return answer

