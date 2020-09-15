from tkinter import *
from tkinter.ttk import Combobox
import tkinter.messagebox
from faker import Faker
import tkinter.messagebox
import os
from random import seed




class All_Info:
    def __init__(self,root):
        self.root=root
        self.root.title("Faker")
        self.root.geometry("610x560")
        self.root.iconbitmap("favicon.ico")
        self.root.resizable(0,0)

        items=StringVar()
        langs=StringVar()
        lens=IntVar()



        
        def on_leave1(e):
            But_get['background']="SystemButtonFace"
            But_get['foreground']="SystemButtonText"

        def on_enter1(e):
            But_get['background']="black"
            But_get['foreground']="cyan"
               
               

        def on_leave2(e):
            But_clear['background']="SystemButtonFace"
            But_clear['foreground']="SystemButtonText"
        
        def on_enter2(e):
            But_clear['background']="black"
            But_clear['foreground']="cyan"


        def Get_Info():
            try:

                texttopaste1.delete("1.0",END)
                Item=items.get()
                language=langs.get()
                Range=lens.get()
                filename="C:\\TEMP\\save.txt"
                fake = Faker(language)
                #fake.seed(4321)
                with open("C:\\TEMP\\save.txt","w",encoding="utf-8")as f:  #os.save(filename)  os.remove(filename)
                    for i in range(1,Range+1):
                        if Item=="name":
                            wr=fake.name()
                            f.write(str(i))
                            f.write(":   "+str(wr)+"\n""\n")

                        if Item=="address":
                            w=fake.address()
                            f.write(str(i))
                            f.write(":   "+str(w)+"\n""\n")

                        if Item=="building_number":
                            w=fake.building_number()
                            f.write(str(i))
                            f.write(":   "+str(w)+"\n""\n")


                        if Item=="city":
                            w=fake.city()
                            f.write(str(i))
                            f.write(":   "+str(w)+"\n""\n")

                        if Item=="city_suffix":
                            w=fake.city_suffix()
                            f.write(str(i))
                            f.write(":   "+str(w)+"\n""\n")


                        if Item=="country":
                            w=fake.country()
                            f.write(str(i))
                            f.write(":   "+str(w)+"\n""\n")


                        if Item=="country_code":
                            w=fake.country_code()
                            f.write(str(i))
                            f.write(":   "+str(w)+"\n""\n")


                        if Item=="country_code":
                            w=fake.country_code()
                            f.write(str(i))
                            f.write(":   "+str(w)+"\n""\n")

                        if Item=="postcode":
                            w=fake.postcode()
                            f.write(str(i))
                            f.write(":   "+str(w)+"\n""\n")

                        if Item=="street_address":
                            w=fake.street_address()
                            f.write(str(i))
                            f.write(":   "+str(w)+"\n""\n")

                        if Item=="street_name":
                            w=fake.street_name()
                            f.write(str(i))
                            f.write(":   "+str(w)+"\n""\n")
                        
                        if Item=="street_suffix":
                            w=fake.street_suffix()
                            f.write(str(i))
                            f.write(":   "+str(w)+"\n""\n")








                        if Item=="profile":
                            w=fake.profile()
                            f.write(str(i))
                            f.write(":   "+str(w)+"\n""\n")

                        if Item=="phone_Number":
                            w=fake.phone_number()
                            f.write(str(i))
                            f.write(":   "+str(w)+"\n""\n")

                        if Item=="firstname":
                            w=fake.first_name()
                            f.write(str(i))
                            f.write(":   "+str(w)+"\n""\n")

                        if Item=="first_Female_name":
                            w=fake.first_name_female()
                            f.write(str(i))
                            f.write(":   "+str(w)+"\n""\n")

                        if Item=="first_male_name":
                            w=fake.name_male()
                            f.write(str(i))
                            f.write(":   "+str(w)+"\n""\n")

                        if Item=="paragraph":
                            w=fake.paragraph()
                            f.write(str(i))
                            f.write(":   "+str(w)+"\n""\n")

                        if Item=="text":
                            w=fake.text()
                            f.write(str(i))
                            f.write(":   "+str(w)+"\n""\n")


                        if Item=="words":
                            w=fake.words()
                            f.write(str(i))
                            f.write(":   "+str(w)+"\n""\n")

                        if Item=="jobs":
                            w=fake.job()
                            f.write(str(i))
                            f.write(":   "+str(w)+"\n""\n")

                        if Item=="email":
                            w=fake.email()
                            f.write(str(i))
                            f.write(":   "+str(w)+"\n""\n")

                        if Item=="company_email":
                            w=fake.company_email()
                            f.write(str(i))   
                            f.write(":   "+str(w)+"\n""\n")

                        if Item=="safe_email":
                            w=fake.safe_email()
                            f.write(str(i))   
                            f.write(":   "+str(w)+"\n""\n")

                        if Item=="free_email":
                            w=fake.free_email()
                            f.write(str(i))   
                            f.write(":   "+str(w)+"\n""\n")

                        if Item=="image_url":
                            w=fake.image_url()
                            f.write(str(i))   
                            f.write(":   "+str(w)+"\n""\n")

                        if Item=="ipv4":
                            w=fake.ipv4()
                            f.write(str(i))   
                            f.write(":   "+str(w)+"\n""\n")

                        if Item=="ipv6":
                            w=fake.ipv6()
                            f.write(str(i))   
                            f.write(":   "+str(w)+"\n""\n")

                        if Item=="mac_address":
                            w=fake.mac_address()
                            f.write(str(i))     
                            f.write(":   "+str(w)+"\n""\n")


                        if Item=="uri":
                            w=fake.uri()
                            f.write(str(i))     
                            f.write(":   "+str(w)+"\n""\n")


                        if Item=="url":
                            w=fake.url()
                            f.write(str(i))     
                            f.write(":   "+str(w)+"\n""\n")

                        if Item=="user_name":
                            w=fake.user_name()
                            f.write(str(i))     
                            f.write(":   "+str(w)+"\n""\n")

                        if Item=="year":
                            w=fake.year()  
                            f.write(str(i))     
                            f.write(":   "+str(w)+"\n""\n")

                        if Item=="date":
                            w=fake.date()  
                            f.write(str(i))     
                            f.write(":   "+str(w)+"\n""\n")


                        if Item=="century":
                            w=fake.century()  
                            f.write(str(i))     
                            f.write(":   "+str(w)+"\n""\n")


                        if Item=="time":
                            w=fake.time()   
                            f.write(str(i))     
                            f.write(":   "+str(w)+"\n""\n")

                        if Item=="timezone":
                            w=fake.timezone()   
                            f.write(str(i))     
                            f.write(":   "+str(w)+"\n""\n")

                        if Item=="date_time_dates":  
                            w=fake.date_time_between_dates()
                            f.write(str(i))     
                            f.write(":   "+str(w)+"\n""\n")

                        if Item=="currency_code":  
                            w=fake.currency_code()
                            f.write(str(i))     
                            f.write(":   "+str(w)+"\n""\n")

                        if Item=="credit_card_expire":  
                            w=fake.credit_card_expire()
                            f.write(str(i))     
                            f.write(":   "+str(w)+"\n""\n")
                        
                        if Item=="credit_card_full":  
                            w=fake.credit_card_full()
                            f.write(str(i))     
                            f.write(":   "+str(w)+"\n""\n")

                        if Item=="credit_card_number":  
                            w=fake.credit_card_number()
                            f.write(str(i))     
                            f.write(":   "+str(w)+"\n""\n")

                        if Item=="credit_card_provider":  
                            w=fake.credit_card_provider()
                            f.write(str(i))     
                            f.write(":   "+str(w)+"\n""\n")

                        if Item=="credit_card_security_code":  
                            w=fake.credit_card_security_code()
                            f.write(str(i))     
                            f.write(":   "+str(w)+"\n""\n")

                        if Item=="company_names":  
                            w=fake.bs()
                            f.write(str(i))     
                            f.write(":   "+str(w)+"\n""\n")

                        if Item=="company_catch_phrase":  
                            w=fake.catch_phrase()
                            f.write(str(i))     
                            f.write(":   "+str(w)+"\n""\n")

                        if Item=="company":  
                            w=fake.company()
                            f.write(str(i))     
                            f.write(":   "+str(w)+"\n""\n")

                        if Item=="company_suffix":  
                            w=fake.company_suffix()
                            f.write(str(i))     
                            f.write(":   "+str(w)+"\n""\n")

                        if Item=="color_name":  
                            w=fake.color_name()
                            f.write(str(i))     
                            f.write(":   "+str(w)+"\n""\n")

                        if Item=="color_name":  
                            w=fake.color_name()
                            f.write(str(i))     
                            f.write(":   "+str(w)+"\n""\n")

                        if Item=="chrome_user":  
                            w=fake.chrome()
                            f.write(str(i))     
                            f.write(":   "+str(w)+"\n""\n")

                        if Item=="firefox_user":  
                            w=fake.firefox()
                            f.write(str(i))     
                            f.write(":   "+str(w)+"\n""\n")

                        if Item=="internet_explorer":  
                            w=fake.internet_explorer()
                            f.write(str(i))     
                            f.write(":   "+str(w)+"\n""\n")
                            
                        if Item=="linux_platform":  
                            w=fake.linux_platform_token()
                            f.write(str(i))      
                            f.write(":   "+str(w)+"\n""\n")

                        if Item=="linux_processor":  
                            w=fake.linux_processor()
                            f.write(str(i))      
                            f.write(":   "+str(w)+"\n""\n")
                        
                        if Item=="mac_platform_token":  
                            w=fake.mac_platform_token()
                            f.write(str(i))      
                            f.write(":   "+str(w)+"\n""\n")

                        
                        if Item=="mac_processor":  
                            w=fake.mac_processor() 
                            f.write(str(i))      
                            f.write(":   "+str(w)+"\n""\n")

                        if Item=="opera":  
                            w=fake.opera() 
                            f.write(str(i))      
                            f.write(":   "+str(w)+"\n""\n")


                        if Item=="safari":  
                            w=fake.safari() 
                            f.write(str(i))      
                            f.write(":   "+str(w)+"\n""\n")

                        if Item=="user_agent":  
                            w=fake.user_agent() 
                            f.write(str(i))      
                            f.write(":   "+str(w)+"\n""\n")
                        
                        if Item=="windows_platform_token":  
                            w=fake.windows_platform_token() 
                            f.write(str(i))      
                            f.write(":   "+str(w)+"\n""\n")

                        if Item=="ssn":  
                            w=fake.ssn() 
                            f.write(str(i))      
                            f.write(":   "+str(w)+"\n""\n")

                        if Item=="barcode_ean(length=13)":  
                            w=fake.ean(length=13)
                            f.write(str(i))      
                            f.write(":   "+str(w)+"\n""\n")

                        if Item=="barcode_ean(length=8)":  
                            w=fake.ean(length=8)
                            f.write(str(i))      
                            f.write(":   "+str(w)+"\n""\n")

                        if Item=="barcode_ean13()":  
                            w=fake.ean13()
                            f.write(str(i))      
                            f.write(":   "+str(w)+"\n""\n")

                        if Item=="barcode_ean8()":  
                            w=fake.ean8()
                            f.write(str(i))      
                            f.write(":   "+str(w)+"\n""\n")

                        


                        


                        
                        

                        

                        

                      

                with open("C:\\TEMP\\save.txt","r",encoding="utf-8") as f:
                    reads=f.read()
                
                texttopaste1.insert(END,reads)
            except:
                tkinter.messagebox.askretrycancel("Internal Error","Language is Not defined",icon="info")

        def clear():
            texttopaste1.delete("1.0",END)
            os.remove("C:\\TEMP\\save.txt")


                



    #==================Frame==========================================
        MainFrame=Frame(self.root,width=610,height=560,bg="cyan",bd=4,relief=RIDGE)
        MainFrame.place(x=0,y=0)

        First_Frame=Frame(MainFrame,width=603,height=200,bd=4,relief=RIDGE)
        First_Frame.place(x=0,y=0)

        Lab_Frame=LabelFrame(First_Frame,width=594,height=193,text="Select Required Items",bg="gray75")
        Lab_Frame.place(x=1,y=0)

        Second_Frame=Frame(MainFrame,width=603,height=344,bd=4,relief=RIDGE)
        Second_Frame.place(x=0,y=200)

