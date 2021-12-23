#%%
###import packages


import streamlit as st
import streamlit.components.v1 as components
import smtplib
import  random as r
import re
import time
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders

#%%
st.set_page_config(layout="wide")




with st.beta_container():
 #navbar 
#https://bootsnipp.com/snippets/nNX3a     https://www.mockplus.com/blog/post/bootstrap-navbar-template
   components.html(
       """
       <link href="//maxcdn.bootstrapcdn.com/bootstrap/4.1.1/css/bootstrap.min.css" rel="stylesheet" id="bootstrap-css">
<script src="//maxcdn.bootstrapcdn.com/bootstrap/4.1.1/js/bootstrap.min.js"></script>
<script src="//cdnjs.cloudflare.com/ajax/libs/jquery/3.2.1/jquery.min.js"></script>
<!------ Include the above in your HEAD tag ---------->

<nav class="navbar navbar-icon-top navbar-expand-lg navbar-dark bg-dark" >
  <a class="navbar-brand" href="https://www.rstiwari.com">Profile</a>
  <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarSupportedContent" aria-controls="navbarSupportedContent" aria-expanded="false" aria-label="Toggle navigation">
    <span class="navbar-toggler-icon"></span>
  </button>

  <div class="collapse navbar-collapse" id="navbarSupportedContent">
    <ul class="navbar-nav mr-auto">
      <li class="nav-item active">
        <a class="nav-link" href=" https://tiwari11-rst.medium.com/">
          <i class="fa fa-home"></i>
          Medium
          <span class="sr-only">(current)</span>
          </a>
      </li>
      <li class="nav-item">
        <a class="nav-link" href=" https://happyman11.github.io/">
          <i class="fa fa-envelope-o">
            <span class="badge badge-danger">Git Pages</span>
          </i>
         
        </a>
      </li>
      
        <li class="nav-item">
        <a class="nav-link" href="https://happyman11.github.io/">
          <i class="fa fa-globe">
            <span class="badge badge-success">Badges</span>
          </i>
         
        </a>
      </li>
          
        </a>
      </li>
      
      <li class="nav-item">
        <a class="nav-link disabled" href="https://ravishekhartiwari.blogspot.com/">
          <i class="fa fa-envelope-o">
            <span class="badge badge-warning">Blogspot</span>
          </i>
          
        </a>
      </li>
      
      
    </ul>
  
    
  </div>
</nav>
       """, height=70,
    )


# Text/Title

with st.beta_container():
    col4, col5, col6 = st.beta_columns([2,5,1])

    with col5:
        st.title("Centralised Applications")


with st.beta_container():
    
    col7, col8, col9 = st.beta_columns([2,6,1])
    with col8:
        st.header("Recieve Application's url's via Mail ")
   
with st.beta_container():
     
     col10, col11, col12 = st.beta_columns([2,4,3])   
     with col11:
         Email= st.text_input("Email","Type  here...")
        
    
    
with st.beta_container():
     
     col10, col11, col12 = st.beta_columns([4,5,1])   
     with col11:
         Submitted=st.button("Mail")
         

   
       
    
       


#function

def otpgen():
    otp=""
    for i in range(6):
        otp+=str(r.randint(1,9))
    return (otp)

def send_otp(email,otp):
    
    msg = MIMEMultipart()
    msg['From'] = "DeployedApplications@gmail.com"
    msg['Subject'] = "Verification for Centralised Applications by Ravi Shekhar Tiwari"
    msg['To'] = email
    passd="Ravishekhar@11"

    s = smtplib.SMTP('smtp.gmail.com',465) 
    s.starttls() 
    s.login(msg['From'], passd) 
    message_body="""\
<html>
  <body>
    <p>Hi """+email+""",</p>
        
       <h2> Thank you for accessing this application. Please find the below verification code to aceess the application </h2> 
       
       <p style="padding-bottom:25;">
       <h2> <blockquote> Otp : """+otp+"""</blockquote></h2>
       </p>
      
       <b>Regards</b>,<br>
       Ravi Shekhar Tiwari<br>
       Website: https://www.rstiwari.com<br>
       Email: tiwari11.rst@gmail.com <br>
    

  </body>
</html>
"""
    #filename = "Resourse_Artificial Intelligence.pdf"
    #attachment = open("./Resourse_Artificial Intelligence.pdf", "rb") 
   # p = MIMEBase('application', 'octet-stream')
   # p.set_payload((attachment).read()) 
   # encoders.encode_base64(p)
   # p.add_header('Content-Disposition', "attachment; filename= %s" % filename)
   # msg.attach(p) 


    msg.attach(MIMEText(message_body, 'html'))
    s.login(msg['From'], passd) 
    s.sendmail(msg['From'], msg['To'], msg.as_string()) 
    s.quit()  


def check(email):  
  
    regex = '^[a-zA-Z0-9.!#$%&*+/=?^_`{|}~-]+@[a-zA-Z0-9-]+(?:\.[a-zA-Z0-9-]+)*$'
    if(re.search(regex,email)):  
        return(True)       
    else:  
        return(False)  


