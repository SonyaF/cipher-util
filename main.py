def main():
    try:
        keyword = getValidInput("Enter keyword for Encryption: ")
        keyword = keyword.upper()
        
    except KeyboardInterrupt:
        print("\nExiting...")
        raise


if __name__ == "__main__":
    main()
