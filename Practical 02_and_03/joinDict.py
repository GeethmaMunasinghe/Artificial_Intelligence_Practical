dict1={'Jessa':70,'Arul':80,'Emma':55}
dict2={'Kelly':68,'Harry':50,'Olivia':66}

dict1.update(dict2)
print(dict1)

student_dict1={'Aadya':1,'Arul':2}
student_dict2={'Harry':5,'Olivia':6}
student_dict3={'Nancy':7,'Perry':9}

student_dict={**student_dict1,**student_dict2,**student_dict3}
print(student_dict)