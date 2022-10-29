from random import randint


def generate_list():
    list1 = []
    for i in range(8):
        l1 = randint(0, 99)
        l2 = randint(0, 99)
        if l1 == l2:
            while True:
                l2 = randint(0, 99)
                if l2 != l1:
                    break
        list1.append(l1), list1.append(l2)
    return sorted(list1)


def differentiate_list(list1):
    while True:
        count = 0
        for i in range(len(list1)-1):
            if list1[i] in list1[i+1:]:
                # again generate that element to make it unique
                list1[i] = randint(0, 99)
                # list should be sorted
                list1 = sorted(list1)
                break
            else:
                count += 1
                if count == len(list1)-1:
                    # List Slicing
                    l1, l2, l3, l4 = list1[:4], list1[4:8], list1[8:12], list1[12:]
                    return l1, l2, l3, l4


def die_rolled():
    return randint(1, 6)


def main():

    # List of 16 length is generated 8(ladders[4-start : 4-end]) & 8(snakes[4-start : 4-end])

    List = generate_list()

    # ALl the List should be unique

    ladders_start, snakes_start, ladders_end, snakes_end = differentiate_list(List)

    # Die is Rolled and a value is generated randomly

    while True:
        die = die_rolled()
        pos = 1    # Starting Position
        max_pos = 101       # Ending Position

        if die == 6:
            print("Game Start")

            # All the Ladders & hurdles(Snakes)

            # print(ladders_start, ladders_end, snakes_end, snakes_start)

    # Move player to next index

            while True:
                die = die_rolled()
                pos += die

                if pos in ladders_start or pos in snakes_start:
                    for i in range(4):
                        if pos == ladders_start[i]:
                            pos = ladders_end[i]
                            print(f"Die has value {die}, piece moved to cell {ladders_start[i]}")
                            print(f"There is a Ladder on cell {ladders_start[i]}, piece moved to cell {pos}")
                            break

                        if pos == snakes_start[i]:
                            pos = snakes_end[i]
                            print(f"Die has value {die}, piece moved to cell {snakes_start[i]}")
                            print(f"There is a Snake on cell {snakes_start[i]}, piece moved to cell {pos}")
                            break

                if pos not in ladders_start and pos not in snakes_start and pos <= max_pos:
                    print(f"Die has value {die}, piece moved to cell {pos}")

                if pos == max_pos:
                    print("\nHurrah! you reach the cell 101 and you won the Game..!!")
                    break

                if pos > max_pos:
                    pos -= die
            break


main()
