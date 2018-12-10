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