#===============================================================================================

        Lab_lang=Label(Lab_Frame,text="Select Language :=",font=('times new roman',12,'bold'),bg="gray75")
        Lab_lang.place(x=30,y=20)

        Lab_range=Label(Lab_Frame,text="Select Range :=",font=('times new roman',12,'bold'),bg="gray75")
        Lab_range.place(x=240,y=20)


        Lab_Items=Label(Lab_Frame,text="Select Items :=",font=('times new roman',12,'bold'),bg="gray75")
        Lab_Items.place(x=400,y=20)


#===========================================================================================================

        lang=["ar_EG","ar_PS","ar_SA","bg_BG","bs_BA","cs_CZ","de_DE","dk_DK","el_GR","en_AU","en_CA","en_GB","en_IN","en_NZ","en_US","es_ES","es_MX","et_EE","fa_IR","fi_FI","fr_FR","hi_IN","hr_HR","hu_HU","hy_AM","it_IT","ja_JP","ka_GE","lt_LT","lv_LV","ne_NP","nl_NL","no_NO","pl_PL","pt_BR","pt_PT","ro_RO","ru_RU","sl_SI","sv_SE","tr_TR","uk_UA","zh_CN","zh_TW"]
        txtlang=Combobox(Lab_Frame,values=lang,font=('arial',10),width=20,state="readonly",textvariable=langs)
        txtlang.place(x=30,y=60)
        txtlang.set("select Language")


        ranges=list(range(1,501))
        txtranges=Combobox(Lab_Frame,values=ranges,font=('arial',10),width=20,state="readonly",textvariable=lens)
        txtranges.place(x=220,y=60)
        txtranges.set("select Range")

        


        Items=["name","address","building_number","city","city_suffix","country","country_code","postcode","street_address","street_name","street_suffix","profile","phone_Number","firstname","first_Female_name","first_male_name","paragraph","text","words","jobs","email","company_email","safe_email","free_email","image_url","ipv4","ipv6","mac_address","uri","url","user_name","date","century","time","timezone","year","date_time_dates","currency_code","credit_card_expire","credit_card_full","credit_card_number","ssn","credit_card_provider","credit_card_security_code","company_names","company_catch_phrase","company","company_suffix","color_name","chrome_user","firefox_user","internet_explorer","linux_platform","linux_processor","mac_platform_token","mac_processor","opera","safari","user_agent","windows_platform_token","barcode_ean(length=13)","barcode_ean(length=8)","barcode_ean13()","barcode_ean8()"]
        txtItems=Combobox(Lab_Frame,values=Items,font=('arial',10),width=20,state="readonly",textvariable=items)
        txtItems.place(x=400,y=60)
        txtItems.set("select Items")





