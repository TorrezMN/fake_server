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
<<<<<<< HEAD
        """
        .########..##.....##.########..##.......####..######.
        .##.....##.##.....##.##.....##.##........##..##....##
        .##.....##.##.....##.##.....##.##........##..##......
        .########..##.....##.########..##........##..##......
        .##........##.....##.##.....##.##........##..##......
        .##........##.....##.##.....##.##........##..##....##
        .##.........#######..########..########.####..######.
        """

=======
         
        # ██████╗  █████╗ ███████╗███████╗    ██████╗  ██████╗  ██████╗
        # ██╔══██╗██╔══██╗██╔════╝██╔════╝    ██╔══██╗██╔═══██╗██╔════╝
        # ██████╔╝███████║███████╗█████╗      ██║  ██║██║   ██║██║
        # ██╔══██╗██╔══██║╚════██║██╔══╝      ██║  ██║██║   ██║██║
        # ██████╔╝██║  ██║███████║███████╗    ██████╔╝╚██████╔╝╚██████╗
        # ╚═════╝ ╚═╝  ╚═╝╚══════╝╚══════╝    ╚═════╝  ╚═════╝  ╚═════╝
        
>>>>>>> 2f2dedbf2a68311ba34929de225d2f62797f8290
        if self.path == '/':
            self.path = '/public_doc/index.html'
            try:
                file_to_open = open(self.path[1:]).read()
                self.send_response(200)
            except:
                file_to_open = 'File not found!'
                self.send_response(404)
            self.end_headers()
            self.wfile.write(bytes(file_to_open, 'utf-8'))

<<<<<<< HEAD
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
        if re.match(r'/basic_profile/\d$', self.path) is not None:
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
=======
        
        # ██████╗ ██████╗  ██████╗ ███████╗██╗██╗     ███████╗
        # ██╔══██╗██╔══██╗██╔═══██╗██╔════╝██║██║     ██╔════╝
        # ██████╔╝██████╔╝██║   ██║█████╗  ██║██║     █████╗
        # ██╔═══╝ ██╔══██╗██║   ██║██╔══╝  ██║██║     ██╔══╝
        # ██║     ██║  ██║╚██████╔╝██║     ██║███████╗███████╗
        # ╚═╝     ╚═╝  ╚═╝ ╚═════╝ ╚═╝     ╚═╝╚══════╝╚══════╝
        if self.path == '/basic_profile':
>>>>>>> 2f2dedbf2a68311ba34929de225d2f62797f8290
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
<<<<<<< HEAD

        # Surname various
        if re.match(r'/last_name/\d+$', self.path) is not None:
=======
        if self.path == '/full_name':
>>>>>>> 2f2dedbf2a68311ba34929de225d2f62797f8290
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

<<<<<<< HEAD
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
=======
        # ██╗   ██╗ █████╗ ██████╗ ██╗███████╗██████╗
        # ██║   ██║██╔══██╗██╔══██╗██║██╔════╝██╔══██╗
        # ██║   ██║███████║██████╔╝██║█████╗  ██║  ██║
        # ╚██╗ ██╔╝██╔══██║██╔══██╗██║██╔══╝  ██║  ██║
        #  ╚████╔╝ ██║  ██║██║  ██║██║███████╗██████╔╝
        #   ╚═══╝  ╚═╝  ╚═╝╚═╝  ╚═╝╚═╝╚══════╝╚═════╝
        if self.path == '/task':
            parsed_path = parse.urlparse(self.path)
            task = {
                'id':str(uuid.uuid4()),
>>>>>>> 2f2dedbf2a68311ba34929de225d2f62797f8290
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

<<<<<<< HEAD
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
=======
        if re.match(r'/task/\d+',self.path) is not None:
            parsed_path = parse.urlparse(self.path)
            total_req = int(self.path.split('/')[-1])
            req = {
            'req_url':self.path,
            'quantity_req': self.path.split('/')[-1],
            'tasks':[{
                'id':str(uuid.uuid4()),
                'task': Faker().sentence(),
                'responsible': str(Faker().name()),
                'status': choice(['completed', 'pending', 'finished', 'lacks_approval']),
                'created': str(Faker().date()),
                'priority_level' : choice(['high ',' medium ',' low ',' moderate ',' undefined']),
                'term_in_days': choice([i for i in range(0,30)])
            } for i in range(0,total_req)],
            }
            
                
            message = json.dumps(str(req))
>>>>>>> 2f2dedbf2a68311ba34929de225d2f62797f8290
            self.send_response(200)
            self.send_header('Content-Type', 'application/json; charset=utf-8')
            self.end_headers()
            self.wfile.write(bytes(message, 'utf-8'))
<<<<<<< HEAD
=======


>>>>>>> 2f2dedbf2a68311ba34929de225d2f62797f8290

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
