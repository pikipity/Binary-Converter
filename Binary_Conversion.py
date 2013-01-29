# coding=gbk
from __future__ import division
import Tkinter
import tkMessageBox
import math

################### 单精度浮点转换窗口 ###########################################
def Floating_and_decimal_window():
    Floating_and_decimal_toplevel=Tkinter.Toplevel()
    Floating_and_decimal_toplevel.title(u"单精度浮点转换")
    Floating_and_decimal_toplevel.iconbitmap("bitmap\\binary.ico")
    
    decimal_label=Tkinter.Label(Floating_and_decimal_toplevel,text=u"十进制: ",\
                               font="Times 23 bold")
    decimal_label.grid(row=0,column=0)

    global decimal_mantissa
    decimal_mantissa=Tkinter.Entry(Floating_and_decimal_toplevel,\
                               font="Times 23 bold")
    decimal_mantissa.grid(row=0,column=1)
    
    decimal_10_label=Tkinter.Label(Floating_and_decimal_toplevel,text="*10^",\
                               font="Times 23 bold")
    decimal_10_label.grid(row=0,column=2)

    global decimal_exp
    decimal_exp=Tkinter.Entry(Floating_and_decimal_toplevel,width=5,\
                               font="Times 10 bold")
    decimal_exp.grid(row=0,column=3)
    decimal_exp.insert('end','0')

    kong_label=Tkinter.Label(Floating_and_decimal_toplevel,width=10,font=\
                             "Times 10 bold")
    kong_label.grid(row=0,column=4)

    Convert_button=Tkinter.Button(Floating_and_decimal_toplevel,text=u"转换",\
                               font="Times 23 bold",\
                                  width=17,command=Floating_and_decimal_function)
    Convert_button.grid(row=1,column=1,columnspan=1)

    Clear_button=Tkinter.Button(Floating_and_decimal_toplevel,text=u"清除",\
                                font="Times 23 bold",\
                                width=5,command=Clear_Function)
    Clear_button.grid(row=1,column=2,columnspan=2)

    bin_label=Tkinter.Label(Floating_and_decimal_toplevel,text=u"二进制: ",\
                               font="Times 23 bold")
    bin_label.grid(row=2,column=0)
    
    global bin_num_entry
    bin_num_entry=Tkinter.Entry(Floating_and_decimal_toplevel,\
                               font="Times 23 bold",\
                          width=32)
    bin_num_entry.grid(row=2,column=1,columnspan=4)

##############################################################################
def Clear_Function():
    decimal_mantissa.delete(0,'end')
    decimal_exp.delete(0,'end')
    bin_num_entry.delete(0,'end')
    decimal_exp.insert('end','0')