def send_mail(email):
    
    msg = MIMEMultipart()
    msg['From'] = "DeployedApplications@gmail.com"
    msg['Subject'] = "Link of Applications"
    msg['To'] = email
    passd="Ravishekhar@11"

    s = smtplib.SMTP('smtp.gmail.com', 465) 
    s.starttls() 
    s.login(msg['From'], passd) 
    message_body="""\
<html>
  <body>
    <p>Hi """+email+""",</p>
        
       <h2> Thank you for accessing this application. Please see the below mentioned url's. </h2> 
       
       <p style="padding-bottom:25;">
    
       <dt>1. <b>Link of Deployed Applications </b></dt>
       
       <p style="padding-top:15;">
       <dd>1.1 <a href="https://share.streamlit.io/happyman11/mnist-svm-streamlit">SVM-Mnist Classification</a></dd>
       <dd>1.2. <a href="https://share.streamlit.io/happyman11/logistic_regression_streamlit_sklearn_dataset">Logistic Regression on sklearn Dataset</a> </dd>
       <dd>1.3. <a href="https://rstiwarisampledeploy.herokuapp.com">Iris Decision Tree Classification</a> </dd>
       <dd>1.4. <a href="https://penguing-prediction-streamlit.herokuapp.com/">Penguine Island Classification</a> </dd>
       <dd>1.5. <a href="https://webscrappingsample.herokuapp.com/">Web Scrapping Sample</a> </dd>
       <dd>1.6. <a href="https://happyman11.github.io/foodorder.github.io/">Food ordering Website</a> </dd>
       <dd>1.7. <a href="https://prisondashboard.herokuapp.com/">Prison Data Analysis Dashboard using Dash and Plotly</a> </dd>
       <dd>1.8. <a href="#">Mass/Bulk mailing Platform</a> </dd>
       
       </p>
       </p>
       
       
       <p style="padding-bottom:25;">
       
       <dt>2. <b>Medium Blog  </b></dt>
       <p style="padding-top:15;">
       <dd>1. <a href="https://tiwari11-rst.medium.com/">Medium</a> </dd>
       </p>
       </p>
      
       <p style="padding-bottom:25;">
       <dt>3. <b>Youtube </b></dt>
       <p style="padding-top:15;">
       <dd>1. <a href="https://www.youtube.com/channel/UCFG5x-VHtutn3zQzWBkXyFQ">Youtube Channel</a> </dd>
       </p>
       </p>
   
       <p style="padding-bottom:25;">
       <dt>4. <b>Find Me</b></dt>
       <p style="padding-top:15;">
       <dd>1. <a href="https://www.rstiwari.com">Profile</a> </dd>
       <dd>2. <a href="https://tiwari11-rst.medium.com">Medium</a> </dd>
       <dd>3. <a href="https://happyman11.github.io/">Github Pages</a> </dd>
       <dd>4. <a href="https://forms.gle/mhDYQKQJKtAKP78V7"> Find me</a> </dd>
       
       </p>
       </p>
   
       <p tyle="padding-bottom:25;padding-bottom:15;">
       <a href="https://tiwari11-rst.medium.com/subscribe">
       <h2 style="color:black;"> Subscribe Medium Blog !!!!!</h2>
       <blockquote> 
       <h3 style="color:green;"> Click Here for Subscribing </h3>
       </blockquote> 
       </a>
       
       </p>
       
     
       <p> For Unsubscribe, please send mail to DeployedApplications@gmail.com  with subject  Unsubscribe from medium </p>
       <br>
      
       <b>Regards</b>,<br>
       Ravi Shekhar Tiwari<br>
       Website: https://www.rstiwari.com<br>
       Email: tiwari11.rst@gmail.com <br>
    

  </body>
</html>
"""
    #filename = "Resourse_Artificial Intelligence.pdf"
    #attachment = open("./Resourse_Artificial Intelligence.pdf", "rb") 
   # p = MIMEBase('application', 'octet-stream')
   # p.set_payload((attachment).read()) 
   # encoders.encode_base64(p)
   # p.add_header('Content-Disposition', "attachment; filename= %s" % filename)
   # msg.attach(p) 


    msg.attach(MIMEText(message_body, 'html'))
    s.login(msg['From'], passd) 
    s.sendmail(msg['From'], msg['To'], msg.as_string()) 
    s.quit()  




def otp_match(sent_otp,typed):
    typed=int(Otp_typed)
    mailed=int(sent_otp)
   
    st.write (typed)
    st.write (mailed)
    
if(Submitted):

    if (check(Email)):
        send_mail(Email)
   
        my_bar = st.progress(0)
        for percent_complete in range(100):
            time.sleep(0.05)
            my_bar.progress(percent_complete + 1)

        time.sleep(3)
        st.success("Check your Email if not found on Inbox check spam") 
                      
                                      
    else:
       st.error("Ooops!!! Incorrect Email..Try again")
       
 



         
    #medium
  #
#with st.beta_container():
  
   
 #  components.html(
 #      """
 #      <div style="border: double;">
 #      <h2>&nbsp &nbsp &nbsp  &nbsp   &nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp
#  Articles </h2>
 #      </div>
 #      <div style="border: 1px solid black;"id="medium-widget"></div>
 #   <script src="https://medium-widget.pixelpoint.io/widget.js"></script>
 #   <script>MediumWidget.Init({renderTo: '#medium-widget', params: {"resource":"https://medium.com/@tiwari11-rst","postsPerLine":3,"limit":4,"picture":"big","fields":["description","author","claps","publishAt"],"ratio":"landscape"}})</script>
 #   </div>""",
 #   width=1200, height=500,
 #   )
#  #footer

with st.beta_container():
    components.html(
     """
     <div style="position: fixed;
   left: 0;
   bottom: 0;
   width: 100%;
   background-color: black;
   color: white;
   text-align: center;">
  <p>Ravi Shekhar Tiwari</p>
</div>
     """,height=140,)
