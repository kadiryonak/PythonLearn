from lesson3.listss import ListL


class BubbleSort:
    def __init__(self, list_obj: ListL):
        self.list_obj = list_obj

    def sort(self):
        n = self.list_obj.length()

        for i in range(n):
            for j in range(0, n - i - 1):
                if self.list_obj.listt[j] > self.list_obj.listt[j + 1]:
                    # swap
                    self.list_obj.listt[j], self.list_obj.listt[j + 1] = (
                        self.list_obj.listt[j + 1],
                        self.list_obj.listt[j],
                    )



if __name__ == "__main__":
    liste = ListL()

    # sayılar ekleyelim
    liste.append(7)
    liste.append(3)
    liste.append(9)
    liste.append(1)
    liste.append(5)

    print("Sıralamadan önce:")
    liste.print_list()

    sorter = BubbleSort(liste)
    sorter.sort()

    print("Sıralamadan sonra:")
    liste.print_list()