from jinja2 import Template, Environment, FileSystemLoader, FunctionLoader


def main1():
    class Player:
        def __init__(self,name,city,height,runk):
            self.name=name
            self.city=city
            self.height=height
            self.runk=runk

    player=Player('Sautenko','Kramatorsk',192,75.84)

    my_template=Template('Player name: {{refer.name.upper()}},'
                         'CITY: {{refer.city}},'
                         'HEIGHT: {{refer.height}},'
                         'RUNK: {{refer.runk}}')

    my_render=my_template.render(refer=player)

    print(my_render)



#main1()

def main2():
    class Pats:
        def __init__(self,name,sort):
            self.name=name
            self.sort=sort


        def get_Name(self):
            return self.name

        def get_Sort(self):
            return self.sort

    animal=Pats('Barsik','CAT')

    my_template=Template('I have a {{ animal_info.get_Sort() }}, his name is {{ animal_info.get_Name() }}!')
    my_render=my_template.render(animal_info=animal)

    print(my_render)

#main2()

def main3():
    class Employee:
        def __init__(self,pos,id):
            self.pos=pos
            self.id=id

    employee=Employee('developer',3496)

    my_template=Template('Его должность {{employee_info.pos}}, а id: {{employee_info.id}}.')
    my_render=my_template.render(employee_info=employee)

    print(my_render)

#main3()


def main4():
    my_info={'name':'Андрей','surname':'Саутенко'}

    my_template=Template('Здравствуйте! Мое имя {{info.name}}, а фамилия {{info.surname}}.')
    my_render=my_template.render(info=my_info)

    print(my_render)

#main4()

def main5():
    class Bid:
        def __init__(self,name,bid):
            self.name=name
            self.bid=bid

        def get_name(self):
            return self.name

        def get_bid(self):
            return self.bid

    player=Bid('Alex',6456.54)

    my_template=Template('Игрок {{player_info.get_name()}} сделал ставку в размере {{player_info.get_bid()}} грн.')
    my_render=my_template.render(player_info=player)

    print(my_render)

#main5()

def main_6():
    class Spyders:
        def __init__(self,sort,poison,size):
            self.sort=sort
            self.poison=poison
            self.size=size


    geniculata=Spyders('ground','no danger','25 cm')

    spyder_template=Template('This is {{spyder.sort.upper()}},'
                             ' her poison runk :"{{spyder.poison}}" and size is about {{spyder.size}}.')
    spyder_render=spyder_template.render(spyder=geniculata)

    print(spyder_render)
#main_6()


def main7():
    class Footballer:
        def __init__(self,club,position):
            self.club=club
            self.position=position

        def get_club(self):
            return self.club

        def get_position(self):
            return self.position


    player=Footballer('Arsenal London','midfielder')

    my_template=Template('Kieran Tirny plays for {{player_info.get_club()}} on {{player_info.get_position()}} position.')
    my_render=my_template.render(player_info=player)

    print(my_render)

#main7()


def main8():
    clubArsenal={'club':'Arsenal','city':'London','position':'four'}

    text_template=Template('I support {{info.club}} which bases in {{info.city}}'
                           ' and ultimatelly trying to get {{info.position}} position.')
    render=text_template.render(info=clubArsenal)

    print(render)

#main8()

def main9():
    item='Nike Hoody FL'
    price=50.74

    my_template=Template('I wanna buy back {{some}} which costs {{money}} usd.')
    render=my_template.render(some=item,money=price)

    print(render)

#main9()

def main10():
    text='{%raw%} i am learning {{language}} now. {%endraw%}'

    my_template=Template(text)
    my_render=my_template.render(language='English')

    print(my_render)

#main10()

def main11():
    link='Working with HTML you can always see this tag < a href=#>some text</a>.'

    my_template=Template('{{my_link | e}}')
    my_render=my_template.render(my_link=link)


    print(my_render)

#main11()

def main12():
    teams=[{'id':1,'team':'Arsenal'},
           {'id':2,'team':'Liverpool'},
           {'id':3,'team':'Man City'}]

    link="""<select name= 'teams'>
    {% for each_team in teams -%}
        <option value={{each_team['id']}}>{{each_team['team']}}</option>
    {% endfor -%}
    </select>"""

    my_template=Template(link)
    my_render=my_template.render(teams=teams)

    print(my_render)

