with open("emails.txt") as file:
    emails = file.read()
    split_emails = emails.split(',') 
    #print(split_emails)

    #emails_arr = split_emails
    dup_arr = []
    unique_arr = []
    for email in split_emails:
        if email not in unique_arr:
            unique_arr.append(email)
        if email in unique_arr:
            dup_arr.append(email)
    print(unique_arr)


    with open('unitq_emails.txt', 'a') as file:
        for email in unique_arr:
            file.write(email)
            file.write("\n")
