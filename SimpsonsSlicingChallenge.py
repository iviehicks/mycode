challenge= ["science", "turbo", ["goggles", "eyes"], "nothing"]


trial= ["science", "turbo", {"eyes": "goggles", "goggles": "eyes"}, "nothing"]


nightmare= [{"slappy": "a", "text": "b", "kumquat": "goggles", "user":{"awesome": "c", "name": {"first": "eyes", "last": "toes"}},"banana": 15, "d": "nothing"}]

e = challenge[2][1]
n = challenge[-1]

#print challenge level
print(f"My {e}! The goggles do {n}!")

#print trial level

E = trial[2]["goggles"]
G = trial[2]["eyes"]
N = trial[-1]

print(f"My {E}! The {G} do {N}!")

#print nightmare

a= nightmare[0]["user"]["name"]["first"]
b= nightmare[0]["kumquat"]
c= nightmare[0]["d"]

print(f"My {a}! The {b} do {c}!")

#trial = goggles