################## 单精度浮点转换功能 ##########################################
def Floating_and_decimal_function():
    mantissa_num=decimal_mantissa.get()
    exp_num=decimal_exp.get()
    bin_num=bin_num_entry.get()
    if(len(mantissa_num)<>0 and len(exp_num)<>0):
        decimal_decision=1
    else:
        decimal_decision=0
    if(len(bin_num)<>0):
        bin_decision=1
    else:
        bin_decision=0
    if(decimal_decision==1 and bin_decision==1):
        tkMessageBox.showwarning(u"输入错误",u"不要都填东西!!")
    elif(decimal_decision==0 and bin_decision==0):
        tkMessageBox.showwarning(u"输入错误",u"不要啥都不填!!")
    elif(bin_decision==1 and decimal_decision==0):
        bin_not_num=0
        try:
            int(bin_num)
        except ValueError:
            bin_not_num=1
        for i in bin_num:
            if(i<>'0' and i<>'1'):
                bin_not_num=1
                break
        if(bin_not_num==1):
            tkMessageBox.showwarning(u"输入错误",u"不要耍我，输入二进制数")
        elif(len(bin_num)<>32):
            tkMessageBox.showwarning(u"输入错误",u"二进制必须32 bit!!")
        else:
            if(bin_num=="00000000000000000000000000000000"):
                decimal_mantissa.delete(0,'end')
                decimal_mantissa.insert('end',0)
                decimal_exp.delete(0,'end')
                decimal_exp.insert('end','')
            elif(bin_num=="11111111111111111111111111111111"):
                decimal_mantissa.delete(0,'end')
                decimal_mantissa.insert('end','Infinity')
                decimal_exp.delete(0,'end')
                decimal_exp.insert('end','')
            else:
                sign_label=bin_num[0]
                exp_label=bin_num[1:9]
                mantissa_label=bin_num[9:32]
                if(sign_label=='1'):
                    sign_label='-'
                elif(sign_label=='0'):
                    sign_label='+'
                exp_label=int(exp_label,2)-127
                flag=0
                final_decimal=0
                for i in mantissa_label:
                    flag=flag+1
                    final_decimal=1/2**flag*int(i)+final_decimal
                final_decimal=final_decimal+1
                final_decimal=final_decimal*2**exp_label
                final_decimal='%E'%final_decimal
                decimal_mantissa.delete(0,'end')
                decimal_mantissa.insert('end',sign_label+final_decimal[0:final_decimal.rfind('E')])
                decimal_exp.delete(0,'end')
                decimal_exp.insert('end',final_decimal[final_decimal.rfind('E')+1:len(final_decimal)])
    elif(decimal_decision==1 and bin_decision==0):
       decimal_not_num=0
       mantissa_not_num=0
       exp_not_num=0
       try:
           float(mantissa_num)
       except ValueError:
           mantissa_not_num=1
       try:
           int(exp_num)
       except ValueError:
           exp_not_num=1
       if(mantissa_not_num==1 or exp_not_num==1):
           decimal_not_num=1
       if(decimal_not_num==1):
           tkMessageBox.showwarning(u"输入错误",u"不要耍我，输入十进制数")
       elif(mantissa_num=='0'):
           bin_num_entry.delete(0,'end')
           bin_num_entry.insert('end','00000000000000000000000000000000') 
       else:
           DecimalNumber=float(mantissa_num)*10**int(exp_num)
           DecimalNumber='%f'%DecimalNumber
           sign_label=DecimalNumber[0]
           if(sign_label=='-'):
               bin_sign='1'
               DecimalNumber=DecimalNumber[1:len(DecimalNumber)]
           else:
               bin_sign='0'
           DecimalNumber_10=DecimalNumber[0:DecimalNumber.rfind('.')]
           DecimalNumber_1='0.'+DecimalNumber[DecimalNumber.rfind('.')+1:len(DecimalNumber)]
           if(int(DecimalNumber_10)<>0):
               BinNumber_10=bin(int(DecimalNumber_10))
               BinNumber_10=BinNumber_10[BinNumber_10.rfind('b')+1:len(BinNumber_10)]
               DecimalNumber_1=float(DecimalNumber_1)
               BinNumber_1=''
               i=0
               while(DecimalNumber_1<1.0 and i<25):
                   i=i+1
                   DecimalNumber_1=DecimalNumber_1*2
                   if(DecimalNumber_1<1):
                       BinNumber_1=BinNumber_1+'0'
                   elif(DecimalNumber_1>1):
                       BinNumber_1=BinNumber_1+'1'
                       DecimalNumber_1=DecimalNumber_1-1
               ExpNumber=(len(BinNumber_10)-1)+127
               ExpNumber=bin(ExpNumber)
               ExpNumber=ExpNumber[ExpNumber.rfind('b')+1:len(ExpNumber)]
               ManissaNumber=BinNumber_10+BinNumber_1
               if(len(ManissaNumber)<24):
                   ManissaNumber=ManissaNumber+'00000000000000000000000000000'[0:24-len(ManissaNumber)]
               elif(len(ManissaNumber)>24):
                   while(len(ManissaNumber)>24):
                       if(ManissaNumber[24]=='0'):
                           ManissaNumber=ManissaNumber[0:24]
                       elif(ManissaNumber[24]=='1'):
                           ManissaNumber=ManissaNumber[0:24]
                           ManissaNumber=bin(int('0b'+ManissaNumber,2)+1)
                           ManissaNumber=ManissaNumber[ManissaNumber.rfind('b')+1:len(ManissaNumber)]
               bin_num_entry.delete(0,'end')
               if(len(ExpNumber)<>8):
                   ExpNumber='00000000'[0:8-len(ExpNumber)]+ExpNumber
               bin_num_entry.insert('end',bin_sign+ExpNumber+ManissaNumber[1:len(ManissaNumber)])        
           elif(int(DecimalNumber_10)==0):
               DecimalNumber_1=float(mantissa_num)*10**int(exp_num)
               if(DecimalNumber_1<0):
                   DecimalNumber_1=DecimalNumber_1*(-1)
               DecimalNumber_1=float(DecimalNumber_1)
               ExpNumber=int(math.log(DecimalNumber_1,2)-1)+127
               ExpNumber=bin(ExpNumber)
               ExpNumber=ExpNumber[ExpNumber.rfind('b')+1:len(ExpNumber)]
               if(len(ExpNumber)<>8):
                   ExpNumber='00000000'[0:8-len(ExpNumber)]+ExpNumber
               n=int(math.log(DecimalNumber_1,2)-1)
               DecimalNumber_1=DecimalNumber_1/(2**n)-1
               BinNumber_1=''
               i=0
               while(DecimalNumber_1<1.0 and i<25):
                   i=i+1
                   DecimalNumber_1=DecimalNumber_1*2
                   if(DecimalNumber_1<1):
                       BinNumber_1=BinNumber_1+'0'
                   elif(DecimalNumber_1>1):
                       BinNumber_1=BinNumber_1+'1'
                       DecimalNumber_1=DecimalNumber_1-1
               ManissaNumber='1'+BinNumber_1
               if(len(ManissaNumber)<24):
                   ManissaNumber=ManissaNumber+'00000000000000000000000000000'[0:24-len(ManissaNumber)]
               elif(len(ManissaNumber)>24):
                   while(len(ManissaNumber)>24):
                       if(ManissaNumber[24]=='0'):
                           ManissaNumber=ManissaNumber[0:24]
                       elif(ManissaNumber[24]=='1'):
                           ManissaNumber=ManissaNumber[0:24]
                           ManissaNumber=bin(int('0b'+ManissaNumber,2)+1)
                           ManissaNumber=ManissaNumber[ManissaNumber.rfind('b')+1:len(ManissaNumber)]
               bin_num_entry.delete(0,'end')
               bin_num_entry.insert('end',bin_sign+ExpNumber+ManissaNumber[1:len(ManissaNumber)])
               
