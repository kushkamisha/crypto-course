from Crypto.Hash import SHA256


def bytes_to_hex(bs):
    res = ""
    for bb in bs:
        if len(hex(bb)[2:]) < 2:
            res += "0" + hex(bb)[2:]
        else:
            res += hex(bb)[2:]

    return res


def get_tag_of_file(filename):
    chunks = []
    with open(filename, "rb") as f:
        chunk = f.read(1024)
        while chunk:
            chunks.append(chunk)
            chunk = f.read(1024)

    prev_h = b''
    for chunk in reversed(chunks):
        data = chunk + prev_h
        prev_h = SHA256.new(data).digest()

    return bytes_to_hex(prev_h)


def main():
    f1 = "videos/03c08f4ee0b576fe319338139c045c89c3e8e9409633bea29442e21425006ea8.mp4"
    f1_hash = "03c08f4ee0b576fe319338139c045c89c3e8e9409633bea29442e21425006ea8"
    tag1 = get_tag_of_file(f1)
    print("Is tag correct for the test file? %s" % (f1_hash == tag1))

    f2 = "videos/to-compute-hash.mp4"
    tag2 = get_tag_of_file(f2)
    print("Tag for the file 'to-compute-hash.mp4' is: \n%s" % tag2)


if __name__ == "__main__":
    main()
