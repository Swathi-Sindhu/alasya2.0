import PyMySQL


try:
    db = PyMySQL.connect("chandracanth95.mysql.pythonanywhere-services.com", "chandracanth95", "onlinedatabase",
                         "chandracanth95$chan");
    cur=db.cursor();
    cursor.execute("create table sample(num int);")
except:
    print("error")