###############################################################################

################### 十六进制与二进制转换窗口 ###########################################
def hex_2_two_window():
    hex_2_two_toplevel=Tkinter.Toplevel()
    hex_2_two_toplevel.title(u"十六进制与二进制转换")
    hex_2_two_toplevel.iconbitmap("bitmap\\binary.ico")
    
    hex_label=Tkinter.Label(hex_2_two_toplevel,text=u"十六进制: ",\
                               font="Times 23 bold")
    hex_label.grid(row=0,column=0)

    global hex_number_entry
    hex_number_entry=Tkinter.Entry(hex_2_two_toplevel,\
                               font="Times 23 bold")
    hex_number_entry.grid(row=0,column=1)

    kong_label=Tkinter.Label(hex_2_two_toplevel,width=10,font=\
                             "Times 10 bold")
    kong_label.grid(row=0,column=2,columnspan=3)

    Convert_button=Tkinter.Button(hex_2_two_toplevel,text=u"转换",\
                               font="Times 23 bold",\
                                  width=17,command=hex_2_two_function)
    Convert_button.grid(row=1,column=1,columnspan=1)

    Clear_button=Tkinter.Button(hex_2_two_toplevel,text=u"清除",\
                                font="Times 23 bold",\
                                width=5,command=hex_2_two_Clear_Function)
    Clear_button.grid(row=1,column=2,columnspan=2)

    bin_label=Tkinter.Label(hex_2_two_toplevel,text=u"二进制: ",\
                               font="Times 23 bold")
    bin_label.grid(row=2,column=0)
    
    global bin_num_entry_hex_2_two
    bin_num_entry_hex_2_two=Tkinter.Entry(hex_2_two_toplevel,\
                               font="Times 23 bold",\
                          width=32)
    bin_num_entry_hex_2_two.grid(row=2,column=1,columnspan=4)

