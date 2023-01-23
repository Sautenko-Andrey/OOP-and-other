class DailyBasicPractice:

    def quantify_factorial(self, digit, base=1):
        for i in range(1, digit + 1):
            base *= i
        print(f'Factorial of {digit} = {base}')

    def christmass_tree(self, layers):
        for i in range(1, layers + 1):
            print('*' * i)

    def zamikanie(self, name):
        def welcome():
            print(f'Welcome to our website, {name}')

        return welcome()

    def string_methods(self):
        text = 'I have been Arsenal supporter since 2007'
        res = text.upper()
        res = text.lower()
        res = text.find('A')
        res = text.rfind('0')
        res = text.index('p')
        res = text.rjust(25, '*')
        res = text.ljust(25, '*')
        res = text.isdigit()
        res = text.isalpha()
        res = text.replace('A', 'a')
        res = text.count('e')
        res = '-'.join(text)
        res = text.split()
        res = text.strip()
        res = text.rstrip()
        res = text.lstrip()
        print(res)

    def list_methods(self):
        lst = ['Arsenal', 'Chelsea', 'Liverpool', 'Man City', 'Brighton']

        res=lst.append('Man Unt')
        res=lst.insert(3,'Wolves')
        res=lst.reverse()
        res=lst.count('Arsenal')
        res=lst.copy()
        res=lst.clear()
        res=lst.sort()
        res=lst.remove('Arsenal')
        res=lst.index('Liverpool')
        res=lst.pop()

        print(res)



user = DailyBasicPractice()

