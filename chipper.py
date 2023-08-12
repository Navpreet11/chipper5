import streamlit as st
import pyrebase
from datetime import datetime
from streamlit_option_menu import option_menu
from PIL import Image
import requests
import streamlit.components.v1 as components
import random
import json
from io import BytesIO
import feedparser
import urllib.request
from datetime import datetime,timedelta
import uuid
import ast 
#streamlit=1.24.0
#on streamlit cloud streamlit=1.16.0
#current version changed to streamlit=1.16.0 from streamlit=1.24.0











logot=Image.open("logo.png")

st.set_page_config(page_title="Chipper",page_icon=logot)





hide_streamlit_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;
            #GithubIcon{visiblity:hidden;};
            </style>
            """
st.markdown(hide_streamlit_style, unsafe_allow_html=True)



st.markdown("<center><img src=https://img.icons8.com/fluency/500/soulseek.png; alt=centered image; height=200; width=200> </center>",unsafe_allow_html=True)

textcolor= """
    <style>
    .gradient-text{
        background: linear-gradient(to left,#3CCBF4,#2DB4EC,#20A2E6);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        font-family:serif;font-weight: 800;font-style:italic;color:#1A6DFF;text-align:center;font-size:40px;
    }
    </style>
    """
st.markdown(textcolor,unsafe_allow_html=True)

st.markdown('<p class="gradient-text">Chipper</p>', unsafe_allow_html=True)


button_style = '''
    <style>
        .stButton button {
            background: linear-gradient(to left,#3CCBF4,#2DB4EC,#20A2E6);
            color: #FFFFFF; 
            border-color:#2DB4EC; 
        }
    </style>
'''


st.markdown(button_style, unsafe_allow_html=True)
st.markdown('<style>.stButton>button { margin-left: auto; margin-right: auto; display: block; }</style>', unsafe_allow_html=True)




textcolor= """
    <style>
    .textlogin{
        background: linear-gradient(to left,#3CCBF4,#2DB4EC,#20A2E6);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        font-family:serif;font-style:italic;color:#1A6DFF;text-align:left;font-size:30px;
    }
    </style>
    """
st.markdown(textcolor,unsafe_allow_html=True)


textcolor= """
    <style>
    .text{
        background: linear-gradient(to left,#3CCBF4,#2DB4EC,#20A2E6);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        font-family:serif;font-style:italic;color:#1A6DFF;text-align:center;font-size:30px;
    }
    </style>
    """
st.markdown(textcolor,unsafe_allow_html=True)




firebaseConfig = {
  "apiKey": "AIzaSyCz8xHkd4OccY4QyRXU57Wnx8HLzxNOpnY",
  "authDomain": "chipper-a5095.firebaseapp.com",
  "projectId": "chipper-a5095",
  "storageBucket": "chipper-a5095.appspot.com",
  "messagingSenderId": "1003706768195",
  "databaseURL": "https://chipper-a5095-default-rtdb.firebaseio.com/",
  "appId": "1:1003706768195:web:c748d7c2da028df40e2df6",
  "measurementId": "G-11SV8D1MSZ"
}

firebase= pyrebase.initialize_app(firebaseConfig)

auth=firebase.auth()

data=firebase.database()
storage=firebase.storage()


textcolor= """
    <style>
    .holdertext{
        background: linear-gradient(to left,#3CCBF4,#2DB4EC,#20A2E6);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        font-family:serif;font-style:italic;color:#1A6DFF;text-align:left;font-size:30px;
    }
    </style>
    """
st.markdown(textcolor,unsafe_allow_html=True)
       

textcolor= """
    <style>
    .holdertexts{
        background: linear-gradient(to left,#3CCBF4,#2DB4EC,#20A2E6);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        font-family:serif;font-style:italic;color:#1A6DFF;text-align:center;font-size:25px;
    }
    </style>
    """
st.markdown(textcolor,unsafe_allow_html=True)

streamlitstyle = """
			<style>
			sidebar,body,[class*="css"]{background-image: url("https://thepythoncodingbook.com/wp-content/uploads/2021/09/orbiting_planets_in_solar_system_using_python.jpg");
                        background-attachment: fixed;
                        background-size: cover 
			
			
                       
			
			
                        }
			</style>
			"""



#st.markdown(streamlitstyle, unsafe_allow_html=True)

font_css = """
<style>
button[data-baseweb="tab"] > div[data-testid="stMarkdownContainer"] > p {
  font-size: 20px;
  padding:10px
}
</style>
"""
st.write(font_css, unsafe_allow_html=True)

placeholder=st.empty()
with placeholder.container():

     st.markdown(f"___")
     st.markdown("<p class='holdertext'>Welcome to Chipper </p>", unsafe_allow_html=True)
     st.markdown(f"___")
     st.markdown("<p class='holdertext'>You can use Chipper to :</p>", unsafe_allow_html=True)
     #st.markdown("<p class='holdertexts'>👉 See the post's of various user's</p>", unsafe_allow_html=True)
     st.markdown("<p class='holdertexts'>👉 Stay in touch with world</p>", unsafe_allow_html=True)
     st.markdown("<p class='holdertexts'>👉 Engage in topics which matter's to you</p>", unsafe_allow_html=True)
     st.markdown("<p class='holdertexts'>👉 Share your thought's with world</p>", unsafe_allow_html=True)
     st.markdown("<p class='holdertexts'>👉 Customize your profile</p>", unsafe_allow_html=True)
     st.markdown(f"___")
     st.markdown("<p class='holdertext'>Join chipper today and experience a new way to connect with other's</p>", unsafe_allow_html=True)
     

st.sidebar.markdown("<p class='holdertext'>Login or Register :</p>", unsafe_allow_html=True)
choice=st.sidebar.selectbox("",["Login","Register"])



email=st.sidebar.text_input("",placeholder="Email")
passw=st.sidebar.text_input("",placeholder="Password",type="password")

if choice=="Register":
    
    handle=st.sidebar.text_input("",placeholder="Username")
    subbt=st.sidebar.button("Register now !")

    if subbt:
        if not email or not passw or not handle:
            st.sidebar.error("Please enter your full credentials !")
        else:
            try:
                user=auth.create_user_with_email_and_password(email,passw)
                user=auth.sign_in_with_email_and_password(email,passw)
                data.child(user["localId"]).child("Handle").set(handle)
                data.child(user["localId"]).child("ID").set(user["localId"])
                st.sidebar.success("Account created you may login now !")
            except:
                 st.sidebar.error("Invalid email or user already exist's")
if choice=="Login":
   
    signin=st.sidebar.checkbox("Login")
    if signin:
        if not email or not passw :
            st.sidebar.error("Please enter your full credentials !")
        else:
            try:
                placeholder.empty()
                user=auth.sign_in_with_email_and_password(email,passw)
               
          
                nav = option_menu(menu_title=None,   options=["", " ","    ", "   ","  "],icons=["house-fill","search","pencil-square","gear-fill","person-fill"],menu_icon="cast",default_index=0,orientation="horizontal",styles={
        "container": {"padding": "0!important", "background":"linear-gradient(to left,#3CCBF4,#2DB4EC,#20A2E6)"},
        "icon": {"color": "black", "font-size": "20px"}, 
        "nav-link": {"text-align":"left", "margin":"1px", "--hover-color": "#1c1c1c"},
        "nav-link-selected": {"background-color": "lightblue","color":"#1c1c1c"},})
                if nav=="":
                     st.subheader("🏠 Home :")
                     
                     all_user_posts_response = data.get("Posts")
                     all_user_posts = all_user_posts_response.val()
                    

                     if all_user_posts is not None:
                          reversed_users = list(reversed(list(all_user_posts.items())))
                          
                          for post_id, post_content in all_user_posts.items():
                               if "Posts" in post_content:
                                   
                                 
                                    posts_data = list(post_content["Posts"].items())[::-1]
                                    for post_id,post_info in posts_data:
                                         
                                         
                                          st.success(post_info)
                                          st.markdown(f"___")
                                        
                                   
                                         
                     #st.markdown("<center><h1>⚠️</h1>  </center>",unsafe_allow_html=True)
                     #st.warning("Sorry this page is currently under construction")
                    #st.components.v1.html('<center><iframe src="https://giphy.com/embed/hV1dkT2u1gqTUpKdKy" frameBorder=0></iframe><center>', width=800, height=800)

                elif nav=="    ":
                      st.subheader("Share a Thought or Pic :")
                      st.markdown(f"___")
                      
                      tab1,tab2 = st.tabs(["📝 Share a thought","📷 Share a pic "])
                      with tab1:
                           
                          
                         
                          post=st.text_input("",placeholder="Share your thought with the world",max_chars=400)
                          add_post=st.button("Share your thought")
                          if add_post:
                               if not post:
                                    st.error("Please enter your thought")
                               else:
                                    now=datetime.now()
                                    dt=now.strftime("%d / %m / %y")
                                    dtt=now.strftime("%I:%M %p")
                                    post=post + " ; "  +  "  shared on :" + dt + "  at  " + dtt
                                    results=data.child(user["localId"]).child("Posts").push(post)
                                    st.success("Thought shared successfully")
                      with tab2:
                           
                         
                          
                          caption = st.text_input("",placeholder="Add a caption to your pic")
                          expan=st.expander("Share your pic")
                          with expan:
                               image = st.file_uploader("", type=["jpg", "jpeg", "png","mp3"])
                               if image is None:
                                    st.warning("Please select an pic")
                               upbta=st.button("Share the pic and caption")
                               if upbta:
                                   with st.spinner("Uploading image..."):
                                        storage.child("images/" + image.name).put(image)
                                        post_data = {"caption": caption,"image_url": storage.child("images/" + image.name).get_url(None) }
                                        data.child(user["localId"]).child("posts").push(post_data)
                                        st.success("Pic shared successfully")

                     

                     
                     
                              
                               
                     

                     
                                                     
                     
                      
                                
                elif nav==" ":
                     allu=data.get()
                     resa=[]
                     for ush in allu.each():
                          k=ush.val().get("Handle")
                          resa.append(k)
                     n = len(resa)
            
                     st.subheader("🔍 Search :")
                     cho = st.selectbox('',resa)
                     pusha = st.button('Show Profile')

                     if pusha:
                          for ush in allu.each():
                              k=ush.val().get("Handle")
                              if k==cho:
                                   l=ush.val().get("ID")
                              
                                   userdata=data.child(l).child("Handle").get().val()
                                  
                                   
                         
                                   st.markdown(f"___")
                           
                                   nimg=data.child(l).child("Image").get().val()
                                   if nimg is not None:
                                        v=data.child(l).child("Image").get()
                                        for img in v.each():
                                             imgc=img.val()
                                    
                                        st.markdown(f'<div style="display: flex; justify-content: center;"><img src="{imgc}" width="200" height="200" style="border-radius:50%;"></div>', unsafe_allow_html=True)
                       
                                   else:
                                        st.markdown(f'<div style="display: flex; justify-content: center;"><img src="https://img.icons8.com/fluency/500/user-male-circle.png" width="200" height="200"  style="border-radius:50%;"></div>', unsafe_allow_html=True)
                                   st.markdown(f'<div style="display: flex; justify-content: center;"><h2>{userdata}</h2></div>',unsafe_allow_html=True)
                         
                                   st.subheader("Bio :")
                                   
                                   bio=data.child(l).child("Bio").get().val()
                                   if bio is not None:
                                        bioinfo=data.child(l).child("Bio").get()
                                        for bio in bioinfo.each():
                                             bioc=bio.val()
                                        st.info(bioc)
                                             
                                   else:
                                        st.info("No Bio  till now !")


                                   tab5,tab6=st.tabs(["💭 Thought's","📷 Pic's"])

                                   with tab5:
                                        all_posts=data.child(l).child("Posts").get()
                                        if all_posts.val() is not None:
                                             for Posts in reversed(all_posts.each()):
                                                  st.success(Posts.val())
                                        else:
                                             st.info("No thought's  till now !")
                                   with tab6:
                                        posts=data.child(l).child("posts").get()
                                        if  posts.val() is not None:
                                             for Posts in posts.each():
                                                  caption = Posts.val()["caption"]
                                                  image_url = Posts.val()["image_url"]
                                                  st.success(caption)
                                                  response = requests.get(image_url)
                                                  img = Image.open(BytesIO(response.content))
                                                  st.image(img, use_column_width=True)
                                                  st.markdown(f"___")
                                        else:
                                             st.info("No pic's  till now !")
                                            
                                

                            
                                
                     
               
                  

                  
                   
                elif nav=="  ":
                     
                     
                     
                     nimg=data.child(user["localId"]).child("Image").get().val()
                     if nimg is not None:
                          v=data.child(user["localId"]).child("Image").get()
                          for img in v.each():
                               imgc=img.val()
                          st.markdown(f'<div style="display: flex; justify-content: center;"><img src="{imgc}" width="200" height="200" style="border-radius:50%;"></div>', unsafe_allow_html=True)
                          userdata=data.child(user['localId']).child("Handle").get().val()
                          st.markdown(f'<div style="display: flex; justify-content: center;"><h2>{userdata}</h2></div>',unsafe_allow_html=True)
                     else:
                          st.markdown(f'<div style="display: flex; justify-content: center;"><img src="https://img.icons8.com/fluency/500/user-male-circle.png" width="200" height="200"  style="border-radius:50%;"></div>', unsafe_allow_html=True)
                    
                          userdata=data.child(user['localId']).child("Handle").get().val()
                          #st.header(userdata)
                          st.markdown(f'<div style="display: flex; justify-content: center;"><h2>{userdata}</h2></div>',unsafe_allow_html=True)
                         
                         
                     st.subheader("Bio :")
                     bio=data.child(user["localId"]).child("Bio").get().val()
                     if bio is not None:
                        bio=data.child(user["localId"]).child("Bio").get()
                        for bio in bio.each():
                            bioc=bio.val()
                        st.info(bioc)

                        
                      
                        
                     else:
                          st.info("No Bio  till now !")
                          
                 #["chat-left-fill","camera-fill"]
                     tab3,tab4=st.tabs(["💭 Thought's","📷 Pic's"])
                     with tab3:
                         
                        
                         
                         all_posts=data.child(user['localId']).child("Posts").get()
                        
                         if all_posts.val() is not None:
                              for Posts in reversed(all_posts.each()):
                                   st.success(Posts.val())
                                   if st.button("🗑 Double tap to delete this thought ",key=f"Delete_({Posts.key()})"):
                                        data.child(user["localId"]).child("Posts").child(Posts.key()).remove()
                                   st.markdown(f"___")
                                   
                         else:
                            st.info("No thought's  till now !")
                            st.markdown(f"___")
                     with tab4:
                         posts=data.child(user['localId']).child("posts").get()
                        
                        
                         
                         if  posts.val() is not None:
                              for Posts in posts.each():
                                   caption = Posts.val()["caption"]
                                   image_url = Posts.val()["image_url"]
                                   st.success(caption)
                                   response = requests.get(image_url)
                                   img = Image.open(BytesIO(response.content))
                                   st.image(img, use_column_width=True)
                                   st.markdown(f"___")
                         else:
                              st.info("No pic's  till now !")
                              st.markdown(f"___")
                     
                    
                         

                            
                     
                         
                                    

                     
                     
                elif nav=="   ":
                     nimg=data.child(user["localId"]).child("Image").get().val()
                     if nimg is not None:
                          Image=data.child(user["localId"]).child("Image").get()
                          for img in Image.each():
                               imgc=img.val()
                          st.markdown(f'<div style="display: flex; justify-content: center;"><img src="{imgc}" width="200" height="200" style="border-radius:50%;"></div>', unsafe_allow_html=True)
                          expa=st.expander("👤 Change your profile pic")
                          with expa:
                               st.subheader("📷 Choose your profile pic :")
                               newimgp=st.file_uploader("")
                               upbt=st.button("Upload profile pic")
                               
                               if upbt:
                                    uid=user["localId"]
                                    dataup=storage.child(uid).put(newimgp,user["idToken"])
                                    aimgdata=storage.child(uid).get_url(dataup["downloadTokens"])

                                    data.child(user["localId"]).child("Image").push(aimgdata)
                                    
                                    
                               

                                    st.info("profile pic set successfully !")
                          if st.button("🗑 Double tap to remove your profile pic"):
                                    data.child(user["localId"]).child("Image").remove()
                               
                                 
                     else:
                                st.markdown(f'<div style="display: flex; justify-content: center;"><img src="https://img.icons8.com/fluency/500/user-male-circle.png" width="200" height="200"  style="border-radius:50%;"></div>', unsafe_allow_html=True)
                                st.subheader("📷 Choose your profile pic :")
                                newimgp=st.file_uploader("")
                                upbt=st.button("Upload profile pic")
                                if upbt:
                                    uid=user["localId"]
                                    dataup=storage.child(uid).put(newimgp,user["idToken"])
                                    aimgdata=storage.child(uid).get_url(dataup["downloadTokens"])
                                    data.child(user["localId"]).child("Image").push(aimgdata)
                     st.markdown(f"___")
                     st.subheader("🪪 Update your Bio :")
                     bio=data.child(user["localId"]).child("Bio").get().val()
                     if bio is not None:
                        bio=data.child(user["localId"]).child("Bio").get()
                        for bio in bio.each():
                            bioc=bio.val()
                        st.info(bioc)
                        
                        bioin=st.text_area("",placeholder="Enter your Bio to be uploaded eg: name,date of birth etc")
                        upbtn=st.button("Upload Bio")

                        if upbtn:
                           
                            

                            data.child(user["localId"]).child("Bio").push(bioin)

                            st.info("Bio set successfully !")
                            st.balloons()
                    
                     else:
                        st.info("No Bio till now !")
                        bioin=st.text_area("",placeholder="Enter your Bio to be uploaded eg: name,date of birth etc")
                        upbtn=st.button("Upload Bio")

                        if upbtn:
                           
                           
                            data.child(user["localId"]).child("Bio").push(bioin)

                            st.info("Bio set successfully !")
                    
                           


                    
                              
                                 
                       
                 
                     
            except:
                 st.sidebar.error("Invalid email or password !")
               
                 



