from Implementation_DAO import BludisteDAOFile
from Bludiste_data import Bludiste

if __name__ == "__main__":
    # Initialize DAO with file path
    bludiste_dao = BludisteDAOFile('bludiste_data.txt')

    # Read maze data using DAO
    bludiste_data = bludiste_dao.precti_data()

    # Initialize Bludiste object with data
    bludiste = Bludiste(bludiste_data)

    # Print maze dimensions and exit
    print(f"Sirka bludiste: {bludiste.get_sirka()}")
    print(f"Vyska bludiste: {bludiste.get_vyska()}")
    exit_position = bludiste.get_vychod()
    if exit_position:
        print(f"Vychod se nachazi na souradnicich: {exit_position}")
    else:
        print("V bludisti neni vychod.")
