import os, threading, time, uuid, random, json, ctypes, string, sys, string

try:
    import requests
    import colorama
    import tls_client 
    import pystyle
    import datetime
except ModuleNotFoundError:
    os.system('pip install requests')
    os.system('pip install colorama')
    os.system('pip install tls_client')
    os.system('pip install pystyle')
    os.system('pip install datetime')

from colorama import *
from pystyle import *

red = Fore.RED
blue = Fore.BLUE
cyan = Fore.CYAN
yellow = Fore.YELLOW
lightcyan = Fore.LIGHTMAGENTA_EX + Fore.LIGHTCYAN_EX
magenta = Fore.MAGENTA
orange = Fore.RED + Fore.YELLOW
green = Fore.GREEN
white = Fore.WHITE
gray = Fore.LIGHTBLACK_EX + Fore.WHITE
pink = Fore.LIGHTGREEN_EX + Fore.LIGHTMAGENTA_EX
reset = Fore.RESET

total = 0
generated = 0
failed = 0
joined = 0
checked = 0
messages = 0
status_num = 0
presence = 0
ctypes.windll.kernel32.SetConsoleTitleW("『 Guilded Hub 』 By ~Z3R003~")

def get_time():
    date = datetime.datetime.now()
    current_time = date.strftime('%H:%M:%S')
    return current_time

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def fake_account_generator_title():
    global total, generated, failed, joined, checked
    ctypes.windll.kernel32.SetConsoleTitleW(f"『 Guilded Hub 』 By ~Z3R003~ | Fake Account Generator | Created : {generated} ~ Joined : {joined}")
def real_account_generator_title():
    global total, generated, failed, joined, checked
    ctypes.windll.kernel32.SetConsoleTitleW(f"『 Guilded Hub 』 By ~Z3R003~ | Real Account Generator | Created : {generated} ~ Joined : {joined}")
def account_joiner_title():
    global total, generated, failed, joined, checked
    ctypes.windll.kernel32.SetConsoleTitleW(f"『 Guilded Hub 』 By ~Z3R003~ | Account Joiner | Joined : {joined}")
def account_checker_title():
    global total, generated, failed, joined, checked
    ctypes.windll.kernel32.SetConsoleTitleW(f"『 Guilded Hub 』 By ~Z3R003~ | Account Checker | Checked : {checked}")
def chat_spammer_title():
    global total, generated, failed, joined, checked, messages
    ctypes.windll.kernel32.SetConsoleTitleW(f"『 Guilded Hub 』 By ~Z3R003~ | Chat Spammer | Messages Sent : {messages}")
def account_status_presence_title():
    global total, generated, failed, joined, checked, messages,status_num,presence
    ctypes.windll.kernel32.SetConsoleTitleW(f"『 Guilded Hub 』 By ~Z3R003~ | Account-Status-Presence | Status : {status_num} ~ Online : {presence}")

def email_gen():
    email = ''.join(random.choices(string.ascii_letters + string.digits, k =10))
    return email

def username_gen():
    with open('config.json','r')as d:
        data = json.load(d)
        username = data["username"]
    if username == '' or username == ' ':
        username = 'DaboorOnTop'
        return username
    else:
        return username

def password_gen():
    with open('config.json','r')as d:
        data = json.load(d)
        password = data["password"]
    if password == '' or password == ' ':
        password = 'DaboorOnTop'
        return password
    else:
        return password

def load_proxies():
    with open('proxies.txt','r')as p:
        proxies = p.read().splitlines()
    return proxies

def fake_account_generator():
    global total, generated, failed, joined
    with open('config.json','r')as d:
        data = json.load(d)
        invite = data['invite']
        referrerId = data['referrerId']
    output_lock = threading.Lock()
    proxies = load_proxies()
    proxy = random.choice(proxies)
    username = username_gen()
    email = email_gen() + '@DaboorOnTop.com'
    password = password_gen()
    session = tls_client.Session(
        client_identifier="chrome_113",
        random_tls_extension_order=True
    )
    session.proxies = {
        'http':f'http://{proxy}',
        'https':f'https://{proxy}'
    }
    payload = {
        'extraInfo': {
            'platform': 'desktop',
            'referrerId':referrerId
        },
        'name': username,
        'email': email,
        'password': password,
        'fullName': username,
    }
    while True:
        try:
            gen = session.post('https://www.guilded.gg/api/users?type=email?r=4P1YwWnd',json=payload)
            break
        except:
            continue    
    if gen.status_code == 200:
        with output_lock:
            generated += 1
            total += 1
            time_rn = get_time()
            print(f"{reset}[ {cyan}{time_rn}{reset} ] {gray}({green}+{gray}) {lightcyan}Account Created {gray} | ", end="")
            sys.stdout.flush()
            Write.Print(f"{email} : {password} (#{generated})\n", Colors.yellow_to_red, interval=0.000)
            open('fake-accounts.txt', 'a').write(f'{email}:{password}\n') 
            fake_account_generator_title()
        session.headers['content-length'] = "19"
        join = session.put(f'https://www.guilded.gg/api/invites/{invite}', data=json.dumps({"type":"consume"}))  
        if join.status_code == 200:
            with output_lock:
                time_rn = get_time()
                print(f"{reset}[ {cyan}{time_rn}{reset} ] {gray}({yellow}~{gray}) {blue}Account Joined {gray} | ", end="")
                sys.stdout.flush()
                Write.Print(f"{email} : {password}\n", Colors.yellow_to_red, interval=0.000)
                joined += 1
                fake_account_generator_title()
        else:
            with output_lock:
                time_rn = get_time()
                print(f"{reset}[ {cyan}{time_rn}{reset} ] {gray}({red}-{gray}) {blue}Account Couldn't Join {gray} | ", end="")
                sys.stdout.flush()
                Write.Print(f"{email} : {password}\n", Colors.yellow_to_red, interval=0.000)
                fake_account_generator_title()
    elif gen.status_code == 400:
        time_rn = get_time()
        print(f"{reset}[ {cyan}{time_rn}{reset} ] {gray}({red}-{gray})Password is to short! ({red}must be at least 8{reset})")
    else:
        pass