#main12()

def main13():
    debts=[{'pos':1,'name':'Ivan'},
          {'pos':2,'name':'Yuriy'},
          {'pos':3,'name':'Farya'}]

    link='''Мои должники:
    {% for each_debt in debts -%}
        номер по порядку: {{each_debt['pos']}}-----{{each_debt['name']}}
    {% endfor -%}
    the end'''

    my_template=Template(link)
    my_render=my_template.render(debts=debts)

    print(my_render)
#main13()

def main14():
    plan=[{'num':1,'task':'wake up'},
          {'num':2,'task':'brush teeth'},
          {'num':3,'task':'studying'}]

    link='''My daily plans:
    {% for each_task in plan -%}
        task number {{each_task['num']}} ) have to do: {{each_task['task']}}
    {% endfor -%}
    have a nice day!'''

    my_template=Template(link)
    my_render=my_template.render(plan=plan)

    print(my_render)
#main14()

def main15():
    cityes=[{'number':1,'city':'Kramatorsk'},
            {'number':2,'city':'Slovyansk'},
            {'number':3,'city':'Kiev'},
            {'number':4,'city':'Odessa'}]

    my_link='''My favourite cityes:
        {% for each_city in cityes -%}
        {% if each_city.number>1 -%}
            # {{each_city['number']}} {{each_city['city']}}
        {% elif each_city.number==4 %}
            I want to play volleyball in {{each_city['city']}}
        {% else -%}
            My homecity is {{each_city['city']}}
        {% endif -%}   
        {% endfor -%}
        I like them so much!'''

    template=Template(my_link)
    render=template.render(cityes=cityes)
    print(render)

#main15()

def main16():
    data=[{'team':'Donbass','runk':99},
          {'team':'DGMA','runk':80},
          {'team':'Gigant','runk':87},
          {'team':'NKMZ','runk':67}]

    my_link='''<Registered teams>
    {% for each_team in data -%}
    {% if each_team.runk>70 -%}
        {{each_team['team']}} (runk: {{each_team['runk']}}) - main draw
    {% else -%}
        {{each_team['team']}} (runk: {{each_team['runk']}}) - qualification draw
    {% endif -%}
    {% endfor -%}'''

    my_template=Template(my_link)
    my_render=my_template.render(data=data)

    print(my_render)

#main16()

def main17():
    sneakers=[{'model':'Nike Downshifter 11','price':72},
              {'model':'Nike Revolution 5','price':66},
              {'model':'Asics Cumulus','price':130},
              {'model':'Asics Patriot 12','price':70},
              {'model':'Adidas Adizerro','price':272}]

    text='Total price : {{ sneakers | sum(attribute="price") }}'
    my_template=Template(text)
    my_render=my_template.render(sneakers=sneakers)

    print(my_render)
#main17()

def main18():
    digits=[10,20,70]

    text='Сумма чисел в списке {{digits | sum}}'
    my_template=Template(text)
    my_render=my_template.render(digits=digits)
    print(my_render)
#main18()

def main19():
    rich_people=[
        {'name':'Ilon Mask','money':10000000000},
        {'name':'Mark Cukerberg','money':10000000},
        {'name':'Bill Gates','money':1000000}
    ]

    text='Самый богатый человек в мире {{(data | max(attribute="money")).name}}'
    text2 = 'самый бедный в этом списке {{(data | min(attribute="money")).name}}.'
    my_template=Template(text)
    my_template2 = Template(text2)
    my_render=my_template.render(data=rich_people)
    my_render2=my_template2.render(data=rich_people)
    print(my_render,',а',my_render2)


#main19()

def main20():
    lotery_numbers=[1,2,3,4,5,6,7,8,9,10]

    text='Сегодня выигрывает номер : {{digit | random }}'
    lotery_template=Template(text)
    lotery_render=lotery_template.render(digit=lotery_numbers)
    print(lotery_render)
#main20()

def main21():
    phone_book=[
        {'name':'Danil','number':80506541236},
        {'name':'Rodik','number':80639874562},
        {'name':'Alexandr','number':80995046245}
    ]

    text='Список моих контактов : {{data | replace("a","A")}}'
    phone_template=Template(text)
    phone_render=phone_template.render(data=phone_book)
    print(phone_render)

