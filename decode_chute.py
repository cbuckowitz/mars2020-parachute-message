
# mars perseverance parachute color coding inner ring 0 to outer ring 3 (W)hite (R)ed
chuteseg = ["WWWWWWWRWWWWWWWWWWWRWWWWWRWWRWWWWWWWWRWRWWWRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRR",
            "WWWWWRWRWWWWWWWRRWWRWWWRRRRRRRRRRRRRRRRRWWWWWWRRWRWWWWWWRWWRWWWWWWWRRRWWWWWWRWWW",
            "WWWRRRRRRRRRRRRRRRRRWWWWWRWRWWWWWWWWRWWWWWWWWWRWWRWWWWWWRRRWWWWWWWWRRRWWWWWRWWRR",
            "WWWWRWWWRWWWWWWWRWRRWWWWRRRWRWWWWWWWRRRWWWWRRRWRRWWWWWWWRWRWWWWWWRRRRRWWWWWRWRRR"]

# bit chunk size of the code sequence
chunksize = 10


# decode rings color white(0) red(1)
chutecodes = []

for seg in chuteseg:
    bin = seg.replace("W", "0")
    bin = bin.replace("R", "1")
    chutecodes.append(bin)


# dump all 80 ring 0 rotations
bits = list(chutecodes[0])
for s in range(len(bits)):

    # rotate ring code to start position
    code = ''.join(bits[s:] + bits[:s])
    print(code)

# simple scan for ascii offsets
for d in range(128):

    for chutecode in chutecodes:
        bits = list(chutecode)
        matches = 0

        # bit shift code to any of the possible start positions
        for s in range(len(bits)):

            # rotate ring code to start position
            code = ''.join(bits[s:] + bits[:s])

            text = ""
            letters = 0
            nums = []
            chars = []

            # process the chunks of the ring code
            for i in range(len(code) // chunksize):
                chunk = code[i * chunksize: i * chunksize + chunksize]

                # parse int from chunk bits
                num = int(chunk, 2)
                nums.append(num)

                # add ascii scan offset
                chrnum = num + d

                char = chr(chrnum)
                text += char

                # count uppercase letters
                if chrnum >= 65 and chrnum <= 90:
                    letters += 1

            if letters > 3:
                matches += 1
                print(d, s, text, nums)

        if matches > 0:
            print()
