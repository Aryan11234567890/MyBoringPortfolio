from PIL import Image
import requests
import os
import streamlit as st
from streamlit_lottie import st_lottie
st.set_page_config(page_title='ba bum ba bum!!!!!', page_icon='🧑‍💻', layout = 'wide')

def animate(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

def styleLocal(fileName):
    with open(fileName) as f:
        st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html = True)

# styleLocal('style\style.css')
current_dir = os.path.dirname(os.path.abspath(__file__))
style_path = os.path.join(current_dir, 'style', 'style.css')
styleLocal(style_path)

animation_gif = animate('https://lottie.host/eb0e538c-fdaf-41c7-9a25-01a1f6787f6e/kix6FcrWy9.json')
profile_gif = animate('https://lottie.host/c16d3e93-c203-4b56-a9fe-c4d1c2db1606/AtmAZu87xX.json')

# img_django_react = Image.open('images\djangoreact.png')
# img_django = Image.open('images\django.png')

img_django_react = Image.open(os.path.join(current_dir, 'images', 'djangoreact.png'))
img_django = Image.open(os.path.join(current_dir, 'images', 'django.png'))
img_devd = Image.open(os.path.join(current_dir, 'images', 'logo.png'))


with st.container():
    lc, rc = st.columns(2)
    with lc:
        st.subheader('Ayo fellas, It is me hehehehhe !!!!!')
        st.title('Aryan Shanker Saxena')
        st.write('Random coder who also plays games and touches grass!! I love Mathematics and Computer Science. Mostly I just love to solve things using Mathematics and Computers are the best way to express your mathematical fantasies and creations')
        st.write('[MY RESUME!](https://drive.google.com/file/d/14sx4U8EP6dXFVAiVF9oI-T3R9mNTze19/view?usp=sharing)')
    with rc:
        st_lottie(profile_gif, height=300, key="coding")
        
with st.container():
    st.write('---')
    lc, rc = st.columns(2)
    with lc:
        st.header('What I do when i dont touch grass...')
        st.write('Play games like Valorant, Counter Strike, PS4 games, code in Python......')
        st.header('What I do when i touch grass...')
        st.write('Play games like Chess (IRL not app), Cricket, Basektball, Football and a lot more......')
    with rc:
        st_lottie(animation_gif, height = 300, key = "gaming")

with st.container():
    st.write('---')
    st.header('''My Tech Stack (I know it is pretty boring but yeah this is what I've got as of now)...''')
    lc, mp, rc = st.columns(3)
    with lc:
        st.write('*Languages (भाषाएँ)*')
        st.write('Python (seh lenge)')
        st.write('C/C++ (isse bhi seh lenge)')
        st.write('HTML/CSS/JavaScript (sirf JS bahut bawaal hai)')
    with mp:
        st.write('*Frameworks*')
        st.write('ReactJS, Streamlit, Django')
        st.write('TensorFlow, Scikit-learn, NumPy, Pandas, Matplotlib, Seaborn')
    with rc:
        st.write('*Databases*')
        st.write('MySQL, PostgreSQL')

with st.container():
    st.write('---')
    st.header('''My projects 🎮🐱‍👤([Visit my github for the full list xD](https://www.github.com/Aryan11234567890). Your avg college grad projects)....''')
    st.write('    ')
    imgc, textc = st.columns((1, 2))
    with imgc:
        st.image(img_django)
        st.write('    ')
        st.write('    ')
        st.write('    ')
        st.write('    ')
        st.image(img_django_react)
        st.write('    ')
        st.write('    ')
        st.write('    ')
        st.write('    ')
        st.image(img_devd)
    with textc:
        st.subheader('Forums and Discussions using Django')
        st.write('A Fullstack website which allows users to login or register, to start a discussion and others can also comment on it. Mini communities can be created within a specific topic called room. Django, oh boy, is an absolute life saver for this project. Backend is so easy to maintain. This made me fall in love with python. Django templates also helped me in eliminating JavaScript, phew. This project helped learning the architecture and the functioning of the Django framework.')
        st.write('    ')
        st.write('    ')
        st.write('    ')
        st.write('    ')
        st.write('    ')
        st.write('    ')
        st.write('    ')
        st.subheader('Notes App using React and Django')
        st.write('''A Fullstack website which allows users to create notes. Yeah, pretty basic I get it. But, I implemented various things in it. Sure, I had to work with JavaScript, but on the backend sided, I used JWT tokens, add some security features and protected routes. I also used the Django rest framework to build the APIs. I mean it is wayyyyyyyyy better than making APIs on Express. Moreover I used PostgreSQL as the database which provided on the Choreo platform. Where it is deployed as of now. To use this website, just contact me because Choreo turns off my database every hour since I'm a free user 😢😢. So I gotta Turn it on every hour. But hey, all in all this project helped me make APIs, Two different languages and their frameworks, Database maintainance, and Deployment. ''')
        st.write('    ')
        st.write('    ')
        st.write('    ')
        st.write('    ')
        st.write('    ')
        st.write('    ')
        st.write('    ')
        st.subheader('Online Coding Judge Platform using Django')
        st.write('A Fullstack website which allows users to login or register, to code and test it against test cases and a get a verdict whether it is accepted or not. Users can improve their coding skills for free!!!!!!!! It is deployed on AWS. Discussions page is under testing and chatbot is under development and they are coming soon!!! ')
        st.write('    ')
        st.write('    ')
        st.write('    ')
        st.write('    ')
        st.write('    ')
        st.write('    ')
        st.write('    ')
with st.container():
    st.write('---')
    st.header('Hit me up! If you have some crazy Ideas or just contact even if you wanna mess with me xD....')
    
    contact = '''
    <form action="https://formsubmit.co/c8937f59b7d70f6f6118711139731565" method="POST">
     <input type='hidden' name='_captcha' value='false'>
     <input type="text" name="name" placeholder='Your Name' required>
     <input type="email" name="email" placeholder='Your Email' required>
     <textarea name='Message' placeholder='Your hopefully fruitful words xD' required></textarea>
     <button type="submit">Send</button>
    </form>
    
    
    '''
    lc, rc = st.columns(2)
    with lc:
        st.markdown(contact, unsafe_allow_html = True)
    with rc:
        st.empty()
    
        
        
        
        
        