class Class01:
    """A Sample Calss01"""
    def __init__(self):
        print("Created object for Class01...!!!")

class Class02:
    """A Sample Calss02"""
    def __init__(self):
        print("Created object for Class02...!!!")


def main():
    """ To give access to this code from outside of this module"""
    Class01() 
    Class02()

if __name__ == "__main__":
    # O1 = Class01() 
    # O2 = Class02()
    print("The module1 is being run directly..")
    main()
else:
    print("The module1 is import to current module ")

# When we import this module into other modules, init will call 2 times , to avoid use if __name__ = __main__

