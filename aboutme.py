import streamlit as st
from PIL import Image

with open("style.css") as f:
    st.markdown('<style>{}</style>'.format(f.read()), unsafe_allow_html=True)

#####################
# Header 
st.write('''
# **about me**
''')
st.write('**I have the ability to adapt and manage when the situation is different. I always aim for achievements and job well done. I am proud of myself because of my good  manner and truly respectful, where I need to be careful of my actions so I cannot bother anyone or disrespect anyone. I do everything that makes my self happy. Focusing on good things, and positive vibes. Showing some Peace and Love for everyone. .**')

image = Image.open('bassist.jpg')
st.image(image, caption = "I wasn't originally a bass player. I just found out I was needed, because everyone wants to play guitar. - Tina Weymouth", 
width=700)

st.markdown('## **Background**', unsafe_allow_html=True)
st.success('''
- Hi! I'm Kenan Kier Albarando Colita, 21 years Old.
- Born in June 29, 2002 at Caraga Regional Hospital. 
-  I play Basketball, and I was a varsity player at SCNHS.
-  I'm in a band called Menace and I play bass guitar.
''')

#####################
# Navigation

st.markdown('<link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/css/bootstrap.min.css" integrity="sha384-Gn5384xqQ1aoWXA+058RXPxPg6fy4IWvTNh0E263XmFcJlSAwiGgFAW/dAiS6JXm" crossorigin="anonymous">', unsafe_allow_html=True)

st.markdown("""
<nav class="navbar fixed-top navbar-expand-lg navbar-dark" style="background-color: #0B0D0C;">
  <a class="navbar-brand" href="https://www.facebook.com/kenankier" target="_blank">Kenan Kier Colita</a>
  <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarNav" aria-controls="navbarNav" aria-expanded="false" aria-label="Toggle navigation">
    <span class="navbar-toggler-icon"></span>
  </button>
  <div class="collapse navbar-collapse" id="navbarNav">
    <ul class="navbar-nav">
      <li class="nav-item active">
        <a class="nav-link disabled" href="/">Home <span class="sr-only">(current)</span></a>
      </li>
      <li class="nav-item">
        <a class="nav-link" href="#education">Education</a>
      </li>
      <li class="nav-item">
        <a class="nav-link" href="#work-experience">Work Experience</a>
      </li>
      <li class="nav-item">
        <a class="nav-link" href="#hobbies-in-life">Hobbies in life</a>
      </li>
      <li class="nav-item">
        <a class="nav-link" href="#my-social-media">My Social Media</a>
      </li>
    </ul>
  </div>
</nav>
""", unsafe_allow_html=True)

#####################
# Custom function for printing text
def txt(a, b):
  col1, col2 = st.columns([4,1])
  with col1:
    st.markdown(a)
  with col2:
    st.markdown(b)

def txt2(a, b):
  col1, col2 = st.columns([1,4])
  with col1:
    st.markdown(f'`{a}`')
  with col2:
    st.markdown(b)

def txt3(a, b):
  col1, col2 = st.columns([1,2])
  with col1:
    st.markdown(a)
  with col2:
    st.markdown(b)


#####################
# EDUCATION
st.markdown('''
## **Education**
''')

col1, col2, col3 = st.columns(3)

with col1:
   st.image("skuyla3.jpg") 

with col2:
   st.image("skuyla2.jpg")

with col3:
   st.image("skuyla1.jpg")

txt('**First year Engineer Student** (Computer Egineer) , SNSU , Phillippines'  ,
'2023 - 2024 ')
st.markdown('''
- Graduated in 2021 Sr. High School with the strand **Information and Communication Technology** (ICT) at **STI COLLEGE SURIGAO**.
- 2015 - 2019 **SURIGAO CITY NATIONAL HIGH SCHOOL**.
- 2009 - 2015 **SURIGAO WEST CENTRAL ELEMENTARY SCHOOL**.
''')

image = Image.open('me.jpg')
st.image(image, caption = "While waiting to our Instructor, Sandyr is very comfortable sleeping HAHAHA", 
width=700)

#####################
# WORK EXPERIENCE
st.markdown('''
## **Work Experience**
''')

col1, col2, col3 = st.columns(3)

with col1:
   st.image("zabeth3.jpg") 

with col2:
   st.image("zabeth1.jpg")

with col3:
   st.image("zabeth2.jpg")

txt('**Waiter,  Zabeth Grill House**, Narciso St. Surigao City, Phillippines',
'2021-2022')
st.markdown('''
- Meeting the needs of the customers and offering excellent customer service. 
- Receiving and completing orders from customers and addressing feedback from them in a positive manner. 
- Frequent Cleanup.
''')
image = Image.open('partime.jpg')
st.image(image, caption = "First day of Working part time", 
width=700)

