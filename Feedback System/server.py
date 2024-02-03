import http.server
import http.client
import urllib
import csv
from http.server import SimpleHTTPRequestHandler

class FormHandler(SimpleHTTPRequestHandler):
    def do_POST(self):
        content_length = int(self.headers['Content-Length'])
        form_data = self.rfile.read(content_length).decode('utf-8')
        data = urllib.parse.parse_qs(form_data)

        # Print the received form data for debugging
        print("Received form data:", data)

        with open('form_data.csv', 'a', newline='') as csv_file:
            writer = csv.writer(csv_file)
            writer.writerow([data['name'][0],data['email'][0],data['age'][0],data['First'][0], data['second'][0], data['third'][0], data['product'][0], data['comments'][0]])


        # Customize the response HTML
        response = """
                        <html>
                        <head>
                            <title>Form Submitted</title>
                            <style>
                                body {
                                        font-family: Arial, sans-serif;
                                        margin: 0;
                                        padding: 0;
                                        background: black;
                                        opacity: 0.8; 
                                    }
                                    .bg {
                                    animation:slide 3s ease-in-out infinite alternate;
                                    background-image: linear-gradient(-60deg, #000000 50%, rgb(28, 28, 28) 50%);
                                    bottom:0;
                                    left:-50%;
                                    opacity:.5;
                                        position:fixed;
                                            right:-50%;
                                top:0;
                                z-index:-1;
                            }
                            div
            {
                word-wrap: break-word;
            }
            .bg2 {
                animation-direction:alternate-reverse;
                animation-duration:4s;
            }
            
            .bg3 {
                animation-duration:3s;
            }
            
            
            @keyframes slide {
                0% {
                transform:translateX(-25%);
                }
                100% {
                transform:translateX(25%);
                }
            }

            h1{
                align-items: center;
                margin-top: 200px;
                margin-left: 500px;
                position: relative;
                color: #fff;
            
            }
            h3{
                position: relative;
                margin-left: 560px;
                color: #fff;

            }
            .neon-button {
    display: inline-block;
    background: linear-gradient(to right, #ff6ec4, #7873f5);
    color: #fff;
    padding: 10px 20px;
    font-size: 18px;
    border: none;
    border-radius: 25px;
    text-align: center;
    text-decoration: none;
    cursor: pointer;
    box-shadow: 0 0 10px rgba(255, 110, 196, 0.5);
    margin-left: 47%;
    margin-top: 3%;
}
a
{
    text-decoration: none;
}
.neon-button:hover {
    background: linear-gradient(to right, #7873f5, #ff6ec4);
    box-shadow: 0 0 10px rgba(255, 110, 196, 0.8);
    text-decoration: none;
}

            </style>
        </head>
        <body>
            <div class="bg"></div>
            <div class="bg bg2"></div>
            <div class="bg bg3"></div>
            <h1>Thank you for submitting the form!</h1>
            <h3>Your data has been successfully recorded.</h3>
            <a href="hackathons-events.html" class="neon-button">Home</a>
        </body>
        </html>
        """
        self.send_response(200)
        self.end_headers()
        self.wfile.write(response.encode('utf-8'))

if __name__ == '__main__':
    server_address = ('', 8000)
    httpd = http.server.HTTPServer(server_address, FormHandler)
    print('Server is running on http://localhost:8000')
    httpd.serve_forever()