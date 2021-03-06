from bottle import route, run, template
import os 


@route('/')
def index():
    name = 'APT Spring 2015'
    participants = [

       'Almaz Issembergenov',
        "#20 Robert Pattinson",
        "#19 Kesha",
        "#18 Megan Fox",
        "#17 Nicki Minaj",
        "#16 Beyonce",
        "#15 Taylor Swift",
        "#14 Selena Gomez",
        "#13 Ronaldo",
        "#12 Lil Wayne",
        "#11 Kim Kardashian",
        'German Ilyin',
        "#10 Drake",
        "#9 Katy Perry",
        "#8 Obama",
        "#7 Michael Jackson",
        "#6 Rihanna",
        "#5 Shakira",
        "#4 Eminem",
        "#3 Miley Cyrus",
        "#2 Lady Gaga",
        "#1 Justin Bieber",
    ]
    return template("""
    <h1>HW2 for {{course}}</h1>
    Participants list:
    <ul>
      % for item in lst:
      <li>{{ item }}</li>
      % end
    </ul>
    """, course=name, lst=participants)

run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))