##############################################################################

def hex_2_two_Clear_Function():
    hex_number_entry.delete(0,'end')
    bin_num_entry_hex_2_two.delete(0,'end')

def hex_2_two_function():
    HexNumber=hex_number_entry.get()
    BinNumber=bin_num_entry_hex_2_two.get()
    if(len(HexNumber)<>0 and len(BinNumber)<>0):
        tkMessageBox.showwarning(u"输入错误",u"不要啥都填东西，我知道转化谁么？")
    elif(len(HexNumber)==0 and len(BinNumber)==0):
        tkMessageBox.showwarning(u"输入错误",u"啥都不输？")
    elif(len(HexNumber)<>0 and len(BinNumber)==0):
        wrong=0
        try:
            final_answer=int(HexNumber,16)
        except ValueError:
            wrong=1
        if(wrong==1):
            tkMessageBox.showwarning(u"输入错误",u"请输入正确十六进制数")
        else:
            final_answer=bin(final_answer)
            final_answer=final_answer[final_answer.rfind('b')+1:\
                                      len(final_answer)]
            bin_num_entry_hex_2_two.delete(0,'end')
            bin_num_entry_hex_2_two.insert('end',final_answer)
    elif(len(HexNumber)==0 and len(BinNumber)<>0):
        wrong=0
        try:
            final_answer=int(BinNumber,2)
        except ValueError:
            wrong=1
        if(wrong==1):
            tkMessageBox.showwarning(u"输入错误",u"请输入正确二进制数")
        else:
            final_answer=hex(final_answer)
            final_answer=final_answer[final_answer.rfind('x')+1:\
                                      len(final_answer)]
            hex_number_entry.delete(0,'end')
            hex_number_entry.insert('end',final_answer.upper())
###############################################################################

################### 十六进制与十进制转换窗口 ###########################################
def hex_2_ten_window():
    hex_2_ten_toplevel=Tkinter.Toplevel()
    hex_2_ten_toplevel.title(u"十六进制与十进制转换")
    hex_2_ten_toplevel.iconbitmap("bitmap\\binary.ico")
    
    hex_label=Tkinter.Label(hex_2_ten_toplevel,text=u"十六进制: ",\
                               font="Times 23 bold")
    hex_label.grid(row=0,column=0)

    global hex_number_entry_2_ten
    hex_number_entry_2_ten=Tkinter.Entry(hex_2_ten_toplevel,\
                               font="Times 23 bold")
    hex_number_entry_2_ten.grid(row=0,column=1)

    kong_label=Tkinter.Label(hex_2_ten_toplevel,width=10,font=\
                             "Times 10 bold")
    kong_label.grid(row=0,column=2,columnspan=3)

    Convert_button=Tkinter.Button(hex_2_ten_toplevel,text=u"转换",\
                               font="Times 23 bold",\
                                  width=17,command=hex_2_ten_function)
    Convert_button.grid(row=1,column=1,columnspan=1)

    Clear_button=Tkinter.Button(hex_2_ten_toplevel,text=u"清除",\
                                font="Times 23 bold",\
                                width=5,command=hex_2_ten_Clear_Function)
    Clear_button.grid(row=1,column=2,columnspan=2)

    bin_label=Tkinter.Label(hex_2_ten_toplevel,text=u"十进制: ",\
                               font="Times 23 bold")
    bin_label.grid(row=2,column=0)
    
    global bin_num_entry_hex_2_ten
    bin_num_entry_hex_2_ten=Tkinter.Entry(hex_2_ten_toplevel,\
                               font="Times 23 bold",\
                          width=32)
    bin_num_entry_hex_2_ten.grid(row=2,column=1,columnspan=4)

##############################################################################
def hex_2_ten_Clear_Function():
    hex_number_entry_2_ten.delete(0,'end')
    bin_num_entry_hex_2_ten.delete(0,'end')

