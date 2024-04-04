from duck import MallardDuck, DecoyDuck
from fly import FlyRocketPowered
from quack import Quack


def main():
    mallard = MallardDuck()
    mallard.display()
    mallard.quack()
    mallard.fly()
    mallard.set_fly_behavior(FlyRocketPowered())
    mallard.fly()

    decoy = DecoyDuck()
    decoy.display()
    decoy.quack()
    decoy.fly()
    decoy.set_quack_behavior(Quack())
    decoy.quack()


if __name__ == '__main__':
    main()