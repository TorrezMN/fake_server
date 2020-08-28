import json
from http.server import BaseHTTPRequestHandler
from urllib import parse
from faker import Faker
from random import choice
import uuid
import re

# PROVIDERS
from faker.providers import profile

class Fake_Server(BaseHTTPRequestHandler):

    def do_GET(self):
         
        # ██████╗  █████╗ ███████╗███████╗    ██████╗  ██████╗  ██████╗
        # ██╔══██╗██╔══██╗██╔════╝██╔════╝    ██╔══██╗██╔═══██╗██╔════╝
        # ██████╔╝███████║███████╗█████╗      ██║  ██║██║   ██║██║
        # ██╔══██╗██╔══██║╚════██║██╔══╝      ██║  ██║██║   ██║██║
        # ██████╔╝██║  ██║███████║███████╗    ██████╔╝╚██████╔╝╚██████╗
        # ╚═════╝ ╚═╝  ╚═╝╚══════╝╚══════╝    ╚═════╝  ╚═════╝  ╚═════╝
        
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

        
        # ██████╗ ██████╗  ██████╗ ███████╗██╗██╗     ███████╗
        # ██╔══██╗██╔══██╗██╔═══██╗██╔════╝██║██║     ██╔════╝
        # ██████╔╝██████╔╝██║   ██║█████╗  ██║██║     █████╗
        # ██╔═══╝ ██╔══██╗██║   ██║██╔══╝  ██║██║     ██╔══╝
        # ██║     ██║  ██║╚██████╔╝██║     ██║███████╗███████╗
        # ╚═╝     ╚═╝  ╚═╝ ╚═════╝ ╚═╝     ╚═╝╚══════╝╚══════╝
        if self.path == '/basic_profile':
            parsed_path = parse.urlparse(self.path)
            message = json.dumps(str(Faker().simple_profile()))
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

        if self.path == '/full_profile':
            parsed_path = parse.urlparse(self.path)
            F = Faker()
            F.add_provider(profile)
            message = json.dumps(str(F.profile()))
            self.send_response(200)
            self.send_header('Content-Type', 'application/json; charset=utf-8')
            self.end_headers()
            self.wfile.write(bytes(message, 'utf-8'))
        if self.path == '/full_name':
            parsed_path = parse.urlparse(self.path)
            message = json.dumps(str(Faker().name()))
            self.send_response(200)
            self.send_header('Content-Type', 'application/json; charset=utf-8')
            self.end_headers()
            self.wfile.write(bytes(message, 'utf-8'))
        if self.path == '/last_name':
            parsed_path = parse.urlparse(self.path)
            message = json.dumps(str(Faker().last_name()))
            self.send_response(200)
            self.send_header('Content-Type', 'application/json; charset=utf-8')
            self.end_headers()
            self.wfile.write(bytes(message, 'utf-8'))
        if self.path == '/first_name':
            parsed_path = parse.urlparse(self.path)
            message = json.dumps(str(Faker().last_name()))
            self.send_response(200)
            self.send_header('Content-Type', 'application/json; charset=utf-8')
            self.end_headers()
            self.wfile.write(bytes(message, 'utf-8'))

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
                'task': Faker().sentence(),
                'responsible': str(Faker().name()),
                'status': choice(['completed', 'pending', 'finished', 'lacks_approval']),
                'created': str(Faker().date()),
                'priority_level' : choice(['high ',' medium ',' low ',' moderate ',' undefined']),
                'term_in_days': choice([i for i in range(0,30)])
            }
            message = json.dumps(str(task))
            self.send_response(200)
            self.send_header('Content-Type', 'application/json; charset=utf-8')
            self.end_headers()
            self.wfile.write(bytes(message, 'utf-8'))

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