def hex_2_ten_function():
    HexNumber=hex_number_entry_2_ten.get()
    BinNumber=bin_num_entry_hex_2_ten.get()
    if(len(HexNumber)<>0 and len(BinNumber)<>0):
        tkMessageBox.showwarning(u"输入错误",u"不要啥都填东西，我知道转化谁么？")
    elif(len(HexNumber)==0 and len(BinNumber)==0):
        tkMessageBox.showwarning(u"输入错误",u"啥都不输？")
    elif(len(HexNumber)<>0 and len(BinNumber)==0):
        wrong=0
        try:
            final_answer=int(HexNumber,16)
        except ValueError:
            wrong=1
        if(wrong==1):
            tkMessageBox.showwarning(u"输入错误",u"请输入正确十六进制数")
        else:
            bin_num_entry_hex_2_ten.delete(0,'end')
            bin_num_entry_hex_2_ten.insert('end',final_answer)
    elif(len(HexNumber)==0 and len(BinNumber)<>0):
        wrong=0
        try:
            final_answer=int(BinNumber)
        except ValueError:
            wrong=1
        except TypeError:
            wrong=1
        if(wrong==1):
            tkMessageBox.showwarning(u"输入错误",u"请输入正确十进制整数")
        else:
            final_answer=hex(final_answer)
            final_answer=final_answer[final_answer.rfind('x')+1:\
                                      len(final_answer)]
            hex_number_entry_2_ten.delete(0,'end')
            hex_number_entry_2_ten.insert('end',final_answer.upper())

###############################################################################

################### 二进制与十进制转换窗口 ###########################################
def two_2_ten_window():
    two_2_ten_toplevel=Tkinter.Toplevel()
    two_2_ten_toplevel.title(u"二进制与十进制转换")
    two_2_ten_toplevel.iconbitmap("bitmap\\binary.ico")
    
    two_label=Tkinter.Label(two_2_ten_toplevel,text=u"二进制: ",\
                               font="Times 23 bold")
    two_label.grid(row=0,column=0)

    global two_number_entry_two_2_ten
    two_number_entry_two_2_ten=Tkinter.Entry(two_2_ten_toplevel,\
                               font="Times 23 bold")
    two_number_entry_two_2_ten.grid(row=0,column=1)

    kong_label=Tkinter.Label(two_2_ten_toplevel,width=10,font=\
                             "Times 10 bold")
    kong_label.grid(row=0,column=2,columnspan=3)

    Convert_button=Tkinter.Button(two_2_ten_toplevel,text=u"转换",\
                               font="Times 23 bold",\
                                  width=17,command=two_2_ten_function)
    Convert_button.grid(row=1,column=1,columnspan=1)

    Clear_button=Tkinter.Button(two_2_ten_toplevel,text=u"清除",\
                                font="Times 23 bold",\
                                width=5,command=two_2_ten_Clear_Function)
    Clear_button.grid(row=1,column=2,columnspan=2)

    ten_label=Tkinter.Label(two_2_ten_toplevel,text=u"十进制: ",\
                               font="Times 23 bold")
    ten_label.grid(row=2,column=0)
    
    global ten_num_entry_two_2_ten
    ten_num_entry_two_2_ten=Tkinter.Entry(two_2_ten_toplevel,\
                               font="Times 23 bold",\
                          width=32)
    ten_num_entry_two_2_ten.grid(row=2,column=1,columnspan=4)

##############################################################################
def two_2_ten_Clear_Function():
    two_number_entry_two_2_ten.delete(0,'end')
    ten_num_entry_two_2_ten.delete(0,'end')

