#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    this_list = []
    for i in range(list_length):
        try:
            this_list[i] = my_list_1[i] / my_list_2[i]
        except TypeError:
            this_list[i] = 0
            print("wrong type")
        except ZeroDivisionError:
            this_list[i] = 0
            print("division by 0")
        except indexError:
            this_list[i] = 0
            print("out of range")
        finally:
            pass
    return this_list