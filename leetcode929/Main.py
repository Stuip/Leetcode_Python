class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        ans = set()
        for email in emails:
            email = email.split("@")
            # print(email)
            if "+" in email[0]:
                index = email[0].index("+")
                email[0] = email[0][:index]
            email[0] = email[0].replace(".","")
            e = email[0] + '@' +email[1]
            ans.add(e)
        return len(ans)