def two_2_ten_function():
    TwoNumber=two_number_entry_two_2_ten.get()
    TenNumber=ten_num_entry_two_2_ten.get()
    if(len(TwoNumber)<>0 and len(TenNumber)<>0):
        tkMessageBox.showwarning(u"输入错误",u"不要啥都填东西，我知道转化谁么？")
    elif(len(TwoNumber)==0 and len(TenNumber)==0):
        tkMessageBox.showwarning(u"输入错误",u"啥都不输？")
    elif(len(TenNumber)<>0 and len(TwoNumber)==0):
        wrong=0
        try:
            final_answer=int(TenNumber)
        except ValueError:
            wrong=1
        except TypeError:
            wrong=1
        if(wrong==1):
            tkMessageBox.showwarning(u"输入错误",u"请输入正确十进制整数")
        else:
            final_answer=bin(final_answer)
            final_answer=final_answer[final_answer.rfind('b')+1:\
                                      len(final_answer)]
            two_number_entry_two_2_ten.delete(0,'end')
            two_number_entry_two_2_ten.insert('end',final_answer)
    elif(len(TenNumber)==0 and len(TwoNumber)<>0):
        wrong=0
        try:
            final_answer=int(TwoNumber,2)
        except ValueError:
            wrong=1
        except TypeError:
            wrong=1
        if(wrong==1):
            tkMessageBox.showwarning(u"输入错误",u"请输入正确二进制数")
        else:
            ten_num_entry_two_2_ten.delete(0,'end')
            ten_num_entry_two_2_ten.insert('end',final_answer)

###############################################################################

def AboutUs_Open():
    AboutUs=Tkinter.Toplevel()
    AboutUs.title("About me")
    AboutUs.iconbitmap("bitmap\\binary.ico")

    TitleLabel=Tkinter.Label(AboutUs,text=u"进制转换器",\
                         font="Times 23 bold",fg="red")
    TitleLabel.pack(side="top",padx=2,pady=1,ipadx=1,ipady=1)

    VersionLabel=Tkinter.Label(AboutUs,text="Version: 1.0",font="Times 20 bold",\
                           fg="blue")
    VersionLabel.pack(side="top",padx=2,pady=1,ipadx=1,ipady=1)

   #BitLabel=Tkinter.Label(AboutUs,image="bitmap\\home.ico")
   #BitLabel.pack(side="top",padx=2,pady=1,ipadx=1,ipady=1)

    SoftwareLabel=Tkinter.Message(AboutUs,text="""                 Wang Ze
wangze19910407@gmail.com"""\
                        ,font="Times 15 bold",\
                           fg="#D2691E",width=600)
    SoftwareLabel.pack(side="top",padx=2,pady=1,ipadx=1,ipady=1)

    ContentLabel=Tkinter.Message(AboutUs,text=u"""如果发现什么问题，请联系我，谢谢""",font="Times 13 bold",fg="#CD5C5C",width=600)
    ContentLabel.pack(side="top",padx=2,pady=1,ipadx=1,ipady=1)
    
#################### 主窗口 ####################################################
root=Tkinter.Tk()
root.title(u"进制转换")
root.iconbitmap("bitmap\\binary.ico")

MainFrame=Tkinter.Frame(root,borderwidth=2,width=200,height=300)
MainFrame.pack(fill='y',expand=1,padx=15,pady=5,ipadx=5,ipady=9)

Floating_and_decimal=Tkinter.Button(MainFrame,borderwidth=1,\
                               text=u"单精度浮点转换",\
                               font="Times 23 bold",\
                                command=Floating_and_decimal_window)
Floating_and_decimal.pack(fill='both',expand=1,padx=2,pady=1,ipadx=2,ipady=1)

hex_two=Tkinter.Button(MainFrame,borderwidth=1,\
                               text=u"十六进制与二进制转换",\
                               font="Times 23 bold",\
                       command=hex_2_two_window)
hex_two.pack(fill='both',expand=1,padx=2,pady=1,ipadx=2,ipady=1)

hex_ten=Tkinter.Button(MainFrame,borderwidth=1,\
                               text=u"十六进制与十进制转换",\
                               font="Times 23 bold",\
                       command=hex_2_ten_window)
hex_ten.pack(fill='both',expand=1,padx=2,pady=1,ipadx=2,ipady=1)

two_ten=Tkinter.Button(MainFrame,borderwidth=1,\
                               text=u"二进制与十进制转换",\
                               font="Times 23 bold",\
                       command=two_2_ten_window)
two_ten.pack(fill='both',expand=1,padx=2,pady=1,ipadx=2,ipady=1)

AboutButton=Tkinter.Button(MainFrame,borderwidth=1,text="About"\
                           ,font="Times 23 bold",command=AboutUs_Open)
AboutButton.pack(fill='both',expand=1,padx=2,pady=1,ipadx=2,ipady=1)

root.mainloop()
