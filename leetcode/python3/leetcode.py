
def numUniqueEmails(emails):
    """
    :type emails: List[str]
    :rtype: int
    """
    emails_new = []
    for email in emails:
        em = list(email)
        at_index = em.index('@')
        local_name = em[0:at_index]
        domain_name = em[at_index+1:-1]
        email_list = []
        for i,value in enumerate(local_name):
            if value is not '.' and value is  not '+':
                email_list.append(value)
            elif value=='.':
                email_list.append('')
            elif value=='+':
                break

        local_name_str = ''.join(email_list)
        print(local_name_str)
        domain_name_str = ''.join(domain_name)
        # local_name_str = local_name_str.replace('.','')
        # local_name_str = re.sub(r'+.*$','',local_name_str)
        email_new = local_name_str + '@' + domain_name_str
        emails_new.append(email_new)
    emails_new2 = set(emails_new)
    print(len(emails_new2))
    return len(emails_new2)
inputs = ["test.email+alex@leetcode.com","test.e.mail+bob.cathy@leetcode.com","testemail+david@lee.tcode.com"]
numUniqueEmails(inputs)