def real_account_generator():
    global total, generated, failed, joined
    with open('config.json','r')as d:
        data = json.load(d)
        invite = data['invite']
        referrerId = data['referrerId']
    output_lock = threading.Lock()
    proxies = load_proxies()
    proxy = random.choice(proxies)
    usernames = ['Skyler','MRRobot','aboogiewithahoodie','Gustavo', 'Johan', 'Estella', 'Rabetta', 'Jason', 'Peter', 'Raiden', 'Mia', 'Evelyn', 'Harper', 'Luna', 'Camila', 'Gianna', 'Elizabeth', 'Eleanor', 'Ella', 'Abigail', 'Sofia', 'Avery', 'Scarlett', 'Emily', 'Aria', 'Penelope', 'Chloe', 'Layla', 'Mila', 'Nora', 'Hazel', 'Madison', 'Ellie', 'Lily', 'Nova', 'Isla', 'Grace', 'Violet', 'Aurora', 'Riley', 'Zoey', 'Willow', 'Emilia', 'Stella', 'Zoe', 'Victoria', 'Hannah', 'Addison', 'Leah', 'Lucy', 'Eliana', 'Ivy', 'Everly', 'Lillian', 'Paisley', 'Elena', 'Naomi', 'Maya', 'Natalie', 'Kinsley', 'Delilah', 'Claire', 'Audrey', 'Aaliyah', 'Ruby', 'Brooklyn', 'Alice', 'Aubrey', 'Autumn', 'Leilani', 'Savannah', 'Valentina', 'Kennedy', 'Madelyn', 'Josephine', 'Bella', 'Skylar', 'Genesis', 'Sophie', 'Hailey', 'Sadie', 'Natalia', 'Quinn', 'Caroline', 'Allison', 'Gabriella', 'Anna', 'Serenity', 'Nevaeh', 'Cora', 'Ariana', 'Emery', 'Lydia', 'Jade', 'Sarah', 'Eva', 'Adeline', 'Madeline', 'Piper', 'Rylee', 'Athena', 'Peyton', 'Everleigh', 'Liam', 'Noah', 'Oliver', 'Elijah', 'James', 'William', 'Benjamin', 'Lucas', 'Henry', 'Theodore', 'Jack', 'Levi', 'Alexander', 'Jackson', 'Mateo', 'Daniel', 'Michael', 'Mason', 'Sebastian', 'Ethan', 'Logan', 'Owen', 'Samuel', 'Jacob', 'Asher', 'Aiden', 'John', 'Joseph', 'Wyatt', 'David', 'Leo', 'Luke', 'Julian', 'Hudson', 'Grayson', 'Matthew', 'Ezra', 'Gabriel', 'Carter', 'Isaac', 'Jayden', 'Luca', 'Anthony', 'Dylan', 'Lincoln', 'Thomas', 'Maverick', 'Elias', 'Josiah', 'Charles', 'Caleb', 'Christopher', 'Ezekiel', 'Miles', 'Jaxon', 'Isaiah', 'Andrew', 'Joshua', 'Nathan', 'Nolan', 'Adrian', 'Cameron', 'Santiago', 'Eli', 'Aaron', 'Ryan', 'Angel', 'Cooper', 'Waylon', 'Easton', 'Kai', 'Christian', 'Landon', 'Colton', 'Roman', 'Axel', 'Brooks', 'Jonathan', 'Robert', 'Jameson', 'Ian', 'Everett', 'Greyson', 'Wesley', 'Jeremiah', 'Hunter', 'Leonardo', 'Jordan', 'Jose', 'Bennett', 'Silas', 'Nicholas', 'Parker', 'Beau', 'Weston', 'Austin', 'Connor', 'Carson', 'Dominic', 'Xavier', 'Kai', 'Zion', 'Jayden', 'Eliana', 'Luca', 'Ezra', 'Maeve', 'Aaliyah', 'Mia', 'Nova', 'Aurora', 'Amara', 'Kayden', 'Ivy', 'Alina', 'Mila', 'Quinn', 'Rowan', 'Elliot', 'Finn', 'Lilibet', 'River', 'Xavier', 'Rachel', 'Amaya', 'Remi', 'Axel', 'Zoey', 'Malachi', 'Alex', 'Blake', 'Lyla', 'Alice', 'Isla', 'Rebecca', 'Rohan', 'Milo', 'Elias', 'Ari', 'Aria', 'Molly', 'Jude', 'Isabella', 'Arthur', 'Millie', 'Andrea', 'Marcus', 'Atlas', 'Ariella', 'Kyle', 'Evan', 'Ira', 'Hayden', 'Bailey', 'Gianna', 'Valerie', 'Brianna', 'Jesse', 'Cecilia', 'Leo', 'Leilani', 'Dante', 'Zoe', 'Khadijah', 'Mya', 'Sharon', 'Sean', 'Brielle', 'Ayla', 'Shia', 'Riley', 'Raya', 'Sloane', 'Alana', 'Charlie', 'Kian', 'Hudson', 'Elise', 'Akira', 'Mika', 'Freya', 'Nia', 'Natasha', 'Myra', 'Mateo', 'Everett', 'Rae', 'Savannah', 'Thea', 'Finley', 'Alaina', 'Mina', 'Yara', 'Emerson', 'Camille', 'Ivan', 'Skyler', 'Skylar', 'Alma', 'Reese', 'Sasha', 'Asa', 'Sage', 'Camila', 'Amira', 'Kieran', 'Monica', 'Everly', 'Evie', 'Maverick', 'Kyra', 'Ian', 'Julia', 'Vivian', 'Theo', 'Ophelia', 'Chelsea', 'Azariah', 'Jade', 'Lara', 'Ava', 'Morgan', 'Lennox', 'Luna', 'Isabelle', 'Amir', 'Rhys', 'Arlo', 'Giovanni', 'Aisha', 'Orion', 'Ahmed', 'Nolan', 'Ezekiel', 'Michelle', 'Lea', 'Silas', 'Elaine', 'Adira', 'Callan', 'Lilith', 'Justin', 'Simon', 'Rhea', 'Marie', 'Lisa', 'Damien', 'Ximena', 'Lilah', 'Elora', 'Sienna', 'Fiona', 'Urban', 'Jean', 'Eden', 'Kayla', 'Avi', 'Octavia', 'Skye', 'Nancy', 'Otis', 'Lila', 'Anya', 'Elena', 'Zayne', 'Gigi', 'Alyssa', 'Amelia', 'Giselle', 'Francis', 'Jacqueline', 'Aiden', 'Kylie', 'Wren', 'Maria', 'Mae', 'Colette', 'Louise', 'Aliyah', 'Chase', 'Tara', 'Lorenzo', 'Sydney', 'Callie', 'Niko', 'Avery', 'Gemma', 'Rafael', 'Hailey', 'Harlow', 'Adeline', 'Margot', 'Rory', 'Nyla', 'Helena', 'Colin', 'Xander', 'Rylee', 'Irene', 'Ashton', 'Marley', 'Arden', 'Kaira', 'Arianna', 'Pia', 'Nola', 'Miles', 'Brooks', 'Annalise', 'Imani', 'Josie', 'Ellis', 'Cali', 'Hadassah', 'Phoenix', 'Piper', 'Emery', 'Aliza', 'Mackenzie', 'Timothy', 'Adrian', 'Sawyer', 'Harvey', 'Enoch', 'Lachlan', 'Kaiden', 'Zuri', 'Shelby', 'Liam', 'Olivia', 'Aubrey', 'Sanjana', 'Rayne', 'Stella', 'Cleo', 'Gracie', 'Oakley', 'Madeline', 'Melissa', 'Lauren', 'Mona', 'Alicia', 'Jasmine', 'Scott', 'Abel', 'Elliott', 'Wesley', 'Aditya', 'Alan', 'Brooke', 'Sunny', 'Sana', 'Blair', 'Leon', 'Emmanuel', 'Lilian', 'Priya', 'Malia', 'Elodie', 'Adriel', 'Amos', 'Trisha', 'Naomi', 'Damian', 'Nevaeh', 'Judah', 'Sloan', 'Joel', 'Nicholas', 'Azriel', 'Lyra', 'Lee', 'Kevin', 'Remy', 'Omar', 'Amelie', 'Caleb', 'Aleena', 'Killian', 'Theodore', 'Asher', 'Mariam', 'Claudia', 'Noelle', 'Juliana', 'Makayla', 'Beau', 'Nikita', 'Beckett', 'Nadia', 'Ana', 'Zane', 'Jayce', 'Brayden', 'Elia', 'Leia', 'Cooper', 'Zain', 'Ronan', 'Liana', 'Kali', 'Serena', 'Davina', 'Zaid', 'Dillon', 'Sylvia', 'Rhiannon', 'Ryder', 'Zara', 'Amina', 'Keanu', 'Amaris', 'Eloise', 'Mara', 'Vera', 'Sonny', 'Keira', 'Ali', 'Sierra', 'Harper', 'Katherine', 'Siobhan', 'Ada', 'Gia', 'Heather', 'Kalani', 'Penny', 'Camilla', 'Cole', 'Amani', 'Emmet', 'Leila', 'Ethan', 'Alani', 'Fallon', 'Joyce', 'Joan', 'Winifred', 'Amyra', 'Mira', 'Quincy', 'Kimberly', 'Faye', 'Colton', 'Cayden', 'Maira', 'Ayana', 'Shiloh', 'Darren', 'Evelyn', 'Lorelei', 'Iva', 'Felix', 'Tessa', 'Jalen', 'Rylan', 'Nellie', 'Masha', 'Amora', 'Alvin', 'Leighton', 'Keziah', 'Mikayla', 'Harley', 'Oliver', 'Huxley', 'Martin', 'Noa', 'Rocco', 'Shane', 'Ines', 'Rai', 'Harry', 'Lily', 'Stanley', 'Darcy', 'Bryce', 'Devin', 'Lucas', 'Jamie', 'Teddy', 'Martha', 'Albert', 'Travis', 'Lucian', 'Emelia', 'Delilah', 'Norah', 'Azalea', 'Valentina', 'Hallie', 'Nora', 'Kara', 'Misha', 'Ishmael', 'Mimi', 'Pamela', 'Genevieve', 'Thalia', 'Collin', 'Grayson', 'June', 'May', 'Kenji', 'Chiara', 'Ravi', 'Rosie', 'Seraphina', 'Juno', 'Sophie', 'Simone', 'Gavin', 'Alayna', 'Miriam', 'Patricia', 'Christine', 'Joaquin', 'Dior', 'Israel', 'Teagan', 'Jocelyn', 'Zaira', 'Tiffany', 'Cedric', 'Reyna', 'Winston', 'Maximus', 'Dennis', 'George', 'Braxton', 'Deborah', 'Lorraine', 'Romy', 'Dakota', 'Reuben', 'Hayley', 'Anisha', 'Saira', 'Veda', 'Tiana', 'Kyler', 'Preston', 'Olive', 'Ellie', 'Rio', 'Yvonne', 'Parker', 'Yana', 'Maia', 'Levi', 'Tyson', 'Graham', 'Cain', 'Kelvin', 'Lynn', 'Lia', 'Kaden', 'Rian', 'Aurelia', 'Spencer', 'Usnavi', 'Elina', 'Ellen', 'Kaya', 'Tamara', 'Mabel', 'Remington', 'Ember', 'Sadie', 'Sahil', 'Azrael', 'Kendall', 'Raine', 'Noah', 'Athena', 'Declan', 'Leigh', 'Helen', 'Rey', 'Janet', 'Ace', 'Alena', 'Lola', 'Karina', 'Grace', 'Jedidiah', 'Alaia', 'Aman','supergamer123','Brian', 'Milan', 'Malcolm', 'Javier', 'Emma', 'Marion', 'Adaline', 'Daisy', 'Amal', 'Holly', 'Cillian', 'Kayleigh']
    username = random.choice(usernames)
    email = email_gen() + "@gmail.com"
    password = password_gen()
    pfps = ['https://s3-us-west-2.amazonaws.com/www.guilded.gg/UserAvatar/259852aa1c98ce1fc6a1383b083e3693-Large.png?w=450&h=450','https://s3-us-west-2.amazonaws.com/www.guilded.gg/UserAvatar/6996a0b1d225187292038c91f150d761-Large.png?w=450&h=450','https://s3-us-west-2.amazonaws.com/www.guilded.gg/UserAvatar/8a482a4bab527e91166d2e6442d23116-Large.png?w=450&h=450','https://s3-us-west-2.amazonaws.com/www.guilded.gg/UserAvatar/1f042a37b1ab82b64862ad462b706b9d-Large.png?w=450&h=450','https://s3-us-west-2.amazonaws.com/www.guilded.gg/UserAvatar/7f9a6612447dd3a507dd30a7df43ffe4-Large.png?w=450&h=450','https://s3-us-west-2.amazonaws.com/www.guilded.gg/UserAvatar/a56e3999fd40939180283376fac54bf0-Large.png?w=450&h=450',"https://s3-us-west-2.amazonaws.com/www.guilded.gg/UserAvatar/58aee327c2ca21f8c5f4a4b5921e31e0-Large.png?w=450&h=450","https://s3-us-west-2.amazonaws.com/www.guilded.gg/UserAvatar/ecf05e95b88477f55839c727729c8183-Large.png?w=450&h=450","https://s3-us-west-2.amazonaws.com/www.guilded.gg/UserAvatar/d43df573c241ce8ae59997b22a60bb7c-Large.png?w=450&h=450","https://s3-us-west-2.amazonaws.com/www.guilded.gg/UserAvatar/e5cddc84cc2268e14af76d631133dbbf-Large.png?w=450&h=450","https://s3-us-west-2.amazonaws.com/www.guilded.gg/UserAvatar/23665a3745a73bfa326a9e99bf8786b8-Large.png?w=450&h=450","https://s3-us-west-2.amazonaws.com/www.guilded.gg/UserAvatar/fb49f62cdf00bd2f68d6cee546e47e90-Large.png?w=450&h=450","https://s3-us-west-2.amazonaws.com/www.guilded.gg/UserAvatar/21be8356a8733a9425f92d7f2d80a448-Large.png?w=450&h=450","https://s3-us-west-2.amazonaws.com/www.guilded.gg/UserAvatar/946bcb354282023de894aeca7d525caa-Large.png?w=450&h=450","https://s3-us-west-2.amazonaws.com/www.guilded.gg/UserAvatar/9c153e4096c2ad3c4ed48959605ad864-Large.png?w=450&h=450","https://s3-us-west-2.amazonaws.com/www.guilded.gg/UserAvatar/450988ecc35ef4094361ce7c581c06bd-Large.png?w=450&h=450","https://s3-us-west-2.amazonaws.com/www.guilded.gg/UserAvatar/6113e8cdace67860056bfd7986d3f59e-Large.png?w=450&h=450","https://s3-us-west-2.amazonaws.com/www.guilded.gg/UserAvatar/2d4f1592f61939ebffcbb30f45eb77d2-Large.png?w=450&h=450","https://s3-us-west-2.amazonaws.com/www.guilded.gg/UserAvatar/11196407e7feb0cbba7d63fd58f4adce-Large.png?w=450&h=450","https://s3-us-west-2.amazonaws.com/www.guilded.gg/UserAvatar/dcd973c00082bdb51c251674386cb0eb-Large.png?w=450&h=450","https://s3-us-west-2.amazonaws.com/www.guilded.gg/UserAvatar/556825aa6ada25f2e8639a62c53ca614-Large.png?w=450&h=450","https://s3-us-west-2.amazonaws.com/www.guilded.gg/UserAvatar/5440779c6005ea8676eee526ea4fd8ee-Large.png?w=450&h=450","https://s3-us-west-2.amazonaws.com/www.guilded.gg/UserAvatar/ace194b55cffee8b23ae7a6bce140a68-Large.png?w=450&h=450","https://s3-us-west-2.amazonaws.com/www.guilded.gg/UserAvatar/d45a62a07f45caaebc3e3181e8b62155-Large.png?w=450&h=450","https://s3-us-west-2.amazonaws.com/www.guilded.gg/UserAvatar/fb3ef5cec6c8d2180559c11557782c31-Large.png?w=450&h=450","https://s3-us-west-2.amazonaws.com/www.guilded.gg/UserAvatar/af0d8e01ccd10743e89c8d0a61970288-Large.png?w=450&h=450","https://s3-us-west-2.amazonaws.com/www.guilded.gg/UserAvatar/85ceacd4e28eeabc7b340124ecc881fa-Large.png?w=450&h=450","https://s3-us-west-2.amazonaws.com/www.guilded.gg/UserAvatar/9a2c5a87f383d96db737409371c04516-Large.png?w=450&h=450", "https://s3-us-west-2.amazonaws.com/www.guilded.gg/UserAvatar/0f830d9ef4f2e86b6abd3581f83b2896-Large.png?w=450&h=450", "https://s3-us-west-2.amazonaws.com/www.guilded.gg/UserAvatar/da78986c55dac92db9af7d5c261318e7-Large.png?w=450&h=450", "https://s3-us-west-2.amazonaws.com/www.guilded.gg/UserAvatar/876cf31909f3357800ca073d2d8eed7e-Large.png?w=450&h=450", "https://s3-us-west-2.amazonaws.com/www.guilded.gg/UserAvatar/e5540d8990f5adc219d18a6d00acf853-Large.png?w=450&h=450", "https://s3-us-west-2.amazonaws.com/www.guilded.gg/UserAvatar/1c1634a889621ffbb110354fd1b06146-Large.png?w=450&h=450", "https://s3-us-west-2.amazonaws.com/www.guilded.gg/UserAvatar/9219e8c06e6aa3f5b9aa559ee980c34b-Large.png?w=450&h=450", "https://s3-us-west-2.amazonaws.com/www.guilded.gg/UserAvatar/d115a13cb8e4ab386cdf952b8b760a0f-Large.png?w=450&h=450", "https://s3-us-west-2.amazonaws.com/www.guilded.gg/UserAvatar/f1bd627df77d76c4d58750f3dd3bd9be-Large.png?w=450&h=450", "https://s3-us-west-2.amazonaws.com/www.guilded.gg/UserAvatar/be6b410d3ffba7db071790cad51eb154-Large.png?w=450&h=450", "https://s3-us-west-2.amazonaws.com/www.guilded.gg/UserAvatar/761b00db4cf5f23d116a5802028d107d-Large.png?w=450&h=450", "https://s3-us-west-2.amazonaws.com/www.guilded.gg/UserAvatar/aacdc99312d0f509310444605f8a619c-Large.png?w=450&h=450", "https://s3-us-west-2.amazonaws.com/www.guilded.gg/UserAvatar/843909f278f6e8fcf695cd12165ca49d-Large.png?w=450&h=450", "https://s3-us-west-2.amazonaws.com/www.guilded.gg/UserAvatar/fd0090ee3144389adb3d5cec81189238-Large.png?w=450&h=450", "https://s3-us-west-2.amazonaws.com/www.guilded.gg/UserAvatar/49bfeb53e1725992e89d0395a4646c2f-Large.png?w=450&h=450", "https://s3-us-west-2.amazonaws.com/www.guilded.gg/UserAvatar/f8cb096b793e4ae1bfc6ec53f56c9746-Large.png?w=450&h=450", "https://s3-us-west-2.amazonaws.com/www.guilded.gg/UserAvatar/2f26bf8f0f17fe3cd1c5984e11dd973d-Large.png?w=450&h=450", "https://s3-us-west-2.amazonaws.com/www.guilded.gg/UserAvatar/ffb5c69831c38675f37f6d10369b0367-Large.png?w=450&h=450", "https://s3-us-west-2.amazonaws.com/www.guilded.gg/UserAvatar/b47ad03af65d36789491737b8bf60915-Large.png?w=450&h=450", "https://s3-us-west-2.amazonaws.com/www.guilded.gg/UserAvatar/ee8d30c9a586ffc9372f4f09f24a85c4-Large.png?w=450&h=450", "https://s3-us-west-2.amazonaws.com/www.guilded.gg/UserAvatar/0a9009748611fd6bb09e2e796b2ffdfe-Large.png?w=450&h=450"]
    pfp = random.choice(pfps)
    bios = ["github.com/Daboor08", "Hacked Nasa with html", "I got hacked by Daboor","Daboor hacked me"]
    bio = random.choice(bios)
    session = tls_client.Session(
        client_identifier="chrome_113",
        random_tls_extension_order=True
    )
    session.proxies = {
        'http':f'http://{proxy}',
        'https':f'https://{proxy}'
    }
    payload = {
        'extraInfo': {
            'platform': 'desktop',
            'referrerId':referrerId
        },
        'name': username,
        'email': email,
        'password': password,
        'fullName': username,
    }
    try:
        gen = session.post('https://www.guilded.gg/api/users?type=email',json=payload)
        if gen.status_code == 200:
            userid = gen.json()['user']["id"]
            with output_lock:
                generated += 1
                total += 1
                time_rn = get_time()
                print(f"{reset}[ {cyan}{time_rn}{reset} ] {gray}({green}+{gray}) {lightcyan}Account Created {gray} | ", end="")
                sys.stdout.flush()
                Write.Print(f"{email} : {password}\n", Colors.yellow_to_red, interval=0.000)
                open('real-accounts.txt', 'a').write(f'{email}:{password}\n')
                real_account_generator_title()
            while True:
                try:
                    join = session.put(f'https://www.guilded.gg/api/invites/{invite}', data=json.dumps({"type":"consume"})) 
                    break
                except:
                    continue
            if join.status_code == 200:
                with output_lock:
                    joined += 1
                    time_rn = get_time()
                    print(f"{reset}[ {cyan}{time_rn}{reset} ] {gray}({yellow}~{gray}) {blue}Account Joined {gray} | ", end="")
                    sys.stdout.flush()
                    Write.Print(f"{email} : {password}\n", Colors.yellow_to_red, interval=0.000)
                    real_account_generator_title()
            send_pfp = session.post(f'https://www.guilded.gg/api/users/me/profile/images', data=json.dumps({"imageUrl": pfp}))
            if send_pfp.status_code == 200:
                taglines = ["github.com/Z3R003", "Z3R003 On Top", "I got hacked by Z3R003","Z3R003 hacked me"]
                tagline = random.choice(taglines)
                payload2 = {
                    "userId": userid,
                    "aboutInfo": {
                        "bio": bio,
                        "tagLine": tagline
                    }
                }
                send_profile = session.put(f'https://www.guilded.gg/api/users/{userid}/profilev2', json=payload2)
                if send_profile.status_code == 200:
                    with output_lock:
                        time_rn = get_time()
                        print(f"{reset}[ {cyan}{time_rn}{reset} ] {gray}({yellow}*{gray}) {pink}Humanized [Bio, Tagline, PFP] {gray}| ", end='')
                        sys.stdout.flush()
                        Write.Print(f"{email} : {password}\n", Colors.yellow_to_red, interval=0.000)   
    except:
        pass       

