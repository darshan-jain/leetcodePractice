class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        res = []
        for email in emails:
            local_name, domain_name = email.split('@')
            local_name = local_name.replace('.','') 
            delimitter = '+'
            local_name = local_name.split(delimitter)[0]
            res.append(local_name +'@' +domain_name)
        unique_count = len(set(res))
        print(res)
        return unique_count

        