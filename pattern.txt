import re 
 
pattern= "^We.*Data$" 

txt = "We love programming with Big Data" 

x = re.search(pattern,txt) 
