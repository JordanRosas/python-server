from http.server import BaseHTTPRequestHandler, HTTPServer
from animals import get_all_animals, get_single_animal
from locations import get_single_location, get_all_locations
from employees import get_single_employee, get_all_employees
from customers import get_single_customer, get_all_customers

class RequestHandler(BaseHTTPRequestHandler):

    def parse_url(self, path):
        path_params = path.split("/")
        resource = path_params[1]
        id = None

        try:
            id = int(path_params[2])
        except IndexError:
            pass
        except ValueError:
            pass
        return(resource, id)

    def _set_headers(self, status):
        self.send_response(status)
        self.send_header('Content-type', 'application/json')
        self.send_header('Access-Control-Allow-Origin', '*')
        self.end_headers()

    def do_OPTIONS(self):
        self.send_response(200)
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('Access-Control-Allow-Methods', 'GET, POST, PUT, DELETE')
        self.send_header('Access-Control-Allow-Headers', 'X-Requested-With, Content-Type, Accept')
        self.end_headers()

    def do_GET(self):

        self._set_headers(200)

        response = {}
        (resource, id) = self.parse_url(self.path)
        print(resource)
        if resource == "animals":
            if id is not None:
                response = f"{get_single_animal(id)}"
            else:
                response = f"{get_all_animals()}"

        if resource == "locations":
            if id is not None:
                response = f"{get_single_location(id)}"
            else:
                response = f"{get_all_locations()}"

        if resource == "employees":
            if id is not None:
                response = f"{get_single_employee(id)}"
            else:
                response = f"{get_all_employees()}"
        
        if resource == "customers":
            if id is not None:
                response = f"{get_single_customer(id)}"
            else:  
                response = f"{get_all_customers()}"

        encoded_response = response.encode()
        decoded_response = encoded_response.decode("utf-8").replace("'", '"')

        self.wfile.write(decoded_response.encode())    

    def do_POST(self):
        self._set_headers(201)

        content_len = int(self.headers.get('content-length', 0))
        post_body = self.rfile.read(content_len)
        response = f"received post request <br>{post_body}"
        self.wfile.write(response.encode())

    def do_PUT(self):
        self.do_POST()
    
def main():
    host=''
    port = 8088
    HTTPServer((host, port), RequestHandler).serve_forever()

if __name__ == "__main__":
    main()