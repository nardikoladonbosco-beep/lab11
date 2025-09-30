user = input("User: ").strip().lower()
passw = input("Pass: ").strip().lower()

if (user == "admin" and passw == "python") or (user == "guest" and passw == "1234"):
    print("Hyrje e lejuar")
else:
    print("Hyrje e refuzuar")
