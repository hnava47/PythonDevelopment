import csv, collections, os

class autompg:
    def __init__(self, make, model, year, mpg):
        self.make = make
        self.model = model
        self.year = year
        self.mpg = mpg

    def __str__(self):
        return "%s, %s, %s, %s" % (self.make, self.model, self.year, self.mpg)

    def __repr__(self):
        return str(self)

    def __eq__(self, other):
        if type(self) == type(other):
            return self.make == other.make and self.model == other.model and self.year == other.year and self.mpg == other.mpg
        else:
            NotImplemented

    def __lt__(self, other):
        if type(self) == type(other):
            return self.make < other.make and self.model < self.model and self.year < other.year and self.mpg < other.mpg
        else:
            NotImplemented

    def __hash__(self):
        return hash((self.make, self.model, self.year, self.mpg))

class AutoMPGData:
    data = []

    def __init__(self):
        self._load_data()

    def __iter__(self):
        return iter(list(self.data))

    def _load_data(self):
        pack = Record.record
        if os.path.exists("auto-mpg.clean.txt") == False:
            self._clean_data()
            with open ("auto-mpg.clean.txt") as cleanFile:
                reader = csv.reader(cleanFile, delimiter= " ", skipinitialspace=True)
                for row in reader:
                    carRecord = pack(row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8])
                    splitName = carRecord.carName.split()
                    makeName = splitName[1:]
                    AutoMPGData.data.append([splitName[0], " ".join(makeName), "19"+str(carRecord.modelYear), carRecord.mpg])
                cleanFile.close()
        else:
            with open("auto-mpg.clean.txt") as cleanFile:
                reader = csv.reader(cleanFile, delimiter= " ", skipinitialspace=True)
                for row in reader:
                    carRecord = pack(row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8])
                    splitName = carRecord.carName.split()
                    makeName = splitName[1:]
                    AutoMPGData.data.append([splitName[0], " ".join(makeName), "19"+str(carRecord.modelYear), carRecord.mpg])
                cleanFile.close()

    def _clean_data(self):
        with open("auto-mpg.data.txt") as readFile:
            autoData = readFile.readlines()
            with open("auto-mpg.clean.txt", "w") as writeFile:
                for l in range(len(autoData)):
                    writeFile.write(str.expandtabs(autoData[l],3))
                writeFile.close()
            readFile.close()

class Record:
    record = collections.namedtuple("record", "mpg cylinders displacement horsepower weight acceleration modelYear origin carName")

def main():
    object = AutoMPGData()
    for a in range(len(object.data)):
        print("AutoMPGData({})".format(object.data[a]))

main()
