def main():
    print("Hello Peoples of Mother")
    print("Here's Your List")

    txt = input("Enter Your Name: ")
    file2 = "bs.txt"

    # Save name to file
    with open(file2, "a") as f:
        f.write(txt + "\n")

    # Show item list
    prices = {
        "laptop": "50k",
        "headphone": "10k",
        "smartphone": "20k",
        "keyboard": "5k",
        "mouse": "5k",
        "monitor": "10k",
        "backpack": "10k",
        "shoes": "20k",
        "t-shirt": "10k",
        "jeans": "15k"
    }

    while True:
        new = input("Enter Your Item (or 'exit' to quit): ").lower()
        if new == "exit":
            print("Exiting program...")
            break
        elif new in prices:
            print(f"Price: {prices[new]}")
        else:
            print("Item not found in list.")

    # Read and show all previous names
    with open(file2, "r") as f:
        names = [line.strip() for line in f.readlines()]
    print("Previous visitors:", names)

if __name__ == "__main__":
    main()