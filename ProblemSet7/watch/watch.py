import re

def main():
    print(parse(input("HTML: ")))

def parse(s):
    pattern = r"^<iframe.*(src=\"https?://(?:www\.)?youtube\.com/embed/(?P<identifier>.*?)\")"
    try:
        if youtube := re.search(pattern, s):
            return f"https://youtu.be/{youtube.group("identifier")}"
    except AttributeError:
        return None

if __name__ == "__main__":
    main()
