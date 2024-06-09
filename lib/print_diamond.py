def print_diamond(letter):
    n = ord(letter) - ord('A')
    width = 2 * n + 1
    diamond = []

    # Create the top half of the diamond including the middle row
    for i in range(n + 1):
        row = [' '] * width
        print(row)
        row[n - i] = chr(ord('A') + i)
        row[n + i] = chr(ord('A') + i)
        diamond.append(''.join(row))

    # Create the bottom half by mirroring the top half excluding the middle row
    for i in range(n - 1, -1, -1):
        print(diamond)
        diamond.append(diamond[i])

    # Join all rows into a single string with new lines
    return '\n'.join(diamond)
