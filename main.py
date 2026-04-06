import os

def encode_basic_rle(text):
    if not text:
        return ""
    compressed = []
    count = 1
    for i in range(1, len(text)):
        if text[i] == text[i - 1]:
            count += 1
        else:
            compressed.append(f"{count}{text[i - 1]}")
            count = 1
    compressed.append(f"{count}{text[-1]}")
    return "".join(compressed)

def decode_basic_rle(text):
    decoded = []
    count_str = ""
    for char in text:
        if char.isdigit():
            count_str += char
        else:
            if count_str:
                decoded.append(char * int(count_str))
                count_str = ""
            else:
                decoded.append(char)
    return "".join(decoded)

def main():
    while True:
        print("\n--- RLE algorithm ---")
        print("1. Encode ")
        print("2. Decode ")
        print("0. Exit")
        choice = input("Choose action: ").strip()

        if choice == '0':
            break
            
        elif choice in ('1', '2'):
            filename = input("  File name: ").strip()
            if not os.path.exists(filename):
                print(f"error: file {filename} does not exist.")
                continue
                
            with open(filename, "r", encoding="utf-8") as f:
                text = f.read()
                
            if choice == '1':
                result_text = encode_basic_rle(text)
                action = "Compressed"
            else:
                result_text = decode_basic_rle(text)
                action = "Archived"
            
            
            with open(filename, "w", encoding="utf-8") as f:
                f.write(result_text)
                
            print(f"Good, Original: {len(text)} symb. {action}: {len(result_text)} symb.")
            print(f"File {filename} rewritten.")
            
        else:
            print("Bad.")

if __name__ == "__main__":
    main()