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
            sorted_data_sets[i].fraud="fast_trans"
        else:
            sorted_data_sets[i].fraud="none"
        prev_data_set=sorted_data_sets[i]

    return sorted_data_sets;



def over_limit_transaction(data_sets):
    for i in range(0,len(data_sets)):
        if data_sets[i].features[14]<data_sets[i].features[9]:
            data_sets[i].fraud="ovr_lim_trans"
        else:
            data_sets[i].fraud="none"
    return data_sets


def probing_transaction(data_sets):
    #sorting by customer id
    sorted_data_sets = sorted(data_sets, key=lambda x: x.features[1], reverse=True)
    prev_customer=sorted_data_sets[0].features[1]
    customer_trans=[sorted_data_sets[0]]

    for i in range(1,len(sorted_data_sets)):
        customer=sorted_data_sets[i].features[1]
        if customer==prev_customer:
            customer_trans.append(sorted_data_sets[i])
        else:
            #sorting by date and time
            sorted(customer_trans, key=lambda x: x.features[2], reverse=False)
            isIncrementing(customer_trans)

            #clean array and initialise with customer var
            customer_trans=[]
            customer_trans.append(sorted_data_sets[i])
        prev_customer=customer
        for i in range(20):
            print(sorted_data_sets[i])
    return data_sets

def is_incrementing(customer_trans):
    if len(customer_trans)<4:
        return False
    count = 0
    for i in range(1,len(customer_trans)):
        customer_trans[i].features[9]
        if customer_trans[i].features[9]-customer_trans[i-1].features[9]<50:
            count++;
        else
            count = 0;
        if count > 3:
            for j in range(0,count):
                if customer_trans[i-j].fraud!="inc":
                    customer_trans[i-j].fraud="inc"


def polling_fraud_flags(k, data_sets):
    poll=[0,0,0,0]
    for i in range(len(data_sets)):
        if data_sets[i].fraud != "none":
            poll[data_sets[i].cluster]=poll[data_sets[i].cluster]+1
    return poll
