
# naive way
def file_manager():
    f = open("sample.txt", "r")
    print(f)
    f.close()

# better way
def file_manager_v2():
    with open("sample.txt") as f:
        print(f)        

# best way
def file_manager_v3():
    try:
        with open("sample.txt", "r+") as f:
            content = f.read()
            print(content)
            f.write("\nSame here, python!")
    except FileNotFoundError as error:
        print(error)   


if __name__ == "__main__":
    # file_manager()
    # file_manager_v2()
    file_manager_v3()