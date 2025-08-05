# Set é um conjunto de dados não ordenado, sem elementos repetidos

pimentas_que_plantei = {"Biquinho", "Dedo-de-moça", "Pimenta do reino", "Malagueta", "Biquinho", "Chipotle", "Pimenta do reino"}
pimentas_que_comprei = {"Caiena", "Pimenta de cheiro", "Pimentão", "Pimenta do reino", "Chipotle", "Pimenta rosa", "Cambuci"}

pimentas_que_plantei.add("Carolina Reaper")
pimentas_que_comprei.remove("Cambuci")
pimentas_que_comprei.discard("Pimenta Calabresa")

pimentas_que_tenho = pimentas_que_plantei | pimentas_que_comprei
pimentas_que_mais_uso = pimentas_que_plantei & pimentas_que_comprei
pimentas_que_faltam_plantar = pimentas_que_comprei -pimentas_que_plantei

print("Pimentas que tenho em casa:")
for todas in pimentas_que_tenho:
    print(todas)

print("\nPimentas que mais uso:")
for favorita in pimentas_que_mais_uso:
    print(favorita)

print("\nPimentas que ainda não pantei, mas pretendo:")
for comprada in pimentas_que_faltam_plantar:
    print(comprada)

