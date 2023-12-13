from jinja2 import Environment, FileSystemLoader
from flask import Flask, request, Response
import colored
bannar_color =[
colored.fg("magenta") + colored.attr("bold"), 
colored.fg("cyan")    + colored.attr("bold"),
colored.fg("yellow")  + colored.attr("bold"),
colored.fg("#bc000b") + colored.attr("bold"),
colored.fg("white")   + colored.attr("bold"),
colored.fg("#33ff29") + colored.attr("bold"),
colored.fg("white") + colored.bg("black")+colored.attr("bold"),
colored.fg("#33ff29") + colored.bg("white")+colored.attr("bold")
]

magenta = bannar_color[0]
cyan = bannar_color[1]
yellow = bannar_color[2]
red = bannar_color[3]
white = bannar_color[4]
green = bannar_color[5]
bold = bannar_color[6]
res = colored.style.RESET
bannar = f'''
{cyan}
          |\___/|                      \\
         =) ^Y^ (=   |\_/|              ||    '
          \  ^  /    )a a '._.-""""-.  //
           )=*=(    =\T_= /    ~  ~  \//
          /     \     `"`\   ~   / ~  /
          |     |         |~   \ |  ~/
         /| | | |\         \  ~/- \ ~\
{res}   
        {green}{bold}╔═╗┌─┐┌─┐┌┬┐┌─┐ ╦┌─┐┌─┐┬┌─┌─┐┬─┐{res}
        {green}{bold}╠═╝├─┤└─┐ │ ├┤  ║├─┤│  ├┴┐├┤ ├┬┘{res}
        {green}{bold}╩  ┴ ┴└─┘ ┴ └─┘╚╝┴ ┴└─┘┴ ┴└─┘┴└─{res}
                                    {white}[{red}=>{white}] {yellow}Created by{red}:{red}{bold}AbdulRahman Mohammed{res}{white}({cyan}De3vil{white}) {white}[{red}<={white}]{green}
                                  \___________________________________________________/ 
'''
print(bannar)
globalvar = input(f"{red}set payload {white}: ")

app = Flask(__name__)

@app.route('/')
def index():
    global globalvar
    payload = request.args.get('payload',f"{globalvar}"'\r\n')

    env = Environment(loader=FileSystemLoader('templates'))
    template = env.get_template('index.html')
    rendered_template = template.render(payload=payload)

    return Response(rendered_template, content_type='text/html')

if __name__ == '__main__':
    app.run(host="0.0.0.0",port=8080)
