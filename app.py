import argparse


def add(x, y):
    return x + y


def subtract(x, y):
    return x - y


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Simple calculator CLI app")
    parser.add_argument("operation", choices=["add", "subtract"], help="Operation to perform: 'add' or 'subtract'")
    parser.add_argument("x", type=float, help="First number")
    parser.add_argument("y", type=float, help="Second number")
    args = parser.parse_args()

    if args.operation == "add":
        result = add(args.x, args.y)
        print(f"{args.x} + {args.y} = {result}")
    elif args.operation == "subtract":
        result = subtract(args.x, args.y)
        print(f"{args.x} - {args.y} = {result}")