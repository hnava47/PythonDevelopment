import csv, collections, os, logging, requests, operator, argparse

logger = logging.getLogger()
logger.setLevel(logging.DEBUG)

fh = logging.FileHandler("example.log", "w")
fh.setLevel(logging.DEBUG)
logger.addHandler(fh)

sh = logging.StreamHandler()
sh.setLevel(logging.WARNING)
logger.addHandler(sh)

logging.debug("very detailed information")
logging.info("tracing information")
logging.warning("something bad might happen")
logging.error("something bad happened")
logging.critical("something really bad happened")

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
        if os.path.exists("auto-mpg.data.txt") == False:
            self._get_data()
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

    def sort_by_default(self):
        self.sort(key=operator.itemgetter(9,7,1))

    def sort_by_year(self):
        self.sort(key=operator.itemgetter(7,9,1))

    def sort_by_mpg(self):
        self.sort(key=operator.itemgetter(1,9,7))

    def _get_data(self):
        request = requests.get("https://archive.ics.uci.edu/ml/machine-learning-databases/auto-mpg/auto-mpg.data")
        with open("auto-mpg.data.txt", "w") as wf:
            try:
                request.text.startswith("<!DOCTYPE HTML PUBLIC")
            except Exception:
                logging.debug("404 Website Not Found")
            wf.write(request.text)
            wf.close()

    parser = argparse.ArgumentParser(description="analyze Auto MPG data set")
    parser.add_argument("-s", "--sort", type=str, choices=["year", "mpg", "default"], default="default")
    args = parser.parse_args()

    if args.sort == "mgp":
        data.sort_by_mpg()
    elif args.sort == "year":
        data.sort_by_year()
    else:
        data.sort_by_default()

class Record:
    record = collections.namedtuple("record", "mpg cylinders displacement horsepower weight acceleration modelYear origin carName")

def main():
    object = AutoMPGData()
    for a in range(len(object.data)):
        print("AutoMPGData({})".format(object.data[a]))

main()