def account_joiner(email,password):
    global total, generated, failed, joined, checked
    output_lock = threading.Lock()
    with open('config.json','r')as d:
        data = json.load(d)
        invite = data['invite']
    proxies = load_proxies()
    proxy = random.choice(proxies)
    session = tls_client.Session(
        client_identifier="chrome_113",
        random_tls_extension_order=True
    )
    session.proxies = {
        'http':f'http://{proxy}',
        'https':f'https://{proxy}'
    }
    payload = {
        "email": email,
        "getMe": True,
        "password": password
    }
    while True:
        try:
            login = session.post('https://www.guilded.gg/api/login', json=payload)
            break
        except Exception as e : 
            continue
    if login.status_code == 200:
        join = session.put(f'https://www.guilded.gg/api/invites/{invite}', data=json.dumps({"type":"consume"}))  
        if join.status_code == 200:
            with output_lock:
                joined += 1
                time_rn = get_time()
                print(f"{reset}[ {cyan}{time_rn}{reset} ] {gray}({green}+{gray}) {blue} Account Joined {gray} | ", end="")
                sys.stdout.flush()
                Write.Print(f"{email} : {password}\n", Colors.yellow_to_red, interval=0.000)
                account_joiner_title()
        else:
            with output_lock:
                time_rn = get_time()
                print(f"{reset}[ {cyan}{time_rn}{reset} ] {gray}({red}-{gray}) {blue} Account Couldn't Join {gray} | ", end="")
                sys.stdout.flush()
                Write.Print(f"{email} : {password}\n", Colors.yellow_to_red, interval=0.000)
                account_joiner_title()
    else:
        with output_lock:
            time_rn = get_time()
            print(f"{reset}[ {cyan}{time_rn}{reset} ] {gray}({red}-{gray}) {magenta} Invalid Account  {gray} | ", end="")
            sys.stdout.flush()
            Write.Print(f"{email} : {password}\n", Colors.yellow_to_red, interval=0.000)
            account_joiner_title()            

