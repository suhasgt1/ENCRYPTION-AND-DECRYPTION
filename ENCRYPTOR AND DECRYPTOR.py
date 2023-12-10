import messagebox
import tkinter as tk

display=tk.Tk()
display.configure(bg="#2E2E2E")
display.geometry("350x200")
display.title("LOGIN PAGE")
dict_complete_user={"suhas":["suhas",16,"abcxyz@gmail.com","suhas","Suhas@123"]}
dict_user={"suhas":"Suhas@123","amruth":"Amruth@123","yash":"Yash@123","supriya":"Supriya@123"}


def new_user():
    new_display=tk.Tk()
    new_display.geometry("125x420")
    new_display.title("NEW USER")
    new_display.configure(bg="#2E2E2E")

    name=tk.Label(new_display,text="ENTER NAME: ",font=("Arial",11),width=10,bg="#2E2E2E",fg="white")
    name.pack(pady=10)
    entered_name=tk.Entry(new_display,font=("Arial",12),width=10)
    entered_name.pack(pady=5)

    age = tk.Label(new_display, text="ENTER AGE : ", font=("Arial", 11), width=10,bg="#2E2E2E",fg="white")
    age.pack(pady=10)
    entered_age = tk.Entry(new_display, font=("Arial", 12), width=10)
    entered_age.pack(pady=5)

    mail=tk.Label(new_display,text="ENTER MAIL ID", font=("Arial", 11), width=10,bg="#2E2E2E",fg="white")
    mail.pack(pady=10)
    entered_mail=tk.Entry(new_display, font=("Arial", 12), width=10)
    entered_mail.pack(pady=5)

    new_userlbl=tk.Label(new_display,text="USERNAME",font=("Arial",12),bg="#2E2E2E",fg="white")
    new_userlbl.pack(pady=10)

    entered_newuser=tk.Entry(new_display,font=("Arial",12),width=10)
    entered_newuser.pack(pady=5)

    set_passowrdlbl=tk.Label(new_display,text="PASSWORD",font=("Arial",12),bg="#2E2E2E",fg="white")
    set_passowrdlbl.pack(pady=10)

    entered_newpassword=tk.Entry(new_display,font=("Arial",12),width=10)
    entered_newpassword.pack(pady=5)

    def full_details():
        name=username_entered.get()
        password=entered_newpassword.get()
        dict_user[entered_newuser.get()]=password
        dict_complete_user[name]=[entered_name.get(),entered_age.get(),entered_mail.get(),entered_newuser.get(),entered_newpassword.get()]
        messagebox.showinfo("SUCCESSFULL LOGIN","REGISTERED SUCESSFULLY")
        new_display.destroy()
    submit_new_user=tk.Button(new_display,text="SUBMIT",font=("Arial",12),width=10,bg="#2E2E2E",fg="white",command=full_details)
    submit_new_user.pack(pady=10)


def checking_if_user_is_there():
    user=username_entered.get()
    password=password_entered.get()
    cond=0
    for i in dict_user:
        if user ==i:
            cond+=1
            if password==dict_user[i]:
                cond+=1
    if cond == 2:
        messagebox.showinfo("SUCCESSFUL","LOGGED IN")
        display.destroy()
        option=tk.Tk()
        option.configure(bg="#525252")
        option.title("ENCRYPT OR DECRYPT")
        option.geometry("350x200")


        def trueenc():

            displayencrypt = tk.Tk()
            displayencrypt.configure(bg="#525252")
            displayencrypt.title("ENCRYPT")
            displayencrypt.geometry("350x200")
            inputlbl=tk.Label(displayencrypt,text="Enter the string to be encrypted",font=("elephant",12))
            inputlbl.pack(pady=10)
            need_to_be_enc=tk.Entry(displayencrypt,font=("elephant",12))
            need_to_be_enc.pack()

            def enc():
                letters = [" ", " ", " ", " ", 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N',
                           'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', 'A', 'B', 'C']
                str = need_to_be_enc.get()
                str = str.upper()
                str = list(str)
                final_str = ""
                for i in str:
                    for j in letters:
                        if i == j:
                            a = letters.index(j)
                            a += 3
                            final_str = final_str + letters[a]
                            break
                print(final_str)
                final_output.configure(text=final_str,font=("elephant",12),fg="white")


            final_output = tk.Label(displayencrypt, text="", bg="#525252")
            final_output.pack()
            submit_button=tk.Button(displayencrypt,text="SUBMIT", font=("elephant", 12),command=enc)
            submit_button.pack(pady=10)
            displayencrypt.mainloop()


        def truedec():
            displayencrypt = tk.Tk()
            displayencrypt.configure(bg="#525252")
            displayencrypt.title("DECRYPT")
            displayencrypt.geometry("350x200")
            inputlbl = tk.Label(displayencrypt, text="Enter the string to be decrypted", font=("elephant", 12))
            inputlbl.pack(pady=10)
            need_to_be_dec = tk.Entry(displayencrypt, font=("elephant", 12))
            need_to_be_dec.pack()
            final_output=tk.Label(displayencrypt,text="",bg="#525252",fg="white")
            final_output.pack()


            def dec():
                letters = [" ", " ", " ", " ", 'X', 'Y', 'Z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K',
                           'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', 'A', 'B', 'C']
                str = need_to_be_dec.get()
                str = str.upper()
                str = list(str)
                final_str = ""
                for i in str:
                    for j in letters:
                        if i == " ":
                            print("  ")
                        elif i == j:
                            a = letters.index(j)
                            a -= 3
                            final_str = final_str + letters[a]
                            break
                print(final_str)
                final_output.configure(text=final_str,font=("elephant",12),fg="white")

            submit_button = tk.Button(displayencrypt, text="SUBMIT", font=("elephant", 12), command=dec)
            submit_button.pack(pady=10)
            displayencrypt.mainloop()

        buttonencrpyt=tk.Button(option,text="Encrypt",font=("elephant",12),command=trueenc).pack(pady=10)
        buttondecrypt=tk.Button(option,text="Decrypt",font=("elephant",12),command=truedec).pack(pady=10)


    elif cond == 1:
        messagebox.showerror("WRONG PASSWORD","ENTER THE RIGHT PASSOWRD!!!")
    elif cond == 0:
        messagebox.showerror("WRONG CREDENTIALS","ENTER THE RIGHT CREDENTIALS")



usernamelbl=tk.Label(display,text="USERNAME: ",font=("elephant",12),fg="white",bg="#525252")
usernamelbl.grid(row=2,column=0,padx=10,pady=10)

username_entered=tk.Entry(display,font=("Arial",12))
username_entered.grid(row=2,column=1,padx=10,pady=10)

passwordlbl=tk.Label(display,text="PASSWORD: ",font=("elephant",12),fg="white",bg="#525252")
passwordlbl.grid(row=3,column=0,padx=10,pady=10)

password_entered=tk.Entry(display,font=("Arial",12))
password_entered.grid(row=3,column=1,padx=10,pady=10)

login=tk.Button(display,text="LOGIN",font=("Arial",12),width=19,command=checking_if_user_is_there)
login.grid(row=4,column=1)

new_user=tk.Button(display,text="NEW USER?",font=("Arial",12),width=19,command=new_user)
new_user.grid(row=5,column=1,pady=10)

display.mainloop()
print(f"{dict_complete_user}\n{dict_user}")