#main21()


def main22():
    guests=[
        {'name':'Sautenko','room':123},
        {'name':'Tereshyk','room':457},
        {'name':'Ptyshkin','room':101}
    ]

    text="""Guests list:
    {% for person in guests -%}
    {% filter upper -%}{{person.name}}{% endfilter %}
    {% endfor -%}"""

    text2="""Guest list 2:
    {% for person in guests -%}
    {% filter lower -%}{{person.name}}{% endfilter %}
    {% endfor -%}"""


    template=Template(text)
    template2 = Template(text2)
    render=template.render(guests=guests)
    render2 = template2.render(guests=guests)
    print(render,render2)
#main22()

def main23():
    html="""
    {% macro input(name,value='',type='text',size=20) -%}
        <input type ="{{type}}" name="{{name}}" value="{{value | e}}" size="{{size}}">
    {% endmacro %}
    
    <p>{{ input ('username') }}
    <p>{{ input ('email') }}
    <p>{{ input ('password') }}
    """

    template=Template(html)
    render=template.render()
    print(render)
#main23()
def main24():
    html='''
    {% macro input (name,position,sallary) -%}
        <input name='{{name}}' position='{{position}}' sallary='{{sallary}}'>
    {% endmacro %}
    
    <p>{{ input ('Andrey','developer',5000) }}
    <p>{{ input ('Danil','manager',5500) }}
    <p>{{ input ('Alex') }}
    '''
    template=Template(html)
    render=template.render()
    print(render)
#main24()

def main25():
    players=[
        {'name':'Sautenko','city':'Kramatorsk','height':192},
        {'name': 'Tereshyk', 'city': 'Dnepr', 'height': 202},
        {'name': 'Kostrub', 'city': 'Slavyansk', 'height': 172},
        {'name': 'Veselov', 'city': 'Kramatorsk', 'height': 189}
    ]
    html="""
    {% macro list_players(some_list) -%}
    <ul>
    {% for player in some_list -%}
        <li>{{player.name}} {{caller(player)}}
    {% endfor %}
    </ul>
    {% endmacro %}
    {% call(player) list_players(players) -%}
        <ul>
        <li> city: {{player.city}}
        <li> height: {{player.height}}
        </ul>
    {% endcall -%}
    """

    template=Template(html)
    render=template.render(players=players)
    print(render)

#main25()

def main26():
    cars=[
        {'model':'nissan','color':'orange','year':1997},
        {'model': 'dewoo', 'color': 'grey', 'year': 2005},
        {'model': 'renault', 'color': 'black', 'year': 2017}
    ]

    html='''
    {% macro list_car(some_list) -%}
    <ul>
    {% for car in some_list -%}
        <li>{{car.model}} {{caller(car)}}
    {% endfor %}
    <ul>
    {% endmacro %}
    {% call(car) list_car(cars) -%}
        <ul>
        <li>color: {{car.color}}
        <li>year: {{car.year}}
        </ul>
    {% endcall %}
    
    '''
    template=Template(html)
    render=template.render(cars=cars)
    print(render)

#main26()

def main27():
    subjects=[
        {'name':'math','lessons':20},
        {'name': 'phisics', 'lessons': 15},
        {'name': 'alchemy', 'lessons': 12},
    ]

    html="""
    {% macro sciens_list(some_list) -%}
    <ul>
    {% for sub in some_list -%}
        <li>{{sub.name}} {{caller(sub)}}
    {% endfor %}
    <ul>
    {% endmacro -%}
    {% call(sub) sciens_list(subjects) %}
        <ul>
        <li>lessons amount : {{sub.lessons}}
        </ul>
    {% endcall %}
    """

    template=Template(html)
    render=template.render(subjects=subjects)
    print(render)
#main27()

def main28():
    players=[
        {'name':'Саутенко','old':32,'height':192},
        {'name': 'Терещук', 'old': 33, 'height': 202},
        {'name': 'Чаусов', 'old': 34, 'height': 197},
        {'name': 'Макогон', 'old': 31, 'height': 190},
        {'name': 'Дыкань', 'old': 34, 'height': 192},
    ]
    file_loader=FileSystemLoader('templates')
    env=Environment(loader=file_loader)

    template=env.get_template('main.htm')
    render=template.render(users=players)
    print(render)