def account_checker(email,password):
    global total, generated, failed, joined, checked
    output_lock = threading.Lock()
    proxies = load_proxies()
    proxy = random.choice(proxies)
    session = tls_client.Session(
        client_identifier="chrome_113",
        random_tls_extension_order=True
    )
    session.proxies = {
        'http':f'http://{proxy}',
        'https':f'https://{proxy}'
    }
    payload = {
        "email": email,
        "getMe": True,
        "password": password
    }
    while True:
        try:
            check = session.post('https://www.guilded.gg/api/login', json=payload)
            break
        except:
            continue
    if check.status_code == 200:
        with output_lock:
            checked += 1
            time_rn = get_time()
            print(f"{reset}[ {cyan}{time_rn}{reset} ] {gray}({green}+{gray}) {green} Valid Account {gray} | ", end="")
            sys.stdout.flush()
            Write.Print(f"{email} : {password}\n", Colors.yellow_to_red, interval=0.000)
            account_checker_title()
            open('working-accounts.txt', 'a').write(f'{email} : {password}\n')
    else:
        with output_lock:
            checked += 1
            time_rn = get_time()
            print(f"{reset}[ {cyan}{time_rn}{reset} ] {gray}({red}-{gray}) {magenta} Invalid Account {gray} | ", end="")
            sys.stdout.flush()
            Write.Print(f"{email} : {password}\n", Colors.yellow_to_red, interval=0.000)
            account_checker_title()

