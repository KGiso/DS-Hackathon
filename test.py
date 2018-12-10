def convert_time_format(time_str):

    #import re
    time_str=re.sub("[^0-9]", "", time_str)
    #convert to int

    return int(time_str);

def removeBlanks(data_set):
    dataset_no_blanks=[]
    for i in range(len(data_set)):
        for j in range(len(data_set.feature)):
            if data_set[i][j]=="":
                break
            dataset_no_blanks.append(data_set[i][j])

    return dataset_no_blanks

def fast_transaction(data_sets):
    # data_sets[i][1]
    # data_sets[i].features[2

    sorted_data_sets = sorted(data_sets, key=lambda x: x.features[1], reverse=True)
    prev_data_set=sorted_data_sets[0];
    for i in range(1,len(sorted_data_sets)):

        if prev_data_set.features[2] == sorted_data_sets[i].features[2]
        & prev_data_set[i].features[1] == sorted_data_sets[i].features[1]:
            sorted_data_sets[i].fraud=True
        else:
            sorted_data_sets[i].fraud=False
        prev_data_set=sorted_data_sets[i]

    return sorted_data_sets;



def over_limit_transaction(data_sets):
    for i in range(0,len(data_sets)):
        if data_sets[i].features[14]<data_sets[i].features[9]:
            data_sets[i].fraud=True
        else:
            data_sets[i].fraud=False
    return data_sets