#main28()

def main29():
    teams=[
        {'name':'Donbass','runk':99},
        {'name': 'NKMZ', 'runk': 42},
        {'name': 'Swandor', 'runk': 54},
    ]

    file_loader=FileSystemLoader('templates')
    env=Environment(loader=file_loader)

    template=env.get_template('main2.htm')
    render=template.render(some_dict=teams)
    print(render)

#main29()

def main30():
    teams = [
        {'name': 'Donbass', 'runk': 99},
        {'name': 'NKMZ', 'runk': 42},
        {'name': 'Swandor', 'runk': 54},
    ]
    def loading(path):
        if path=='index':
            return """Имя {{every_name.name}},рейтинг {{every_name.runk}}"""
        else:
            return "указан неверный путь"

    file_loader=FunctionLoader(loading)
    env = Environment(loader=file_loader)

    template = env.get_template('index')
    render = template.render(every_name=teams[0])
    print(render)

#main30()

def main31():
    persons=[
        {'name':'Андрей','old':32,'weight':75},
        {'name': 'Александр', 'old': 33, 'weight': 90},
        {'name': 'Данил', 'old': 31, 'weight': 85},
    ]

    file_loader=FileSystemLoader('templates')
    env=Environment(loader=file_loader)

    template=env.get_template('page.htm')
    render=template.render(domain='http://proproprogs.ru',title='Про Jinja')

    print(render)
#main31()

def main32():
    teams=[
        {'name':'Arsenal','manager':'Mikel Arteta','position':4},
        {'name': 'Man City', 'manager': 'Pep Guardiola', 'position': 1},
        {'name': 'Liverpool', 'manager': 'Jurgen Klopp', 'position': 2},
    ]

    file_loader=FileSystemLoader('templates')
    env=Environment(loader=file_loader)
    my_template=env.get_template('football_page.htm')
    my_render=my_template.render(my_domain='http://football.ua',my_title='Про футбол!')

    print(my_render)
#main32()

def main33():
    subjects=[
        {'subject':'math','month':3},
        {'subject': 'chemical', 'month': 5},
        {'subject': 'phylosophy', 'month': 1},
    ]

    file_loader=FileSystemLoader('templates')
    env=Environment(loader=file_loader)
    my_template=env.get_template('smart_page.htm')
    my_render=my_template.render(smart_domain='http://smartprices.com',smart_title='Всео кроссовках!')

    print(my_render)

#main33()

def main34():
    friends=[
        {'name':'Жарчинский Серега','phone':380951234568},
        {'name': 'Чаусов Саша', 'phone': 380954562168},
        {'name': 'Терещук Саня', 'phone': 380951456568},
        {'name': 'Жила Радик', 'phone': 380934578568},
        {'name': 'Макогон Данил', 'phone': 380667894512}
    ]

    file_loader=FileSystemLoader('templates')
    env=Environment(loader=file_loader)

    my_template=env.get_template('friends_page.htm')
    my_render=my_template.render(domain_adress='http://bestfriends.com',site_title='Телефоны моих друзей.',
                                 text_end='THE END',some_list=friends)

    print(my_render)

#main34()

def main35():

    list_table=[1,2,3,4,5,6,7]

    file_loader=FileSystemLoader('templates')
    env=Environment(loader=file_loader)

    my_template=env.get_template('about.htm')
    my_render=my_template.render(list_table=list_table)

    print(my_render)
#main35()

def main36():
    file_loader=FileSystemLoader('templates')
    env=Environment(loader=file_loader)

    my_template=env.get_template('about_shoes.htm')
    my_render=my_template.render()

    print(my_render)
#main36()

def main37():
    file_loader=FileSystemLoader('templates')
    env=Environment(loader=file_loader)

    my_template=env.get_template('site_page.htm')
    my_render=my_template.render()

    print(my_render)
#main37()

def main38():

    teams=['Donbass','DGMA','NKMZ']

    file_loader=FileSystemLoader('templates')
    env=Environment(loader=file_loader)

    my_template=env.get_template('about_volley.htm')
    my_render=my_template.render(some_list=teams)
    print(my_render)

main38()