def chat_spammer(email,password,message,channel_id):
    global total, generated, failed, joined, checked, messages
    output_lock = threading.Lock()
    proxies = load_proxies()
    proxy = random.choice(proxies)
    session = tls_client.Session(
        client_identifier="chrome_113",
        random_tls_extension_order=True
    )
    session.proxies = {
        'http':f'http://{proxy}',
        'https':f'https://{proxy}'
    }
    login_payload = {
        "email": email,
        "getMe": True,
        "password": password
    }
    message_payload = {
        'messageId': str(uuid.uuid4()),
        'content': {
            'object': 'value',
            'document': {
                'object': 'document',
                'data': {},
                'nodes': [
                    {
                        'object': 'block',
                        'type': 'paragraph',
                        'data': {},
                        'nodes': [
                            {
                                'object': 'text',
                                'leaves': [
                                    {
                                        'object': 'leaf',
                                        'text': message,
                                        'marks': [],
                                    },
                                ],
                            },
                        ],
                    },
                ],
            },
        },
        'repliesToIds': [],
        'confirmed': False,
        'isSilent': False,
        'isPrivate': False,
    }
    while True:
        try:
            login = session.post('https://www.guilded.gg/api/login', json=login_payload)
            break
        except:
            continue
    if login.status_code == 200:
        with output_lock:
            time_rn = get_time()
            print(f"{reset}[ {cyan}{time_rn}{reset} ] {gray}({yellow}~{gray}) {lightcyan} Logged In {gray} | ", end="")
            sys.stdout.flush()
            Write.Print(f"{email} : {password}\n", Colors.yellow_to_red, interval=0.000)
        while True:
            try:
                send_message = session.post(f'https://www.guilded.gg/api/channels/{channel_id}/messages', json=message_payload)
                break
            except:
                continue
        if send_message.status_code == 200:
            with output_lock:
                messages += 1
                time_rn = get_time()
                print(f"{reset}[ {cyan}{time_rn}{reset} ] {gray}({green}+{gray}) {green} Message Sent {gray} | ", end="")
                sys.stdout.flush()
                Write.Print(f"{email} : {password}\n", Colors.yellow_to_red, interval=0.000)
                chat_spammer_title()
        else:
            pass
    else:
        pass

