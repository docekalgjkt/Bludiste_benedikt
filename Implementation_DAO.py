from Interface_DAO import BludisteDAO


class BludisteDAOFile(BludisteDAO):
    def __init__(self, filename):
        self.filename = filename

    def precti_data(self):
        with open(self.filename, 'r') as file:
            bludiste = []
            for line in file:
                row = [int(cell) for cell in line.strip().split(',')]
                bludiste.append(row)
            return bludiste

    def uloz_data(self, bludiste):
        with open(self.filename, 'w') as file:
            for row in bludiste:
                file.write(','.join(map(str, row)) + '\n')
