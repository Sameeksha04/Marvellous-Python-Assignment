def main():
    print("Enter the length of the rectangle: ")
    length = float(input())
    print("Enter the breadth of the rectangle: ")
    breadth = float(input())

    area = length * breadth
    perimeter = 2 * (length + breadth)

    print("Area of the rectangle:", area)
    print("Perimeter of the rectangle:", perimeter)

if __name__ == "__main__":
    main()