def account_status_presence(email,password):
    global status_num, presence
    output_lock = threading.Lock()
    proxies = load_proxies()
    proxy = random.choice(proxies)
    emojis = [90002170,90001865,90002057,90001537,90001964,90000868,90002190,90000377,90000036,90001723,90001571,90001441]
    status_string = ["Gamesense.pub","Fatality.win","CS:GO","Gamesense.dog","Medusa.uno","Airflow.su","Aimware.pl","Neverlose.cc","minecraft","genshin impact","among us"]
    emoji = random.choice(emojis)
    rand_status = random.choice(status_string)
    with open('config.json','r')as d:
        data = json.load(d)
        status = data['status']
    session = tls_client.Session(
        client_identifier="chrome_113",
        random_tls_extension_order=True
    )
    session.proxies = {
        'http':f'http://{proxy}',
        'https':f'https://{proxy}'
    }
    login_payload = {
        "email": email,
        "getMe": True,
        "password": password
    }
    if status == '' or status == 'n' or status == 'no':
        status_payload = {
            'content': {
                'object': 'value',
                'document': {
                    'object': 'document',
                    'data': {},
                    'nodes': [
                        {
                            'object': 'block',
                            'type': 'paragraph',
                            'data': {},
                            'nodes': [
                                {
                                    'object': 'text',
                                    'leaves': [
                                        {
                                            'object': 'leaf',
                                            'text': rand_status,
                                            'marks': [],
                                        },
                                    ],
                                },
                            ],
                        },

                    ],
                },
            },
            'customReactionId': emoji,
            'expireInMs': 0,
        }
    else:
        status_payload = {
            'content': {
                'object': 'value',
                'document': {
                    'object': 'document',
                    'data': {},
                    'nodes': [
                        {
                            'object': 'block',
                            'type': 'paragraph',
                            'data': {},
                            'nodes': [
                                {
                                    'object': 'text',
                                    'leaves': [
                                        {
                                            'object': 'leaf',
                                            'text': status,
                                            'marks': [],
                                        },
                                    ],
                                },
                            ],
                        },

                    ],
                },
            },
            'customReactionId': emoji,
            'expireInMs': 0,
        }
    presence_payload = {
        'status':random.randint(2,3)
    }
    while True:
        try:
            login = session.post('https://www.guilded.gg/api/login', json=login_payload)
            break
        except:
            continue
    if login.status_code == 200:
        with output_lock:
            time_rn = get_time()
            print(f"{reset}[ {cyan}{time_rn}{reset} ] {gray}({yellow}~{gray}) {lightcyan} Logged In {gray} | ", end="")
            sys.stdout.flush()
            Write.Print(f"{email} : {password}\n", Colors.yellow_to_red, interval=0.000)         
        while True:
            try:
                set_status = session.post('https://www.guilded.gg/api/users/me/status', json=status_payload)
                break
            except:
                continue
        if set_status.status_code == 200:
            with output_lock:
                time_rn = get_time()
                print(f"{reset}[ {cyan}{time_rn}{reset} ] {gray}({green}+{gray}) {lightcyan} Status Set {gray} | ", end="")
                sys.stdout.flush()
                Write.Print(f"{email} : {password}\n", Colors.yellow_to_red, interval=0.000)  
                status_num += 1
                account_status_presence_title()
        while True:
            try:
                set_presence = session.post('https://www.guilded.gg/api/users/me/presence', json=presence_payload)
                break
            except:
                continue
        if set_presence.status_code == 200:
            with output_lock:
                time_rn = get_time()
                print(f"{reset}[ {cyan}{time_rn}{reset} ] {gray}({green}+{gray}) {lightcyan} Online Set {gray} | ", end="")
                sys.stdout.flush()
                Write.Print(f"{email} : {password}\n", Colors.yellow_to_red, interval=0.000)  
                presence += 1
            account_status_presence_title()

