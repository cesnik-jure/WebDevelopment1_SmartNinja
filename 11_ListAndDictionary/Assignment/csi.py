with open("dna.txt", "r") as dns_file:
    dna_string = dns_file.read()

hair_color = {"black": "CCAGCAATCGC", "brown": "GCCAGTGCCG", "blonde": "TTAGCTATCGC"}
face_shape = {"square": "GCCACGG", "round": "ACCACAA", "oval": "AGGCCTCA"}
eye_color = {"blue": "TTGTGGTGGC", "green": "GGGAGGTGGC", "brown": "AAGTAGTGAC"}
gender = {"female": "TGAAGGACCTTC", "male": "TGCAGGAACTTC"}
race = {"white": "AAAACCTCA", "black": "CGACTACAG", "asian": "CGCGGGCCG"}

person_eva = {"name": "Eva", "gender": "female", "race": "white", "hair_color": "blonde", "eye_color": "blue", "face_shape": "oval"}
person_larisa = {"name": "Larisa", "gender": "female", "race": "white", "hair_color": "brown", "eye_color": "brown", "face_shape": "oval"}
person_matej = {"name": "Matej", "gender": "male", "race": "white", "hair_color": "black", "eye_color": "blue", "face_shape": "oval"}
person_miha = {"name": "Miha", "gender": "male", "race": "white", "hair_color": "brown", "eye_color": "green", "face_shape": "square"}

suspects = [person_eva, person_larisa, person_matej, person_miha]

for suspect in suspects:

    if hair_color.get(suspect.get("hair_color")) in dna_string and \
            face_shape.get(suspect.get("face_shape")) in dna_string and \
            eye_color.get(suspect.get("eye_color")) in dna_string and \
            gender.get(suspect.get("gender")) in dna_string and \
            race.get(suspect.get("race")) in dna_string:

        print(suspect.get("name"))
