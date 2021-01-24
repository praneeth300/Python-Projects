###Email slicer with python

#An email slicer is a very useful program for separating the username and domain name of an email address.

email=input('Enter your email').strip()
username=email[:email.index("@")]
domain_name=email[email.index("@")+1:]
form=(f"Your username is '{username},Your domain is '{domain_name}")
print(form)