def main():
    global total, generated, failed, checked, messages, status, presence
    with open('config.json','r')as d:
        data = json.load(d)
    os.system("cls")
    Write.Print(f"""
               \t ██████╗ ██╗   ██╗██╗██╗     ██████╗ ███████╗██████╗     ██╗  ██╗██╗   ██╗██████╗ 
               \t██╔════╝ ██║   ██║██║██║     ██╔══██╗██╔════╝██╔══██╗    ██║  ██║██║   ██║██╔══██╗
               \t██║  ███╗██║   ██║██║██║     ██║  ██║█████╗  ██║  ██║    ███████║██║   ██║██████╔╝
               \t██║   ██║██║   ██║██║██║     ██║  ██║██╔══╝  ██║  ██║    ██╔══██║██║   ██║██╔══██╗
               \t╚██████╔╝╚██████╔╝██║███████╗██████╔╝███████╗██████╔╝    ██║  ██║╚██████╔╝██████╔╝
               \t ╚═════╝  ╚═════╝ ╚═╝╚══════╝╚═════╝ ╚══════╝╚═════╝     ╚═╝  ╚═╝ ╚═════╝ ╚═════╝                                                                                                                                                     
                                                    by ~Z3R003~     
                                            (https://github.com/Z3R003) 

                        [01] Account Generator (Fake)           [04] Account Joiner          
                        [02] Account Generator (Real)           [05] Chat Spammer           
                        [03] Account Checker                    [06] Account Onliner/Status  
           
\n\n""", Colors.yellow_to_red, interval=0.000)
    choice = input(f""" {yellow}
┌──{red}(Guilded@Hub){yellow} ~ [{red}Ϟ{yellow}]
└─> """)
    threads = []
    if choice == '1' or choice == '01':
        num_threads = data['threads']
        start_time = time.time()
        for _ in range(num_threads):
                t = threading.Thread(target=fake_account_generator)
                t.start()
                threads.append(t)
        update_title_threads = threading.Thread(target=fake_account_generator_title)
        update_title_threads.start()
        threads.append(update_title_threads)
        for thread in threads:
            thread.join()
        current_time = time.time()
        elapsed_time = current_time - start_time
        elapsed_hours = int((elapsed_time % 86400) // 3600)
        elapsed_minutes = int((elapsed_time % 3600) // 60)
        elapsed_seconds = int(elapsed_time % 60)
        print(f'\n{white}[{red}!{white}]{green} finished! {yellow}Generated {red}{generated} {yellow}fake accounts in {red}{elapsed_hours}h {elapsed_minutes}m {elapsed_seconds}s')
        input(f'{reset}\nEnter to go back!')
        main()
    if choice == '2' or choice == '02':
        num_threads = data['threads']
        print('\n')
        start_time = time.time()
        for _ in range(num_threads):
            t3 = threading.Thread(target=real_account_generator)
            t3.start()
            threads.append(t3)
        update_title_threads = threading.Thread(target=real_account_generator_title)
        update_title_threads.start()
        threads.append(update_title_threads)
        for thread in threads:
            thread.join()
        current_time = time.time()
        elapsed_time = current_time - start_time
        elapsed_hours = int((elapsed_time % 86400) // 3600)
        elapsed_minutes = int((elapsed_time % 3600) // 60)
        elapsed_seconds = int(elapsed_time % 60)
        print(f'\n{white}[{red}!{white}]{green} finished! {yellow}Generated {red}{generated} {yellow}real accounts in {red}{elapsed_hours}h {elapsed_minutes}m {elapsed_seconds}s')
        input(f'{reset}\nEnter to go back!')
        main()
    if choice == '3' or choice == '03':
        file = input(f'{yellow}[{red}?{yellow}] {yellow}.txt file (real-accounts.txt or fake-accounts.txt) > ')
        print('\n')
        with open(file,'r')as a:
            accounts = a.read().splitlines()
        start_time = time.time()
        for account in accounts:
            email,password = account.split(':')
            t = threading.Thread(target=account_checker, args=(email,password))
            t.start()
            threads.append(t)
        update_title_threads = threading.Thread(target=account_checker_title)
        update_title_threads.start()
        threads.append(update_title_threads)    
        for thread in threads:
            thread.join()
        current_time = time.time()
        elapsed_time = current_time - start_time
        elapsed_hours = int((elapsed_time % 86400) // 3600)
        elapsed_minutes = int((elapsed_time % 3600) // 60)
        elapsed_seconds = int(elapsed_time % 60)
        print(f'\n{white}[{red}!{white}]{green} finished! {yellow}Checked {red}{checked} {yellow}accounts in {red}{elapsed_hours}h {elapsed_minutes}m {elapsed_seconds}s')
        input(f'{reset}\nEnter to go back!')
        main()
    if choice == '4' or choice == '04':
        file = input(f'{yellow}[{red}?{yellow}] {yellow}.txt file (real-accounts.txt or fake-accounts.txt) > ')
        print('\n')
        with open(file,'r')as a:
            accounts = a.read().splitlines()
        start_time = time.time()
        for account in accounts:
            email,password = account.split(':')
            t = threading.Thread(target=account_joiner, args=(email,password))
            t.start()
            threads.append(t)
        update_title_threads = threading.Thread(target=account_joiner_title)
        update_title_threads.start()
        threads.append(update_title_threads)    
        for thread in threads:
            thread.join()    
        current_time = time.time()
        elapsed_time = current_time - start_time
        elapsed_hours = int((elapsed_time % 86400) // 3600)
        elapsed_minutes = int((elapsed_time % 3600) // 60)
        elapsed_seconds = int(elapsed_time % 60)
        print(f'\n{white}[{red}!{white}]{green} finished! {yellow}Joined {red}{joined} {yellow} accounts in {red}{elapsed_hours}h {elapsed_minutes}m {elapsed_seconds}s')
        input(f'{reset}\nEnter to go back!')
        main()            
    if choice == '5' or choice == '05':
        message = input(f'{yellow}[{red}?{yellow}]{red} What message you want to spam? > ')
        channel_id = input(f'{yellow}[{red}?{yellow}]{red} channel_id > ')
        file = input(f'{yellow}[{red}?{yellow}]{red} .txt file (real-accounts.txt or fake-accounts.txt) > ')
        print('\n')
        with open(file,'r')as a:
            accounts = a.read().splitlines()
        start_time = time.time()
        for account in accounts:
            email,password = account.split(':')
            t = threading.Thread(target=chat_spammer, args=(email,password,message,channel_id))
            t.start()
            threads.append(t)
        update_title_threads = threading.Thread(target=chat_spammer_title)
        update_title_threads.start()
        threads.append(update_title_threads)    
        for thread in threads:
            thread.join()
        current_time = time.time()
        elapsed_time = current_time - start_time
        elapsed_hours = int((elapsed_time % 86400) // 3600)
        elapsed_minutes = int((elapsed_time % 3600) // 60)
        elapsed_seconds = int(elapsed_time % 60)
        print(f'\n{white}[{red}!{white}]{green} finished! {yellow}{red}{generated} {yellow} messages sent in {red}{elapsed_hours}h {elapsed_minutes}m {elapsed_seconds}s')
        input(f'{reset}\nEnter to go back!')
        main()    
    if choice == '6' or choice == '06':
        file = input(f'{yellow}[{red}?{yellow}] {yellow}.txt file (real-accounts.txt or fake-accounts.txt) > ')
        with open(file,'r')as a:
            accounts = a.read().splitlines()
        start_time = time.time()
        for account in accounts:
            email,password = account.split(':')
            t = threading.Thread(target=account_status_presence, args=(email,password))
            t.start()
            threads.append(t)
        account_status_presence_title_threads = threading.Thread(target=account_status_presence_title)    
        account_status_presence_title_threads.start()
        threads.append(account_status_presence_title_threads)
        for thread in threads:
            thread.join()
        current_time = time.time()
        elapsed_time = current_time - start_time
        elapsed_hours = int((elapsed_time % 86400) // 3600)
        elapsed_minutes = int((elapsed_time % 3600) // 60)
        elapsed_seconds = int(elapsed_time % 60)
        print(f'\n{white}[{red}!{white}]{green} finished! {yellow}Status {red}{status} {yellow}Presence {red}{presence} {yellow} in {red}{elapsed_hours}h {elapsed_minutes}m {elapsed_seconds}s')
        input(f'{reset}\nEnter to go back!')
        main()    
    else:
        clear_screen()
        print(f'{yellow}[{red}!{yellow}]{red} Invalid choice', end=' ')
        [print('.', end='', flush=True) or time.sleep(0.7) for _ in range(3)]
        main()
if __name__ == "__main__":
    main()    