txt('**Griller**, IvyMore Bbq House @GFoodpark, Surigao City',
'2023')
st.markdown('''
- I'm always ready for every order, I managed and organized everything especially the stocks so I can serve my customer without complaint.
- I show love in grilling to add beautiful taste.
- When I'm grilling I always make sure that the bbq is well cooked inside, also in the outside, I will make it sure that it is not overcooked. 
- Every customer the only request they want for their food is well done because "Malasado" type of food is delicious.
''')

image = Image.open('griller.jpg')
st.image(image, caption = "IVY MORE BBQ HOUSE @GFOOD PARK ", 
width=700)

#####################
# HOBBIES IN LIFE
st.markdown('''
## **Hobbies in life**
''')

st.write("These are my hobbies that makes me happy and filled.") 
st.write("**Basketball** is my very first hobby. I started playing it when I am 8 years Old, my older cousin inspire me to play basketball cause every time I watch his game he play very good, and he is my first idol, and that time I'm inspired because of him, that is why I started my training, working out my dribbles, doing drills, and practicing my shooting. After that, I got interested in basketball try outs at my school when I was elementary and that is my very first try out, I'm about a 6th grader that time, and my age is 12yrs Old. After our try out I didn't know my coach like the way I played and he said that he will put me in a point guard position and then I feel so amazed and happy. In the opening of the tournament our first game is my team SWCES against MEMCES and we got our first win. That day the strongest team that time is SCPS and Cvdiez and we only got the 3rd place spot, not bad for a first timer hahaha . After I graduated elementary, I continued my Basketball journey in Surigao City National High School, and We won so many championship at Mayor's cup tournament, that is because of the coach system is good and the players is very dedicated in practice, we always practicing almost everyday. In my 9th grade in jr high school, I finished my basketball career because my mother got so angry cause I have a low average in mathematics so I decided to stop being a varsity player.  ")

video_file = open('bball.mp4', 'rb')
video_bytes = video_file.read()

st.video(video_bytes)
st.write('that last play is me :D')

st.title("Hobbies are great distractions from the worries and troubles that plague daily living, - Bill Malone")

#####################
# FREEDIVING
st.markdown('## **Freediving**', unsafe_allow_html=True)
st.write("**“Freediving is like meditation. It's a connection with the sea, with yourself, and with your own limits.”** - Guillaume Néry.")
col1, col2, col3 = st.columns(3)

with col1:
   st.image("GOPR1715.png") 

with col2:
   st.image("GOPR1716.png")

with col3:
   st.image("GOPR1746.png")

st.write("Freediving is one of my best experience in life, it helps me to relieve my stress and anxiety.I'll never forget the very first moments of my freediving training. One of my closed friend stephen help me and trained me well that time, MGCQ moments hahaha. Freediving has also benefits in our body it will strengthens your lungs and it improves your fitness level and flexibility, and again It is a great experience cause when you are about to dive you will find peace in the underwater world and see the beauty of sea creatures, and it's a peace of mind. ")

#####################
# IMAGE GALLERY
col1, col2, col3 = st.columns(3)

with col1:
   st.image("ako.jpg") 

with col2:
   st.image("IMG20230205202523.jpg")

with col3:
   st.image("kenan.jpg")
st.write("Surround yourself with what you love, whether it is family, pets, keepsakes, music, plants, hobbies, whatever. - George Carlin")

st.write("**My Band MENACE**")
image = Image.open('myband.jpg')
st.image(image, caption = "MENACE at Paburock 2.0 last september 8 @Surigao City  Boulevard ", 
width=700)

#####################
# MY INFLUENCE IN MUSIC
st.markdown('## **My Influence in Music**', unsafe_allow_html=True)

col1, col2, col3 = st.columns(3)

with col1:
   st.header("Soul Adventurer")
   st.image("franco.jpg")

with col2:
   st.header("Moviente Comp.")
   st.image("Capture.png")

with col3:
   st.header("Neck Deep Band")
   st.image("Life's_Not_Out_to_Get_You.jpg")

#####################
# FRANCO BAND
st.markdown('''
## **My most-like Band FRANCO PH**
''')
image = Image.open('islaw.jpg')
st.image(image, caption = "Franco concert in Surigao City Last October 21, 2023 @GFoodpark", 
width=700)


st.markdown('''
## **My Social Media**
''')
txt2('Facebook', 'https://www.facebook.com/kenankier')
txt2('Twitter', 'https://twitter.com/kenankier')
txt2('Instagram', 'https://www.instagram.com/knankier/')
txt2('Youtube', 'https://www.youtube.com/channel/UCt96rNS-eHtJYW7UKl6qC1g/')
