#Homogeneous list
integers = [1, 2, 3, 4, 5]

animals = ['cat', 'elephant', 'dog'  ]

names = ['Michelle', 'Poller', 'Anahi']

floats = [2.3, 4.5, 8.9 ]

#Heterogeneous list
number_animals_floats_names = [2, 'cat', 33.34, 'Deriva']

list_lists= [[1,2,3], ['cat', 'dog', 'dragon']]

#How to access an element in the list 
random_words = [
    "apple", "giraffe", "ocean", "whisper", "quantum",
    "serendipity", "jigsaw", "horizon", "mosaic", "telescope",
    "lighthouse", "kaleidoscope", "dragonfly", "paradox", "nebula",
    "stardust", "cascade", "phantom", "rendezvous", "labyrinth",
    "sky", "cloud", "mountain", "river", "forest",
    "firefly", "whirlwind", "echo", "symphony", "dandelion",
    "enigma", "journey", "voyage", "twilight", "harmony",
    "illusion", "spectacle", "gravity", "sapphire", "ethereal",
    "dreamcatcher", "crystal", "sunrise", "moonlight", "petal",
    "glimmer", "mystery", "cosmos", "reflection", "solstice",
    "serenade", "traverse", "breeze", "ember", "fable",
    "whirl", "canvas", "pulse", "velocity", "alchemy",
    "sundown", "raindrop", "melody", "seeker", "wanderlust",
    "whimsy", "paradise", "sphinx", "tapestry", "anomaly",
    "flare", "catalyst", "crescendo", "bloom", "veil",
    "seraph", "epiphany", "mirage", "odyssey", "glisten",
    "soliloquy", "eclipse", "frost", "spectrum", "cynosure",
    "quasar", "kismet", "lullaby", "reverie", "quilt",
    "tides", "siren", "quicksilver", "sundance", "horizon",
    "ripple", "whistle", "tide", "vortex", "tornado",
    "crimson", "flame", "wisp", "nexus", "cascades",
    "incandescent", "tranquil", "enlightenment", "chroma", "radiance",
    "harbinger", "moonbeam", "celestial", "vagabond", "synthesis",
    "sublime", "phoenix", "zenith", "luminary", "adventure",
    "haven", "evergreen", "iridescence", "shadow", "panorama",
    "gleam", "arcadia", "dream", "sanctuary", "reflections",
    "ephemeral", "rift", "gleam", "crystalline", "nostalgia",
    "serenity", "dusk", "reflection", "ambrosia", "utopia",
    "galaxy", "infinity", "euphoria", "crescent", "vortex",
    "mystique", "radiate", "gleaming", "luminescence", "whirl",
    "ethos", "spectrum", "timbre", "kaleidoscope", "haze",
    "sanctum", "melancholy", "apogee", "valiant", "verdant",
    "tether", "cascade", "mirage", "bastion", "eclipse",
    "aura", "gossamer", "silhouette", "tryst", "ciphers",
    "interlude", "mirth", "bliss", "eclipse", "phantasm",
    "scepter", "neophyte", "seraphim", "talisman", "epoch",
    "destiny", "meadow", "soulmate", "enchantment", "whimsical",
    "phenomenon", "embrace", "galore", "whirlwind", "cipher",
    "stardust", "whistle", "solstice", "flicker", "mystic",
    "dreamscape", "radiance", "canvas", "allure", "cherub",
    "paragon", "evanescent", "brilliance", "blossom", "tide",
    "serenity", "odyssey", "expanse", "whirl", "utopia"
]

#List slicing

List= [3, 22, 30, 5, 3, 20]

print (list[:])

print(list[1:3])

#Update a list

science=["art", "chemistry", "math"]

science[1]= "geology"

print(science)

integers = [2,5,9,20,27]

integers.remove (27)

print(integers)

integers.pop()

print(integers)

list_fruits=["Sandia", "Limon", "naranja"]

#pop remove del

del list_fruits[1]

print(list_fruits)

list_names=["Anahi", "Pamela", "Quebec"]

list_names.append("Dania")

print(list_names)

list_of_squares= []
for int in range (1,10):
    square= int**2
    list_of_squares.append(square)
    
print(list_of_squares)

numbers=[1, 2, 3, 4, 5, 6, 7, 8, 9]
#[expression for int in list if condition]
squared2 = [int**2 for int in range(1, 10)]
print(squared2)

numbers= [1, 2, 3, 4, 5, 6, 7, 8, 9,]
for numbers in numbers:
    print(numbers**3)
    
cubic = [num**3]
print

numbers= [1, 2, 3, 4, 5, 6, 7, 8, 9,]

#1 doubling the values of each element

#2 filtering the list to include and double only the even numbers

#3 combining list comprehensions with condition.


double_numbers = [num*2 for num in numbers if num%2 == 0]

print (double_numbers)