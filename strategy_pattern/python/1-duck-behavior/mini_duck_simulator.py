from duck import MallardDuck, DecoyDuck


def main():
    mallard = MallardDuck()
    mallard.display()
    mallard.quack()
    mallard.fly()

    decoy = DecoyDuck()
    decoy.display()
    decoy.quack()
    decoy.fly()


if __name__ == '__main__':
    main()