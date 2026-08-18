usuarios = {
    "user1": {"name": "Kauany", "email": "kauany.katsan@gmail.com"},
    "user2": {"name": "Kau", "email": "kauany.katsan@gmail.com"}
}


print(usuarios["user1"]["email"])
print(usuarios["user2"]["name"])

for user, info in usuarios.items():
    print(f"Dados do usuario: {user}")
    for key, value in info.items():
        print(f"{key} - {value}")