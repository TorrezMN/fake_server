import json
from http.server import BaseHTTPRequestHandler
from urllib import parse
from faker import Faker
from random import choice
import uuid
import re

# PROVIDERS
from faker.providers import profile
from faker.providers import geo

class Fake_Server(BaseHTTPRequestHandler):

    def do_GET(self):
        """
        .########..##.....##.########..##.......####..######.
        .##.....##.##.....##.##.....##.##........##..##....##
        .##.....##.##.....##.##.....##.##........##..##......
        .########..##.....##.########..##........##..##......
        .##........##.....##.##.....##.##........##..##......
        .##........##.....##.##.....##.##........##..##....##
        .##.........#######..########..########.####..######.
        """

        if self.path == '/':
            # Returns the main page of the server. Contains documentation related to available end-points.
            self.path = '/public_doc/index.html'
            try:
                file_to_open = open(self.path[1:]).read()
                self.send_response(200)
            except:
                file_to_open = 'File not found!'
                self.send_response(404)
            self.end_headers()
            self.wfile.write(bytes(file_to_open, 'utf-8'))

        """
        .########..########...#######..########.####.##.......########
        .##.....##.##.....##.##.....##.##........##..##.......##......
        .##.....##.##.....##.##.....##.##........##..##.......##......
        .########..########..##.....##.######....##..##.......######..
        .##........##...##...##.....##.##........##..##.......##......
        .##........##....##..##.....##.##........##..##.......##......
        .##........##.....##..#######..##.......####.########.########
        """

        # Basic Profile
        if re.match(r'/basic_profile$', self.path) is not None:
            """
            This end-point returns a basic user profile.
            It contains the following elements:
            {'id': <str: It corresponds to a unique basic id for the request made, it can be used for profile-id.>, 
            'req_url': <str: It contains the url of the request completely parceled. Can be used as debug mode>, 
            'basic_profile':
                 {'username': <str: A username for the user.>, 
                 'name': <str:Full name of the user.>, 
                 'sex': <str: A single letter to define the gender of the user.>, 
                 'address': <str: An address for the user.>,
                  'mail':<str: A valid e-mail address.>,
                   'birthdate':< date: Retorna un objeto python tipo 'date'-> ej: date(1954, 9, 4)>
                   }
                   }
            """

            parsed_path = parse.urlparse(self.path)
            data_req = {
                'id': str(uuid.uuid4()),
                'req_url': self.path,
                'basic_profile': Faker().simple_profile()
            }
            message = json.dumps(str(data_req))
            self.send_response(200)
            self.send_header('Content-Type', 'application/json; charset=utf-8')
            self.end_headers()
            self.wfile.write(bytes(message, 'utf-8'))

        # Basic Profile various
        if re.match(r'/basic_profile/various/\d$', self.path) is not None:
            """
            It is the same end-point as '/basic_profile' but allows requesting <n> number of profiles simultaneously.
            Retorna un objeto como este:
            "{
                'id': <str: It corresponds to a unique basic id for the request made, it can be used for profile-id.>, 
                'req_url': <str: It contains the url of the request completely parceled. Can be used as debug mode>, 
                'required_quantity': <int: It corresponds to the required quantity. It is for debugging purposes.>, 
                'profiles':<array: Corresponds to an array of objects that contains the required number of basic profiles.> 
                }"
            """

            parsed_path = parse.urlparse(self.path)
            quant = int(self.path.split('/')[-1])
            data_req = {
                'id': str(uuid.uuid4()),
                'req_url': self.path,
                'required_quantity': quant,
                'profiles': [Faker().simple_profile() for i in range(0, quant)]
            }
            message = json.dumps(str(data_req))
            self.send_response(200)
            self.send_header('Content-Type', 'application/json; charset=utf-8')
            self.end_headers()
            self.wfile.write(bytes(message, 'utf-8'))

        # Basic Profile by Sex only one
        if re.match(r'/basic_profile/sex/[M|F]$', self.path) is not None:
            # End-point that returns a basic male or female profile as requested.
            parsed_path = parse.urlparse(self.path)
            sex = self.path.split('/')[-1]
            F = Faker()
            F.add_provider(profile)
            data_req = {
                'id': str(uuid.uuid4()),
                'req_url': self.path,
                'sex_req': sex,
                'basic_profile': Faker().simple_profile(sex=sex)
            }
            message = json.dumps(str(data_req))
            self.send_response(200)
            self.send_header('Content-Type', 'application/json; charset=utf-8')
            self.end_headers()
            self.wfile.write(bytes(message, 'utf-8'))

        # Basic Profile by Sex various
        if re.match(r'/basic_profile/sex/[M|F]/\d+$', self.path) is not None:
            """
            Returns a group of basic profiles as requested, male or female and determined amount.
            Sample answer:
            "{
                'id': <str:Corresponds to a unique ID for the server response ... It is used for the calls of react 'unique-key'.>,
                'req_url': <str: The fully parceled url. To debug>,
                'sex_req': <str: One digit corresponding to the sex of the required profiles.>,
                'quantity_required': <int: The number of profiles required corresponds.>,
                'profiles': <array: It is an array containing each of the individual basic profiles.>
                }"
            """
            parsed_path = parse.urlparse(self.path)
            sex = self.path.split('/')[-2]
            quant = int(self.path.split('/')[-1])
            F = Faker()
            F.add_provider(profile)
            data_req = {
                'id': str(uuid.uuid4()),
                'req_url': self.path,
                'sex_req': sex,
                'quantity_required': quant,
                'profiles': [Faker().simple_profile(sex=sex) for i in range(0, quant)]
            }
            message = json.dumps(str(data_req))
            self.send_response(200)
            self.send_header('Content-Type', 'application/json; charset=utf-8')
            self.end_headers()
            self.wfile.write(bytes(message, 'utf-8'))

        # Full Profile
        if re.match(r'/full_profile$', self.path) is not None:
            """
            Returns a complete personal profile. (User profile.)
            Sample answer: 
            "{
                'id': <str: It corresponds to a unique basic id for the request made, it can be used for profile-id.>, 
                'req_url': <str: It contains the url of the request completely parceled. Can be used as debug mode>, 
                'full_profile': {
                    'job': <str: Describes the profession of the generated user.>,
                    'company': <str: Corresponds to the name of the company of the generated user.>,
                    'ssn': <str: Corresponds to the social security number of the created user.>,
                    'residence': <str: Corresponds to a user's residence address.>,
                    'current_location': <touple: A python-tuple of GPS positions corresponds to the current position of the user.>,
                    'blood_group': <str: Corresponds to the user's blood group.>, 
                    'website': <array: Corresponds to an array of urls.>, 
                    'username': <str:Corresponds to a username for the user.>,
                    'name': <str: Corresponds to the full name of the user.>,
                    'sex': <str: A digit corresponding to the gender of the user generated.>,
                    'address': <str: A second address, can be used as a work address.>,
                    'mail': <str: An email address for the user.>,
                    'birthdate': <date: Date object, corresponding to the user's birthday.>
                       }
                       }"
            """
            parsed_path = parse.urlparse(self.path)
            F = Faker()
            F.add_provider(profile)
            data_req = {
                'id': str(uuid.uuid4()),
                'req_url': self.path,
                'full_profile': F.profile()
            }
            message = json.dumps(str(data_req))
            self.send_response(200)
            self.send_header('Content-Type', 'application/json; charset=utf-8')
            self.end_headers()
            self.wfile.write(bytes(message, 'utf-8'))

        # Full Profile by Sex only one
        if re.match(r'/full_profile/sex/[M|F]$', self.path) is not None:
            parsed_path = parse.urlparse(self.path)
            F = Faker()
            F.add_provider(profile)
            sex = self.path.split('/')[-1]
            data_req = {
                'id': str(uuid.uuid4()),
                'req_url': self.path,
                'sex_required': sex,
                'full_profile': F.profile(sex=sex)
            }
            message = json.dumps(str(data_req))
            self.send_response(200)
            self.send_header('Content-Type', 'application/json; charset=utf-8')
            self.end_headers()
            self.wfile.write(bytes(message, 'utf-8'))
        
        if re.match(r'/basic_profile/\d+', self.path) is not None:
            
            total_req = int(self.path.split('/')[-1])
            req = {
            'req_url': self.path,
            'quantity_req': self.path.split('/')[-1],
            'profiles': [Faker().simple_profile() for i in range(0, total_req)]
            }
            message = json.dumps(str(req))
            self.send_response(200)
            self.send_header('Content-Type', 'application/json; charset=utf-8')
            self.end_headers()
            self.wfile.write(bytes(message, 'utf-8'))

        # Full Profile by Sex various
        if re.match(r'/full_profile/sex/[M|F]/\d+$', self.path) is not None:
            parsed_path = parse.urlparse(self.path)
            F = Faker()
            F.add_provider(profile)
            sex = self.path.split('/')[-2]
            quant = int(self.path.split('/')[-1])
            data_req = {
                'id': str(uuid.uuid4()),
                'req_url': self.path,
                'sex_required': sex,
                'required_quantity': quant,
                'profiles': [F.profile(sex=sex) for i in range(0, quant)]
            }
            message = json.dumps(str(data_req))
            self.send_response(200)
            self.send_header('Content-Type', 'application/json; charset=utf-8')
            self.end_headers()
            self.wfile.write(bytes(message, 'utf-8'))

        # Full name only one
        if re.match(r'/full_name$', self.path) is not None:
            # Returns an object containing a full name, last name, and first names.
            parsed_path = parse.urlparse(self.path)
            data_req = {
                'id': str(uuid.uuid4()),
                'req_url': self.path,
                'full_name': Faker().name()
            }
            message = json.dumps(str(data_req))
            self.send_response(200)
            self.send_header('Content-Type', 'application/json; charset=utf-8')
            self.end_headers()
            self.wfile.write(bytes(message, 'utf-8'))

        # Full name various
        if re.match(r'/full_name/\d+$', self.path) is not None:
            parsed_path = parse.urlparse(self.path)
            quant = int(self.path.split('/')[-1])
            data_req = {
                'id': str(uuid.uuid4()),
                'req_url': self.path,
                'required_quantity': quant,
                'names': [Faker().name() for i in range(0, quant)]
            }
            message = json.dumps(str(data_req))
            self.send_response(200)
            self.send_header('Content-Type', 'application/json; charset=utf-8')
            self.end_headers()
            self.wfile.write(bytes(message, 'utf-8'))

        # Surname only
        if re.match(r'/last_name$', self.path) is not None:
            parsed_path = parse.urlparse(self.path)
            data_req = {
                'id': str(uuid.uuid4()),
                'req_url': self.path,
                'last_name': Faker().last_name()
            }
            message = json.dumps(str(data_req))
            self.send_response(200)
            self.send_header('Content-Type', 'application/json; charset=utf-8')
            self.end_headers()
            self.wfile.write(bytes(message, 'utf-8'))

        # Surname various
        if re.match(r'/last_name/\d+$', self.path) is not None:
            parsed_path = parse.urlparse(self.path)
            quant = int(self.path.split('/')[-1])
            data_req = {
                'id': str(uuid.uuid4()),
                'req_url': self.path,
                'quantity_required': quant,
                'last_names': [Faker().last_name() for i in range(0, quant)]
            }
            message = json.dumps(str(data_req))
            self.send_response(200)
            self.send_header('Content-Type', 'application/json; charset=utf-8')
            self.end_headers()
            self.wfile.write(bytes(message, 'utf-8'))

        # Name only one
        if re.match(r'/first_name', self.path) is not None:
            parsed_path = parse.urlparse(self.path)
            data_req = {
                'id': str(uuid.uuid4()),
                'req_url': self.path,
                'first_name': Faker().first_name()
            }
            message = json.dumps(str(data_req))
            self.send_response(200)
            self.send_header('Content-Type', 'application/json; charset=utf-8')
            self.end_headers()
            self.wfile.write(bytes(message, 'utf-8'))

        # Name varius
        if re.match(r'/first_name/\d+$', self.path) is not None:
            parsed_path = parse.urlparse(self.path)
            quant = int(self.path.split('/')[-1])
            data_req = {
                'id': str(uuid.uuid4()),
                'req_url': self.path,
                'required_quantity': quant,
                'first_name': [Faker().first_name() for i in range(0, quant)]
            }
            message = json.dumps(str(data_req))
            self.send_response(200)
            self.send_header('Content-Type', 'application/json; charset=utf-8')
            self.end_headers()
            self.wfile.write(bytes(message, 'utf-8'))

        # Address only one
        if re.match(r'/address$', self.path) is not None:
            parsed_path = parse.urlparse(self.path)
            data_req = {
                'id': str(uuid.uuid4()),
                'req_url': self.path,
                'address': Faker().address()
            }
            message = json.dumps(str(data_req))
            self.send_response(200)
            self.send_header('Content-Type', 'application/json; charset=utf-8')
            self.end_headers()
            self.wfile.write(bytes(message, 'utf-8'))

        # Address only various
        if re.match(r'/address/\d+$', self.path) is not None:
            parsed_path = parse.urlparse(self.path)
            quant = int(self.path.split('/')[-1])
            data_req = {
                'id': str(uuid.uuid4()),
                'req_url': self.path,
                'required_quantity': quant,
                'addresses': [Faker().address() for i in range(0, quant)]
            }
            message = json.dumps(str(data_req))
            self.send_response(200)
            self.send_header('Content-Type', 'application/json; charset=utf-8')
            self.end_headers()
            self.wfile.write(bytes(message, 'utf-8'))

        """
        .########....###.....######..##....##..######.
        ....##......##.##...##....##.##...##..##....##
        ....##.....##...##..##.......##..##...##......
        ....##....##.....##..######..#####.....######.
        ....##....#########.......##.##..##.........##
        ....##....##.....##.##....##.##...##..##....##
        ....##....##.....##..######..##....##..######.
        """

        # Single task
        if re.match(r'/task', self.path) is not None:
            parsed_path = parse.urlparse(self.path)
            data_req = {
                'id': str(uuid.uuid4()),
                'req_url': self.path,
                'task': Faker().sentence(),
                'responsible': str(Faker().name()),
                'status': choice(['completed', 'pending', 'finished', 'lacks_approval']),
                'created': str(Faker().date()),
                'priority_level' : choice(['high ',' medium ',' low ',' moderate ',' undefined']),
                'term_in_days': choice([i for i in range(0,30)])
            }
            message = json.dumps(str(data_req))
            self.send_response(200)
            self.send_header('Content-Type', 'application/json; charset=utf-8')
            self.end_headers()
            self.wfile.write(bytes(message, 'utf-8'))

        # Several tasks
        if re.match(r'/task/\d+$', self.path) is not None:
            parsed_path = parse.urlparse(self.path)
            total_req = int(self.path.split('/')[-1])
            req = {
                'req_url': self.path,
                'quantity': self.path.split('/')[-1],
                'tasks': [{
                    'id': str(uuid.uuid4()),
                    'task': Faker().sentence(),
                    'responsable': str(Faker().name()),
                    'status': choice(['completed', 'pending', 'finished', 'leacks_approval']),
                    'created': str(Faker().date()),
                    'priority_level': choice(['high', 'medium', 'low', 'moderate', 'undefined']),
                    'term_in_days': choice([i for i in range(0, 30)])
                } for i in range(0, total_req)],
            }

            message = json.dumps(str(req))
            self.send_response(200)
            self.send_header('Content-Type', 'application/json; charset=utf-8')
            self.end_headers()
            self.wfile.write(bytes(message, 'utf-8'))

        """
        ..######...########..#######.
        .##....##..##.......##.....##
        .##........##.......##.....##
        .##...####.######...##.....##
        .##....##..##.......##.....##
        .##....##..##.......##.....##
        ..######...########..#######.
        """
        # Single lat & long
        if re.match(r'/lat_long$', self.path) is not None:
            parsed_path = parse.urlparse(self.path)
            f = Faker()
            f.add_provider(geo)
            data_req = {
                'id': str(uuid.uuid4()),
                'req_url': self.path,
                'lat_long': [str(i) for i in f.latlng()]
            }
            message = json.dumps(str(data_req))
            self.send_response(200)
            self.send_header('Content-Type', 'application/json; charset=utf-8')
            self.end_headers()
            self.wfile.write(bytes(message, 'utf-8'))

        # Local lat & long only one
        if re.match(r'/lat_long/local/\w+$', self.path) is not None:
            parsed_path = parse.urlparse(self.path)
            loc = self.path.split('/')[-1].split('_')[-1]
            f = Faker()
            f.add_provider(geo)
            data_req = {
                'id': str(uuid.uuid4()),
                'req_url': self.path,
                'lat_long': f.local_latlng(country_code=str(loc))
            }
            message = json.dumps(str(data_req))
            self.send_response(200)
            self.send_header('Content-Type', 'application/json; charset=utf-8')
            self.end_headers()
            self.wfile.write(bytes(message, 'utf-8'))

        # Local lat & long various
        if re.match(r'/lat_long/local/\w+/\d+$', self.path) is not None:
            parsed_path = parse.urlparse(self.path)
            loc = self.path.split('/')[-2].split('_')[-1]
            quant = int(self.path.split('/')[-1])
            f = Faker()
            f.add_provider(geo)
            data_req = {
                'id': str(uuid.uuid4()),
                'req_url': self.path,
                'required_area': loc,
                'required_quantity': quant,
                'lat_long':  [[i for i in f.local_latlng(country_code=str(loc))] for i in range(0, quant)]
            }
            message = json.dumps(str(data_req))
            self.send_response(200)
            self.send_header('Content-Type', 'application/json; charset=utf-8')
            self.end_headers()
            self.wfile.write(bytes(message, 'utf-8'))

        # Secure lat & long
        if re.match(r'/lat_long/secure$', self.path) is not None:
            parsed_path = parse.urlparse(self.path)

            f = Faker()
            f.add_provider(geo)
            data_req = {
                'id': str(uuid.uuid4()),
                'req_url': self.path,
                'lat_long':   f.location_on_land()
            }
            message = json.dumps(str(data_req))
            self.send_response(200)
            self.send_header('Content-Type', 'application/json; charset=utf-8')
            self.end_headers()
            self.wfile.write(bytes(message, 'utf-8'))

        # Secure lat & long various
        if re.match(r'/lat_long/secure/\d+$', self.path) is not None:
            parsed_path = parse.urlparse(self.path)
            quant = int(self.path.split('/')[-1])
            f = Faker()
            f.add_provider(geo)
            data_req = {
                'id': str(uuid.uuid4()),
                'req_url': self.path,
                'required_quantity': quant,
                'lat_long': [[i for i in f.location_on_land()] for i in range(0, quant)]
            }
            message = json.dumps(str(data_req))
            self.send_response(200)
            self.send_header('Content-Type', 'application/json; charset=utf-8')
            self.end_headers()
            self.wfile.write(bytes(message, 'utf-8'))

        """
        .##......##.########....###....########.##.....##.########.########.
        .##..##..##.##.........##.##......##....##.....##.##.......##.....##
        .##..##..##.##........##...##.....##....##.....##.##.......##.....##
        .##..##..##.######...##.....##....##....#########.######...########.
        .##..##..##.##.......#########....##....##.....##.##.......##...##..
        .##..##..##.##.......##.....##....##....##.....##.##.......##....##.
        ..###..###..########.##.....##....##....##.....##.########.##.....##
        """
        # Single weather report
        if re.match(r'/weather$', self.path) is not None:
            parsed_path = parse.urlparse(self.path)
            data_req = {
                'id': str(uuid.uuid4()),
                'req_url': self.path,
                'weather_report': {
                    'temperature': choice([i for i in range(30, 45)]),
                    'wind_speed': str(choice([i for i in range(50, 130)])) + 'km/h',
                    'humidity': choice([i for i in range(5, 100)]),
                    'hours_of_sun': choice([i for i in range(15, 20)]),
                    'sunrise_time': Faker().time(),
                    'sunset': Faker().time(),
                    'report_date': Faker().date()
                }
            }
            message = json.dumps(str(data_req))
            self.send_response(200)
            self.send_header('Content-Type', 'application/json; charset=utf-8')
            self.end_headers()
            self.wfile.write(bytes(message, 'utf-8'))

        # Various weather reports
        if re.match(r'/weather/\d+$', self.path) is not None:
            parsed_path = parse.urlparse(self.path)
            quant = int(self.path.split('/')[-1])
            data_req = {
                'id': str(uuid.uuid4()),
                'req_url': self.path,
                'required_quantity': quant,
                'weather_reports': [{
                    'temperature': choice([i for i in range(30, 45)]),
                    'wind_speed': str(choice([i for i in range(50, 130)])) + 'km/h',
                    'humidity': choice([i for i in range(5, 100)]),
                    'hours_of_sun': choice([i for i in range(15, 20)]),
                    'sunrise_time': Faker().time(),
                    'sunset': Faker().time(),
                    'report_date': Faker().date()
                } for i in range(0, quant)]
            }
            message = json.dumps(str(data_req))
            self.send_response(200)
            self.send_header('Content-Type', 'application/json; charset=utf-8')
            self.end_headers()
            self.wfile.write(bytes(message, 'utf-8'))

if __name__ == '__main__':
    from http.server import HTTPServer
    server = HTTPServer(('localhost', 8080), Fake_Server)
    print('Server startet at: [localhost:8080]')
    print('Use <ctrl-c> to stop.')
    server.serve_forever()