#========================================================================================================================
        But_get=Button(Lab_Frame,text="GET INFO",command=Get_Info,font=('times new roman',12,'bold'),width=20,cursor="hand2")
        But_get.place(x=20,y=110)
        But_get.bind("<Enter>",on_enter1)
        But_get.bind("<Leave>",on_leave1)


        But_clear=Button(Lab_Frame,text="Clear",command=clear,font=('times new roman',12,'bold'),width=20,cursor="hand2")
        But_clear.place(x=380,y=110)
        But_clear.bind("<Enter>",on_enter2)
        But_clear.bind("<Leave>",on_leave2)

#==============================================================================================================================




    #============================= Text and Scrollbar ==========================================
        Scol1=Scrollbar(Second_Frame,orient="vertical")
        Scol1.grid(column=10,sticky="NS")

        #Scol2=Scrollbar(Second_Frame,or    \ient="horizontal")
        #Scol2.grid(column=10,sticky="NS")
    
        texttopaste1=Text(Second_Frame,height=18,width=72,font=('times new roman',12,'bold'),yscrollcommand=Scol1.set)
        texttopaste1.grid(row=0,column=4)
        Scol1.config(command=texttopaste1.yview)

#==============================================================================================================



if __name__ == "__main__":
    root=Tk()
    app=All_Info(root)
    root.mainloop()