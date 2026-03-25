import json
class Rapper:
    def _init_(self, name, age, genre):
        self.name = name,
        self.age = age,
        self.genre = genre

        def to_dict(self):
            return{
                "name":self.name,
                "age":self.age,
                "genre":self.genre
            }
        name = input("Enter rapper name:")
        age = int(input("Enter age:"))
        genre = input("Enter genre")

        rapper1 = Rapper(name, age, genre)
        data = rapper1.to_dict()
        json_data = json.dumps(data, indent=4)

        print("JSON Output:")
        print(json_data)