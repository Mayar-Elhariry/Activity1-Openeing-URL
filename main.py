from my_sites import sites, open_site
print("\nFavorite Websites Menu:")
for number, (name, _) in sites.items():
    print(f"{number}. {name}")
while True:
    print("Hint: for exit please press 0.")
    choice = int(input("\nEnter the number of the website you want to open: "))
    if choice in sites:
        _, url = sites[choice]
        open_site(url)
    elif choice==0:
        print("See you soon, Goodbye.")
        break
    else:
        print("Invalid choice. Please enter a number from the list.")