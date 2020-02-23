from gmpy2 import divm, powmod, mul


class MeetInTheMiddle:

    def __init__(self, p, g, h, b):
        self.p = p
        self.g = g
        self.h = h
        self.b = b
        self.attack_table_file = "attack_table.txt"
        self.attack_table = {}

    def _calc_left(self, x1):
        """h/g^x1 mod p"""
        return divm(self.h, powmod(self.g, x1, self.p), self.p)

    def _calc_right(self, x0):
        """(g^B)^x0"""
        return powmod(self.g, mul(self.b, x0), self.p)

    def _create_table(self):
        with open(self.attack_table_file, "w") as f:
            for x1 in range(self.b + 1):
                f.write(str(self._calc_left(x1)) + "," + str(x1) + "\n")

    def _read_table_from_file(self):
        with open(self.attack_table_file) as f:
            data = [x.replace("\n", "").split(",") for x in f.readlines()]
            for key, value in data:
                self.attack_table[key] = value

    def _crack(self):
        print("Reading the table from the file...")
        self._read_table_from_file()
        print("Reading completed")

        for x0 in range(self.b + 1):
            if x0 % 10000 == 0:
                print("Testing with x0 =", x0)
            if str(self._calc_right(x0)) in self.attack_table:
                return x0

        return -1

    def attack(self):
        # self._create_table()
        # print("Creation of the table completed")

        x0 = self._crack()
        x1 = self.attack_table[str(self._calc_right(x0))]

        print("\nx0 =", x0)
        print("x1 =", x1)
        print("x =", int(x0) * self.b + int(x1))


def main():
    p = 13407807929942597099574024998205846127479365820592393377723561443721764030073546976801874298166903427690031858186486050853753882811946569946433649006084171
    g = 11717829880366207009516117596335367088558084999998952205599979459063929499736583746670572176471460312928594829675428279466566527115212748467589894601965568
    h = 3239475104050450443565264378728065788649097520952449527834792452971981976143292558073856937958553180532878928001494706097394108577585732452307673444020333
    b = 2**20

    mitm = MeetInTheMiddle(p, g, h, b)
    mitm.attack()


if __name__ == "__main__":
    main()
