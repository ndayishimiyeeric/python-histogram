def make_histo(inputFile, nbin=20, height=20):
    data = []
    with open(inputFile, "r") as f:
        content = f.read()
        data = content.split(", ")
        for i in data:
            if i.endswith("\n"):
                data[data.index(i)] = i[0:-1]

    data = [float(i) for i in data]

    nbinList = []
    freq_list = []
    min_dist = min(data)
    max_dist = max(data)
    distance = ((max_dist - min_dist)/nbin)
    while True:
        if (len(nbinList) > nbin):
            break
        tempList = []
        freq_list.append(int(min_dist))
        for i in data:
            if i >= min_dist and i < min_dist + distance:
                tempList.append(i)
        min_dist = min_dist + distance
        nbinList.append(len(tempList))
    max_nbinList = max(nbinList)

    height_list = []
    for i in nbinList:
        temp = int((i * height) / max_nbinList)
        height_list.append(temp)
    histo_list = []
    star_str = "  "
    while True:
        if sum(height_list) == 0:
            break
        for i in range(len(height_list)):
            if height_list[i] != 0:
                star_str = star_str + "*   "
                height_list[i] = height_list[i] - 1
            else:
                star_str = star_str + "    "
        histo_list.append(star_str)
        star_str = "  "
    histo_list.reverse()
    freq_str = " "
    for i in freq_list:
        if len(str(i)) == 1:
            freq_str = freq_str + str(i) + "   "
        else:
            freq_str = freq_str + str(i) + "  "

    histo_list.append(freq_str)
    for i in histo_list:
        print(i)
