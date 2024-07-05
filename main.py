import json
import faker

# Creare un'istanza di Faker
fake = faker.Faker()

# Generare 10.000 documenti con dati casuali
data = []
for _ in range(10000):
    document = {
        "nome": fake.name(),
        "indirizzo": fake.address(),
        "email": fake.email()
    }
    data.append(document)

# Salvare i dati in un file JSON
with open("dataset.json", "w") as f:
    json.dump(data, f)
