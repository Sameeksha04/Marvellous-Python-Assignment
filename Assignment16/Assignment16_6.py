def main():
    try:
        with open("source.txt", "r") as source:
            content = source.read()

        with open("destination.txt", "w") as destination:
            destination.write(content)

        print("Contents copied successfully...")

    except FileNotFoundError:
        print("source.txt file not found...")

    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    main()
