def flatten_dict(dd, separator ='.', prefix =''): 
	return { prefix + separator + k if prefix else k : v 

             for kk, vv in dd.items() 

             for k, v in flatten_dict(vv, separator, kk).items() 

             } if isinstance(dd, dict) else { prefix : dd } 

ini_dict = eval(input()) 
print ("final_dictionary",(flatten_dict(ini_dict))) 
